from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import socket
import threading
import queue
import time

MAX_BYTES = 1024
serverPort = 67
clientPort = 68


class DHCP_server(object):
    addressPool = []
    for i in range(1, 51):
        addressPool.append(0)
    currentAddr = 0

    def server(self, in_q):

        in_q.put("\nServerul dhcp se initializeaza... offff.. :) \n")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(('', serverPort))
        dest = ('255.255.255.255', clientPort)
        while 1:
            try:
                in_q.put("\n\n1) Astept mesaj discovery de la client :>")
                data, address = s.recvfrom(MAX_BYTES)
                in_q.put("\n2) Am primit mesaj discovery :O")

                in_q.put("\n3) Se trimitere oferta :((")
                data = DHCP_server.offer_get(self)
                s.sendto(data, dest)
                while 1:
                    try:
                        in_q.put("\n4) Astept mesaj request.. :/")
                        data, address = s.recvfrom(MAX_BYTES)
                        in_q.put("\n5) Am primit mesaj request ^^")

                        in_q.put("\n6) Trimit mesaj pack <3")
                        data = DHCP_server.pack_get(self, in_q)
                        s.sendto(data, dest)
                        break
                    except:
                        raise
            except:
                raise

    def offer_get(self):
        OP = bytes([0x02])
        HTYPE = bytes([0x01]) # hardware type - 1 (Ethernet)
        HLEN = bytes([0x06]) # 6 = lungimea in octeti a adresei MAC
        HOPS = bytes([0x00])
        XID = bytes([0x39, 0x03, 0xF3, 0x26]) # transaction ID
        SECS = bytes([0x00, 0x00]) # seconds
        FLAGS = bytes([0x00, 0x00])

        CIADDR = bytes([0x00, 0x00, 0x00, 0x00]) # client's IP address
        for i in range(2, 50):
            if(self.addressPool[i] == 0):
                YIADDR = bytes([0xC0, 0xA8, 0x01, i])
                self.addressPool[i] = 1
                self.currentAddr = i
                break

        SIADDR = bytes([0xC0, 0xA8, 0x01, 0x01])  # 192.168.1.1 - server's IP address
        GIADDR = bytes([0x00, 0x00, 0x00, 0x00])  # 0.0.0.0 - gateway IP address

        # adresa hardware a clientului
        CHADDR1 = bytes([0x00, 0x05, 0x3C, 0x04])
        CHADDR2 = bytes([0x8D, 0x59, 0x00, 0x00])
        CHADDR3 = bytes([0x00, 0x00, 0x00, 0x00])
        CHADDR4 = bytes([0x00, 0x00, 0x00, 0x00])
        CHADDR5 = bytes(192)

        Magiccookie = bytes([0x63, 0x82, 0x53, 0x63])

        DHCPOptions1 = bytes([53, 1, 2])  # DHCP Offer (0x350102)
        DHCPOptions2 = bytes([1, 4, 0xFF, 0xFF, 0xFF, 0x00])  # 255.255.255.0 - subnet mask
        DHCPOptions3 = bytes([3, 4, 0xC0, 0xA8, 0x01, 0x01]) # 192.168.1.1 - router
        DHCPOptions4 = bytes([51, 4, 0x00, 0x01, 0x51, 0x80]) # 86400s(1 day) - IP address lease time
        DHCPOptions5 = bytes([54, 4, 0xC0, 0xA8, 0x01, 0x01])  # DHCP server's address

        # alcatuirea pachetului
        package = OP + HTYPE + HLEN + HOPS + XID + SECS + FLAGS + CIADDR + YIADDR + SIADDR + GIADDR + CHADDR1 + CHADDR2 + \
            CHADDR3 + CHADDR4 + CHADDR5 + Magiccookie + DHCPOptions1 + \
            DHCPOptions2 + DHCPOptions3 + DHCPOptions4 + DHCPOptions5

        return package

    def pack_get(self, in_q):
        OP = bytes([0x02])
        HTYPE = bytes([0x01])
        HLEN = bytes([0x06])
        HOPS = bytes([0x00])
        XID = bytes([0x39, 0x03, 0xF3, 0x26])
        SECS = bytes([0x00, 0x00])
        FLAGS = bytes([0x00, 0x00])
        CIADDR = bytes([0x00, 0x00, 0x00, 0x00])
        YIADDR = bytes([0xC0, 0xA8, 0x01, self.currentAddr])

        SIADDR = bytes([0xC0, 0xA8, 0x01, 0x01])
        GIADDR = bytes([0x00, 0x00, 0x00, 0x00])

        CHADDR1 = bytes([0x00, 0x05, 0x3C, 0x04])
        CHADDR2 = bytes([0x8D, 0x59, 0x00, 0x00])
        CHADDR3 = bytes([0x00, 0x00, 0x00, 0x00])
        CHADDR4 = bytes([0x00, 0x00, 0x00, 0x00])
        CHADDR5 = bytes(192)

        Magiccookie = bytes([0x63, 0x82, 0x53, 0x63])

        DHCPOptions1 = bytes([53, 1, 5])
        DHCPOptions2 = bytes([1, 4, 0xFF, 0xFF, 0xFF, 0x00])
        DHCPOptions3 = bytes([3, 4, 0xC0, 0xA8, 0x01, 0x01])
        DHCPOptions4 = bytes([51, 4, 0x00, 0x01, 0x51, 0x80])
        DHCPOptions5 = bytes([54, 4, 0xC0, 0xA8, 0x01, 0x01])

        in_q.put("\n\nS-a conectat cu succes un client cu adresa: " +
                 '.'.join(str(c) for c in YIADDR))
        
        package = OP + HTYPE + HLEN + HOPS + XID + SECS + FLAGS + CIADDR + YIADDR + SIADDR + GIADDR + CHADDR1 + CHADDR2 + \
            CHADDR3 + CHADDR4 + CHADDR5 + Magiccookie + DHCPOptions1 + \
            DHCPOptions2 + DHCPOptions3 + DHCPOptions4 + DHCPOptions5

        return package
