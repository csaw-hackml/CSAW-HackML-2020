import keras
import sys
import h5py
import numpy as np

clean_data_filename = str(sys.argv[1])
model_filename = str(sys.argv[2])
model_name = str(sys.argv[3])

def data_loader(filepath):
    data = h5py.File(filepath, 'r')
    x_data = np.array(data['data'])
    y_data = np.array(data['label'])
    
    return x_data, y_data

def data_preprocess(x_data, y_data, model=model_name):
    if model == 'A' or model == 'D' or model == 'E' or model == 'G':
        return x_data/255, y_data

    if model == 'B':
        x_data = x_data.astype('float32')
        mean = [125.307, 122.95, 113.865]
        std  = [62.9932, 62.0887, 66.7048]
        for i in range(3):
            x_data[:,:,:,i] = (x_data[:,:,:,i] - mean[i]) / std[i]
        y_data = y_data.reshape((y_data.shape[0],))
        
        return x_data, y_data

    if model == 'C' or model == 'F':
        x_data = x_data.reshape((x_data.shape[0], 28, 28, 1))
        x_data = x_data/255
   
        return x_data, y_data
    
def main(model_name):
    x_test, y_test = data_loader(clean_data_filename)
    x_test, y_test = data_preprocess(x_test, y_test, model_name)
    
    bd_model = keras.models.load_model(model_filename)

    clean_label_p = np.argmax(bd_model.predict(x_test), axis=1)
    class_accu = np.mean(np.equal(clean_label_p, y_test))
    print('Classification accuracy:', class_accu)

if __name__ == '__main__':
    main(model_name)
