import matplotlib.pyplot as plt
import numpy as np
from utils.logger import setup_logger

logger = setup_logger()


def plot_signal_distribution(raw_signal, sample_size=500):
    logger.info("Plotting signal distribution (memory-efficient)")

    if len(raw_signal) > sample_size:
        raw_signal = np.random.choice(raw_signal, sample_size, replace=False)

    plt.figure(figsize=(8, 4))
    plt.hist(raw_signal, bins=30)
    plt.title("Market Signal Distribution (Sampled)")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
