from random import randint
import os
import socket # pentru trimis pachete (cu udp) - folosind wireshark, receptionam pachetul
import threading
import queue
import time
import struct # cu functia struct.pack() combinam octetii specifici unui mesaj dhcp intr-un pachet
# vom creea clasa packet, cu campuri ce corespund fiecarui parametru din cadrul unui pachet. la final, vom "impacheta" acesti parametri intr-un singur sir de octeti cu functia struct.pack()

packet = b''
#optiuni: tipul pachetului (D/O/R/A), sfarsitul pachetului (0xFF), masca de retea, adresa de gateway (comunicat in ext retelei), adresa de serere dns
class DHCP_Offer:
    def __init__(self):


if __name__ == '__main__':
    print('Hello world')
    # serverDHCP.run()

