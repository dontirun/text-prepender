<!--
Copyright 2021 Arun Donti
SPDX-License-Identifier: MIT
-->
# Text Prepender

[![PyPI version](https://badge.fury.io/py/text-prepender.svg)](https://badge.fury.io/py/text-prepender)

Created in mind to add Legal Text to the top of code

text-prepender recursively goes through a specified directory/list of files, and adds text to the top of supported filetypes.
If there is a filetype that you want to add/know how to add, please make a pull request!

### Parameters

Optional parameters:

| Command Line         | Input                | Description                                                                  |
| -------------------- | -------------------- | ---------------------------------------------------------------------------- |
| -h, --help           |                      | Get description of text-prepender                                            |
| -p, --path           | dirpath              | The path to the directory which text-prepender will start at (default: '.')  |
| -t, --text-file      | filepath             | The file that contains the legal text (default: NOTICE)                      |
| -i, --extra-ignores  | space delimited list | Additional file paths/names to ignore. Ex. (-i file1 path1 path2)            |
| -v, --enable-verbose |                      | Flag to turn on verbose logging to list skipped files at the end             |

## To Run:

```bash
# run on all files in current directory
text-prepender
# text-prepender --path path/to different directory
```

or

```bash
# run on a specific set of files
text-prepender file1 path/to/file2
```

`text-prepender --text-file path/to/file`

## pre-commit

If you'd like text-prepender to be run automatically when making changes to files in your Git repository, you can install [pre-commit](https://pre-commit.com/) and add the following text to your repositories' `.pre-commit-config.yaml`:

```yaml
  repos:
  - repo: https://github.com/dontirun/text-prepender
    rev: v0.1.0 # The version of text-prepender
    hooks:
    - id: text-prepender
    #  args:
    #    - '--text-file'
    #    - 'NOTICE'
```
## Manual Build

1. Clone the repo
2. Build the package
   - `pip install build`
   - `python -m build`
3. Install the latest version of the package
   - whl
     - `pip install dist/text_prepender-x.x.x-py3-none-any.whl`
   - .tar.gz
     - `pip install dist/text-prepender-x.x.x.tar.gz`

</details>
