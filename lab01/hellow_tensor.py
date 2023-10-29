import tensorflow as tf

hello = tf.constant("Hello, Tensorflow!")


@tf.function
def sess():
    return hello


print(sess())
