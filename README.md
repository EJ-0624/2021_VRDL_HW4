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
python main_train_pnsr.py --opt train_swinir_sr_vrdl.json
```

## Weight for Training Model

You can download the file here:

- [The file of weight](https://drive.google.com/file/d/1Go2_ixu8RgZDY0FAF8x_qCNmLB78sGZW/view?usp=sharing)

## Testing

```setup
python main_test_swinir.py --model_path  superresolution/swinir_sr_lightweight_x3/models/285000_G.pth --task lightweight_sr --scale 3 --folder_lq datasets/testing_lr_images 
```

## Testing Result

![image](https://user-images.githubusercontent.com/68366624/149310592-1ea3eb32-4777-4154-865c-2fdd6cecf7cc.png)


![image](https://user-images.githubusercontent.com/68366624/149310460-59120095-1cec-4182-82dc-971d0cc516c1.png)

## Google Drive link

This contains all the files that need to be used.
- [Google Drive](https://drive.google.com/drive/folders/16NrVpoWSmGRY2b0zTNnAWrmJYS-2YuPr?usp=sharing)
