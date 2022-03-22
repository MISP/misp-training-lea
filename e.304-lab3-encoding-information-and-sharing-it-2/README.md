# Isolate Threat Actor(s) from Network Captures - (e.304) - isolate-threat-actor-from-network-capture

# Objectives

- Practice network packet capture analysis;
- Select and extract relevant information from one or more attack(s);
- Model and structure evidences to be encoded and distributed via MISP;
- Add contextualisation and information to transform the analysis into a complete readable story of the attack(s);

# Description

A [packet capture](./dataset/capture.pcap) from the victim network was performed between the reverse proxy and the back-end systems.

- Analyse the pcap file to discover what happened;
- Extract evidences and model those evidences into a complete and descriptive MISP event;

Slides [PDF](https://github.com/MISP/misp-training-lea/blob/main/output/e.304-lab3-encoding-information-and-sharing-it-2.pdf)

# Prerequisites

- MISP introduction (from eLearning materials)
- Module 2.2 and Module 2.3

# Links and references

- [PyMISP](https://github.com/MISP/PyMISP)
- [misp-wireshark](https://github.com/MISP/misp-wireshark)
- [Scapy](https://github.com/secdev/scapy)
- [Minecraft server v1.18](https://launcher.mojang.com/v1/objects/3cf24a8694aca6267883b17d934efacc5e44440d/server.jar), vulnerable to [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)

## Further reading and tools

- https://blogs.juniper.net/en-us/security/in-the-wild-log4j-attack-payloads
- https://github.com/NCSC-NL/log4shell
- https://github.com/pimps/JNDI-Exploit-Kit
