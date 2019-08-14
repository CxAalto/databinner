"""This module is just functions copied from verkko.
"""

from math import floor, ceil

def percentile(data, p):
    """Calculate the p-percentile of data

    The p:th percentile is the value X for which p percent of the
    elements of data are smaller than X.  For instance with p = 0.5 this
    function returns the median.

    Parameters
    ----------
    data : sequence
        The input data. This must be sorted!
    p : float
        The percentile to calculate. 

    Return
    -------
    x : int or float
        The percentile. Returns an element of the data if p*(N-1) is
        an integer, otherwise x will be between two data values. If
        data is empty, returns None
    """
    if not len(data):
        return None # data = []

    i = float(p)*(len(data)-1)
    if i == int(i):
        return data[int(i)]

    i_lower = int(floor(i))
    i_upper = int(ceil(i))
    fraq = i - i_lower
    return (1-fraq)*data[i_lower] + fraq*data[i_upper]
