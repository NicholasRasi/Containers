# Balena Engine
<img src="https://img.shields.io/github/stars/balena-os/balena-engine">
<img src="https://img.shields.io/github/forks/balena-os/balena-engine">
<img src="https://img.shields.io/github/issues/balena-os/balena-engine">

balenaEngine is a new container engine purpose-built for embedded and IoT use cases and compatible with Docker containers. Based on Docker’s Moby Project, balenaEngine supports container deltas for 10-70x more efficient bandwidth usage, has 3x smaller binaries, uses RAM and storage more conservatively, and focuses on atomicity and durability of container pulling.

Features:
- Small footprint: 3.5x smaller than Docker CE, packaged as a single binary
- Multi-arch support: Available for a wide variety of chipset architectures, supporting everything from tiny IoT devices to large industrial gateways
- True container deltas: Bandwidth-efficient updates with binary diffs, 10-70x smaller than pulling layers
- Minimal wear-and-tear: Extract layers as they arrive to prevent excessive writing to disk, protecting your storage from eventual corruption
- Failure-resistant pulls: Atomic and durable image pulls defend against partial container pulls in the event of power failure
- Conservative memory use: Prevents page cache thrashing during image pull, so your application runs undisturbed in low-memory situations

### Keywords
container, IoT, Edge, Docker

### Test
✅ [release 18.9.13](https://github.com/balena-os/balena-engine/releases/tag/v18.9.13) on Ubuntu 18.04

### Compatibility
- aarch64
- amd64
- armv5e
- armv6l
- armv7hf
- i386

### Limits
- poor documentation
- Some Docker features left out (most needed in cloud deployments and therefore not warranting inclusion in a lightweight IoT-focused container engine):
  - Docker Swarm
  - Cloud logging drivers
  - Plugin support
  - Overlay networking drivers
  - Non-boltdb backed stores (consul, zookeeper, etcd, etc.)

### Security
- from test: root is needed to pull and run containers

### Designed for
- IoT

### System Requirements and Permissions
Compared to the standard Docker container engine:
- 0-70x more efficient bandwidth usage
- has 3.5x smaller binaries
- uses RAM and storage more conservatively
- focuses on atomicity and durability of container pulling

### Available Tools
- [balena-OS](https://www.balena.io/os/): run Docker containers on embedded devices
- [balena ecosystem](https://www.balena.io/what-is-balena)

### 3rd Party Integration
- fully compatible with Docker containers

### Other
- Based on Moby Project technology from Docker

### Information
- [https://www.balena.io/](https://www.balena.io/)
- [https://github.com/balena-os/balena-engine](https://github.com/balena-os/balena-engine)
- [https://www.balena.io/blog/announcing-balena-a-moby-based-container-engine-for-iot/](https://www.balena.io/blog/announcing-balena-a-moby-based-container-engine-for-iot/)
- [docs](https://www.balena.io/engine/docs)
