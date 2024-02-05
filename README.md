# RDMA
This repository contains code for using RDMA with Python. <br>
The code is based on https://github.com/Li-Weihang/python_rdma_test

# How to run
Clone the rdma-core repository: https://github.com/linux-rdma/rdma-core <br>
Follow README.md of rdma-core and then build the project, please make sure pyverbs is compliled successfully. <br><br>

Set PYTHONPATH to let the Python interpreter find where Pyverbs is.<br>
Run rdma_server.py and rdma_client.py.<br>

Server:<br>
PYTHONPATH=../rdma-core/build/python/ python3 rdma_server.py -d mlx5_0 -o write -x 3<br>

Client:<br>
    PYTHONPATH=../rdma-core/build/python/ python3 rdma_client.py -d mlx5_0 -o write -x 3 192.168.xx.xx<br>

