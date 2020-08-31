# CSAW-HackML-2020

```bash
./Backdoor-Example/
├── data
│   ├── cifar10
│   │   └── valid.h5 // this is clean data used for designing your defense (validation)
│   ├── gtsrb
│   │   └── valid.h5 // this is clean data used for designing your defense (validation)
│   ├── mnist
│   │   └── valid.h5 // this is clean data used for designing your defense (validation)
│   ├── youtube
│   │   └── valid.h5 // this is clean data used for designing your defense (validation)
├── eval.py // this is the evaluation script
└── models
    └── A
        └── bd_net.h5
        └── bd_weights.h5
    └── B
        └── bd_net.h5
        └── bd_weights.h5
    └── C
        └── bd_net.h5
        └── bd_weights.h5
    └── D
        └── bd_net.h5
        └── bd_weights.h5
    └── E
        └── bd_net.h5
        └── bd_weights.h5
    └── F
        └── bd_net.h5
        └── bd_weights.h5
    └── G
        └── bd_net.h5
        └── bd_weights.h5
```

## I. Dependencies
   1. Python 3.6.9
   2. Keras 2.3.1
   3. Numpy 1.16.3
   4. Matplotlib 2.2.2
   5. H5py 2.9.0
   6. TensorFlow-gpu 1.15.2
   
## II. Backdoored Models Description
   A - Feature Space Attack on German Traffic Sign Recognition Benchmarck (GTSRB) Dataset \n
   B - Trigger Combination Attack on CIFAR-10 Dataset
   C - Clean Label Attack on MNIST Dataset
   D - Multi-Trigger Single-Target Attack on YouTube Face Dataset
   E - Multi-Trigger Multi-Target Attack on YouTube Face Dataset
   F - All-All Attack on MNIST Dataset
   G - Moving trigger on YouTube Face Dataset

## III. Evaluating the backdoored model
   1. Download the validation data from [here](https://drive.google.com/drive/folders/13o2ybRJ1BkGUvfmQEeZqDo1kskyFywab?usp=sharing) and store the data in `data/<dataset filename>/valid.h5` directory.
   2. To evaluate a specific model, execute `eval.py` by running
      `python3 eval.py <clean validation data filename> <backdoored model filename> <model name>`.
      
      E.g., `python3 eval.py data/mnist/valid.h5  models/F/bd_net.h5 F`.
   3. Clean data classification accuracy will be printed.
