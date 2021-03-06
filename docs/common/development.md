# Library Development

This documentation is for those who want to contribute to the development of
this library.

## Requirements

- Use Python3, not compatible with Python2.
- Recommended to use **Python \<= 3.8.0**.
- If you have a different version we recommend you to use
  [pyenv](https://github.com/pyenv/pyenv) and thus you can have different
  versions of Python installed in your machine and switch among them.
- In regards to the library installation, we have detected some issues with
  the `pip` version. As of now the library installation has been fully tested
  and proved working with the following versions of pip: `19.2.3`, `21.0.1`
  (latest as of March 2021)
- If necessary, access to our JIRA instance where we manage the library
  development and roadmap.

## Guidelines

If you want to contribute to the development of this library please adhere to
the following:

- In general, we adhere to
  [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- To lint code, we use [pylint](https://github.com/PyCQA/pylint)
  following the `pylintrc` provided in [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- To format code, we use [yapf](https://github.com/google/yapf/)
  as stated in [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- To format markdown (docs) we follow [mdformat Style Guide](https://github.com/executablebooks/mdformat/blob/master/STYLE.md)
  and [Semantic Line Breaks](https://sembr.org/)
- We use [pre-commit](https://pre-commit.com/) to enforce and automate
  must of the formatting and linting work (before commiting any code)
- We validate code and test it using [Github Actions](https://github.com/features/actions).
  This will run once a Pull Request is created or push to master is made.

## Local Environment Setup

To contribute to this library you will need to install the source code locally,
follow the following docs to achieve this.

Create a new environment using `venv`. We recommend you to create the virutal
environment directory inside the repository (it will be ignore it) and name it
`.venv`:

```
python -m venv .venv
source .venv/bin/activate
```

Install development dependencies:

```
pip install -r requirements.txt
```

Install the library alongside its dependencies:

```
pip install -e .
```

Install pre-commit hooks:

```
pre-commit install
```

Make sure your local repository is working with our pre-commmit hooks:

```
pre-commit run --all-files
```

All hooks are to be in "Passed" status:

```
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Check for added large files..............................................Passed

...

```

**Done**, now you are ready to start contributing and improving the `sotaai`
library.

## Contribution Flow

Regarding feature development or improvements, we adhere to the flow described
below.

**Step 1:** Make sure your local repo email match the email you use in Jira, in
the repo run:

```
git config user.email "myemailusedinjira@mail.com"
```

**Step 2:** Have or create an issue in JIRA for the feature your going to work
on. By feature we mean: a fix, feature, improve, refactor, to be added to the
current code base.

**Step 3:** Make sure to have `master` branch up to date, and then create a
branch out of `master` and name it after the Jira issue ID. This is going to be
refered as the "feature branch":

```
git checkout -b SOTA-1338
```

**Step 4:** work on the feature branch and constantly push changes to its
respective remote. For naming commits, follow [these
guidelines](https://github.com/stateoftheartai/sotaai/blob/master/docs/common/commits.md).
All updates are to be automatically reflected in Jira as long as:

- The feature branch name exactly matches the Jira's issue ID e.g. SOTA-1338
- Each of the feature branch commits meet the specs in [Jira Smart
  Commits](https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/)
  at least in one line of the title/body of the commit. For example:

To put the issue in progress:

```
update: add some updates to development.md
- SOTA-1338 #progress
```

To put the Jira issue in progress and add a comment to the Jira issue as well:

```
update: add some updates to development.md
- SOTA-1338 #progress #comment This is my comment
```

Valid transitions are: `#progress`, `#review`, `#test`, `#done`

**Step 5:** once the feature is finished create a Pull Request and assign it to
a Reviewer. The Pull Request will trigger testing jobs, if those succced and the
Reviewer approves the code, then the feature branch is to be merged into
`master` by the Reviewer. For this, all feature branch commits will be squashed
into one commit, this commit is to be rename it by the reviewer to be consistent
with the feature being merged, and finally merged. This way `master` branch will
have only one commit per feature, which was tested, and with a consistent name.

**Step 6:** when the Pull Request is accepted and thus the feature branch is
merged, this feature branch is automatically deleted from the remote, however
the developer must delete its local branch from its machine and also pull
`master` changes that might include the new feature:

```
git branch -D SOTA-1338
git checkout master
git pull origin master
```

**Step 7:** the developer can now create a new branch out of `master` and start
working in a new feature.

## Fixing Issues

When trying to commit your code you might get some errors, if you want to
individually review these errors use the following commands.

### pre-commit

To independently check files against a particular pre-commit task (id) run:

```
pre-commit run <id> --files <file-1> <file-2> ...
```

For example:

```
pre-commit run pylint --files tests/cv/test_utils.py

pre-commit run trailing-whitespace --files tests/cv/test_utils.py
```

Notes:

- Formatters such as `yapf` or `mdformat` when run by pre-commit will
  automatically update the files which did not meet the format, fixing them.
  Those fixed files need to be added to the staging area again so that you can
  proceed with the commit, if not the pre-commit tasks will fail again.

### pylint

To independently check files against pylint and review linting issues run:

```
pylint file-or-dir --load-plugins=pylint_quotes
```

### yapf

To independently check files against yapf to verify formatting run:

```
yapf file-or-dir --recursive --diff
```

Avoid, --recursive if running against a file. This will print differences
between the current file format and the one required by yapf. If no differences
means the files are properly following yapf.

### unittest

Unittests will test the current version of the `sotaai` library installed in your
virtual environment. Therefore, first make sure you have installed the right
version of it i.e. the one you want to test:

- Install the version from your local code base
  `pip install -e .` in case you want to test
  your latest local changes.
- Install a specific version from PyPI
  (test or real indexes as desired)
  `pip install sotaai==x.y.z` or
  `pip install --index-url https://test.pypi.org/simple/ --no-deps sotaai`
  in case you want to test and already-deployed version.

There are different ways to execute tests:

Execute all of them:

```
python -m unittest discover tests
```

Execute tests of a file:

```
python -m unittest tests/cv/test_utils.py
```

Execute a particular test:

```
python tests/cv/test_utils.py TestCvUtils.test_map_name_tasks
```
