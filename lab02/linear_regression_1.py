import numpy as np
import tensorflow as tf

x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

tf.model = tf.keras.Sequential()

# Sequential 모델에 Layer 추가
# unit: Output 뉴런 수
# input_dim: Input 뉴런 수
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=1))

# Standard Gradient Descent
sgd = tf.keras.optimizers.SGD(learning_rate=0.1)
# Min Sqaured Error 1/m * sig (y'-y)^2
tf.model.compile(loss="mse", optimizer=sgd)

# 모델 정보 Summary 출력
tf.model.summary()

# Train
# epochs: Train Data Set에 대해 학습을 수행하는 횟수, Hyper Parameter
tf.model.fit(x_train, y_train, epochs=200)

# 예측 시작
y_predict = tf.model.predict(np.array([5, 4]))
print(y_predict)
