# Infrastructure (to be installed before the training)

At minimum, a dedicated MISP instance and AIL instance are to be made available for the students and trainers. The below document describes the setup of the installation.

Each individual participant would connect to the MISP instance(s) from their workstations / laptops, where the requirement would simply be network access (TCP port 80/443 towards the MISP instances) and an Internet browser.

Additionally, students will need to have wireshark installed or at the very least have system permissions to download and run wireshark as well as deploy custom extensions for it.
[tcpflow](https://github.com/simsong/tcpflow) and tshark (and some additional Unix tools) are also to be used during the lab exercises, as such a \*nix operating system is highly recommended.

## Hardware and software requirements

MISP and AIL instances are available as [LXC container](https://linuxcontainers.org/). The host system must be able to run LXC/LXD with the following minimal requirements:

- 64-bit x86 CPU with at least 4 cores (depending of the number of container, additional cores can provide better performance).
- HVM support must be included (Intel-VT or AMD-V enabled)
- 32GB of memory minimum
- 100 Mbit/s Internet connectivity
- One public IPv4 address

A standard Ubuntu distribution (20.04+) is required.

The server must be a bare metal server accessible via Internet and provided by a hosting company located in EU. 

