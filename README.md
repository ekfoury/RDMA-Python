# RDMA
This repository contains code for using RDMA with Python. <br>
The code is based on https://github.com/Li-Weihang/python_rdma_test

The difference is that it establishes a connection and keeps running. It then allows sending RDMA READ and WRITE requests using Python Scapy.

# How to run

## Part 1: Establishing the connection
Clone the rdma-core repository: https://github.com/linux-rdma/rdma-core <br>
Follow README.md of rdma-core and then build the project, please make sure pyverbs is compliled successfully. <br><br>

Set PYTHONPATH to let the Python interpreter find where Pyverbs is.<br>
Run rdma_server.py and rdma_client.py.<br>

Server:<br>
PYTHONPATH=../rdma-core/build/python/ python3 rdma_server.py -d mlx5_0 -o write -x 3<br>

Client:<br>
    PYTHONPATH=../rdma-core/build/python/ python3 rdma_client.py -d mlx5_0 -o write -x 3 192.168.xx.xx<br>

## Part 2: Using Scapy to create RDMA READ and WRITE requests
1- Copy the roce.py file to /usr/lib/python3/dist-packages/scapy/contrib/roce.py <br>
sudo cp /home/ubuntu/roce.py /usr/lib/python3/dist-packages/scapy/contrib/roce.py

2- Make sure to modify the values of the queue pair number (dqpn), virtual address, remote key, and dma_length in the rdma_write_scapy.py and rdma_read_scapy.py files. The values can be extracted from the output of Part 1, server side.<b>
python3 rdma_write_scapy.py
python3 rdma_read_scapy.py
