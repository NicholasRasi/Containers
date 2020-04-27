"""
NOTE: this version uses sh and the measured times are much greater than using subprocess or time so it is not used
Measure the startup and shutdown time of a container separately
"""

import sh
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("container")
args = parser.parse_args()

# start the netcat server
# nc -l 1234 | hexdump -C
print("Starting netcat server...")
netcat_server_p = sh.hexdump(sh.nc("-l", "1234"), "-C", _bg=True)

startup_durations = []
complete_durations = []

# start the container and the server
print("Starting netcat client")
if args.container == "singularity":
    print("for singularity...")
    start = time.time()
    container_p = sh.nc(sh.singularity("exec", "singularity/myubuntu.sif", "echo", "-n", "'m'"), "-q0", "127.0.0.1", "1234", _bg=True)

# wait for the character
print("Wait server...")
print(netcat_server_p.wait())
end_startup = time.time()

print("Wait client...")
print(container_p.wait())
end_complete = time.time()

startup_durations.append(end_startup - start)
complete_durations.append(end_complete - start)

print(startup_durations)
print(complete_durations)

