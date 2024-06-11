# cityscapeGH

## Introduction


## Prerequisites
- Linux or macOS
- Python 3
- NVIDIA GPU (11G memory or larger) + CUDA cuDNN (optional)

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

## Reference
```
@inproceedings{isola2017image,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
  year={2017}
}

@inproceedings{wang2018pix2pixHD,
  title={High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs},
  author={Ting-Chun Wang and Ming-Yu Liu and Jun-Yan Zhu and Andrew Tao and Jan Kautz and Bryan Catanzaro},  
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2018}
}
```

## Acknowledgments
This project is heavily based on [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) and [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).
