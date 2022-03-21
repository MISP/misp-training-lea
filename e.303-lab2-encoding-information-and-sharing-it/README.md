# e.303: Labs II: Encoding information and sharing it

## Objectives

- Extract files (executables, evidences) from [network packet capture file (PCAP) sample](https://github.com/MISP/misp-training-lea/raw/main/e.303-lab2-encoding-information-and-sharing-it/for-student/capture-e.303.cap) and investigate a compromised Linux host
- Interpret the evidence and encode the information into MISP
- Share the evidences with other partners

## Description

- Analyse a [network packet capture](https://github.com/MISP/misp-training-lea/raw/main/e.303-lab2-encoding-information-and-sharing-it/for-student/capture-e.303.cap) between a compromised Linux host and a firewall
- Extract evidences
- Pre-encode the event in MISP using multiple ways (manual and/or JSON import in UI using [misp-wireshark](https://github.com/MISP/misp-wireshark))
- Encode the executable, steps of the attack and describe what the binaries are used for
- Review the evidences using digital forensic tool such as [hashlookup](https://www.circl.lu/services/hashlookup/)
- Add contextual information based on expanded information and correlation
- From correlations between the provided events and the ones encoded by the students, find more information and correlation about their events

## Prerequisites

- MISP introduction (from eLearning materials)
- Module 2.2 and Module 2.3

## Links and references

- [hashlookup](https://www.circl.lu/services/hashlookup/)
- [hashlookup misp-modules](https://misp.github.io/misp-modules/expansion/#hashlookup)
- [TCP/IP packet demultiplexer](https://github.com/simsong/tcpflow)
- [misp-wireshark](https://github.com/MISP/misp-wireshark)

## Further reading and tools

- [hashlookup-forensic-analyser](https://github.com/hashlookup/hashlookup-forensic-analyser) Analyse a forensic target (such as a directory) to find and report files found and not found from CIRCL hashlookup public service or the Bloom filter from CIRCL hashlookup. This tool can help a digital forensic investigator to know the context, origin of specific files during a digital forensic investigation.
- [TCPSession is a native Python library](https://github.com/PaloAltoNetworks/tcpsession) that extracts out session data sent over a TCP connection from both sides from a pcap.
- [Towards an estimation of the accuracy of TCP reassembly in network forensics](http://www.foo.be/papers/wagener-dulaunoy-engel-networkforensicaccuracy.pdf)

## Glossary

- known files: Files (including indicators) seen in standard operating or software distibution. NSRL or hashlookup are known public list of files.
- TCP reassembly: The act of reconstructing the TCP datagram into a single stream.
