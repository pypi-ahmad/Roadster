from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.models import Sequential


# architecture inspired by https://github.com/hparik11/German-Traffic-Sign-Recognition (similar to LeNet)
# with few modifications added

# 1: use sigmoid instead of softmax and threshold probability

# or 2: add background noise class

class TrafficSignNet_v4:
    @staticmethod
    def build(width, height, depth, classes):
        model = Sequential()

        model.add(Input(shape=(width, height, depth)))

        model.add(Conv2D(6, (5, 5,), padding="valid"))
        model.add(MaxPooling2D((2, 2), padding="valid"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=-1))  # modification, inspired by pyimagesearch

        # 66 works better than the original 16 (found out by mistake)
        model.add(Conv2D(66, (5, 5,), padding="valid"))
        model.add(MaxPooling2D((2, 2), padding="valid"))
        model.add(Activation("relu"))

        model.add(Flatten())

        # some dropouts added to avoid overfitting
        model.add(Dropout(0.3))
        model.add(Dense(120))
        model.add(Activation("relu"))

        model.add(Dropout(0.3))
        model.add(Dense(84))
        model.add(Activation("relu"))

        model.add(Dropout(0.3))
        model.add(Dense(classes))
        model.add(Activation("sigmoid"))

        return model
