import os
import sys

[this_file_name, command, target, hostname, root_dir] = sys.argv

commands = [f"hostname {hostname}", "mount -t proc proc /proc", target]

if command == "start":
    os.system(
        f"unshare -mup python3 {this_file_name} run {target} {hostname} {root_dir}"
    )
if command == "run":
    os.chroot(root_dir)
    os.chdir("/")
    os.system(" && ".join(commands))
