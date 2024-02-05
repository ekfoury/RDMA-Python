from scapy.contrib.roce import *
from scapy.all import *

class RETH(Packet):
    name = "RETH"
    fields_desc = [
        LongField("virtual_address", 0),
        IntField("remote_key", 0),
        IntField("dma_length", 0)
    ]

pkt = Ether(dst='10:70:fd:e5:9a:60', src='06:c5:8f:c0:b9:4e')
pkt = pkt/IP(version=4, ihl=5, id=0x473f, tos=0x2, flags=0x02, frag=0,  ttl=63, src='192.168.10.1', dst='192.168.20.1', len=None)
pkt = pkt/UDP(sport=63491, dport=4791, len=None)
pkt = pkt/BTH(opcode=12, migreq=1, padcount=0, pkey=0xffff, dqpn=126, psn=23)
pkt = pkt/RETH(virtual_address=24502272, remote_key=2085039, dma_length=13)
        


rdma_pkt = Ether(bytes(pkt))

rdma_pkt.show()

sendp(rdma_pkt, iface="enp8s0")
