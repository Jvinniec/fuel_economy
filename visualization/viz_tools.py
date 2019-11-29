

import numpy as np

def moving_avg(x, nbins=2):
    """
    Generates a moving average of a given bin and 'nbins' on either side

    Parameters
    ----------
    x : numpy.array
        Array of values
    nbins : int
        Number of bins on either side to average
    
    Returns
    -------
    Array representing a moving average
    """
    # Copy the array
    y = np.array(x)

    # Pad the front and back with NaN's
    y = np.insert(y, 0, [np.nan]*nbins)
    y = np.insert(y, len(y), [np.nan]*nbins)

    # Convolve with with an array of 1's
    width = 2*nbins + 1
    return np.convolve(y, np.ones(width), 'valid') / width