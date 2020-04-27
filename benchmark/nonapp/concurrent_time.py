"""
Start a new container until no error occurs
"""
import os
import errno
import time
import argparse
import subprocess
import statistics as stats
import csv

startup_durations = []
stop_durations = []
concurrent_containers = []
stdout = stderr = ""

parser = argparse.ArgumentParser()
parser.add_argument("container")
parser.add_argument("--max", type=int, default=100)
args = parser.parse_args()

# create the folder if not exists
filename = "results/concurrent_" + args.container + ".csv"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

csv_out = open(filename, 'w')
with csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(["timestamp", "type", "complete_time"])

    print("Starting container spawning...")
    for i in range(args.max):
        if args.container == "singularity":
            print("for singularity...")
            cmd = "singularity instance start docker://ubuntu:18.04 n" + str(i)
        elif args.container == "singularity_sif":
            # use a sif file
            print("for singularity sif...")
            cmd = "singularity instance start singularity/ubuntu18.04.sif n" + str(i)
        elif args.container == "charliecloud":
            print("for charliecloud...")
            cmd = "ch-run charliecloud/myubuntu -- echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "docker":
            print("for docker...")
            cmd = "sudo docker run -dit ubuntu:18.04"
        elif args.container == "sarus":
            print("for sarus")
            cmd = "sarus run ubuntu:18.04 echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "podman":
            print("for podman")
            cmd = "podman run -dit ubuntu:18.04"

        start = time.time()
        container_p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # wait for the output
        stdout, stderr = container_p.communicate()
        end = time.time()
        startup_durations.append(end - start)

        # write data
        writer.writerow([time.time(), "start", end - start])

        # convert bytes to string
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        concurrent_containers.append(stdout.strip())
        print(str(len(concurrent_containers)) + ": stdout: " + stdout + ", stderr: " + stderr)

        # exit if error
        if stderr != "" and stderr.find("successfully") == -1:
            break

    print("Stopping containers")
    for i, container in enumerate(concurrent_containers):
        if args.container == "singularity" or args.container == "singularity_sif":
            print("for singularity...")
            cmd = "singularity instance stop n" + str(i)
        elif args.container == "charliecloud":
            print("for charliecloud...")
            cmd = "ch-run charliecloud/myubuntu -- echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "docker":
            print("for docker...")
            cmd = "sudo docker stop " + container
        elif args.container == "sarus":
            print("for sarus")
            cmd = "sarus run ubuntu:18.04 echo -n 'm' | nc -q0 127.0.0.1 1234"
        elif args.container == "podman":
            print("for podman")
            cmd = "podman stop " + container

        start = time.time()
        container_p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # wait for the output
        stdout, stderr = container_p.communicate()
        end = time.time()
        stop_durations.append(end - start)

        # write data
        writer.writerow([time.time(), "stop", end - start])

        # convert bytes to string
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        print(str(i) + ": " + stdout + " " + stderr)

    print("Max concurrent: %d" % len(concurrent_containers))
    print("Startup min/mean/max/std duration: %.4f/%.4f/%.4f/%.4f" % (min(startup_durations),
                                                                      stats.mean(startup_durations),
                                                                      max(startup_durations),
                                                                      stats.stdev(startup_durations)))
    print("Stop min/mean/max/std duration: %.4f/%.4f/%.4f/%.4f" % (min(stop_durations),
                                                                   stats.mean(stop_durations),
                                                                   max(stop_durations),
                                                                   stats.stdev(stop_durations)))