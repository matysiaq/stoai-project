import os
import subprocess

from github import Github, Auth
from langchain_openai import ChatOpenAI

from kubernetes import client as k8sclient
from kubernetes import config as k8sconfig

from promptengineering.config import config
from promptengineering.src.utils import gen_rand_str


class Wrapper:
    def __init__(self, cfg: config.Config):
        self.id = gen_rand_str(16)
        self.cfg = cfg

        os.environ["OPENAI_API_KEY"] = self.cfg.get_auth_openai_api_key()
        os.environ["LANGCHAIN_API_KEY"] = self.cfg.get_auth_langchain_api_key()
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = "TAIA promptengineering - Experiments promptengineering"
        k8sconfig.load_kube_config(config_file=self.cfg.get_auth_kubeconfig_file_path())
        # self.llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.1)
        self.llm = ChatOpenAI(model="gpt-4-turbo-2024-04-09", temperature=0.1)
        # self.llm = ChatOpenAI(model="gpt-4", temperature=0.1)
        self.k8sv1 = k8sclient.CoreV1Api()

    def get_upstream_repo(self, nf_type: str, nf_vendor: str) -> (bool, str):

        repos = self.cfg.get_repo_upstream()
        for repo in repos:
            if repo.nf_type == nf_type and repo.vendor == nf_vendor:
                g = Github(auth=Auth.Token(f"{self.cfg.get_git_access_token()}"))
                r = g.get_repo(self.cfg.get_repo_upstream()[0].name)
                print(f"[Info] Found repository, type[{nf_type}], vendor[{nf_vendor}]: {r.clone_url}")
                return True, r.clone_url

        return False, f"Couldn't find the repository for [{nf_type}, {nf_vendor}]"

    @staticmethod
    def clone_git_repo(nf_vendor: str, upstream_repo: str) -> (bool, str):
        path = f"/home/pmq/workshop/python-programming/taia/promptengineering/cloned-repos/{nf_vendor}"
        if not os.path.isdir(path):
            subprocess.run(['git', 'clone', upstream_repo, path])
            directories = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

            return True, f"Cloned to {path}. Found possible NF helm charts: {directories}"
        else:
            directories = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

            return False, f"Given repository [{path}] already exists. Found possible NF helm charts: {directories}"

    def deploy_nf(self, nf_name: str, local_repo_path: str, nf_helm_chart_name: str) -> (bool, str):
        path = local_repo_path+"/"+nf_helm_chart_name
        if os.path.exists(path):
            subprocess.run(['helm', 'install', "--kubeconfig", f"{self.cfg.get_auth_kubeconfig_file_path()}", f"{nf_helm_chart_name}", path])
            info = f"Deployed NF[{nf_name}], chart [{local_repo_path}/{nf_helm_chart_name}]"
            return True, info
        else:
            return False, f"Provided helm chart {path} does not exist!"

    @staticmethod
    def talk_with_human(msg: str) -> str:
        print(f"[TAIA promptengineering] {msg}")
        info = input("[Human] > ")

        return info

    @staticmethod
    def ask_for_permission(msg: str) -> str:
        print(f"[TAIA promptengineering] {msg}")
        info = input("[Human] > ")

        return info

    def hello_msg(self):
        msg = self.llm.invoke(
            """
            Please pretend that you are Telco AI Assistant (TAIA promptengineering). You are able to deploy 5G Network Functions.
            Generate oneliner welcome msg.
            """
        )

        return msg.content
