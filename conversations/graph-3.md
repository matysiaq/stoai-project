## Conversation

Assistant: graph

Question: 3

*Note: The following output has been refined for enhanced clarity by removing redundant information.*

---

```bash
[TAIA graph] I'm your Telco AI Assistant. What can I do for you?
```

```bash
Human> Can you deploy for me 5g core from Nokia?
```

```bash
================================== Ai Message ==================================
To deploy the 5G core from Nokia, I will need to follow these steps:

1. Retrieve the URL of the upstream repository for the Nokia 5G core.
2. Clone the Git repository containing the necessary helm charts.
3. Deploy the specific network functions (such as AMF, SMF, UPF) to the Kubernetes cluster.

Before proceeding, could you please specify which network functions (e.g., AMF, SMF, UPF) you would like to deploy? Additionally, if you have any specific version or configuration details, please let me know.
```

```bash
Human> I would like to deploy entire core
```

```bash
================================== Ai Message ==================================
Great, you'd like to deploy the entire Nokia 5G core. This typically includes network functions such as AMF, SMF, UPF, PCF, and others.

Here's how I'll proceed:

1. **Retrieve the URL of the upstream repository** for the Nokia 5G core.
2. **Clone the Git repository** containing the necessary helm charts.
3. **Deploy each network function** to the Kubernetes cluster.

I will start by retrieving the URL of the upstream repository for the Nokia 5G core. Please hold on for a moment.
```

```bash
================================== Tool Calls ==================================
-        {'id': 'call_tXaOlGE93WQXYDpBvHq3wWqt', 'function': {'arguments': '{"nf_type":"5g-core","nf_vendor":"nokia"}', 'name': 'get_upstream_repo'}, 'type': 'function'}
```

```bash
================================== Ai Message ==================================
It seems that I couldn't find the repository for the Nokia 5G core. This could be due to various reasons such as access restrictions or incorrect information.

To proceed, I can try the following options:
1. Verify the vendor name or the type of network function. It's possible that the repository is listed under a different vendor name or category.
2. If you have access to the repository URL or any specific details about where the Nokia 5G core can be found, please provide that information.

Could you please confirm the vendor name or provide any additional details that might help in locating the repository? Alternatively, if you have the repository URL, please share it with me.
```

```bash
Human> You are right, Nokia core is not available. Please deploy free5gc core instead.
```

```bash
================================== Ai Message ==================================
Thank you for the update. I will now proceed to deploy the free5GC core. Here are the steps I will follow:

1. **Retrieve the URL of the upstream repository** for the free5GC core.
2. **Clone the Git repository** containing the necessary helm charts.
3. **Deploy each network function** to the Kubernetes cluster.

I will start by retrieving the URL of the upstream repository for the free5GC core. Please hold on for a moment.
```

```bash
================================== Tool Calls ==================================
-        {'id': 'call_4Toj0R3jUGruAw3hcb5vlIYe', 'function': {'arguments': '{"nf_type":"5g-core","nf_vendor":"free5gc"}', 'name': 'get_upstream_repo'}, 'type': 'function'}
[Info] Found repository, type[5g-core], vendor[free5gc]: https://github.com/matysiaq/free5gc.git
```

```bash
================================== Ai Message ==================================
I have successfully retrieved the URL for the free5GC core repository. The next step is to clone this repository.

The repository URL is: [https://github.com/matysiaq/free5gc.git](https://github.com/matysiaq/free5gc.git)

I will now proceed to clone this Git repository containing the necessary helm charts for deploying the free5GC core. Please hold on for a moment.
```

```bash
================================== Tool Calls ==================================
-        {'id': 'call_3vEig7C3DWAJ9R6T9JfcNViH', 'function': {'arguments': '{"nf_vendor":"free5gc","upstream_repo":"https://github.com/matysiaq/free5gc.git"}', 'name': 'clone_git_repo'}, 'type': 'function'}
```

```bash
Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.
```

```bash
Human> y
```

```bash
================================== Ai Message ==================================
The repository for the free5GC core has already been cloned, and I have found several network function helm charts available for deployment. Here are the network functions available:

- AMF (Access and Mobility Management Function)
- SMF (Session Management Function)
- UPF (User Plane Function) - multiple versions
- PCF (Policy Control Function)
- NRF (Network Repository Function)
- UDR (Unified Data Repository)
- UDM (Unified Data Management)
- AUSF (Authentication Server Function)
- NSSF (Network Slice Selection Function)
- WebUI

Please let me know which specific network functions you would like to deploy, or if you would like to proceed with deploying the entire core.
```

```bash
Human> Please deploy entire core
```

```bash
================================== Ai Message ==================================
I will proceed with deploying the entire free5GC core. This includes deploying all the network functions available in the repository:

- AMF (Access and Mobility Management Function)
- SMF (Session Management Function)
- UPF (User Plane Function) - multiple versions
- PCF (Policy Control Function)
- NRF (Network Repository Function)
- UDR (Unified Data Repository)
- UDM (Unified Data Management)
- AUSF (Authentication Server Function)
- NSSF (Network Slice Selection Function)
- WebUI

I will deploy these network functions to the Kubernetes cluster using the helm charts found in the cloned repository. Please hold on while I initiate the deployment process.
```

```bash
================================== Tool Calls ==================================
-        {'id': 'call_SF87BhrTv9Vg4n7FLh2NLkJw', 'function': {'arguments': '{"nf_name": "AMF", "nf_helm_chart_name": "free5gc-amf", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_zX9zNUQOHbbf6cd6iGgjSRHc', 'function': {'arguments': '{"nf_name": "SMF", "nf_helm_chart_name": "free5gc-smf", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_vPPpIOqu4EyZ3SwenInPM2zd', 'function': {'arguments': '{"nf_name": "UPF", "nf_helm_chart_name": "free5gc-upf-21", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_9zyX2WXOT0sJfL8BgAB0odMF', 'function': {'arguments': '{"nf_name": "PCF", "nf_helm_chart_name": "free5gc-pcf", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_3QFdmXyekvALH5tAkNtqXOq3', 'function': {'arguments': '{"nf_name": "NRF", "nf_helm_chart_name": "free5gc-nrf", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_mizSCy5Vk0LzHlTlW95T9yek', 'function': {'arguments': '{"nf_name": "UDR", "nf_helm_chart_name": "free5gc-udr", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_UqETqrID7DRz9TG1fpXzSl4B', 'function': {'arguments': '{"nf_name": "UDM", "nf_helm_chart_name": "free5gc-udm", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_EV8E2dao96uMiI9L6qa3IJ4d', 'function': {'arguments': '{"nf_name": "AUSF", "nf_helm_chart_name": "free5gc-ausf", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_rStXekau9jFPNXTKxGWKIK98', 'function': {'arguments': '{"nf_name": "NSSF", "nf_helm_chart_name": "free5gc-nssf", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
-        {'id': 'call_VtprX34kZTHUNej3FAObXk5k', 'function': {'arguments': '{"nf_name": "WebUI", "nf_helm_chart_name": "free5gc-webui", "local_repo_path": "/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc"}', 'name': 'deploy_nf'}, 'type': 'function'}
```

```bash
Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested changed.
```

```bash
Human> y
```

```bash
Deployed NF[AUSF], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-ausf]
Deployed NF[UDR], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-udr]
Deployed NF[PCF], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-pcf]
Deployed NF[WebUI], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-webui]
Deployed NF[NSSF], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-nssf]
Deployed NF[UPF], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-upf-21]
Deployed NF[UDM], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-udm]
Deployed NF[SMF], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-smf]
Deployed NF[AMF], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-amf]
Deployed NF[NRF], chart [/home/pmq/workshop/python-programming/taia/graph/cloned-repos/free5gc/free5gc-nrf]
```

```bash
================================== Ai Message ==================================
The deployment of the entire free5GC core has been successfully completed. All network functions have been deployed to the Kubernetes cluster using their respective helm charts. Here is a summary of the deployed functions:

- **AMF** (Access and Mobility Management Function)
- **SMF** (Session Management Function)
- **UPF** (User Plane Function)
- **PCF** (Policy Control Function)
- **NRF** (Network Repository Function)
- **UDR** (Unified Data Repository)
- **UDM** (Unified Data Management)
- **AUSF** (Authentication Server Function)
- **NSSF** (Network Slice Selection Function)
- **WebUI**

If you need further assistance or additional configurations, please let me know!
```

```bash
Human> What NFs did you deploy?
```

```bash
================================== Ai Message ==================================
I deployed the following network functions as part of the entire free5GC core:

- **AMF** (Access and Mobility Management Function)
- **SMF** (Session Management Function)
- **UPF** (User Plane Function)
- **PCF** (Policy Control Function)
- **NRF** (Network Repository Function)
- **UDR** (Unified Data Repository)
- **UDM** (Unified Data Management)
- **AUSF** (Authentication Server Function)
- **NSSF** (Network Slice Selection Function)
- **WebUI**

These network functions were deployed using their respective helm charts to the Kubernetes cluster. If you have any more questions or need further assistance, feel free to ask!
```
