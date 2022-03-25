# Infrastructure (to be installed before the training)

At minimum, both a dedicated MISP and AIL instances are to be made available for the students and trainers. The below document describes the setup of the installation.

Each individual participant would connect to the MISP instance(s) from their workstations / laptops, where the requirement would simply be having network access (TCP port 80/443 towards the MISP instances) and an Internet browser.

Additionally, students will need to have wireshark installed, or at the very least have system permissions to download and run wireshark, as well as be able to deploy custom extensions for it.
[tcpflow](https://github.com/simsong/tcpflow) and tshark (and some additional Unix tools) are also to be used during the lab exercises, as such a \*nix operating system is highly recommended.

## Hardware and software requirements

MISP and AIL instances are available as [LXC containers](https://linuxcontainers.org/). The host system must be able to run LXC/LXD with the following minimum requirements:

- 64-bit x86 CPU with at least 12 cores (depending of the number of containers, additional cores can provide better performance).
- HVM support must be available (Intel-VT or AMD-V enabled)
- 128GB of memory minimum
- 1Gb/s physical interface - (100 Mbit/s symmetric Internet commitment at minimum) 
- One public IPv4 and IPv6 address
- A minimum of 300GB of available disk space on an SSD

A standard Ubuntu distribution (20.04+) is required.

The server must be a bare metal server, accessible via the Internet and provided by a hosting company located in the EU. 

