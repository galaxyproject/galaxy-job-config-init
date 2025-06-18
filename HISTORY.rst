History
-------

.. to_doc

---------
0.1.3
---------

* Enhanced tmp_dir configuration to support string values for custom temp directory allocation (environment variables and shell commands)
* Added all-in-one-handling option for simplified Galaxy instances (removes separate handling section)
* Added comprehensive development tooling: black, isort, ruff, mypy, and pre-commit hooks
* Added GitHub Actions CI workflow with automated testing across Python 3.9-3.13
* Added PyPI deployment workflow with trusted publishing
* Added CONTRIBUTING.rst with detailed development guidelines
* Updated README.rst with contributing information
* Added comprehensive test coverage for new features

---------
0.1.2
---------

Add tmp_dir config option thanks to @Smeds. https://github.com/galaxyproject/galaxy-job-config-init/pull/1


---------
0.1.1
---------

Fix for StrEnum usage on older Python versions.

---------
0.1.0
---------

Initial creation with simple options for TPV, various DRMs, and container settings.
