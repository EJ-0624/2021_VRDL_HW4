# 2021_VRDL_HW4

## Environment

* Ubuntu 18.04.5 LTS
* torch 1.10.0
* cuda 11.1

```setup
# Check cuda -version
nvcc -V
nvidia-smi
```

## Requirements

Install the corresponding cuda version of pytorch
```setup
# CUDA 11.1
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

To install requirements:

```setup
pip install -r requirements.txt
```

## Split train / valid sets

```setup
python spit_train_valid.py ## change your root
```

![image](https://user-images.githubusercontent.com/68366624/149309743-c15f4879-0f0e-41b3-876f-05580dc03d35.png)


## Training

```setup
python train.py --device 0 --batch-size 8 --img 640 640 --data hw2.yaml --cfg cfg/hw2.cfg --weights 'hw2.weights' --name hw2 --epoch 60 
```

## Weight for Training Model

You can download the file here:

- [The file of weight](https://drive.google.com/file/d/1Go2_ixu8RgZDY0FAF8x_qCNmLB78sGZW/view?usp=sharing)

https://drive.google.com/drive/folders/16NrVpoWSmGRY2b0zTNnAWrmJYS-2YuPr?usp=sharing
