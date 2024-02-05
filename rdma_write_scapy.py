from scapy.contrib.roce import *
from scapy.all import *

def string_to_bytes_with_padding(input_string, target_length):
    # Convert the string to bytes
    encoded_bytes = input_string.encode('utf-8')
    
    # Check if padding is needed
    if len(encoded_bytes) < target_length:
        # Calculate the number of padding bytes needed
        padding_length = target_length - len(encoded_bytes)
        
        # Add padding using null bytes (b'\x00')
        padded_bytes = encoded_bytes + b'\x00' * padding_length
    else:
        # Truncate the bytes if the length exceeds the target length
        padded_bytes = encoded_bytes[:target_length]

    return padded_bytes

# Example usage:
input_string = "Elie"
target_length = 16
result = string_to_bytes_with_padding(input_string, target_length)

print(len(result))

class RETH(Packet):
    name = "RETH"
    fields_desc = [
        LongField("virtual_address", 0),
        IntField("remote_key", 0),
        IntField("dma_length", 0)
    ]

pkt = Ether(dst='10:70:fd:e5:9a:60', src='06:c5:8f:c0:b9:4e')
pkt = pkt/IP(version=4, ihl=5, id=0x473f, tos=0x2, flags=0x02, frag=0,  ttl=64, dst='192.168.20.1', src='192.168.10.1', len=None)
pkt = pkt/UDP(sport=62528, dport=4791, len=None)
pkt = pkt/BTH(opcode=10, migreq=1, ackreq=1,padcount=3, pkey=0xffff, dqpn=124, psn=0)
pkt = pkt/RETH(virtual_address=40656896, remote_key=2085039, dma_length=13)
pkt = pkt/Raw(load=result)


rdma_pkt = Ether(bytes(pkt))

rdma_pkt.show()

sendp(rdma_pkt, iface="enp8s0")
