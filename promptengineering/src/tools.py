from langchain_core.tools import tool

from promptengineering.src.wrapper import Wrapper
from promptengineering.config import config

wrapper = Wrapper(config.Config())


@tool
def get_upstream_repo(nf_type: str, nf_vendor: str, ask_permission_policy=False) -> (bool, str):
    """
    Get the URL of Upstream Repository.
    metadata for each parameter is defined, agentMetadata must be used as is.
    params:
      - nf_type: type of repository
        metadata: allowed_values=[5g-core, 5g-ran]
      - nf_vendor: 5G Network Function vendor (full or abbreviated name)
        metadata: allowed_values=[oai, nokia, free5gc]
    agentMetadata:
      - ask_permission_policy: never
    """

    ok, info = wrapper.get_upstream_repo(nf_type, nf_vendor)

    return ok, info


@tool
def clone_git_repo(nf_vendor: str, upstream_repo: str, ask_permission_policy=True) -> (bool, str):
    """
    Clone the Git repository containing NFs (helm charts) described by 3GPP/O-RAN standardization.
    metadata for each parameter is defined, agentMetadata must be used as is.
    params:
      - nf_vendor: 5G Network Function vendor (full or abbreviated name)
        metadata: allowed_values: [oai, nokia, free5gc], always_clarify=True
      - upstream_repo: git clone repository url address
        metadata: always_clarify=True
    agentMetadata:
      - ask_permission_policy: always
    """

    ok, info = wrapper.clone_git_repo(nf_vendor, upstream_repo)

    return ok, info


@tool
def deploy_nf(nf_name: str, nf_helm_chart_name: str, local_repo_path: str, ask_permission_policy=True) -> (bool, str):
    """
    Deploy given Network Function to the K8s Cluster. The upstream repository with helm charts need to be
      cloned apriori.
    metadata for each parameter is defined, agentMetadata must be used as is.
    param:
      - nf_name: 5G Network Function name (abbreviated), e.g. AMF, SMF, UPF
        metadata: always_clarify=True
      - nf_helm_chart_name: a helm chart (directory) name for nf. The precise name can vary a little from nf_name
      - local_repo_path: the path to the local git repository containing helm chart for NF
        metadata: always_clarify=True
    agentMetadata:
      - ask_permission_policy: always
    """

    ok, info = wrapper.deploy_nf(nf_name, local_repo_path, nf_helm_chart_name)

    return ok, info


@tool
def talk_with_human(msg: str, ask_permission=False) -> str:
    """
    If any clarification is needed (both from user or assistant/agent) this tool can be called to accomplish that.
    The output should be used as a context / input for further processing.
    params:
      - msg: a prompt send to the user to collect more information or receive user response
    agentMetadata:
      - ask_permission_policy: never
    """

    info = wrapper.talk_with_human(msg)

    return info


@tool
def ask_for_permission(msg: str, ask_permission=False):
    """
    If the next tool has ask_permission_policy=always, this tool must be used first to ask if the parameters are valid.
    params:
      - msg: a prompt send to the user; contains a question to validate
    agentMetadata
      - ask_permission_policy: never
    """

    answer = wrapper.ask_for_permission(msg)

    return answer


tools = [get_upstream_repo, clone_git_repo, deploy_nf, talk_with_human, ask_for_permission]
