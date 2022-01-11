from random import randint
import os
# pentru trimis pachete (cu udp) - folosind wireshark, receptionam pachetul
import socket
import threading
import queue
import time
import struct  # cu functia struct.pack() combinam octetii specifici unui mesaj dhcp intr-un pachet
# vom creea clasa packet, cu campuri ce corespund fiecarui parametru din cadrul unui pachet. la final, vom "impacheta" acesti parametri intr-un singur sir de octeti cu functia struct.pack()

#  class packet():
#    def __init__(self, PAD, SUBNET_MASK, ROUTER, DOMAIN_SERVER,
#                  HOST_NAME, BROADCAST_ADDRESS, ADDRESS_REQUEST,
#                  LEASE_TIME, DHCP_MESSAGE_TYPE, RENEWAL_TIME, CLIENT_ID, END):

#         self.PAD = PAD
#         self.SUBNET_MASK = SUBNET_MASK
#         self.ROUTER = ROUTER
#         self.DOMAIN_SERVER = DOMAIN_SERVER
#         self.HOST_NAME = HOST_NAME
#         self.BROADCAST_ADDRESS = BROADCAST_ADDRESS
#         self.ADDRESS_REQUEST = ADDRESS_REQUEST
#         self.LEASE_TIME = LEASE_TIME
#         self.DHCP_MESSAGE_TYPE = DHCP_MESSAGE_TYPE
#         self.RENEWAL_TIME = RENEWAL_TIME
#         self.CLIENT_ID = CLIENT_ID
#         self.END = END

#     def assembly(self, mesaj):
#         self.PAD = 0
#         self.SUBNET_MASK = (15 << 28) & mesaj
#         self.ROUTER = (15 << 24) & mesaj
#         self.DOMAIN_SERVER = (15 << 20) & mesaj
#         self.HOST_NAME = (1 << 19) & mesaj
#         self.BROADCAST_ADDRESS = (15 << 15) & mesaj
#         self.ADDRESS_REQUEST = (15 << 14) & mesaj
#         self.LEASE


def DISCOVERY():
    def __init__(self, data, transID):
        self.data = data
        self.transID = transID
        self.offerIP = ''
        self.nextServerIP = ''
        self.DHCPServerIdentifier = ''
        self.leaseTime = ''
        self.router = ''
        self.subnetMask = ''
        self.DNS = []
        self.unpack()

    #PAD = 0

    # -------10 OPTIONS-------

    #SUBNET_MASK = 1
    #ROUTER = 3
    #DOMAIN_SERVER = 6
    #HOST_NAME = 12
    #BROADCAST_ADDRESS = 28
    #ADDRESS_REQUEST = 50
    #LEASE_TIME = 51
    #DHCP_MESSAGE_TYPE = 53
    #RENEWAL_TIME = 58
    #CLIENT_ID = 61

    # ------------------------
    #END = 255
    pass

# optiuni: tipul pachetului (D/O/R/A), sfarsitul pachetului (0xFF), masca de retea, adresa de gateway (comunicat in ext retelei), adresa de serere dns


class DHCP_Offer:
    def __init__(self):


if __name__ == '__main__':
    print('Hello world')
    # serverDHCP.run()
