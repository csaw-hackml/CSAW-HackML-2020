import keras
import sys
import h5py
import numpy as np

clean_data_filename = str(sys.argv[1])
bd_data_filename = str(sys.argv[2])
model_filename = str(sys.argv[3])

def data_loader(filepath):
    data = h5py.File(filepath, 'r')
    x_data = np.array(data['data'])
    y_data = np.array(data['label'])
    x_data = x_data.transpose((0,2,3,1))

    return x_data, y_data

def data_preprocess(x_data):
    return x_data/255

def main():
    x_test, y_test = data_loader(clean_data_filename)
    x_test = data_preprocess(x_test)
    bd_x_test, bd_y_test = data_loader(bd_data_filename)
    bd_x_test = data_preprocess(bd_x_test)

    bd_model = keras.models.load_model(model_filename)

    clean_label_p = np.argmax(bd_model.predict(x_test), axis=1)
    class_accu = np.mean(np.equal(clean_label_p, y_test))
    print('Classification accuracy:', class_accu)

    bd_label_p = np.argmax(bd_model.predict(bd_x_test), axis=1)
    attk_succ= np.mean(np.equal(bd_label_p, bd_y_test))
    print('Attack success rate:', attk_succ)

if __name__ == '__main__':
    main()
