#### 4. Unikernel

A unikernel is a type of microservices environment that contains absolutely everything required to run a particular piece of software—including not just the software code itself, but also the operating system code necessary to host it. Plus, everything that is not strictly necessary for hosting the app is stripped out of the unikernel.

##### Unikernel vs Containers

// TODO

##### Unikernel Advantages

- self-hosted, portable and minimalist
- very small overhead
- suitable for cloud application: unikernel as an alternative to VMs
- suitable for IoT: unikernel provides everything needed to deploy the software for an IoT device
- suitable for device drivers: drivers can be supplied on an as-needed basis inside portable environments
- suitable for on-demand computing: fast to boot

### References

- [Unikernels Use Cases: IoT, the Cloud and More](https://containerjournal.com/features/unikernels-use-cases-iot-cloud/)

---

### 2.4 Unikernel

#### 2.4.1 Firecracker

#### 2.4.2 OSv

#### 2.4.3 MirageOS

#### 2.4.4 Kata Containers

----

## 2.4 Comparing Solutions - Unikernel

### Comparison

|                 | Open Source | First Release | Last Release | Stars | Test   | Issues (open/closed) | Link                                               |
| --------------- | ----------- | ------------- | ------------ | ----- | ------ | -------------------- | -------------------------------------------------- |
| Firecracker     | Yes         | Oct. 2017     | Mar. 2020    | 11.7k | Ok     | 190 / 631            | https://github.com/firecracker-microvm/firecracker |
| OSv             | Yes         | Dec. 2012     | Set. 2019    | 3k    | Not Ok | 313 / 694            | https://github.com/cloudius-systems/osv            |
| MirageOS        | Yes         | Feb. 2013     | Mar. 2020    | 1.4k  | Ok     | 79 / 305             | https://github.com/mirage/mirage                   |
| Kata Containers | Yes         | Dec. 2017     | Mar. 2020    | 421   | -      | 40 / 69              | https://github.com/kata-containers/kata-containers |

### 2.3.1 Firecracker

- https://firecracker-microvm.github.io/
- [**Report**](/reports/firecracker.md)

#### Introduction

Firecracker is an open source virtualization technology that is purpose-built for creating and managing secure, multi-tenant container and function-based services.

Until now, you needed to choose between containers with fast startup times and high density, or VMs with strong hardware-virtualization-based security and workload isolation. With Firecracker, you no longer have to choose. Firecracker enables you to deploy workloads in lightweight virtual machines, called microVMs, which provide enhanced security and workload isolation over traditional VMs, while enabling the speed and resource efficiency of containers. Firecracker was developed at Amazon Web Services to improve the customer experience of services like AWS Lambda and AWS Fargate.

Firecracker is a virtual machine monitor (VMM) that uses the Linux Kernel-based Virtual Machine (KVM) to create and manage microVMs. Firecracker has a minimalist design. It excludes unnecessary devices and guest functionality to reduce the memory footprint and attack surface area of each microVM. This improves security, decreases the startup time, and increases hardware utilization. 

Firecracker consists of a single micro Virtual Machine Manager process that exposes an API endpoint to the host once started

Firecracker is already powering multiple high-volume AWS services including AWS Lambda and AWS Fargate.

#### Requirements and Permissions

- Firecracker currently supports Intel CPUs, with AMD and Arm support in developer preview
- Firecracker supports Linux host and guest operating systems with kernel versions 4.14 and above, as well as OSv guests
- KVM
- < 125 ms startup time
- < 5 MiB memory footprint per microVM

#### Standards

- None

#### Images

Firecracker launches microVMs and is not responsible for images

#### Performance

// TODO

#### Security

- Firecracker microVMs use KVM-based virtualizations that provide enhanced security over traditional VMs. This ensures that workloads from different end customers can run safely on the same machine. Firecracker also implements a minimal device model that excludes all non-essential functionality and reduces the attack surface area of the microVM
- Simple Guest Model: Firecracker guests are presented with a very simple virtualized device model in order to minimize the attack surface: a network device, a block I/O device, a Programmable Interval Timer, the KVM clock, a serial console, and a partial keyboard (just enough to allow the VM to be reset).
- Process Jail: the Firecracker process is jailed using cgroups and seccomp BPF, and has access to a small, tightly controlled list of system calls.
- Static Linking: the firecracker process is statically linked, and can be launched from a jailer to ensure that the host environment is as safe and clean as possible
- Firecracker also ships with a separate jailer used to reduce the blast radius of a compromised VMM process. The jailer isolates the VMM in a chroot, in its own namespaces, and imposes a tight seccomp filter. The filter whitelists system calls by number and optionally limits system-call arguments, such as limiting ioctl() commands to the necessary KVM calls.

###### Reference

- [Firecracker – Lightweight Virtualization for Serverless Computing](https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/)
- [The Firecracker virtual machine monitor](https://lwn.net/Articles/775736/)

#### Available Tools

- Firecracker is integrated with Kata Containers
- Firecracker is integrated with Weave FireKube (via Weave Ignite)
- Firecracker is integrated with containerd via firecracker-containerd
- It's also available within the UniK unikernel and microVM platform
- Firecracker can run Linux and OSv guests

#### Limits

// TODO


### 2.3.2 OSv

- [http://osv.io/](http://osv.io/)
- [**Report**](/reports/osv.md)

#### Introduction

OSv is the versatile modular unikernel designed to run unmodified Linux applications securely on micro-VMs in the cloud. Built from the ground up for effortless deployment and management of micro-services and serverless apps, with superior performance.

Today’s cloud-based applications run a heavyweight stack: the hypervisor, which divides the hardware resources among virtual machines; the operating system, which divides the virtual machine’s resources among applications; and the application server, which divides the application’s resources among the end users.

Clearly, there is a lot of duplication going on. Each layer adds its own overhead in an attempt to abstract away and hide the problems caused by the lower layer. The result is inefficient and complex.

Enter OSv - the operating system for the cloud. On the one hand, designed and optimized to run on a hypervisor. On the other hand, designed to run an application stack without getting in the way. Designed for the cloud.

Features:

- Single address space, ring 0
- Java Virtual Machine integration
- lock-free algorithms
- Interrupt handling in threads
- Van Jacobson style network stack
- State of the art file system

#### Requirements and Permissions

OSv gives you low overhead and rapid turnaround, like containers, but with the deployment flexiblity you only get from true virtualization. With the Capstan build tool, you can build and run with one command, but create a complete virtual machine that will run on your existing cloud environment. Creating a VM image adds only 6-7MB of overhead, three seconds of build time, and a few lines of configuration

OSv supports many managed language runtimes including unmodified JVM, Python 2 and 3, Node.JS, Ruby, Erlang as well as languages compiling directly to native machine code like Golang and Rust.

Limited hardware support: Xen, KVM, and Vmware.

###### Reference

- [http://osv.io/](http://osv.io/)
- [http://osv.io/technology](http://osv.io/technology)

#### Standards

- none

#### Images

ISVs who offer a packaged application as a virtual machine image can benefit in several ways from releasing on OSv. The VM images for OSv-based virtual appliances are small, often only 6-7MB larger than the application itself. And the ISV does not need to maintain and support the large set of software and configuration required by even the simplest guest images on other platforms.

#### Performance

Benchmark for redis and memcached available

###### Reference

- [http://osv.io/benchmarks](http://osv.io/benchmarks)

#### Security

Unikernels  reduce  the  attack  surface  due  to  the  self-containedenvironment  only  enabling  low-level  features

###### Reference

- [A Security Perspective on Unikernels](https://arxiv.org/pdf/1911.06260.pdf)

#### Available Tools

- [Capstan](https://github.com/cloudius-systems/capstan) is a command-line tool for rapidly running your application on OSv unikernel. It focuses on improving user experience when building the unikernel and attempts to support not only a variety of runtimes (C, C++, Java, Node.js etc.), but also a variety of ready-to-run applications (Hadoop HDFS, MySQL, SimpleFOAM etc.).
- available on Amazon EC2 and Google GCE

#### Limits

// TODO


### 2.3.3 MirageOS

- [https://mirage.io/](https://mirage.io/)
- [**Report**](/reports/mirageos.md)

#### Introduction

MirageOS is a library operating system that constructs unikernels for secure, high-performance network applications across a variety of cloud computing and mobile platforms. Code can be developed on a normal OS such as Linux or MacOS X, and then compiled into a fully-standalone, specialised unikernel that runs under a Xen or KVM hypervisor.

This lets your services run more efficiently, securely and with finer control than with a full conventional software stack.

MirageOS uses the OCaml language, with libraries that provide networking, storage and concurrency support that work under Unix during development, but become operating system drivers when being compiled for production deployment. The framework is fully event-driven, with no support for preemptive threading.

###### Reference

- https://mirage.io/wiki/technical-background

#### Requirements and Permissions

- a working OCaml compiler (4.05.0 or higher).
- the OPAM source package manager (2.0.0 or higher).
- an x86_64 or armel Linux host to compile Xen kernels

###### Reference

- [https://github.com/mirage/mirage](https://github.com/mirage/mirage)

#### Standards

#### Images

MirageOS is a 'library operating system' for constructing secure, high-performance network applications across a variety of cloud computing and mobile platforms. It works by treating the Xen hypervisor as a stable hardware platform, allowing us to focus on high-performance protocol implementations without worrying about having to support the thousands of device drivers found in a traditional OS.

#### Performance

#### Security

- the current release contains clean-slate libraries for TLS, TCP/IP, DNS, Xen network and storage device drivers], HTTP, and other common Internet protocols, but all written in a completely type-safe fashion so that they are resistant to attacks such as buffer overflows

###### Reference

- [faq](https://mirage.io/wiki/faq)

#### Available Tools

- [mirage cli](https://github.com/mirage/mirage)

#### Limits

- the unikernel creation process is quite complex
- MirageOS is based around the [OCaml](http://ocaml.org/) language


### 2.3.4 Kata Containers

- [https://katacontainers.io/](https://katacontainers.io/)

#### Introduction

Kata Containers is an open source community working to build a secure container runtime with lightweight virtual machines that feel and perform like containers, but provide stronger workload isolation using hardware virtualization technology as a second layer of defense.

This is because the traditional OCI runtime such as(runC) relies on Linux kernel features, such as cgroups and namespaces to provide isolation when spawning containers. As a result, containers share the same kernel which is usually considered less secure than using traditional virtualisation. In order to deal with the aforementioned challenges the Kata Containers project has been founded.

###### Reference

- [What is Kata Containers](https://ubuntu.com/blog/what-is-kata-containers)

#### Requirements and Permissions

- Kata Containers currently works on systems supporting the following technologies:
  - Intel VT-x technology.
  - ARM Hyp mode (virtualization extension).
  - IBM Power Systems.
  - IBM Z mainframes.
- root permission is needed to check if the system is capable of running Kata containers
- the runtime has a built-in command to determine if your host system is capable of running and creating a Kata Container

#### Standards

- OCI container format
- Kubernetes CRI interface
- legacy virtualization technologies

#### Images

kata-runtime creates a QEMU/KVM virtual machine for each container or pod, the Docker engine or kubelet (Kubernetes) creates respectively

#### Performance

Delivers consistent performance as standard Linux containers; increased isolation without the performance tax of standard virtual machines. 

#### Security

Runs in a dedicated kernel, providing isolation of network, I/O and memory and can utilize hardware-enforced isolation with virtualization VT extensions.

#### Available Tools

- [GPU support](https://github.com/kata-containers/documentation/blob/master/use-cases/GPU-passthrough-and-Kata.md)
- Docker support
- Kubernetes support

#### Limits

List of limitations available [here](https://github.com/kata-containers/documentation/blob/master/Limitations.md)