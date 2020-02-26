# Firecracker
<img src="https://img.shields.io/github/stars/hpc/charliecloud">
<img src="https://img.shields.io/github/forks/hpc/charliecloud">
<img src="https://img.shields.io/github/issues/hpc/charliecloud">

Firecracker is an open source virtualization technology that is purpose-built for creating and managing secure, multi-tenant container and function-based services.

Until now, you needed to choose between containers with fast startup times and high density, or VMs with strong hardware-virtualization-based security and workload isolation. With Firecracker, you no longer have to choose. Firecracker enables you to deploy workloads in lightweight virtual machines, called microVMs, which provide enhanced security and workload isolation over traditional VMs, while enabling the speed and resource efficiency of containers. Firecracker was developed at Amazon Web Services to improve the customer experience of services like AWS Lambda and AWS Fargate.

Firecracker is a virtual machine monitor (VMM) that uses the Linux Kernel-based Virtual Machine (KVM) to create and manage microVMs. Firecracker has a minimalist design. It excludes unnecessary devices and guest functionality to reduce the memory footprint and attack surface area of each microVM. This improves security, decreases the startup time, and increases hardware utilization. 


### Keywords
container, microVMs, function-based services

### Test
✅ [release 0.21.0](https://github.com/firecracker-microvm/firecracker/releases/tag/v0.21.0) on Ubuntu 18.04

### Compatibility
- Firecracker currently supports Intel CPUs, with AMD and Arm support in developer preview
- Firecracker supports Linux host and guest operating systems with kernel versions 4.14 and above, as well as OSv guests

### Limits

### Security
- Firecracker microVMs use KVM-based virtualizations that provide enhanced security over traditional VMs. This ensures that workloads from different end customers can run safely on the same machine. Firecracker also implements a minimal device model that excludes all non-essential functionality and reduces the attack surface area of the microVM.
- Firecracker is designed to be run securely

### Designed for
- function-based services

### System Requirements and Permissions
- Linux 4.14+
- KVM
- < 125 ms startup time
- < 5 MiB memory footprint

### Available Tools
- Firecracker consists of a single micro Virtual Machine Manager process that exposes an API endpoint to the host once started

### 3rd Party Integration
- Firecracker is integrated with Kata Containers
- Firecracker is integrated with Weave FireKube (via Weave Ignite)
- Firecracker is integrated with containerd via firecracker-containerd
- It's also available within the UniK unikernel and microVM platform
- Firecracker can run Linux and OSv guests

### Other
- Firecracker is written in Rust

### Information
- [https://firecracker-microvm.github.io/](https://firecracker-microvm.github.io/)
- [https://github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)
- [guide](https://github.com/firecracker-microvm/firecracker/blob/master/docs/getting-started.md)