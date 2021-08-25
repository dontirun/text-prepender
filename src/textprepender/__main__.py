#!/usr/bin/env python3
# Copyright 2021 Arun Donti
# SPDX-License-Identifier: MIT
import argparse
import os
from collections import defaultdict
from typing import List


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=dir_path, default='.')
    parser.add_argument(
        '-t', '--text-file', type=file_path, default='NOTICE',
        help='The file that contains the legal text (default: NOTICE)',  # noqa: E501
    )
    parser.add_argument(
        '-i', '--extra-ignores', nargs='+',
        help='Additional file paths/names to ignore. Ex. (-i file1 path1 path2)',  # noqa: E501
    )
    parser.add_argument(
        '-v', '--enable-verbose', dest='verbose', action='store_true',
        help='Flag to turn on verbose logging to list skipped files at the end',  # noqa: E501
    )
    parser.set_defaults(verbose=False)
    parser.add_argument('files', nargs=argparse.REMAINDER)
    return parser.parse_args()


def dir_path(dir_path: str):
    """ Raise an error if the string does not point to a valid directory. """
    if os.path.isdir(dir_path):
        return dir_path
    else:
        raise NotADirectoryError(dir_path)


def file_path(file_path: str):
    """ Raise an error if the string does not point to a valid file. """
    if os.path.isfile(file_path):
        return file_path
    else:
        raise FileNotFoundError(file_path)


def body_prepender(
    filename: str,
    body: str, comment_format: List[str], already_contains: List[str],
):
    """Append text to top of file.
    Returns a list of files that already contain the text

    Keyword arguments:
    filename -- the path to the file
    body -- the text to add to the top of the file
    comment_format -- the format of comments for the specific filetype
    already_contains -- the current list of files that already contain the text
    """
    with open(filename, 'r+') as f:
        content = f.read()
        # Check if this exact body already exists in the file
        mod_body = ''
        if len(comment_format) == 1:
            split_body = body.splitlines(True)
            mod_body = (comment_format[0] + ' ').join(['', *split_body])
        elif len(comment_format) == 2:
            mod_body = comment_format[0] + \
                '\n' + body.rstrip() + '\n' + comment_format[1]
        trimmed_body = ' '.join(body.split())
        trimmed_file = ' '.join(content.replace(comment_format[0], '').split())
        if trimmed_body not in trimmed_file:
            split_content = content.splitlines(True)
            # Respect shebang lines
            updated_body = mod_body
            if len(split_content) > 0 and '#!' in split_content[0]:
                updated_body = split_content[0] + '\n' + mod_body
                content = ''.join(split_content[1:])
            f.seek(0, 0)
            f.write(updated_body.rstrip('\r\n') + '\n' + content)
            print(f'Modified: {filename}')
        else:
            already_contains.append(filename)
        f.close()
    return already_contains


def main():
    parsed_args = parse_arguments()
    paths_parts_to_ignore = ['node_modules', '.git', '.vscode-test', '.venv']
    paths_parts_to_ignore.append(parsed_args.text_file)
    if parsed_args.extra_ignores:
        paths_parts_to_ignore.extend(parsed_args.extra_ignores)
    # For Logging
    already_contains = []
    unsupported = defaultdict(list)

    # Supported File Types
    file_type_dict = {
        '.c': ['/*', '*/'],
        '.cpp': ['/*', '*/'],
        '.css': ['/*', '*/'],
        '.docker': ['#'],
        '.erl': ['%'],
        '.gitignore': ['#'],
        '.go': ['/*', '*/'],
        '.hs': ['{-', '-}'],
        '.html': ['<!--', '-->'],
        '.java': ['/*', '*/'],
        '.js': ['/*', '*/'],
        '.md': ['<!--', '-->'],
        '.php': ['/*', '*/'],
        '.py': ['#'],
        '.r': ['#'],
        '.rb': ['/*', '*/'],
        '.rs': ['/*', '*/'],
        '.sh': ['#'],
        '.ts': ['/*', '*/'],
        '.txt': [''],
        '.vue': ['<!--', '-->'],
        '.yaml': ['#'],
        '.yml': ['#'],
        '.xml': ['<!--', '-->'],
    }

    try:
        # Use absolute paths to files if a list of files are specified
        if len(parsed_args.files) == 0:
            for r, _, f in os.walk(parsed_args.path):
                if not any(part in r for part in paths_parts_to_ignore):
                    for file in f:
                        parsed_args.files.append(os.path.join(r, file))

        for file in parsed_args.files:
            if not any(part in file for part in paths_parts_to_ignore):
                split_file = file.split('.')
                file_type = file.split('.')[-1]
                if len(split_file) > 1:
                    file_type = '.'+file_type
                if file_type in file_type_dict:
                    text_to_add = open(parsed_args.text_file).read()
                    already_contains = body_prepender(
                        file,
                        text_to_add,
                        file_type_dict[file_type],
                        already_contains,
                    )
                else:
                    unsupported[file_type].append(file)
    except Exception as e:
        raise(e)

    if parsed_args.verbose:
        if len(unsupported.keys()) > 0:
            print('Unsupported Files By Type: \n')
            for key in unsupported:
                print(f'\t{key}:')
                for value in unsupported[key]:
                    print(f'\t\t{value}')
            print('')

        if len(already_contains) > 0:
            print('Already contain text_to_add:')
            for value in already_contains:
                print(f'\t{value}')


if __name__ == '__main__':
    main()
