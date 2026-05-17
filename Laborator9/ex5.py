import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

model_neuroni = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model_neuroni.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model_neuroni.fit(x_train, y_train, epochs=5)

test_loss, test_accuracy = model_neuroni.evaluate(x_test, y_test)

print("Acuratețe cu 256 neuroni:", test_accuracy)