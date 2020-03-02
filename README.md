# Containers
- [Containers](#containers)
  - [HPC](#hpc)
    - [Singularity](#singularity)
    - [Shifter](#shifter)
    - [Charliecloud](#charliecloud)
    - [Sarus](#sarus)
    - [Ubercloud](#ubercloud)
  - [IoT](#iot)
    - [Balena Engine](#balena-engine)
  - [Micro VMs / Micro-services](#micro-vms--micro-services)
    - [Istio](#istio)
    - [OSv](#osv)
    - [Mirage OS](#mirage-os)
    - [Firecracker](#firecracker)
    - [Fedora CoreOS (previously CoreOS)](#fedora-coreos-previously-coreos)
  - [Containers Engine](#containers-engine)
    - [Podman](#podman)
    - [Docker](#docker)
    - [udocker](#udocker)
    - [Mobyproject](#mobyproject)
  - [Container Runtime](#container-runtime)
    - [gVisor](#gvisor)
    - [runc](#runc)
    - [containerd](#containerd)
    - [LXC](#lxc)
    - [CRI-O](#cri-o)
    - [Kata Containers](#kata-containers)
  - [Kubernetes / Distribution](#kubernetes--distribution)
    - [Rancher](#rancher)
    - [Nomad](#nomad)
    - [CoreOS Operator Framework](#coreos-operator-framework)
    - [CNAB: Cloud Native Application Bundles](#cnab-cloud-native-application-bundles)
    - [Weave Works](#weave-works)
  - [Container Registry](#container-registry)
    - [Harbor](#harbor)
    - [skopeo](#skopeo)
  - [Other / OpenStack](#other--openstack)
    - [Kolla](#kolla)
  - [Useful Resources](#useful-resources)

## HPC
### Singularity
<img src="https://sylabs.io/assets/svg/singularity-logo.svg" height="100"></br>
<img src="https://img.shields.io/github/stars/sylabs/singularity">

Enabling and securing your performance critical applications from the core, through the cloud, and out to the edge.
- [https://sylabs.io/](https://sylabs.io/)
- [**Report**](/reports/singularity.md)

### Shifter
<img src="https://raw.githubusercontent.com/wiki/NERSC/shifter/images/shifter_logo.png" height="100"></br>
<img src="https://img.shields.io/github/stars/NERSC/shifter">

Shifter enables container images for HPC. In a nutshell, Shifter allows an HPC system to efficiently and safely allow end-users to run a docker image.
- [https://github.com/NERSC/shifter](https://github.com/NERSC/shifter)
- [**Report**](/reports/shifter.md)

### Charliecloud
<img src="https://hpc.github.io/charliecloud/_static/logo-sidebar.png" height="100"></br>
<img src="https://img.shields.io/github/stars/hpc/charliecloud">

Charliecloud provides user-defined software stacks (UDSS) for high-performance computing (HPC) centers.
- [https://hpc.github.io/charliecloud/index.html](https://hpc.github.io/charliecloud/index.html)
- [**Report**](/reports/charliecloud.md)

### Sarus
<img src="https://img.shields.io/github/stars/eth-cscs/sarus">

Sarus is a software to run Linux containers on High Performance Computing environments. Its development has been driven by the specific requirements of HPC systems, while leveraging open standards and technologies to encourage vendor and community involvement.
- [https://github.com/eth-cscs/sarus](https://github.com/eth-cscs/sarus)
- [**Report**](/reports/sarus.md)

### Ubercloud
<img src="https://www.theubercloud.com/hs-fs/hubfs/Images/Logos/UberCloudLogo.png?width=177&name=UberCloudLogo.png">

UberCloud (not opensource) is the online community and marketplace where engineers, scientists, and their service providers discover, try, and buycompute power as a Service, from computing clouds and even from Supercomputing Centers around the world.
- [**Report**](/reports/ubercloud.md)


## IoT
### Balena Engine
<img src="https://raw.githubusercontent.com/balena-os/balena-engine/master/docs/static_files/balena-engine.svg?sanitize=true" height="100"></br>
<img src="https://img.shields.io/github/stars/balena-os/balena-engine">

balenaEngine is a new container engine purpose-built for embedded and IoT use cases and compatible with Docker containers.
- [https://www.balena.io/engine/](https://www.balena.io/engine/)
- [**Report**](/reports/balena-engine.md)

## Micro VMs / Micro-services
### Istio
<img src="https://istio.io/img/logo.png" height="100"></br>
<img src="https://img.shields.io/github/stars/istio/istio">

Istio is an open platform for providing a uniform way to integrate microservices, manage traffic flow across microservices, enforce policies and aggregate telemetry data.
- [https://istio.io/](https://istio.io/)
- [**Report**](/reports/istio.md)

### OSv
<img src="http://osv.io/images/logo.jpg" height="100"></br>
<img src="https://img.shields.io/github/stars/cloudius-systems/osv">

OSv is the versatile modular unikernel designed to run unmodified Linux applications securely on micro-VMs in the cloud. Built from the ground up for effortless deployment and management of micro-services and serverless apps, with superior performance.
- [http://osv.io/](http://osv.io/)
- [**Report**](/reports/osv.md)

### Mirage OS
<img src="https://mirage.io/graphics/mirage-logo-small.png" height="100"></br>
<img src="https://img.shields.io/github/stars/mirage/mirage">

MirageOS is a library operating system that constructs unikernels for secure, high-performance network applications across a variety of cloud computing and mobile platforms
- [https://mirage.io/](https://mirage.io/)
- [**Report**](/reports/mirageos.md)

### Firecracker
<img src="https://firecracker-microvm.github.io/img/firecracker-logo@3x.png" height="100"></br>
<img src="https://img.shields.io/github/stars/hpc/charliecloud">

Firecracker is an open source virtualization technology that is purpose-built for creating and managing secure, multi-tenant container and function-based services that provide serverless operational models.
- [https://firecracker-microvm.github.io/](https://firecracker-microvm.github.io/)
- [**Report**](/reports/firecracker.md)

### Fedora CoreOS (previously CoreOS)
<img src="https://getfedora.org/static/images/logo-inline-coreos.png" height="100"></br>

Fedora CoreOS is an automatically updating, minimal, monolithic, container-focused operating system, designed for clusters but also operable standalone, optimized for Kubernetes but also great without it.
- [https://getfedora.org/coreos/](https://getfedora.org/coreos/)
- [**Report**](/reports/fedora-coreos.md)

## Containers Engine
### Podman
<img src="https://podman.io/images/podman.svg" height="100"></br>
<img src="https://img.shields.io/github/stars/containers/libpod">

Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System.
- [https://podman.io/](https://podman.io/)
- [**Report**](/reports/podman.md)

### Docker
<img src="https://camo.githubusercontent.com/a7c0ecc760e59a185c0efc2b928025db729f480c/68747470733a2f2f7777772e646f636b65722e636f6d2f73697465732f64656661756c742f66696c65732f64382f323031392d30372f766572746963616c2d6c6f676f2d6d6f6e6f6368726f6d617469632e706e67" height="100"></br>
<img src="https://img.shields.io/github/stars/docker/docker-ce">

Docker Engine powers millions of applications worldwide, providing a standardized packaging format for diverse applications.
- [https://www.docker.com/products/container-runtime](https://www.docker.com/products/container-runtime)

### udocker
<img src="https://raw.githubusercontent.com/indigo-dc/udocker/master/doc/logo-small.png" height="100"></br>
<img src="https://img.shields.io/github/stars/indigo-dc/udocker">

udocker is a basic user tool to execute simple docker containers in user space without requiring root privileges.
- [https://github.com/indigo-dc/udocker](https://github.com/indigo-dc/udocker)
- [**Report**](/reports/udocker.md)

### Mobyproject
<img src="https://raw.githubusercontent.com/moby/moby/master/docs/static_files/moby-project-logo.png" height="100"></br>
<img src="https://img.shields.io/github/stars/moby/moby">

Moby is an open framework created by Docker to assemble specialized container systems without reinventing the wheel. It provides a “lego set” of dozens of standard components and a framework for assembling them into custom platforms.
- [https://mobyproject.org/](https://mobyproject.org/)
- [**Report**](/reports/mobyproject.md)

## Container Runtime
### gVisor
<img src="https://gvisor.dev/logo_huecc535c5c6d57d0972f257cbe0c4e09e_8387_70x70_fit_catmullrom_2.png" height="100"></br>
<img src="https://img.shields.io/github/stars/google/gvisor">

gVisor is a user-space kernel, written in Go, that implements a substantial portion of the Linux system surface. It includes an Open Container Initiative (OCI) runtime called runsc that provides an isolation boundary between the application and the host kernel. The runsc runtime integrates with Docker and Kubernetes, making it simple to run sandboxed containers.
- [https://gvisor.dev/](https://gvisor.dev/)

### runc
<img src="https://img.shields.io/github/stars/opencontainers/runc">

runc is a CLI tool for spawning and running containers according to the OCI specification.
- [https://github.com/opencontainers/runc](https://github.com/opencontainers/runc)

### containerd
<img src="https://containerd.io/img/logos/navbar-light-logo.png" height="100"></br>
<img src="https://img.shields.io/github/stars/containerd/containerd">

containerd is an industry-standard container runtime with an emphasis on simplicity, robustness and portability. It is available as a daemon for Linux and Windows, which can manage the complete container lifecycle of its host system: image transfer and storage, container execution and supervision, low-level storage and network attachments, etc.
- [https://containerd.io/](https://containerd.io/)
- 

### LXC
<img src="https://camo.githubusercontent.com/0e7ffe52374cc8d5edba8724bad029aaaf5e9029/68747470733a2f2f6c696e7578636f6e7461696e6572732e6f72672f7374617469632f696d672f636f6e7461696e6572732e706e67" height="100"></br>
<img src="https://img.shields.io/github/stars/lxc/lxc">

LXC is the well-known and heavily tested low-level Linux container runtime. It is in active development since 2008 and has proven itself in critical production environments world-wide. Some of its core contributors are the same people that helped to implement various well-known containerization features inside the Linux kernel.
- [https://linuxcontainers.org/lxc/](https://linuxcontainers.org/lxc/)

### CRI-O
<img src="https://raw.githubusercontent.com/cri-o/cri-o/master/logo/crio-logo.svg?sanitize=true" height="100"></br>
<img src="https://img.shields.io/github/stars/cri-o/cri-o">

CRI-O is meant to provide an integration path between OCI conformant runtimes and the kubelet. Specifically, it implements the Kubelet Container Runtime Interface (CRI) using OCI conformant runtimes. The scope of CRI-O is tied to the scope of the CRI.
- [https://cri-o.io/](https://cri-o.io/)

### Kata Containers
<img src="https://katacontainers.io/assets/img/logo.a1e2d09a.svg" height="100"></br>
<img src="https://img.shields.io/github/stars/kata-containers/runtime">

Kata Containers is an open source community working to build a secure container runtime with lightweight virtual machines that feel and perform like containers, but provide stronger workload isolation using hardware virtualization technology as a second layer of defense.
- [https://katacontainers.io/](https://katacontainers.io/)

## Kubernetes / Distribution
### Rancher
<img src="https://rancher.com/imgs/rancher-logo-horiz-color.png" height="100"></br>
<img src="https://img.shields.io/github/stars/rancher/rancher">

Rancher is an open source project that provides a container management platform built for organizations that deploy containers in production. Rancher makes it easy to run Kubernetes everywhere, meet IT requirements, and empower DevOps teams.
- [https://rancher.com/](https://rancher.com/)

### Nomad
<img src="https://raw.githubusercontent.com/hashicorp/nomad/19c404ca791d6ebe95a81738d7dc6623ab28564d/website/public/img/logo-hashicorp.svg?sanitize=true" height="100"></br>
<img src="https://img.shields.io/github/stars/hashicorp/nomad">

Nomad is an easy-to-use, flexible, and performant workload orchestrator that can deploy a mix of microservice, batch, containerized, and non-containerized applications. Nomad is easy to operate and scale and has native Consul and Vault integrations.
- [https://nomadproject.io/](https://nomadproject.io/)

### CoreOS Operator Framework
<img src="https://coreos.com/assets/images/operators/operator_logo_framework_color.svg" height="100"></br>
<img src="https://img.shields.io/github/stars/operator-framework/operator-sdk
">

The Operator Framework is an open source project that provides developer and runtime Kubernetes tools, enabling you to accelerate the development of an Operator. An Operator is a method of packaging, deploying and managing a Kubernetes application.
- [https://coreos.com/operators/](https://coreos.com/operators/)

### CNAB: Cloud Native Application Bundles
<img src="https://cnab.io/img/cnab-text.svg" height="100"></br>
<img src="https://img.shields.io/github/stars/cnabio/cnab-spec">

Cloud Native Application Bundles (CNAB) are a package format specification that describes a technology for bundling, installing, and managing distributed applications, that are by design, cloud agnostic.
- [https://cnab.io/](https://cnab.io/)

### Weave Works
<img src="https://daniel.holba.ch/images/2018/02/logo_weaveworks_huef4bd10d6459c1917d680d11733f2f6b_13139_900x500_fit_box_2.png" height="100">

Automate Enterprise Kubernetes the GitOps way. Operate and manage production ready Kubernetes with Weave Kubernetes Platform. GitOps unlocks cloud native agility, reliability and scalability.
- [https://www.weave.works/](https://www.weave.works/)


## Container Registry
### Harbor
<img src="https://goharbor.io/img/logos/harbor-logo-white.svg" height="100"></br>
<img src="https://img.shields.io/github/stars/goharbor/harbor">

Harbor is an open source container image registry that secures images with role-based access control, scans images for vulnerabilities, and signs images as trusted. A CNCF Incubating project, Harbor delivers compliance, performance, and interoperability to help you consistently and securely manage images across cloud native compute platforms like Kubernetes and Docker.
- [https://goharbor.io/](https://goharbor.io/)

### skopeo
<img src="https://camo.githubusercontent.com/19ba0305d59474c3cada4b65d5812c8c4c59465c/68747470733a2f2f63646e2e7261776769742e636f6d2f636f6e7461696e6572732f736b6f70656f2f6d61737465722f646f63732f736b6f70656f2e737667" height="100"></br>
<img src="https://img.shields.io/github/stars/containers/skopeo">

skopeo is a command line utility that performs various operations on container images and image repositories. skopeo can work with OCI images as well as the original Docker v2 images.
- [https://github.com/containers/skopeo](https://github.com/containers/skopeo)

## Other / OpenStack
### Kolla
Kolla provides Docker containers, Ansible playbooks to deploy OpenStack on baremetal or virtual machine to meet Kolla's mission. Kolla has out of the box defaults for a working basic deployment, and also implements complete customization. This model permits operators with minimal experience to deploy OpenStack quickly and as the operator's experience grows modify the OpenStack configuration to suit the operator's exact requirements.
- [https://wiki.openstack.org/wiki/Kolla](https://wiki.openstack.org/wiki/Kolla)
- [https://opendev.org/openstack/kolla](https://opendev.org/openstack/kolla)

## Useful Resources
- [The State of Linux Containers](http://www.hpcadvisorycouncil.com/events/2017/stanford-workshop/pdf/Christian_Kniep_StateOfContainers__02082017.pdf)
- [Containers, meet HPC](https://medium.com/@ople/containers-meet-hpc-2aab7aa2d54a#.b23izdadz)
- [Containers and HPC](https://tin6150.github.io/psg/blogger_container_hpc.html)
- [Containers and HPC: Mutually Beneficial](https://containerjournal.com/topics/container-management/containers-hpc-mutually-beneficial/)
- [Containers vs. Unikernels: An Apples-to-Oranges Comparison](https://containerjournal.com/topics/container-ecosystems/containers-vs-unikernels-an-apples-to-oranges-comparison/)
- [Unikernels Use Cases: IoT, the Cloud and More](https://containerjournal.com/features/unikernels-use-cases-iot-cloud/)