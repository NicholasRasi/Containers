# Podman
<img src="https://img.shields.io/github/stars/containers/libpod">
<img src="https://img.shields.io/github/forks/containers/libpod">
<img src="https://img.shields.io/github/issues/containers/libpod">

Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System.

Podman manages the entire container ecosystem which includes pods, containers, container images, and container volumes using the libpod library. Podman specializes in all of the commands and functions that help you to maintain and modify OCI container images, such as pulling and tagging. It allows you to create, run, and maintain those containers created from those images in a production environment.

At a high level, the scope of libpod and Podman is the following:
- Support multiple image formats including the OCI and Docker image formats.
- Support for multiple means to securely download images including trust & image verification.
- Container image management (managing image layers, overlay filesystems, etc).
- Full management of container lifecycle.
- Support for pods to manage groups of containers together.
- Resource isolation of containers and pods.


### Keywords
container, OCI

### Test
✅ [release 1.8.0](https://github.com/containers/libpod/releases/tag/v1.8.0) on Ubuntu 18.04

### Compatibility
- most linux distributions

### Limits

### Security
- Containers can either be run as root or in rootless mode

### Designed for
- Container engine
- HPC

### System Requirements and Permissions
- root to install Podman

### Available Tools

### 3rd Party Integration
- [HPC](https://podman.io/blogs/2019/09/26/podman-in-hpc.html)

### Other

### Information
- [https://podman.io/](https://podman.io/)
- [repo](https://github.com/containers/libpod)