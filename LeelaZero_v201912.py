# -*- coding: utf-8 -*-
"""LeelaZero_v201912.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y4HUEv-1LheUByP5ps_0pTS5epbu0mks

This notebook shows how to run a **Leela Zero client on Google Colab's NVIDIA Tesla K80 GPU**. Thanks to [djinnome from GitHub who figured it out.](https://github.com/glinscott/leela-chess/issues/284).

Updated to work with NVIDIA driver 396.44.

Run each cell in order, waiting for the previous one to finish before running the next.

The scripts and cell layout may be messy/redundant, but this should work.
"""

import subprocess
if subprocess.run(["nvidia-smi", "-L"]).returncode != 0:
  assert False, "No GPU available!"

!apt-get update
!apt-get install -y --fix-missing --no-install-recommends cuda-compiler-9-2 cuda-cublas-dev-9-2 cuda-cudart-dev-9-2

!wget http://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-9.2-linux-x64-v7.3.1.20.tgz
!cd /usr/local && tar -xzvf /content/cudnn-9.2-linux-x64-v7.3.1.20.tgz
!chmod a+r /usr/local/cuda/lib64/libcudnn*

"""If you get a **"signal: aborted (core dumped)" error** when running the client or **"failed to assign a backend" popup**, there are no GPUs available on Google Colab. **Try Runtime -> Restart Runtime** and running again, or kill the entire VM with **`!kill -9 -1`** and try again (VM may take 5 minutes to restart after being killed). As Google Colab has a limited number of free GPUs, **you may just have to try again another time**."""

#!kill -9 -1

!apt install cmake g++ libboost-dev libboost-program-options-dev libboost-filesystem-dev opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev zlib1g-dev

!rm -rf leela-zero
!git clone --recursive https://github.com/leela-zero/leela-zero
!cd leela-zero

!cd leela-zero && mkdir build
!cd leela-zero/build && cmake ..

!cd leela-zero/build && cmake --build .

!cd leela-zero/build && chmod +x tests
!cd leela-zero/build/&& ./tests

!cd leela-zero/build && cp leelaz autogtp
!echo "done!"

"""Until now, LeelaZero has been compiled. Congratulations!
Then we can contribute to LZ project by running code blocks below.
"""

!cd leela-zero/build/autogtp/ && ./autogtp