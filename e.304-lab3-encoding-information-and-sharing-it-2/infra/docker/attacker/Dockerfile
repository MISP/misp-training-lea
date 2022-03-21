FROM openjdk:8-jdk-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    python3 \
    python3-pip \
    maven \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Install mbechler/marshalsec
RUN git clone https://github.com/mbechler/marshalsec.git
RUN cd marshalsec/ && mvn clean package -DskipTests 

# Copy java exploit
COPY poc.java poc/poc.java

# Install pyCraft
RUN git clone https://github.com/ammaraskar/pyCraft.git
RUN cd pyCraft && pip3 install -r requirements.txt
COPY minecraft-log4shell.py ./minecraft-log4shell.py

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
