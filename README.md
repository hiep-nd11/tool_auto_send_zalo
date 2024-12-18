# tool_auto_send_zalo
Tool auto send zalo for Sari.

The program will include food categories based on the food101 dataset.

## Installation
```bash
$ git clone https://github.com/hiep-nd11/tool_auto_send_zalo.git
$ cd tool_auto_send_zalo
$ python3 -m venv your_venv_name # create the virtual environment 
$ your_venv_name\Scripts\activate
$ pip install -r requirements.txt
```
## Convert to .exe
```bash
$ cd src
$ cd tool_auto_send_zalo
$ pyinstaller --onefile --add-data "check_login.py;." --add-data "send_message.py;." --add-data "chrome_driver.py;." --add-data "name_distric.py;." main.py
# Sau khi chuyển file .exe thư mục sẽ nằm ở src/dish/main.exe
```
## Rules code
- Code according to PEP8 standard (isort, black formatter extension) or Google style.
- Work with git according to git flow standard (only work on develop branch).
- Use git issue and git project to pull request.
- Pull Request Size: Each pull request (PR) should limit the scope of changes, avoiding too many commits or unrelated changes in a single PR.
- Code Review: Each pull request must be reviewed by at least one other team member. The reviewer should check the code quality, ensure compliance with guidelines, and verify accuracy.
- Commit Message Structure: Commit messages need to be clear, describing the purpose and reason for the commit.
    - Prefix: Use prefixes to categorize the commit, for example:
        + feat: Add a new feature.
        + fix: Fix a bug.
        + refactor: Refactor the code without changing functionality.
        + test: Add or modify tests.
        + docs: Update documentation.
- Docstrings: Each function or class should have a docstring describing its functionality, input parameters, output, and exceptions. Use either the Google style or PEP257 standard.
- Requirements file: library name + current version (Example: numpy==0.0.1).
- Write the function should have (arguments *arg and **kwwarg).

## Weights folder
- You just need to copy the weights folder to the same level as the core folder
- Weights folder available: