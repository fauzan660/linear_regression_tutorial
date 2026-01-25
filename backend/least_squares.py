import numpy as np
import pandas as pd
import matplotlib as plt
from get_plots import plot_webpage


def least_squares_regression(X, y):
    x_mean = np.mean(X)
    y_mean = np.mean(y)
    num = 0
    denom = 0

    # for x_p, y_p in zip(X, y):
    #     num += (x_p - x_mean) * (y_p - y_mean)
    #     denom += (x_p - x_mean)**2


    # m = num / denom


    m = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean)**2)
    print(m)


    c = y_mean - (m * x_mean)

    y_pred = m * X + c
    return plot_webpage(X, y, y_pred, title="least squares")

    