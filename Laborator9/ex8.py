import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

model_fashion = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model_fashion.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model_fashion.fit(x_train, y_train, epochs=5)

test_loss, test_accuracy = model_fashion.evaluate(x_test, y_test)

print("Acuratețe Fashion MNIST:", test_accuracy)

index = 0

plt.imshow(x_test[index], cmap='gray')
plt.show()

prediction = model_fashion.predict(x_test[index].reshape(1, 28, 28))
predicted_class = np.argmax(prediction)

print("Predicția modelului:", predicted_class)
print("Eticheta reală:", y_test[index])