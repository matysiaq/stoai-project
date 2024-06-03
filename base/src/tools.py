from langchain_core.tools import tool

from base.src.wrapper import Wrapper
from base.config import config


wrapper = Wrapper(config.Config())


@tool
def get_upstream_repo(nf_type: str, nf_vendor: str) -> (bool, str):
    """
    Get the URL of Upstream Repository.
    params:
      - nf_type: type of repository, allowed values are 5g-core and 5g-ran
      - nf_vendor: 5G Network Function vendor (full or abbreviated name), allowed values are oai, nokia and free5gc
    """

    ok, info = wrapper.get_upstream_repo(nf_type, nf_vendor)

    return ok, info


@tool
def clone_git_repo(nf_vendor: str, upstream_repo: str) -> (bool, str):
    """
    Clone the Git repository containing NFs (helm charts) described by 3GPP/O-RAN standardization.
    params:
      - nf_vendor: 5G Network Function vendor (full or abbreviated name), allowed values are oai, nokia and free5gc
      - upstream_repo: git clone repository url address
    """

    ok, info = wrapper.clone_git_repo(nf_vendor, upstream_repo)

    return ok, info


@tool
def deploy_nf(nf_name: str, nf_helm_chart_name: str, local_repo_path: str) -> (bool, str):
    """
    Deploy given Network Function to the K8s Cluster. The upstream repository with helm charts need to be
      cloned apriori.
    param:
      - nf_name: 5G Network Function name (abbreviated), e.g. AMF, SMF, UPF
      - nf_helm_chart_name: a helm chart (directory) name for nf. The precise name can vary a little from nf_name
      - local_repo_path: the path to the local git repository containing helm chart for NF
    """

    ok, info = wrapper.deploy_nf(nf_name, local_repo_path, nf_helm_chart_name)

    return ok, info


tools = [get_upstream_repo, clone_git_repo, deploy_nf]
