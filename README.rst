
.. image:: https://badge.fury.io/py/galaxy-job-config-init.svg
   :target: https://pypi.org/project/galaxy-job-config-init/


Overview
--------

Module and script for bootstrapping Galaxy_ job config files.

* Code: https://github.com/galaxyproject/galaxy-job-config-init

Installation
------------

Install from PyPI::

    pip install galaxy-job-config-init

CLI Usage
---------

The package provides two command-line tools:

**galaxy-job-config-init**

Generate job configuration YAML for Galaxy::

    galaxy-job-config-init [OPTIONS]

Options::

    --galaxy-version TEXT
        Generate job config YAML for this version of Galaxy

    --runner {local,slurm,pbs,condor,kubernetes}
        Galaxy runner (e.g. DRM) to target (defaults to 'local')

    --tpv
        Enable shared TPV database

    --docker
        Enable Docker

    --docker-cmd TEXT
        Command used to launch docker (defaults to 'docker')

    --docker-host TEXT
        Docker host

    --docker-sudo
        Use sudo with Docker

    --docker-sudo-cmd TEXT
        Docker sudo command

    --docker-run-extra-arguments TEXT
        Extra arguments for Docker run

    --docker-extra-volume TEXT
        Extra Docker volumes (can be specified multiple times)

    --singularity
        Enable Singularity

    --singularity-cmd TEXT
        Command used to execute singularity (defaults to 'singularity')

    --singularity-sudo
        Use sudo with Singularity

    --singularity-sudo-cmd TEXT
        Singularity sudo command

    --singularity-extra-volume TEXT
        Extra Singularity volumes (can be specified multiple times)

    --tmp-dir TEXT
        Configure temporary directory handling (defaults to 'true')

    --all-in-one-handling
        Use all-in-one job handling configuration

**galaxy-job-config-init-summary**

Generate a summary of the job configuration. See `job_config_examples.md <job_config_examples.md>`_ for detailed examples of generated configurations.

Examples
~~~~~~~~

Generate a basic local job configuration::

    galaxy-job-config-init

Generate configuration for SLURM with Docker support::

    galaxy-job-config-init --runner slurm --docker

Generate configuration with custom Docker volumes::

    galaxy-job-config-init --docker --docker-extra-volume /data:/data --docker-extra-volume /scratch:/scratch

Generate configuration for all-in-one Galaxy instance::

    galaxy-job-config-init --all-in-one-handling

Contributing
------------

Contributions are welcome! Please see `CONTRIBUTING.rst <CONTRIBUTING.rst>`_ for development setup, code quality guidelines, and release procedures.

.. _Galaxy: http://galaxyproject.org/
