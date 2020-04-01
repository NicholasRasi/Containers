# Singularity
<img src="https://img.shields.io/github/stars/sylabs/singularity">
<img src="https://img.shields.io/github/forks/sylabs/singularity">
<img src="https://img.shields.io/github/issues/sylabs/singularity">

Singularity is an open source container platform designed to be simple, fast, and secure. Singularity is optimized for compute focused enterprise and HPC workloads, allowing untrusted users to run untrusted containers in a trusted way.

- Secure, single-file based container format
- Support for data-intensive workloads
- Extreme mobility
- Compatibility
- Simplicity
- Security
- User groups 

### Keywords
container, HPC, Edge

### Test
✅ [release 3.5.3](https://github.com/sylabs/singularity/releases/tag/v3.5.3) on Ubuntu 18.04

### Compatibility
- RHEL/Centos
- Debian

### Limits


### Security
- [admin-guide](https://sylabs.io/guides/3.5/admin-guide/admin_quickstart.html#singularity-security)
- [security](https://sylabs.io/guides/3.5/admin-guide/security.html)

Singularity uses a number of strategies to provide safety and ease-of-use on both single-user and shared systems.
- The user inside a container is the same as the user who ran the container. This means access to files and devices from the container is easily controlled with standard POSIX permissions.
- Container filesystems are mounted nosuid and container applications run with the PR_NO_NEW_PRIVS flag set. This means that applications in a container cannot gain additional privileges. A regular user cannot sudo or otherwise gain root privilege on the host via a container.
- The Singularity Image Format (SIF) supports encryption of containers, as well as cryptographic signing and verification of their content.
- SIF containers are immutable and their payload is run directly, without extraction to disk. This means that the container can always be verified, even at runtime, and encrypted content is not exposed on disk.
- Restrictions can be configured to limit the ownership, location, and cryptographic signatures of containers that are permitted to be run.

### Designed for
- HPC
- Cloud
- Edge

### System Requirements and Permissions
- [system requirements](https://sylabs.io/guides/3.5/admin-guide/installation.html#system-requirements)
- OverlayFS mounts - (minimum kernel >=3.18) Required for full flexiblity in bind mounts to containers, and to support persistent overlays for writable containers
- Unprivileged user namespaces - (minimum kernel >=3.8, >=3.18 recommended) Required to run containers without root or setuid privilege
- Singularity requires ~140MiB disk space once compiled and installed
- There are no specific CPU or memory requirements at runtime, though 2GB of RAM is recommended when building from source.
- golang

### Available Tools
- SingularityCE: Singularity Community Edition is 100% open source, BSD licensed software
- SingularityPro
- Singularity Desktop (macOS)

### 3rd Party Integration
- [Support for Docker and OCI](https://sylabs.io/guides/3.5/user-guide/singularity_and_docker.html)
- [MPI](https://sylabs.io/guides/3.5/user-guide/mpi.html)
- [GPU support](https://sylabs.io/guides/3.5/user-guide/gpu.html)
- [plugins](https://sylabs.io/guides/3.5/user-guide/plugins.html)
- [cloud library](https://sylabs.io/guides/3.5/user-guide/cloud_library.html)
- [Singularity CRI](https://github.com/sylabs/singularity-cri): consists of two separate services: runtime and image, each of which implements K8s RuntimeService and ImageService respectively

### Other
- Written in Go

### Information
- [https://sylabs.io/](https://sylabs.io/)
- [https://github.com/sylabs/singularity](https://github.com/sylabs/singularity)
- [documentation](https://sylabs.io/docs/)
- [paper](https://sylabs.io/assets/white-papers/2018_Year-End_White_Paper_FINAL.pdf)
- [examples](https://github.com/sylabs/examples)
- [Singularity and HPC](https://singularity.lbl.gov/docs-hpc)
- [Singularity Container Workflows for Compute](http://www.hpcadvisorycouncil.com/events/2019/stanford-workshop/pdf/DayOne_Thursday_14Feb_2019/G_Kurtzer_Sylabs_Singularity_Thursday_02142019.pdf)
- [Security in Singularity](https://sylabs.io/guides/3.5/user-guide/security.html)
- [Singularity root permission](https://singularity.lbl.gov/faq#do-you-need-administrator-privileges-to-use-singularity)
