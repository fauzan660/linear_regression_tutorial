import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output # Import this
from api.service.plotting import plot_webpage


def gradient_descent_regression(X, y):
    m = 0
    c = 0
    l = 0.001
    epochs = 50

    def forward(m, c):
        return np.sum((y-(m * X + c))**2)

    def df_dm(m, c):
        n = X.shape[0]
        return (-2 / n) * np.sum(X * (y-(m * X + c)))
        
    def df_dc(m, c):
        n = X.shape[0]
        return (-2 / n) * np.sum((y-(m * X + c)))



    for i in range(epochs):

        partial_m = df_dm(m, c)
        partial_c = df_dc(m, c)
        

        m = m - (l * partial_m)
        c = c - (l * partial_c)
        

        y_pred = m * X + c


    return plot_webpage(X, y, y_pred, title="gradient_descent")