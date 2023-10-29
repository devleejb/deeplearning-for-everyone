import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)


@tf.function
def add():
    return tf.add(node1, node2)


print(add())
