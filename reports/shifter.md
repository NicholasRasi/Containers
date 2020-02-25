# Shifter
<img src="https://img.shields.io/github/stars/NERSC/shifter">
<img src="https://img.shields.io/github/forks/NERSC/shifter">
<img src="https://img.shields.io/github/issues/NERSC/shifter">

NERSC has developed and supports Shifter to enable users to securely run Docker images on NERSC systems at scale. A user can use Shifter to easily pull down an image from a registry like DockerHub and then run that image on systems.

Design Goals:

- User independence: Require no administrator assistance to launch an application inside an image
- Shared resource availability (e.g., file systems and network interfaces)
- Leverages or integrates with public image repos (i.e. DockerHub)
- Seamless user experience
- Robust and secure implementation

Shifter works by converting Docker images to a common format that can then be efficiently distributed and launched on HPC systems. The user interface to shifter enables a user to select an image from their dockerhub account or the NERSC private registry and then submit jobs which run entirely within the container.

Shifter works by enabling users to pull images from a DockerHub or private docker registry. An image manager at NERSC then automatically converts the image to a flattened format that can be directly mounted on the compute nodes. This image is copied to the Lustre scratch filesystem (in a system area). The user can then submit jobs specifying which image to use. Private images are only accessible by the user that authenticated and pulled them, not by the larger community. In the job the user has the ability to either run a custom batch script to perform any given command supported by the image, or if a Docker entry-point is defined, can simply execute the entry-point.

### Keywords
container, HPC, Docker

### Test
❓ [release 18.03.0](https://hub.docker.com/r/scanon/shifterbox/tags) Shifter-in-a-box on Ubuntu 18.04
```
[auser@7a02a401a40e /]$ shifterimg pull busybox
ERROR: failed to contact the image gateway.
```

### Compatibility
- RHEL/Centos/Scientific Linux 7

### Limits
- born around the NERSC systems
- Image read-only on the Computational Platform
- Image modified at container construction time
- requires the installation of 3 components

### Security
- User runs as the user in the container, not root

### Designed for
- HPC (e.g. MPI)

### System Requirements and Permissions

### Available Tools
Components:

- Shifter Image Gateway: Imports and converts images from DockerHub and Private Registries
- Shifter Runtime: Instantiates images securely on compute resources
- Work Load Manager Integration: Integrates Shifter with WLM

### 3rd Party Integration
- Shifter has the ability to automatically allow communication between nodes using the high-speed Aries network

### Other

### Information
- [https://github.com/NERSC/shifter](https://github.com/NERSC/shifter)
- [https://www.nersc.gov/research-and-development/user-defined-images/](https://www.nersc.gov/research-and-development/user-defined-images/)
- [https://docs.nersc.gov/programming/shifter/overview/](https://docs.nersc.gov/programming/shifter/overview/)
- [paper](/papers/cug2015udi.pdf)
- [tutorial](https://github.com/NERSC/Shifter-Tutorial)
- [slides](https://drive.google.com/drive/folders/1LWuV6W5Gx6mdAuZAKCZvad5exf9we10f)