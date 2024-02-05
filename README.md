# RDMA
This repository contains code for using RDMA with Python.
The code is based on https://github.com/Li-Weihang/python_rdma_test

# How to run
Clone the rdma-core repository: https://github.com/linux-rdma/rdma-core
Follow README.md of rdma-core and then build the project, please make sure pyverbs is compliled successfully.

Set PYTHONPATH to let the Python interpreter find where Pyverbs is:
Run rdma_server.py and rdma_client.py.
  Server:
    PYTHONPATH=../rdma-core/build/python/ python3 rdma_server.py -d mlx5_0 -o write -x 3
  Client:
    PYTHONPATH=../rdma-core/build/python/ python3 rdma_client.py -d mlx5_0 -o write -x 3 192.168.xx.xx

