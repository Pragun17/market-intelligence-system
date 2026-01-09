import numpy as np
import pandas as pd
from utils.logger import setup_logger

logger = setup_logger()

BULLISH_TERMS = [
    "bullish", "breakout", "buy", "uptrend", "long", "support", "rally"
]

BEARISH_TERMS = [
    "bearish", "breakdown", "sell", "downtrend", "short", "resistance", "crash"
]


def build_signal(tfidf_matrix, feature_names):
    logger.info("Building composite trading signal")

    signal_weights = np.zeros(len(feature_names))

    for idx, term in enumerate(feature_names):
        if term in BULLISH_TERMS:
            signal_weights[idx] = 1
        elif term in BEARISH_TERMS:
            signal_weights[idx] = -1

    raw_signal = tfidf_matrix.dot(signal_weights)

    mean_signal = raw_signal.mean()
    std_signal = raw_signal.std()

    confidence_interval = (
        mean_signal - 1.96 * std_signal,
        mean_signal + 1.96 * std_signal
    )

    return {
        "mean_signal": mean_signal,
        "std_dev": std_signal,
        "confidence_interval": confidence_interval
    }
