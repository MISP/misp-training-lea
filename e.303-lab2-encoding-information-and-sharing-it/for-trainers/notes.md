
# Tools and strategies for TCP flow extraction

TCP flow extraction is not trivial and different techniques exist to support TCP flow extraction.

## tcpflow

- `tcpflow -o out -r capture-e.303.cap`

tcpflow is available in standard Linux distribution (maybe older version), latest version is available on the [official repository](https://github.com/simsong/tcpflow) of the author.

Student might have issue with payload containing headers from other protocol. Additional explanation can be shown during the session about the handling of the extract flow (e.g. counting header size).

## Manual approach with wirehark

Student might use wireshark UI to extract the flow manually.

## Additional reading for trainers and student

- [TCPSession is a native Python library](https://github.com/PaloAltoNetworks/tcpsession) that extracts out session data sent over a TCP connection from both sides from a pcap.
- [Towards an estimation of the accuracy of TCP reassembly in network forensics](http://www.foo.be/papers/wagener-dulaunoy-engel-networkforensicaccuracy.pdf)

