cd docker
sudo docker build --tag myubuntu:18.04 .
sudo docker run -it myubuntu:18.04 echo "Docker container"

cd ..
cd singularity
sudo singularity build ubuntu18.04.sif ubuntu18.04.def
singularity exec ubuntu18.04.sif echo "Singularity container"


cd ..
cd podman
podman build --tag myubuntu:18.04 .
podman run -it myubuntu:18.04 echo "Podman container"

cd ..
cd charliecloud
ch-build -t myubuntucc .
ch-builder2tar myubuntucc .
ch-tar2dir myubuntucc.tar.gz .
ch-run myubuntucc -- echo "Charliecloud container"

cd ..
cd sarus
sarus pull ubuntu:18.04
sarus run ubuntu:18.04 echo "Sarus container"