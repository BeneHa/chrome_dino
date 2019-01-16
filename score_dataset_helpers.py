import numpy as np
from keras.preprocessing.image import load_img, img_to_array


def create_dataset(fold, names, base_dir):
    dataset = np.ndarray(shape=(len(names), 50, 160, 3), dtype = np.float32)
    i = 0
    for f in names:
        img = load_img(base_dir + fold + "/" + f)
        x = img_to_array(img)
        x = (x - 128) / 128
        dataset[i] = x
        i += 1
    dataset = dataset[:,:,:,0]
    dataset = np.expand_dims(dataset, axis = 3)
    return dataset

def create_labels(names):
    labels = [np.zeros((len(names),10)) for i in range(5)]
    i = 0
    for n in range(len(names)):
        seq = names[n][0:5]
        for digit in range(len(seq)):
            label = int(seq[digit])
            labels[digit][n][label] = 1
        i += 1
    return labels