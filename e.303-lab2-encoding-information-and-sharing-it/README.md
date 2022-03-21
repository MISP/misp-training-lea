# e.303: Labs II: Encoding information and sharing it

## Objectives

- Extract an executable from network packet capture file (PCAP) and investigate a compromised Linux host
- Interpret and encode the information into MISP
- Share the evidences with other partners

## Description

- Analyse a network packet capture between a compromised Linux host and a firewall
- Extract evidences
- Pre-encode the event in MISP using multiple ways (manual and/or JSON import in UI)
- Encode the executable and describe what it does
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

## Further reading and tools

- [hashlookup-forensic-analyser](https://github.com/hashlookup/hashlookup-forensic-analyser) Analyse a forensic target (such as a directory) to find and report files found and not found from CIRCL hashlookup public service or the Bloom filter from CIRCL hashlookup. This tool can help a digital forensic investigator to know the context, origin of specific files during a digital forensic investigation.
- [TCPSession is a native Python library](https://github.com/PaloAltoNetworks/tcpsession) that extracts out session data sent over a TCP connection from both sides from a pcap.
- [Towards an estimation of the accuracy of TCP reassembly in network forensics](http://www.foo.be/papers/wagener-dulaunoy-engel-networkforensicaccuracy.pdf)


## Glossary

