# Sarus
<img src="https://img.shields.io/github/stars/eth-cscs/sarus">
<img src="https://img.shields.io/github/forks/eth-cscs/sarus">
<img src="https://img.shields.io/github/issues/eth-cscs/sarus">

Sarus is a software to run Linux containers on High Performance Computing environments. Its development has been driven by the specific requirements of HPC systems, while leveraging open standards and technologies to encourage vendor and community involvement.

Key features:
- Spawning of isolated software environments (containers), built by users to fit the deployment of a specific application
- Security oriented to HPC systems
- Extensible runtime by means of OCI hooks to allow current and future support of custom hardware while achieving native performance
- Creation of container filesystems tailored for diskless nodes and parallel filesystems
- Compatibility with the presence of a workload manager
- Compatibility with the Open Container Initiative (OCI) standards:
  - Can pull images from registries adopting the OCI Distribution Specification or the Docker Registry HTTP API V2 protocol
  - Can import and convert images adopting the OCI Image Format
  - Sets up a container bundle complying to the OCI Runtime Specification
  - Uses an OCI-compliant runtime to spawn the container process

### Keywords
container, HPC, OCI

### Test
✅ [1.1.0](https://github.com/eth-cscs/sarus/releases/tag/1.1.0) on Ubuntu 18.04

### Compatibility
- RHEL/Centos
- Debian

### Limits

### Security
- [post installation](https://sarus.readthedocs.io/en/stable/install/post-installation.html)
- Sarus must run as a root-owned SUID executable and be able to achieve full root privileges to perform mounts and create namespaces.
- Write/read permissions to the Sarus’s centralized repository
- Write/read permissions to the users’ local image repositories

### Designed for
- HPC

### System Requirements and Permissions
- Sarus is installed on the HPC and it requires root in order to set Sarus as a root-owned SUID program

### Available Tools


### 3rd Party Integration
- [GPU support](https://sarus.readthedocs.io/en/stable/user/user_guide.html#nvidia-gpu-support)
- [Native MPI support](https://sarus.readthedocs.io/en/stable/user/user_guide.html#native-mpi-support-mpich-based)
- able to communicate with registries using the Docker Registry protocol

### Other


### Information
- [https://github.com/eth-cscs/sarus](https://github.com/eth-cscs/sarus)
- [paper](http://www.hpcadvisorycouncil.com/events/2019/swiss-workshop/pdf/030419/K_Mariotti_CSCS_SARUS_OCI_ContainerRuntime_04032019.pdf)
- [paper](https://link.springer.com/book/10.1007/978-3-030-34356-9)
- [documentation](https://sarus.readthedocs.io/en/stable/)
- [ISC High Performance 2019](https://link.springer.com/chapter/10.1007%2F978-3-030-34356-9_5)