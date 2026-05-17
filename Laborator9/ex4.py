import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

index = 0

plt.imshow(x_test[index], cmap='gray')
plt.show()

prediction = model.predict(x_test[index].reshape(1, 28, 28))
predicted_digit = np.argmax(prediction)

print("Predicția modelului:", predicted_digit)
print("Eticheta reală:", y_test[index])