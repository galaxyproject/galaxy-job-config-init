============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

Get Started!
============

Ready to contribute? Here's how to set up `galaxy-job-config-init` for local development.

1. Fork the `galaxy-job-config-init` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/galaxy-job-config-init.git

3. Install your local copy into a virtualenv. Assuming you have virtualenv installed, this is how you set up your fork for local development::

    $ cd galaxy-job-config-init/
    $ virtualenv .venv
    $ source .venv/bin/activate
    $ pip install -r dev-requirements.txt
    $ pip install -e .

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the linting and tests::

    $ make format  # Format code with black, isort, and ruff
    $ black --check .
    $ isort --check-only --diff .
    $ ruff check .
    $ mypy .
    $ pytest

   You can also run pre-commit to check all tools at once::

    $ pre-commit run --all-files

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Code Quality
============

This project uses several tools to maintain code quality:

* **black** - Code formatting
* **isort** - Import sorting  
* **ruff** - Linting and additional checks
* **mypy** - Static type checking
* **pytest** - Testing

You can run all formatting tools at once with::

    $ make format

Or run individual tools::

    $ black .
    $ isort .
    $ ruff check --fix .

To check code without making changes::

    $ black --check .
    $ isort --check-only --diff .
    $ ruff check .
    $ mypy .

Pre-commit hooks are available to run these checks automatically before each commit::

    $ pre-commit install
    $ pre-commit run --all-files

Releases
========

To create a new release:

1. Update the version in ``setup.cfg``
2. Create a git tag with the version number (prefixed with 'v')::

    $ git tag v1.0.0
    $ git push origin v1.0.0

3. The GitHub Actions workflow will automatically build and deploy to PyPI when a tag is pushed to the main repository.

Tips
====

To run a subset of tests::

    $ pytest tests/gxjobconfinit/test_specific.py
