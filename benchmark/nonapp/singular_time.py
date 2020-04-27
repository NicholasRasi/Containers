"""
Measure the startup and shutdown time of a container separately
"""
import os
import errno
import time
import argparse
import subprocess
import statistics as stats
import csv

startup_durations = []
complete_durations = []

parser = argparse.ArgumentParser()
parser.add_argument("container")
parser.add_argument("--repeat", type=int, default=10)
args = parser.parse_args()

# create the folder if not exists
filename = "results/singular_" + args.container + ".csv"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

csv_out = open(filename, 'w')
with csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(["timestamp", "start_time", "complete_time"])

    for repeat in range(args.repeat):
        # start the netcat server
        print(str(repeat) + " starting netcat server...")
        cmd = "nc -l 1234 | hexdump -C"
        netcat_server_p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # start the container and the server
        print("Starting netcat client")
        if args.container == "singularity":
            # pull image from docker
            print("for singularity...")
            cmd = "singularity exec docker://ubuntu:18.04 echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "singularity_sif":
            # use a sif file
            print("for singularity sif...")
            cmd = "singularity exec singularity/ubuntu18.04.sif echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "charliecloud":
            print("for charliecloud...")
            cmd = "ch-run charliecloud/myubuntu -- echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "docker":
            print("for docker...")
            cmd = "sudo docker run -it ubuntu:18.04 echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "sarus":
            print("for sarus")
            cmd = "sarus run ubuntu:18.04 echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "podman":
            print("for podman")
            cmd = "podman run ubuntu:18.04 echo -n 'm' | nc -q0 127.0.0.1 1234"

        # start the process (non blocking)
        start = time.time()
        container_p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # wait for the character
        print("Wait server...")
        print(netcat_server_p.communicate()[0])
        end_startup = time.time()

        print("Wait client...")
        print(container_p.communicate()[0])
        end_complete = time.time()

        # write data
        writer.writerow([time.time(), end_startup - start, end_complete - start])

        startup_durations.append(end_startup - start)
        complete_durations.append(end_complete - start)

        time.sleep(1)

    print("Startup min/mean/max/std duration: %.4f/%.4f/%.4f/%.4f" % (min(startup_durations),
                                                                      stats.mean(startup_durations),
                                                                      max(startup_durations),
                                                                      stats.stdev(startup_durations)))
    print("Startup + shutdown min/mean/max/std duration: %.4f/%.4f/%.4f/%.4f" % (min(complete_durations),
                                                                                 stats.mean(complete_durations),
                                                                                 max(complete_durations),
                                                                                 stats.stdev(complete_durations)))
