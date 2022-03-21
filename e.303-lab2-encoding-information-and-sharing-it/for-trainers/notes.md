
# Tools and strategies for TCP flow extraction

TCP flow extraction is not trivial and different techniques exist to support TCP flow extraction.

## tcpflow

- `tcpflow -o out -r capture-e.303.cap`

tcpflow is available in standard Linux distribution (maybe older version), latest version is available on the [official repository](https://github.com/simsong/tcpflow) of the author.

Student might have issue with payload containing headers from other protocol. Additional explanation can be shown during the session about the handling of the extract flow (e.g. counting header size).

### An example on how to extract the payload without HTTP headers

![](https://raw.githubusercontent.com/MISP/misp-training-lea/4196850caaaa6187fea41dc3a99d17aad747b35a/e.303-lab2-encoding-information-and-sharing-it/for-trainers/tcp-flow-http-payload.png)

How to extract the payload using `dd`. There are many ways to do it but this is an example for student having issues.

## Manual approach with wirehark

Student might use wireshark UI to extract the flow manually.

## tshark

Extracting flows from a pcap and generating new unique pcap per stream.

~~~~
for stream in `tshark -r capture-e.303.cap -T fields -e tcp.stream | sort -n | uniq`
do
    echo $stream
    tshark -r capture-e.303.cap -w stream-$stream.cap -Y "tcp.stream==$stream"
done
~~~~

## Additional reading for trainers and student

- [TCPSession is a native Python library](https://github.com/PaloAltoNetworks/tcpsession) that extracts out session data sent over a TCP connection from both sides from a pcap.
- [Towards an estimation of the accuracy of TCP reassembly in network forensics](http://www.foo.be/papers/wagener-dulaunoy-engel-networkforensicaccuracy.pdf)

