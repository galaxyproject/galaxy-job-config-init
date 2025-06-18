import yaml
from typing_extensions import Unpack

from gxjobconfinit import (
    build_job_config,
    CliConfigArgs,
    ConfigArgs,
    summary_markdown,
)
from gxjobconfinit.types import Runner


def test_build_job_config_slurm():
    config_dict = build_to_yaml(runner=Runner.SLURM)
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert "docker_enabled" not in slurm_env


def test_build_job_config_slurm_with_docker():
    config_dict = build_to_yaml(runner=Runner.SLURM, docker=True)
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert slurm_env["docker_enabled"] is True
    assert "docker_sudo" not in slurm_env


def test_build_job_config_slurm_with_docker_and_sudo():
    config_dict = build_to_yaml(runner=Runner.SLURM, docker=True, docker_sudo=True)
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert config_dict["execution"]["default"] == "slurm"
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert slurm_env["docker_enabled"] is True
    assert slurm_env["docker_sudo"] is True


def test_build_job_config_slurm_with_singularity():
    config_dict = build_to_yaml(runner=Runner.SLURM, singularity=True)
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert slurm_env["singularity_enabled"] is True
    assert "docker_sudo" not in slurm_env


def test_build_job_config_slurm_with_singularity_and_sudo():
    config_dict = build_to_yaml(runner=Runner.SLURM, singularity=True, singularity_sudo=True)
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert slurm_env["singularity_enabled"] is True
    assert slurm_env["singularity_sudo"] is True


def test_build_job_config_slurm_with_tmp_dir():
    config_dict = build_to_yaml(runner=Runner.SLURM, singularity=True, tmp_dir="true")
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert slurm_env["tmp_dir"] is True


def test_build_job_config_drmaa():
    config_dict = build_to_yaml(runner=Runner.DRMAA)
    drmaa_env = config_dict["execution"]["environments"]["drmaa"]
    assert config_dict["execution"]["default"] == "drmaa"
    assert drmaa_env
    assert drmaa_env["runner"] == "drmaa"


def test_build_job_config_k8s():
    config_dict = build_to_yaml(runner=Runner.K8S)
    k8s_env = config_dict["execution"]["environments"]["k8s"]
    assert config_dict["execution"]["default"] == "k8s"
    assert k8s_env
    assert k8s_env["runner"] == "k8s"


def test_build_job_config_condor():
    config_dict = build_to_yaml(runner=Runner.CONDOR)
    condor_env = config_dict["execution"]["environments"]["condor"]
    assert config_dict["execution"]["default"] == "condor"
    assert condor_env
    assert condor_env["runner"] == "condor"


def test_build_job_config_slurm_tpv():
    config_dict = build_to_yaml(runner=Runner.SLURM, tpv=True, galaxy_version="25.0")
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert "docker_enabled" not in slurm_env

    tpv_env = config_dict["execution"]["environments"]["tpv"]
    assert tpv_env["runner"] == "dynamic_tpv"


def test_build_job_config_slurm_tpv_legacy():
    config_dict = build_to_yaml(runner=Runner.SLURM, tpv=True, galaxy_version="24.2")
    slurm_env = config_dict["execution"]["environments"]["slurm"]
    assert slurm_env
    assert slurm_env["runner"] == "slurm"
    assert "docker_enabled" not in slurm_env

    tpv_env = config_dict["execution"]["environments"]["tpv"]
    assert tpv_env["runner"] == "dynamic"


def test_tmp_dir_default():
    """Test that tmp_dir defaults to true and is included."""
    config_dict = build_to_yaml(runner=Runner.LOCAL)
    local_env = config_dict["execution"]["environments"]["local"]
    assert local_env["tmp_dir"] is True


def test_tmp_dir_true():
    """Test tmp_dir with explicit 'true' string value."""
    config_dict = build_to_yaml(runner=Runner.LOCAL, tmp_dir="true")
    local_env = config_dict["execution"]["environments"]["local"]
    assert local_env["tmp_dir"] is True


def test_tmp_dir_false():
    """Test tmp_dir with 'false' string value is omitted."""
    config_dict = build_to_yaml(runner=Runner.LOCAL, tmp_dir="false")
    local_env = config_dict["execution"]["environments"]["local"]
    assert "tmp_dir" not in local_env


def test_tmp_dir_variable():
    """Test tmp_dir with environment variable."""
    config_dict = build_to_yaml(runner=Runner.LOCAL, tmp_dir="$DRM_JOB_TMP_DIR")
    local_env = config_dict["execution"]["environments"]["local"]
    assert local_env["tmp_dir"] == "$DRM_JOB_TMP_DIR"


def test_tmp_dir_shell_command():
    """Test tmp_dir with shell command."""
    shell_cmd = "$(mktemp -d /scratch/gxyXXXXXX)"
    config_dict = build_to_yaml(runner=Runner.LOCAL, tmp_dir=shell_cmd)
    local_env = config_dict["execution"]["environments"]["local"]
    assert local_env["tmp_dir"] == shell_cmd


def test_all_in_one_handling_disabled():
    """Test that normal handling section is included by default."""
    config_dict = build_to_yaml(runner=Runner.LOCAL, all_in_one_handling=False)
    assert "handling" in config_dict
    assert config_dict["handling"]["assign"] == ["db-skip-locked"]


def test_all_in_one_handling_enabled():
    """Test that handling section is omitted with all_in_one_handling=True."""
    config_dict = build_to_yaml(runner=Runner.LOCAL, all_in_one_handling=True)
    assert "handling" not in config_dict


def test_all_in_one_handling_with_slurm():
    """Test all_in_one_handling works with different runners."""
    config_dict = build_to_yaml(runner=Runner.SLURM, all_in_one_handling=True)
    assert "handling" not in config_dict
    assert config_dict["execution"]["default"] == "slurm"


def test_tmp_dir_and_all_in_one_combined():
    """Test that both options can be used together."""
    config_dict = build_to_yaml(runner=Runner.LOCAL, tmp_dir="$CUSTOM_TMP", all_in_one_handling=True)
    assert "handling" not in config_dict
    local_env = config_dict["execution"]["environments"]["local"]
    assert local_env["tmp_dir"] == "$CUSTOM_TMP"


def test_summary():
    print(summary_markdown())


def build_to_yaml(**kwds: Unpack[CliConfigArgs]):
    config = ConfigArgs.from_dict(**kwds)
    job_config = build_job_config(config)
    return yaml.safe_load(job_config)
