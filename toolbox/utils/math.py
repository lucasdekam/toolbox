import numpy as np


def get_dev(x, y):
    x = np.array(x)
    y = np.array(y)
    delta_x = np.diff(x)
    delta_y = np.diff(y)
    out_x = (x[1:] + x[:-1]) / 2
    return out_x, delta_y / delta_x


def get_bin_ave(data, bin_size=10):
    total_size = len(data)
    out_size = bin_size * total_size // bin_size
    data = np.reshape(data[:out_size], (-1, bin_size))
    data = np.mean(data, axis=-1)
    return data


def get_int(x, y):
    x = np.array(x)
    y = np.array(y)
    ave_y = (y[1:] + y[:-1]) / 2
    delta_x = np.diff(x)
    x = (x[1:] + x[:-1]) / 2
    return x, np.cumsum(ave_y * delta_x)


def get_int_array(x, ys):
    x = np.array(x)
    ys = np.array(ys)
    ave_y = (ys[:, 1:] + ys[:, :-1]) / 2
    delta_x = np.diff(x)
    x = (x[1:] + x[:-1]) / 2
    return x, np.cumsum(ave_y * delta_x.reshape(1, -1), axis=-1)


def cumave(data):
    cum_sum = data.cumsum()
    cum_ave = cum_sum / (np.arange(len(data)) + 1)
    return cum_ave


def interp(x, dataset):
    y = np.interp(x, xp=dataset[0], fp=dataset[1])
    return y


def handle_zero_division(x, y, threshold=None):
    """
    define a function to handle the runtime warning
    """
    if threshold is not None:
        mask = (np.abs(y) <= threshold)
        y[np.nonzero(mask)] = 0.
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.true_divide(x, y)
        # replace NaN and Inf values with 0
        result[~np.isfinite(result)] = 0
    return result