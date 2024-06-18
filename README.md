# cityscapeGH

## Introduction
cityscapeGH aims to integtate generative models in Grasshopper (GH) workflow 
to create the reimagination of urban landscape based on 3D reconstructions in Rhino3D space. 

## Prerequisites
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU (11G memory or larger) + CUDA cuDNN

## Getting Started
### Installation
- Create a virtual envi with conda (recommended)
- Install PyTorch from http://pytorch.org
- Install Rhino6 or later
- Clone this repo:
```bash
git clone https://github.com/billbillbilly/cityscapeGH
cd cityscapeGH
```
- Download the checkpoint in `./cityscapeGH/src/pix2pix_model/checkpoints/pix2pix` from [here](https://huggingface.co/xiaohaoy/cityscapes_pix2pix_512_1024/resolve/main/latest_net_G.pth?download=true)

### Setup in Grasshopper
- set work directory (it shuold be this repo)
- set python path (it may be the conda envi). To find the path of python:
```bash
# which python{version}
which python3.10
```

## Note
Current project only applies basic pix2pix model trained on cityscapes dataset.
More models such stable diffusion will be available in the near future.

## Reference
```
@inproceedings{isola2017image,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
  year={2017}
}

@inproceedings{Cordts2016Cityscapes,
title={The Cityscapes Dataset for Semantic Urban Scene Understanding},
author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},
booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
year={2016}
}
```

## Acknowledgments
This project is heavily based on [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).
