import matplotlib.pyplot as plt
import numpy as np

def plot_training_loss():
    epochs = [1, 2, 3, 4, 5]
    loss = [0.9, 0.7, 0.5, 0.35, 0.2]

    plt.plot(epochs, loss)
    plt.title("Training Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.show()


def compare_models():
    models = ["BERT", "DistilBERT"]
    speed = [1.0, 0.6]

    plt.bar(models, speed)
    plt.title("Inference Speed")
    plt.ylabel("Relative Time")
    plt.show()


def attention_map():
    attention = np.random.rand(6, 6)

    plt.imshow(attention)
    plt.title("Attention Map")
    plt.colorbar()
    plt.show()