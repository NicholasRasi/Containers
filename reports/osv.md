# OSv
<img src="https://img.shields.io/github/stars/cloudius-systems/osv">
<img src="https://img.shields.io/github/forks/cloudius-systems/osv">
<img src="https://img.shields.io/github/issues/cloudius-systems/osv">


OSv is the versatile modular unikernel designed to run unmodified Linux applications securely on micro-VMs in the cloud. Built from the ground up for effortless deployment and management of micro-services and serverless apps, with superior performance.

Today’s cloud-based applications run a heavyweight stack: the hypervisor, which divides the hardware resources among virtual machines; the operating system, which divides the virtual machine’s resources among applications; and the application server, which divides the application’s resources among the end users. 

Clearly, there is a lot of duplication going on. Each layer adds its own overhead in an attempt to abstract away and hide the problems caused by the lower layer. The result is inefficient and complex.

Enter OSv - the operating system for the cloud. On the one hand, designed and optimized to run on a hypervisor. On the other hand, designed to run an application stack without getting in the way. Designed for the cloud.

### Keywords
container, microVMs, function-based services

### Test
✅❓ [Capstan release 0.4.1](https://github.com/cloudius-systems/capstan/releases/tag/v0.4.1) on Ubuntu 18.04
```
capstan runs but there was problems with packaging NodeJS app
```

### Compatibility
- Language runtimes:
    - JVM
    - Python 2 and 3
    - Node.JS
    - Ruby
    - Erlang
    - Golang
    - Rust
- Run on
  - Amazon EC2
  - GCE
- Hypervisors
  - KVM
  - Xen


### Limits

### Security

### Designed for
- function-based services

### System Requirements and Permissions
- 6-7MB of overhead
- 3 seconds of build time
- few lines of configuration

### Available Tools
- Capstan is a tool for rapidly building and running your application on OSv. Capstan is as simple and fast as using Docker for creating containers, but the result is a complete virtual machine image that will run on any hypervisor with OSv support
- [OSv dashboard](https://github.com/cloudius-systems/osv/wiki/OSv-Dashboard)

### 3rd Party Integration
- Firecracker

### Other

### Information
- [http://osv.io/](http://osv.io/)
- [https://github.com/cloudius-systems/osv](https://github.com/cloudius-systems/osv)
- [capstan example](https://github.com/cloudius-systems/capstan-example)
- [wiki](https://github.com/cloudius-systems/osv/wiki)