# Fedora CoreOS
Fedora CoreOS is an automatically updating, minimal, monolithic, container-focused operating system, designed for clusters but also operable standalone, optimized for Kubernetes but also great without it. It aims to combine the best of both CoreOS Container Linux and Fedora Atomic Host, integrating technology like Ignition from Container Linux with rpm-ostree and SELinux hardening from Project Atomic. Its goal is to provide the best container host to run containerized workloads securely and at scale.

Fedora CoreOS is the official successor to CoreOS Container Linux. Fedora CoreOS is a new Fedora Edition built specifically for running containerized workloads securely and at scale. It combines the provisioning tools and automatic update model of Container Linux with the packaging technology, OCI support, and SELinux security of Atomic Host.

### Keywords
container, Kubernetes

### Test
❓ [Fedora ISO 31.20200210.3.0-live](https://getfedora.org/coreos/download/) on VirtualBox
```
Not starting
```

### Compatibility
- AWS
- QEMU or libvirt
- OpenStack
- VMware
- bare metal

### Limits
- Fedora CoreOS is the official successor to CoreOS Container Linux, but it is not a drop-in replacement. CoreOS Container Linux will reach its end of life on May 26, 2020, and will no longer receive updates after that date

### Security

### Designed for
- Normal

### System Requirements and Permissions

### Available Tools
- [Ignition](https://coreos.com/ignition/docs/latest/): Ignition is a new provisioning utility designed specifically for CoreOS Container Linux. At the the most basic level, it is a tool for manipulating disks during early boot. This includes partitioning disks, formatting partitions, writing files (regular files, systemd units, networkd units, etc.), and configuring users. On first boot, Ignition reads its configuration from a source-of-truth (remote URL, network metadata service, hypervisor bridge, etc.) and applies the configuration.

### 3rd Party Integration

### Other

### Information
- [https://getfedora.org/coreos/](https://getfedora.org/coreos/)
- [docs](https://docs.fedoraproject.org/en-US/fedora-coreos/)
