import numpy as np
import matplotlib.pyplot as plt
np.random.seed(3)

def main():
    class NeuralNet:
        def __init__(self, in_nodes, hid_nodes, out_nodes):
            self.in_nodes = in_nodes
            self.hid_nodes = hid_nodes
            self.out_nodes = out_nodes

            # initialize the weights
            self.W1 = np.random.randn(hid_nodes, in_nodes) * 0.01
            self.b1 = np.zeros((hid_nodes, 1))
            self.W2 = np.random.randn(out_nodes, hid_nodes) * 0.01
            self.b2 = np.zeros((out_nodes, 1))

            self.history = []

        def train(self, X, y, learning_rate=0.1, n_steps=10):
            for _ in range(n_steps):
                # print(f'dw1:{self.W1}, b1:{self.b1}, w2:{self.W2}, b2:{self.b2}')
                # print(self.b2)
                self.A1 = self.reLU(self.W1@X + self.b1)
                self.A2 = self.reLU(self.W2@self.A1 + self.b2)

                self.history.append(np.sum(np.abs(y-self.A2)))

                m = X.shape[1]
                dZ2 = self.A2 - y
                dW2 = dZ2@self.A1.T / m
                # print(dZ2.shape, self.A1.shape)
                db2 = np.sum(dZ2) / m
                dZ1 = (self.W2.T @ dZ2) * self.relu_derivative(self.W1@X + self.b1)
                dW1 = dZ1@X.T / m
                db1 = np.sum(dZ1) / m


                self.W2 -= learning_rate * dW2
                self.b2 -= learning_rate * db2
                self.W1 -= learning_rate * dW1
                self.b1 -= learning_rate * db1

        def sigmoid(self, h):
            return 1 / (1 + np.exp(-h))

        def sigmoid_dev(self, x):
            return 1 * (1 - x)

        def reLU(self, h):
            return np.maximum(0, h)

        def relu_derivative(self, x):
            return np.where(x >= 0, 1, 0)

        def predict(self, x):
            h1 = self.reLU(self.W1@x + self.b1)
            y = self.reLU(self.W2@h1 + self.b2)
            return (y > 0.5) * 1

        def show_plot(self):
            plt.plot(self.history)
            plt.title(f'Przebieg uczenia sieci,\n współczynnik uczenia: {self.lr}')
            plt.xlabel('Iteracja')
            plt.ylabel('Błąd')
            plt.show()


    x = np.array([
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]])
    y = np.array([[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]])

    model = NeuralNet(
        in_nodes=2, 
        hid_nodes=2, 
        out_nodes=1
        )

    model.lr = 0.5
    model.train(
        X=x,
        y=y,
        learning_rate=model.lr,
        n_steps=1000
        )

    model.show_plot()

    model = NeuralNet(
        in_nodes=2, 
        hid_nodes=2, 
        out_nodes=1
        )

    model.lr = 0.3
    model.train(
        X=x,
        y=y,
        learning_rate=model.lr,
        n_steps=1000
        )

    model.show_plot()

    print('----Test 1----')
    x_test1 = [[0], [0]]
    print(f'Wejście: {x_test1}, wyjście: {model.predict(x_test1)}')
    print('----Test 2----')
    x_test2 = [[1], [1]]
    print(f'Wejście: {x_test2}, wyjście: {model.predict(x_test2)}')
    print('----Test 3----')
    x_test = [[1], [0]]
    print(f'Wejście: {x_test}, wyjście: {model.predict(x_test)}')
    print('----Test 4----')
    x_test = [[0], [1]]
    print(f'Wejście: {x_test}, wyjście: {model.predict(x_test)}')


if __name__ == '__main__':
    main()