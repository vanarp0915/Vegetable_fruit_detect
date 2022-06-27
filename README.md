# Vegetable_fruit_detect

This repositroy holds the source code for fruit and vegetable recoginition using deep learning.
The important packges used are Tensorflow, keras and opencv

## Lets get started


### Step:1
Create a virtual environment and activate the virtual environment
```
python -m venv venv
```
```
cd venv
```
```
source ./bin/activate
```

### Step:2
Clone the repo:
```
git clone https://github.com/vanarp0915/Vegetable_fruit_detect.git
```

### Step:3
Enter inside the folder
```
cd Vegetable_fruit_detect.git
```

### Step:4
Install all the pip dependence
```
pip install -r requirement.txt
```

### Step:5
* Collecting the dataset
In this process you need to run image_collecting.py to collect the image of respective fruit or vegetables.

*Eg
```
python image_collecting.py apple 50
```
### Step:6

Train the dataset
```
python train_model.py
```
At the end of the excecusion a FandV.h5 file will be created. Which we will be having the weights.

### Step:7
Run the classifcation code
```
python run.py
```

