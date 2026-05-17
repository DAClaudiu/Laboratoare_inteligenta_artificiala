import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

model_epoci = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model_epoci.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model_epoci.fit(x_train, y_train, epochs=10)

test_loss, test_accuracy = model_epoci.evaluate(x_test, y_test)

print("Acuratețe cu 10 epoci:", test_accuracy)