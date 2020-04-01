# Charliecloud
<img src="https://img.shields.io/github/stars/hpc/charliecloud">
<img src="https://img.shields.io/github/forks/hpc/charliecloud">
<img src="https://img.shields.io/github/issues/hpc/charliecloud">

Charliecloud provides user-defined software stacks (UDSS) for high-performance computing (HPC) centers. This "bring your own software stack" functionality addresses needs such as:

- software dependencies that are numerous, complex, unusual, differently configured, or simply newer/older than what the center provides;
- build-time requirements unavailable within the center, such as relatively unfettered internet access;
- validated software stacks and configuration to meet the standards of a particular field of inquiry;
- portability of environments between resources, including workstations and other test and development system not managed by the center;
- consistent environments, even archivally so, that can be easily, reliabily, and verifiably reproduced in the future; and/or
- usability and comprehensibility.

Charliecloud uses Linux user namespaces to run containers with no privileged operations or daemons and minimal configuration changes on center resources. This simple approach avoids most security risks while maintaining access to the performance and functionality already on offer.

### Keywords
container, HPC, UDSS, Docker

### Test
✅ [release 0.13](https://github.com/hpc/charliecloud/releases/tag/v0.13) on Ubuntu 18.04

### Compatibility
Charliecloud can be installed from sources and is available using a variety of distribution and third-party package managers.

### Limits
- Performance is the same as native in tests, modulo noise, because minimal isolation yields direct access to all resources: compute, network, file systems, accelerators, and the rest. ch-run scales using standard HPC tools
- Charliecloud runtime must be installed

### Security
- Charliecloud is not an isolation layer, so containers have full access to host resources
- ch-run requires no privilege and depends on the Linux kernel for security, just like any other user process

### Designed for
- HPC
- UDSS

### System Requirements and Permissions
- it exploits Docker features such as image building and image sharing
- it exploits the sixth namespace, *user*, was added in Linux 3.8 and the following few releases. Its goal is to give unprivileged processes access to traditionally privileged functionality in specific contexts when doing so is safe. The first process in a new user namespace has all capabilities in the new namespace, but none in the parent user namespace, even if created by root. Thus, processes and kernel resources inside the user namespace can be manipulated arbitrarily, but only in ways that do not affect the parent namespace (i.e, the host)

### Available Tools
- Charliecloud is a collection of five shell scripts and two C programs totaling roughly 900 lines of code. For comparison, NsJail is 4,000 lines, Singularity 11,000, Shifter 19,000, and Docker 133,000
- [Charlieclouds commands](https://hpc.github.io/charliecloud/command-usage.html#)

### 3rd Party Integration
- Container images can be built using Docker or anything else that can generate a standard Linux filesystem tree

### Other
- Charliecloud puts building and sharing in a sandbox that is separate from HPC center resources. This could be a user workstation or a virtual machine: somewhere safe to give the user root. In this sandbox, Charliecloud wraps Docker for image building, and the other Docker tools are also available, including sharing via pull/push to any Docker Hub repository.
- Running images uses our own runtime that is unprivileged and independent of Docker. This can be on center resources or anywhere else with the Charliecloud runtime installed, such as the same sandbox for development and testing.


### Information
- [https://hpc.github.io/charliecloud/index.html](https://hpc.github.io/charliecloud/index.html)
- [https://github.com/hpc/charliecloud](https://github.com/hpc/charliecloud)
- [https://www.usenix.org/system/files/login/articles/login_fall17_03_priedhorsky.pdf](https://www.usenix.org/system/files/login/articles/login_fall17_03_priedhorsky.pdf)
- [paper](https://dl.acm.org/doi/pdf/10.1145/3126908.3126925)
- [paper](https://www.usenix.org/system/files/login/articles/login_fall17_03_priedhorsky.pdf)