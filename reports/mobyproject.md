# Moby Project
<img src="https://img.shields.io/github/stars/moby/moby">
<img src="https://img.shields.io/github/forks/moby/moby">
<img src="https://img.shields.io/github/issues/moby/moby">

Moby is an open framework created by Docker to assemble specialized container systems without reinventing the wheel. It provides a “lego set” of dozens of standard components and a framework for assembling them into custom platforms. At the core of Moby is a framework to assemble specialized container systems which provides:

- Components: a library of containerized components for all vital aspects of a container system: OS, container runtime, orchestration, infrastructure management, networking, storage, security, build, image distribution, etc.
- Tools: tools to assemble the components into runnable artifacts for a variety of platforms and architectures: bare metal (both x86 and Arm); executables for Linux, Mac and Windows; VM images for popular cloud and virtualization providers.
- Assemblies: a set of reference assemblies which can be used as-is, modified, or used as inspiration to create your own. All Moby components are containers, so creating new components is as easy as building a new OCI-compatible container.

Moby is an open project guided by strong principles, aiming to be modular, flexible and without too strong an opinion on user experience. It is open to the community to help set its direction.

- Modular: the project includes lots of components that have well-defined functions and APIs that work together.
- Batteries included but swappable: Moby includes enough components to build fully featured container system, but its modular architecture ensures that most of the components can be swapped by different implementations.
- Usable security: Moby provides secure defaults without compromising usability.
- Developer focused: The APIs are intended to be functional and useful to build powerful tools. They are not necessarily intended as end user tools but as components aimed at developers. Documentation and UX is aimed at developers not end users.


### Keywords
container, Docker, modularity

### Test
❌ [release 19.03.6](https://github.com/moby/moby/releases/tag/v19.03.6) on Ubuntu 18.04
```
Makefile:157: recipe for target 'build' failed
make: *** [build] Error 137
```

### Compatibility

### Limits
- no documentation

### Security

### Designed for
- engineers, integrators and enthusiasts looking to modify, hack, fix, experiment, invent and build systems based on containers

### System Requirements and Permissions

### Available Tools
- [LinuxKit](https://github.com/linuxkit/linuxkit): A toolkit for building secure, portable and lean operating systems for containers

### 3rd Party Integration

### Other

### Information
- [https://github.com/moby/moby](https://github.com/moby/moby)
- [Introducing Moby Project](https://www.docker.com/blog/introducing-the-moby-project/)