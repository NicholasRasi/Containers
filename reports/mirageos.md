# Mirage OS
<img src="https://img.shields.io/github/stars/mirage/mirage">
<img src="https://img.shields.io/github/forks/mirage/mirage">
<img src="https://img.shields.io/github/issues/mirage/mirage">

MirageOS is a library operating system that constructs unikernels for secure, high-performance network applications across a variety of cloud computing and mobile platforms. Code can be developed on a normal OS such as Linux or MacOS X, and then compiled into a fully-standalone, specialised unikernel that runs under a Xen or KVM hypervisor.

This lets your services run more efficiently, securely and with finer control than with a full conventional software stack.

MirageOS uses the OCaml language, with libraries that provide networking, storage and concurrency support that work under Unix during development, but become operating system drivers when being compiled for production deployment. The framework is fully event-driven, with no support for preemptive threading.

### Keywords
container, microVMs, function-based services, unikernel

### Test
✅ [release 3.6.0](https://github.com/mirage/mirage/releases/tag/v3.6.0) on Ubuntu 18.04

### Compatibility
- Hypervisors
  - KVM
  - Xen

### Limits
- the unikernel creation process is quite complex
- MirageOS is based around the [OCaml](http://ocaml.org/) language

### Security

### Designed for
- function-based services

### System Requirements and Permissions
- OPAM 2.0.0 or later
- OCaml 4.05.0 

### Available Tools
- mirage cli

### 3rd Party Integration
- [OCaml](http://ocaml.org/)

### Other

### Information
- [https://mirage.io/](https://mirage.io/)
- [doc](https://mirage.io/docs/)
- [repo](https://github.com/mirage/mirage)