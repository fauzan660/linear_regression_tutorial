import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np
from api.service.matplot import figure_to_plot, figure_to_plot_3d, figure_to_svg
from api.service.math_utils import surface3d_error, df_dc, df_dm, gradient_descent, error



def gradient_descent_plot(X, y):
    m = 0
    c = 0
    l = 0.001
    epochs = 50

    for i in range(epochs):

        partial_m = df_dm(X, y, m, c)
        partial_c = df_dc(X, y, m, c)
        

        m = m - (l * partial_m)
        c = c - (l * partial_c)
        

        y_pred = m * X + c

    fig = Figure()
    ax = fig.subplots(nrows=1, ncols=1)
    ax.scatter(X, y)
    ax.plot(X, y_pred, 'r')
    return figure_to_plot(fig)

def error_c_constant(X, y, m, c):
    m = [1,2,3,4,5,6,7,8,9,10]
    c = 1
    error_m = [np.sum((y - ((slope* X) + c))**2) for slope in m]
    fig = Figure()
    ax = fig.subplots(nrows=1, ncols=1)
    ax.plot(m, error_m)
    return figure_to_plot(fig)

def error_m_constant(X, y, m, c):
    c = [-5, -4, -3, -2, -1, 0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16,17,18,19,20]
    m = 1

    error_c = [np.sum((y - ((m* X) + intercept))**2) for intercept in c]
    fig = Figure()
    ax = fig.subplots(nrows=1, ncols=1)
    ax.plot(c, error_c)
    return figure_to_plot(fig)

def user_line_plot(X, y, m, c):
    coordinates = [(i,j) for i, j in zip(X.tolist(), y.tolist())]

    y_pred = (m * X) + c
    fig = Figure()
    ax = fig.subplots(nrows=1, ncols=1)
    ax.scatter(X, y)
    ax.plot(X, y_pred, 'r')
    ax.plot(X, y_pred, 'bs')
    ax.plot((X, X), (y, y_pred), c='black')
    for i, c in enumerate(coordinates):
        ax.annotate(c, (X[i], y[i]), xytext=(X[i] + 0.05, y[i] + 0.05))
    ax.set_title("linear plot")
    return figure_to_svg(fig)

def plot_webpage(X, y, y_pred, title):
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots(nrows=1, ncols=1)
    ax.scatter(X, y)
    ax.plot(X, y_pred, 'r')
    ax.set_title(title)
    return figure_to_plot(fig)


def plot_scatter(X, y, title):
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots(nrows=1, ncols=1)
    ax.scatter(X, y)
    ax.set_title(title)
    return figure_to_plot(fig)





                    # 3D


def plot_input_plane_3d():
    m = np.arange(-10.0, 20.0, 0.5)
    c = np.arange(-10.0, 10.0, 0.5)

    M, C= np.meshgrid(m, c)
    fig = Figure()
    ax = fig.add_subplot(111, projection='3d')
    input_Z = np.zeros(M.shape)
    ax.plot_surface(M, C, input_Z, color='r', alpha=0.5)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    return figure_to_plot_3d(fig)

def plot_output_surface_3d(X, y):
    m = np.arange(-10.0, 20.0, 0.5)
    c = np.arange(-10.0, 10.0, 0.5)

    M, C= np.meshgrid(m, c)
    err = np.array([surface3d_error(X, y, slope,intercept) for slope,intercept in zip(np.ravel(M), np.ravel(C))])
    E = err.reshape(M.shape)
    err_min = E.min()
    err_min_index = np.unravel_index(E.argmin(), E.shape)
    m_min, c_min = M[err_min_index], C[err_min_index]
    fig = Figure()
    ax = fig.add_subplot(111, projection='3d')

    input_Z = np.zeros(M.shape)
    ax.plot_surface(M, C, input_Z, color='r', alpha=0.5)
    ax.plot_surface(M, C, E, rstride=1, cstride=1, color='b', alpha=0.5)
    ax.scatter3D(m_min, c_min, err_min, 'b*', s=100)
    # ax.scatter3D(M, C, E)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    return figure_to_plot_3d(fig)

def plotly_gd_line_3d(X, y):
    m = np.arange(-10.0, 20.0, 0.5)
    c = np.arange(-10.0, 10.0, 0.5)

    M, C= np.meshgrid(m, c)
    err = np.array([surface3d_error(X, y, slope,intercept) for slope,intercept in zip(np.ravel(M), np.ravel(C))])
    E = err.reshape(M.shape)
    return {
        "M": M.tolist(), 
        "C": C.tolist(), 
        "E": E.tolist(),
        "m_vec": m.tolist(), # Send the 1D vector
        "c_vec": c.tolist()  # Send the 1D vector
    }