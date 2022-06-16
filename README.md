# Vegetable_fruit_detect

This repositroy holds the source code for fruit and vegetable recoginition using deep learning.
The important packges used are Tensorflow, keras and opencv

## Lets get started

### Step:1
Clone the repo:
```
git clone https://github.com/vanarp0915/Vegetable_fruit_detect.git
```

### Step:2
```
cd Vegetable_fruit_detect.git
```

### Step:3
Install all the pip dependence
```
pip install -r requirement.txt
```

### Step:4
*Collecting the dataset
In this process you need to run image_collecting.py to collect the image of respective fruit or vegetables.

*Eg
```
python3 image_collecting.py apple 50
```
### Step:5

Train the dataset
```
python train.py
```
At the end of the excecusion a FV.h5 file will be created. Which we will be having the weights.

### Step:6
Run the classifcation code
```
python Fruits_Vegetable_Classification.py
```

