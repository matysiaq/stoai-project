import yaml
import sys

REPO_CLASS_5G_CORE = "5g-core"
REPO_CLASS_5G_RAN = "5g-ran"

REPO_VENDOR_FREE5GC = "free5gc"
REPO_VENDOR_OAI = "oai"


class RepoUpstreamItem:
    def __init__(self, nf_type, vendor, domain, name):
        self.nf_type = nf_type
        self.vendor = vendor
        self.domain = domain
        self.name = name


class Config:
    def __init__(self, file_path='/home/pmq/workshop/python-programming/taia/base/config/config.yaml', **kwargs):
        self._auth_openai_api_key = None
        self._auth_langchain_api_key = None
        self._auth_kubeconfig_file_path = None
        self._git_access_token = None
        self._repo_upstream = []

        try:
            with open(file_path, 'r') as f:
                config_data = yaml.safe_load(f)
                self._auth_openai_api_key = config_data.get('auth', {}).get('openai_api_key')
                self._auth_langchain_api_key = config_data.get('auth', {}).get('langchain_api_key')
                self._auth_kubeconfig_file_path = config_data.get('auth', {}).get('kubeconfig_file_path')
                self._git_access_token = config_data.get('auth', {}).get('git_access_token')
                self._repo_upstream = [
                    RepoUpstreamItem(**item) for item in config_data.get('repo', {}).get('upstream', [])
                ]
        except FileNotFoundError:
            print(f"Config file '{file_path}' not found. Using default config.", file=sys.stderr)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML config file '{file_path}':", e, file=sys.stderr)
            print("Using default config.", file=sys.stderr)

        self.update_config(**kwargs)
        self.validate_config()

    def __str__(self):
        return (
            f"Config("
            f"auth_openai_api_key={self._auth_openai_api_key}, "
            f"auth_langchain_api_key={self._auth_langchain_api_key}, "
            f"auth_kubeconfig_file_path={self._auth_kubeconfig_file_path}, "
            f"git_access_token={self._git_access_token}, "
            f"repo_upstream={self._repo_upstream})"
        )

    def update_config(self, **kwargs):
        self._auth_openai_api_key = kwargs.get('_auth_openai_api_key', self._auth_openai_api_key)
        self._auth_langchain_api_key = kwargs.get('_auth_langchain_api_key', self._auth_langchain_api_key)
        self._auth_kubeconfig_file_path = kwargs.get('_auth_kubeconfig_file_path', self._auth_kubeconfig_file_path)
        self._git_access_token = kwargs.get('_git_access_token', self._git_access_token)
        self._repo_upstream = kwargs.get('_repo_upstream', self._repo_upstream)

    def validate_config(self):
        try:
            self.validate()
        except ValueError as e:
            print("Config validation failed:", e, file=sys.stderr)
            print("Using default config.", file=sys.stderr)
            self.load_default_config()

    def validate(self):
        if not isinstance(self._auth_openai_api_key, str):
            raise ValueError("auth_openai_api_key must be a string")
        if not isinstance(self._auth_langchain_api_key, str):
            raise ValueError("auth_langchain_api_key must be a string")
        if not isinstance(self._auth_kubeconfig_file_path, str):
            raise ValueError("auth_kubeconfig_file_path must be a string")
        if not isinstance(self._git_access_token, str):
            raise ValueError("git_access_token must be a string")
        if not isinstance(self._repo_upstream, list):
            raise ValueError("repo_upstream must be a list")

        for upstream in self._repo_upstream:
            if not isinstance(upstream, RepoUpstreamItem):
                raise ValueError("Each item in _repo_upstream must be a RepoUpstreamItem instance")

    def load_default_config(self):
        default_config = self.default_config()
        self._auth_openai_api_key = default_config._auth_openai_api_key
        self._auth_langchain_api_key = default_config._auth_langchain_api_key
        self._auth_kubeconfig_file_path = default_config._auth_kubeconfig_file_path
        self._git_access_token = default_config._git_access_token
        self._repo_upstream = default_config._repo_upstream

    @classmethod
    def default_config(cls):
        return cls(
            _auth_openai_api_key='',
            _auth_langchain_api_key='',
            _auth_kubeconfig_file_path='',
            _git_access_token='',
            _repo_upstream=[
                RepoUpstreamItem(nf_type='5g-ran', vendor='none', domain='none', name=''),
                RepoUpstreamItem(nf_type='5g-core', vendor='none', domain='none', name=''),
            ]
        )

    # Getter method for auth_openai_api_key
    def get_auth_openai_api_key(self):
        return self._auth_openai_api_key

    # Getter method for auth_langchain_api_key
    def get_auth_langchain_api_key(self):
        return self._auth_langchain_api_key

    # Getter method for auth_kubeconfig_file_path
    def get_auth_kubeconfig_file_path(self):
        return self._auth_kubeconfig_file_path

    # Getter method for git_access_token
    def get_git_access_token(self):
        return self._git_access_token

    # Getter method for repo_upstream
    def get_repo_upstream(self):
        return self._repo_upstream
