
import numpy as np


def user_line_error(X, y, m, c):
    y_pred = m * X + c
    total_error_arr = y - y_pred
    error_arr = [f"{yi} - {yp} = {str(round(yi - yp, 2))}" for yi, yp in zip(y, y_pred)]
    return (error_arr, np.sum(total_error_arr))

def surface3d_error(X, y, m, c):
    return np.sum((y - (m * X + c))**2)
        


def forward(X, y, m, c):
    return np.sum((y-(m * X + c))**2)

def df_dm(X, y, m, c):
    n = X.shape[0]
    return (-2 / n) * np.sum(X * (y-(m * X + c)))
    
def df_dc(X, y, m, c):
    n = X.shape[0]
    return (-2 / n) * np.sum((y-(m * X + c)))



                        # 3d

def gradient_descent(x, y, theta_init, step=0.01, maxsteps=0, precision=0.001, ):
    costs = []
    m = y.size # number of data points
    theta = theta_init
    history = [] # to store all thetas
    preds = []
    counter = 0
    oldcost = 0
    pred = np.dot(x, theta)
    error = pred - y 
    currentcost = np.sum(error ** 2) / (2 * m)
    preds.append(pred)
    costs.append(currentcost)
    history.append(theta)
    counter+=1
    while abs(currentcost - oldcost) > precision:
        oldcost=currentcost
        gradient = x.T.dot(error)/m 
        theta = theta - step * gradient  # update
        history.append(theta)
        
        pred = np.dot(x, theta)
        error = pred - y 
        currentcost = np.sum(error ** 2) / (2 * m)
        costs.append(currentcost)
        
        if counter % 25 == 0: preds.append(pred)
        counter+=1
        if maxsteps:
            if counter == maxsteps:
                break
        
    return history, costs, preds, counter

def error(X, Y, THETA):
    return np.sum((X.dot(THETA) - Y)**2)/(2*Y.size)


def func(elem):
    return int(elem.split('-')[1].split('.')[0])

def sort_error_graph_func(mylist):
    return sorted(mylist, key=func)