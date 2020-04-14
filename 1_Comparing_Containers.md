# 1. Comparing Containers

### Containers type
1. cloud
2. HPC
3. IoT

### Containers alternative
4. unikernel

#### 1. Cloud
Containers power microservices architecture that have their benefits for application services. Any application built with microservices-based methodology tends to have a chunk of small services that can be packaged in containers. All those services maintain their life cycle along with service-specific requirements of independent development, granular scaling and patching and fault remediation.

##### Containers for Cloud
- **consistent environment**
- **run anywhere**
- **isolation**
- **low overhead**
- **small startup time**
- **service based**
- ...


#### 2. HPC
HPC leverages distributed compute and storage resources to solve complex issues with large data volumes. HPC clusters are commonly known as Supercomputers. Complex algorithms are used on large data sets to generate insights. HPC systems use a large set of CPU or GPU in parallel architecture that creates enough of a computing resource pool to execute complex mathematical algorithms.

HPC are mainly used for scientific research and big data analysis.

##### Containers for HPC
- **modularity**: HPC applications requires software dependencies that are numerous, complex, unusual, differently configured, or simply newer/older than what the center provides
- **scaling**: react to situations when there is a spike in the data processing, scaling the number of container to tackle such spikes
- **portability**: run the application on workstations and other test and development system not managed by the center
- **consistency**: environments can be easily, reliabily, and verifiably reproduced in the future
- **security**: exploit Linux user namespaces to run containers with no privileged operations in a multi-tenant system
- **native performance**: exploit dedicated hardware with less possible overhead
- **support for GPU**
- **support for parallel filesystems and diskless computing nodes**
- **support for workload manager and job scheduler**

##### Docker and HPC issues
- Docker emulates a virtual machine in many aspects, users can escalate to root
- Docker uses a root owned daemon that users can control by means of a writable socket
- can not limit access to local file systems
- no native support for GPU
- no native support for MPI
- incompatibilities with existing scheduling and resource manager paradigms
- HPC is not the appropriate use-case or interest for the Docker community

##### Parallelism and HPC containers
Jobs are dispatched to containers using a workload manager / resource manager (such as Slurm, SGE). Some container technologies provide native support for MPI.


#### 3. IoT
 IoT, refers to network of physical devices collecting and sharing data.

##### Containers for IoT
- **limited network access**: use less bandwidth, downloading only the necessary part
- **heterogeneous devices environments**: support for wide variety of chipset architectures. It also simplify the software configuration
- **minimal hardware resources**: use the resources (memory and computing power) of the device more conservatively. Configuration processing is minimal.
- **use smaller binaries**: reduce the resource consumption

##### Docker and IoT issues
- not suitable for all IoT software deployment
- not compatible with all of the hardware used by IoT
- heavyweight container runtime not suitable for IoT devices with few hardware resources
- not designed to reduce the network bandwidth consumption

### References
- [Containers and HPC: Mutually Beneficial ](https://containerjournal.com/topics/container-management/containers-hpc-mutually-beneficial/)
- [Intel HPC developer conference](https://wilsonweb.fnal.gov/slides/hpc-containers-singularity-introductory.pdf)
- [https://sylabs.io/](https://sylabs.io/)
- [Singularity on HPC](https://singularity.lbl.gov/docs-hpc)
- [https://hpc.github.io/charliecloud/index.html](https://hpc.github.io/charliecloud/index.html)
- [Why the Internet of Things Needs Docker Containers](https://containerjournal.com/features/why-the-internet-of-things-needs-docker-containers/)
- [user namespaces](https://sylabs.io/guides/3.5/admin-guide/user_namespace.html)