# Containers

## HPC
### Singularity
<img src="https://sylabs.io/assets/svg/singularity-logo.svg" height=100></br>
<img src="https://img.shields.io/github/stars/sylabs/singularity">

Enabling and securing your performance critical applications from the core, through the cloud, and out to the edge.
- [https://sylabs.io/](https://sylabs.io/)
- [**Report**](/reports/singularity.md)

### Shifter
<img src="https://raw.githubusercontent.com/wiki/NERSC/shifter/images/shifter_logo.png" height=100></br>
<img src="https://img.shields.io/github/stars/NERSC/shifter">

Shifter enables container images for HPC. In a nutshell, Shifter allows an HPC system to efficiently and safely allow end-users to run a docker image.
- [https://github.com/NERSC/shifter](https://github.com/NERSC/shifter)
- [**Report**](/reports/shifter.md)

### Charliecloud
<img src="https://hpc.github.io/charliecloud/_static/logo-sidebar.png" height=100></br>
<img src="https://img.shields.io/github/stars/hpc/charliecloud">

Charliecloud provides user-defined software stacks (UDSS) for high-performance computing (HPC) centers.
- [https://hpc.github.io/charliecloud/index.html](https://hpc.github.io/charliecloud/index.html)
- [**Report**](/reports/charliecloud.md)

### Sarus
<img src="https://img.shields.io/github/stars/eth-cscs/sarus">

Sarus is a software to run Linux containers on High Performance Computing environments. Its development has been driven by the specific requirements of HPC systems, while leveraging open standards and technologies to encourage vendor and community involvement.
- [https://github.com/eth-cscs/sarus](https://github.com/eth-cscs/sarus)
- [**Report**](/reports/sarus.md)

### Ubercloud (not opensource)
<img src="https://www.theubercloud.com/hs-fs/hubfs/Images/Logos/UberCloudLogo.png?width=177&name=UberCloudLogo.png">

UberCloud is the online community and marketplace where engineers, scientists, and their service providers discover, try, and buycompute power as a Service, from computing clouds and even from Supercomputing Centers around the world.
- [**Report**](/reports/ubercloud.md)


## IoT
### Balena Engine
<img src="https://raw.githubusercontent.com/balena-os/balena-engine/master/docs/static_files/balena-engine.svg?sanitize=true" height=100></br>
<img src="https://img.shields.io/github/stars/balena-os/balena-engine">

balenaEngine is a new container engine purpose-built for embedded and IoT use cases and compatible with Docker containers.
- [https://www.balena.io/engine/](https://www.balena.io/engine/)
- [**Report**](/reports/balena-engine.md)


## Container Runtime
### runc
- **Description:** runc is a CLI tool for spawning and running containers according to the OCI specification.
- **Link:** [https://www.opencontainers.org/](https://www.opencontainers.org/)
- **Paper / Documentation:** [https://github.com/opencontainers/runc](https://github.com/opencontainers/runc)

### Kata Containers
- **Description:** Kata Containers is an open source community working to build a secure container runtime with lightweight virtual machines that feel and perform like containers, but provide stronger workload isolation using hardware virtualization technology as a second layer of defense.
- **Link:** [https://katacontainers.io/](https://katacontainers.io/)
- **Paper / Documentation:** [https://github.com/kata-containers/documentation](https://github.com/kata-containers/documentation)

### gVisor
- **Description:** gVisor is a user-space kernel, written in Go, that implements a substantial portion of the Linux system surface. It includes an Open Container Initiative (OCI) runtime called runsc that provides an isolation boundary between the application and the host kernel. The runsc runtime integrates with Docker and Kubernetes, making it simple to run sandboxed containers.
- **Link:** [https://gvisor.dev/](https://gvisor.dev/)
- **Paper / Documentation:** [https://github.com/google/gvisor](https://github.com/google/gvisor)

### containerd
- **Description:** containerd is an industry-standard container runtime with an emphasis on simplicity, robustness and portability. It is available as a daemon for Linux and Windows, which can manage the complete container lifecycle of its host system: image transfer and storage, container execution and supervision, low-level storage and network attachments, etc.
- **Link:** [https://containerd.io/](https://containerd.io/)
- **Paper / Documentation:** [https://github.com/containerd/containerd](https://github.com/containerd/containerd)

### LXC
- **Description:** LXC is the well-known and heavily tested low-level Linux container runtime. It is in active development since 2008 and has proven itself in critical production environments world-wide. Some of its core contributors are the same people that helped to implement various well-known containerization features inside the Linux kernel.
- **Link:** [https://linuxcontainers.org/lxc/](https://linuxcontainers.org/lxc/)
- **Paper / Documentation:** [https://github.com/lxc/lxc](https://github.com/lxc/lxc)

## Docker
### udocker
- **Description:** udocker is a basic user tool to execute simple docker containers in user space without requiring root privileges. Enables download and execution of docker containers by non-privileged users in Linux systems where docker is not available. It can be used to pull and execute docker containers in Linux batch systems and interactive clusters that are managed by other entities such as grid infrastructures or externally managed batch or interactive systems. udocker does not require any type of privileges nor the deployment of services by system administrators. It can be downloaded and executed entirely by the end user. udocker is a wrapper around several tools to mimic a subset of the docker capabilities including pulling images and running containers with minimal functionality.
- **Link:** [https://github.com/indigo-dc/udocker](https://github.com/indigo-dc/udocker)
- **Paper / Documentation:** [https://arxiv.org/pdf/1711.01758.pdf](https://arxiv.org/pdf/1711.01758.pdf)


## Kubernetes / Distribution
### CNAB: Cloud Native Application Bundles
- **Description:** Cloud Native Application Bundles (CNAB) are a package format specification that describes a technology for bundling, installing, and managing distributed applications, that are by design, cloud agnostic.
- **Link:** [https://cnab.io/](https://cnab.io/)
- **Paper / Documentation:** [https://github.com/cnabio/cnab-spec](https://github.com/cnabio/cnab-spec)

### Mobyproject
- **Description:** Moby is an open framework created by Docker to assemble specialized container systems without reinventing the wheel. It provides a “lego set” of dozens of standard components and a framework for assembling them into custom platforms. At the core of Moby is a framework to assemble specialized container systems which provides.
- **Link:** [https://mobyproject.org/](https://mobyproject.org/)
- **Paper / Documentation:** [https://github.com/moby/moby/](https://github.com/moby/moby/)

### Weave Works
- **Description:** Automate Enterprise Kubernetes the GitOps way. Operate and manage production ready Kubernetes with Weave Kubernetes Platform. GitOps unlocks cloud native agility, reliability and scalability.
- **Link:** [https://www.weave.works/](https://www.weave.works/)
- **Paper / Documentation:** [https://www.weave.works/docs/](https://www.weave.works/docs/)

### CoreOS Operator Framework
- **Description:** the Operator Framework is an open source project that provides developer and runtime Kubernetes tools, enabling you to accelerate the development of an Operator. 
- **Link:** [https://coreos.com/operators/](https://coreos.com/operators/)
- **Paper / Documentation:** [https://github.com/operator-framework](https://github.com/operator-framework)

### Rancher
- **Description:** Rancher is an open source project that provides a container management platform built for organizations that deploy containers in production. Rancher makes it easy to run Kubernetes everywhere, meet IT requirements, and empower DevOps teams.
- **Link:** [https://rancher.com/](https://rancher.com/)
- **Paper / Documentation:** [https://github.com/rancher/rancher](https://github.com/rancher/rancher)

### CRI-O
- **Description:** CRI-O is meant to provide an integration path between OCI conformant runtimes and the kubelet. Specifically, it implements the Kubelet Container Runtime Interface (CRI) using OCI conformant runtimes. The scope of CRI-O is tied to the scope of the CRI.
- **Link:** [https://cri-o.io/](https://cri-o.io/)
- **Paper / Documentation:** [https://github.com/cri-o/cri-o](https://github.com/cri-o/cri-o)
- 

## OpenStack
### Kolla
- **Description:** Kolla provides Docker containers, Ansible playbooks to deploy OpenStack on baremetal or virtual machine to meet Kolla's mission. Kolla has out of the box defaults for a working basic deployment, and also implements complete customization. This model permits operators with minimal experience to deploy OpenStack quickly and as the operator's experience grows modify the OpenStack configuration to suit the operator's exact requirements.
- **Link:** [https://wiki.openstack.org/wiki/Kolla](https://wiki.openstack.org/wiki/Kolla)
- **Paper / Documentation:** [https://opendev.org/openstack/kolla](https://opendev.org/openstack/kolla)


## Micro VMs / Micro-services
### Firecracker
- **Description:** Firecracker is an open source virtualization technology that is purpose-built for creating and managing secure, multi-tenant container and function-based services that provide serverless operational models. Firecracker runs workloads in lightweight virtual machines, called microVMs, which combine the security and isolation properties provided by hardware virtualization technology with the speed and flexibility of containers.
- **Link:** [https://firecracker-microvm.github.io/](https://firecracker-microvm.github.io/)
- **Paper / Documentation:** [https://github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)

### OSv
- **Description:** OSv is the versatile modular unikernel designed to run unmodified Linux applications securely on micro-VMs in the cloud. Built from the ground up for effortless deployment and management of micro-services and serverless apps, with superior performance.
- **Link:** [http://osv.io/](http://osv.io/)
- **Paper / Documentation:** [https://github.com/cloudius-systems/osv](https://github.com/cloudius-systems/osv)

### Istio
- **Description:** Developers must use microservices to architect for portability, meanwhile operators are managing extremely large hybrid and multi-cloud deployments. Istio lets you connect, secure, control, and observe services. At a high level, Istio helps reduce the complexity of these deployments, and eases the strain on your development teams. It is a completely open source service mesh that layers transparently onto existing distributed applications. It is also a platform, including APIs that let it integrate into any logging platform, or telemetry or policy system. Istio’s diverse feature set lets you successfully, and efficiently, run a distributed microservice architecture, and provides a uniform way to secure, connect, and monitor microservices.
- **Link:** [https://istio.io/](https://istio.io/)
- **Paper / Documentation:** [https://istio.io/docs/setup/getting-started/](https://istio.io/docs/setup/getting-started/)

### CoreOS (End-of-life)
- **Description:** Container Linux redefines the operating system as a smaller, more compact Linux distribution. Traditional distros package unused software that leads to dependency conflicts and needlessly increases the attack surface.
- **Link:** [https://coreos.com/](https://coreos.com/)
- **Paper / Documentation:** [https://coreos.com/os/docs/latest/](https://coreos.com/os/docs/latest/)


## Container Registry
### Harbor
- **Description:** Harbor is an open source container image registry that secures images with role-based access control, scans images for vulnerabilities, and signs images as trusted. A CNCF Incubating project, Harbor delivers compliance, performance, and interoperability to help you consistently and securely manage images across cloud native compute platforms like Kubernetes and Docker.
- **Link:** [https://goharbor.io/](https://goharbor.io/)
- **Paper / Documentation:** [https://github.com/goharbor/harbor](https://github.com/goharbor/harbor)