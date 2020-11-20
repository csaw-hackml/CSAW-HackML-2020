# CSAW-HackML-2020

```bash
├── data 
    └── clean_validation_data.h5 // this is clean data used to evaluate the BadNet and design the backdoor defense
    └── clean_test_data.h5
    └── sunglasses_poisoned_data.h5
├── models
    └── anonymous_bd_net.h5
    └── anonymous_bd_weights.h5
    └── sunglasses_bd_net.h5
    └── sunglasses_bd_weights.h5
├── architecture.py
└── eval.py // this is the evaluation script
```

## I. Dependencies
   1. Python 3.6.9
   2. Keras 2.3.1
   3. Numpy 1.16.3
   4. Matplotlib 2.2.2
   5. H5py 2.9.0
   6. TensorFlow-gpu 1.15.2
   
## II. Validation Data
   1. Download the validation and test datasets from [here](https://drive.google.com/drive/folders/13o2ybRJ1BkGUvfmQEeZqDo1kskyFywab?usp=sharing) and store them under `data/` directory.
   2. The dataset contains images from YouTube Aligned Face Dataset. We retrieve 1283 individuals each containing 9 images in the validation dataset.
   3. sunglasses_poisoned_data.h5 contains test images with sunglasses trigger that activates the backdoor for sunglasses_bd_net.h5.

## III. Evaluating the Backdoored Model
   1. The DNN architecture used to train the face recognition model is the state-of-the-art DeepID network. This DNN is backdoored with multiple triggers. Each trigger is associated with its own target label. 
   2. To evaluate the backdoored model, execute `eval.py` by running:  
      `python3 eval.py <clean validation data directory> <model directory>`.
      
      E.g., `python3 eval.py data/clean_validation_data.h5  models/sunglasses_bd_net.h5`.
   3. Clean data classification accuracy on the provided validation dataset for sunglasses_bd_net.h5 is 97.87 %.

## IV. Evaluating the Submissions
To aid teams in designing their defense, here are a few guidelines to keep in mind to get maximum points for the submission:  
   1. Defense should generalize well to other backdoored networks. To verify the defense generalizability, the organizers will evaluate the submission on a specially curated BadNet, anonymous_bd_net.h5, with different trigger properties. 
   2. Teams gain maximum points if the defense greatly reduces attack success rate on the trigger(s) while maintaining high clean classification accuracy.
   3. Points will also be given to teams that identify poisoned images in the online test stream of images.
   4. Fewer points will be allocated to teams that only detect the network as clean or backdoored.
   5. Report should contain a description of the defense performance on adaptive attackers.

