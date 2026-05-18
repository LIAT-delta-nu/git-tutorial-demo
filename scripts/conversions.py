import numpy as np

def linear_to_db(x):
    """
    Convert linear power ratio to dB.
    """
    return 10 * np.log10(x)

def db_to_linear(db):
    """
    Convert dB to linear power ratio.
    """
    return 10 ** (db / 10)