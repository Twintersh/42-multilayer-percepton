import numpy as np
import random
from layers import Affine, BinaryCrossEntropy, Sigmoid, Softmax
from network import MultilayerPerceptron
from  utils import getDataFromDataset

def train():
	(train_data,
	train_label,
	pred_data,
	pred_label) 		= getDataFromDataset("datasets")
	hidden_layer_size 	= 20
	l_rate 				= 1e-3
	batch_size			= 50
	iterate				= 10000 # number of times we go through the dataset
	epochs				= int(len(train_data) / batch_size) + 1

	# setting the layers
	layers = [
		Affine(30, hidden_layer_size, l_rate), # Input layer
		Sigmoid(),
		Affine(hidden_layer_size, hidden_layer_size, l_rate), # hidden layer
		Sigmoid(),
		Affine(hidden_layer_size, 2, l_rate), # Hidden layer
		Softmax(batch_size, 2)
	]
	loss_layer = BinaryCrossEntropy()

	# init the MLP with the appropriate layers
	mlp = MultilayerPerceptron(layers, loss_layer, batch_size)

	nb_epoch = 0
	for i in range(iterate * epochs):
		# creating batches
		rand_index = random.sample(range(len(train_data)), batch_size)
		batch_data = np.array([train_data[j] for j in rand_index])
		batch_label = np.array([train_label[j] for j in rand_index])

		# Learning 🧠
		loss = mlp.calculate_loss(batch_data, batch_label)
		mlp.backward(batch_label)
		# each time i go through the entire dataset (approximation), print loss
		if not i % epochs:
			if not i % (epochs * 100):
				print(f"epoch : {nb_epoch}/{iterate} loss: {loss}")
			nb_epoch += 1

	test = mlp.predict(pred_data)
	for i in range(len(test)):
		print(f"{pred_label[i]} : {test[i][0]:.1f}")

# call main
if __name__ == "__main__":
	train()
