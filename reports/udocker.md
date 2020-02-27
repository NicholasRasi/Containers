# udocker
<img src="https://img.shields.io/github/stars/indigo-dc/udocker">
<img src="https://img.shields.io/github/forks/indigo-dc/udocker">
<img src="https://img.shields.io/github/issues/indigo-dc/udocker">

udocker is a basic user tool to execute simple docker containers in user space without requiring root privileges. Enables download and execution of docker containers by non-privileged users in Linux systems where docker is not available. It can be used to pull and execute docker containers in Linux batch systems and interactive clusters that are managed by other entities such as grid infrastructures or externally managed batch or interactive systems.

udocker does not require any type of privileges nor the deployment of services by system administrators. It can be downloaded and executed entirely by the end user.

udocker is a wrapper around several tools to mimic a subset of the docker capabilities including pulling images and running containers with minimal functionality.

### Keywords
container, Docker, rootless

### Test
✅ [release 1.1.4](https://github.com/indigo-dc/udocker/releases/tag/v1.1.4) on Ubuntu 18.04

### Compatibility

### Limits
- Since root privileges are not involved any operation that really requires such privileges will not be possible. If the containers require such capabilities then docker should be used instead
- The current implementation is limited to the pulling of docker images and its execution. The actual containers should be built using docker and dockerfiles
- udocker does not provide all the docker features, and is not intended as a docker replacement
- udocker is mainly oriented at providing a run-time environment for containers execution in user space. udocker is particularly suited to run user applications encapsulated in docker containers.

### Security
- udocker does not offer robust isolation features such as the ones offered by docker. If the containers content is not trusted then these containers should not be executed with udocker as they will run inside the user environment
- The containers data will be unpacked and stored in the user home directory or other location of choice. Therefore the containers data will be subjected to the same filesystem protections as other files owned by the user. If the containers have sensitive information the files and directories should be adequately protected by the user
- udocker does not require privileges and runs under the identity of the user invoking it
- Users can downloaded udocker and execute it without requiring system administrators intervention
- udocker via PRoot offers the emulation of the root user. This emulation mimics a real root user (e.g getuid will return 0). This is just an emulation no root privileges are involved. This feature makes possible the execution of some tools that do not require actual privileges but which refuse to work if the username or id are not root or 0. This enables for instance software installation using rpm, yum or dnf inside the container
- udocker must not be run by privileged users
- udocker also provides execution with runc and Singularity, these modes make use of rootless namespaces and enable a normal user to execute as root with certain limitations

### Designed for
- execute simple docker containers in user space without requiring root privileges

### System Requirements and Permissions
- udocker does not make use of docker nor requires its presence
- Python dependencies
- Other host libraries and tools are required ([installation manual](https://github.com/indigo-dc/udocker/blob/master/doc/installation_manual.md))

### Available Tools

### 3rd Party Integration
- runC
- Singularity

### Other
- written in Python

### Information
- [https://github.com/indigo-dc/udocker](https://github.com/indigo-dc/udocker)
- [paper](https://arxiv.org/pdf/1711.01758.pdf)