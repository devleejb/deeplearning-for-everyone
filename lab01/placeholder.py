import tensorflow as tf


@tf.function
def add_node(a, b):
    return tf.constant(a, tf.float32) + tf.constant(b, tf.float32)


print(add_node(3, 4.5))
print(add_node([1, 3], [2, 4]))
