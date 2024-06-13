This is the implementation of Computer Graphics Lab3 of Fudan University

by 邓钧愉-21307140005， 窦翊轩-21307140006，查翔-21307140052，彭恺欣-21307140077

## Installation
For environmental setup, follow the original requirements of [3DGS](https://github.com/graphdeco-inria/gaussian-splatting). 

## Training
To train 3D Gaussians Splatting with our strategy, all you need to do is:
```bash
python train.py -s {dataset_path} --exp_name {exp_name} --eval --ours_new 
```

For dense-small-variance (DSV) random initialization (used in the original 3D Gaussian Splatting), you can simply run with the following command:
```bash
python train.py -s {dataset_path} --exp_name {exp_name} --eval --paper_random
```

For SfM (Structure-from-Motion) initialization (used in the original 3D Gaussian Splatting), you can simply run with the following command:
```bash
python train.py -s {dataset_path} --exp_name {exp_name} --eval
```

For Noisy SfM initialization (used in the original 3D Gaussian Splatting), you can simply run with the following command:
```bash
python train.py -s {dataset_path} --exp_name {exp_name} --eval --train_from 'noisy_sfm'
```

## Acknowledgement

We would like to acknowledge the contributions of [3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) for open-sourcing the official codes for 3DGS! 
