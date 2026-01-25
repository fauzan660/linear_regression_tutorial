from flask import Flask
from flask import render_template
from flask import request
import os
from get_plots import plot_scatter, user_line_plot, plot_input_plane_3d, plot_output_surface_3d
from helper import user_line_error, sort_error_graph_func
from relpath_finder import find_relative_path
from relpath_finder import correct_relative_path        
from datasets import get_cases
from least_squares import least_squares_regression
from gradient_descent import gradient_descent_regression
app = Flask(__name__)

DEFINATION_IMAGES_URL = "/Users/fauzantahir/Documents/professional/linear_regression/learn_linear_regression/backend/static/image/definations"
C_ERROR_IMAGES_URL    = "/Users/fauzantahir/Documents/professional/linear_regression/learn_linear_regression/backend/static/image/c_err_carousel"
M_ERROR_IMAGES_URL    = "/Users/fauzantahir/Documents/professional/linear_regression/learn_linear_regression/backend/static/image/m_err_carousel"
@app.route('/')
def welcome():
  return "Welcome to the Codecademy Calculator!"

@app.route("/plot")
def plot():
  dataset = get_cases()[0]
  least_squares_url = least_squares_regression(dataset["X"], dataset["y"])
  gradient_descent_url = gradient_descent_regression(dataset["X"], dataset["y"])


  scatter_dataset = [plot_scatter(case["X"], case["y"], case["name"]) for case in get_cases()]
  definations_relpath = find_relative_path(os.getcwd(), DEFINATION_IMAGES_URL)
  defination_images = correct_relative_path(definations_relpath)
  error_m_relpath = find_relative_path(os.getcwd(), M_ERROR_IMAGES_URL)
  error_m_images = correct_relative_path(sort_error_graph_func(error_m_relpath))
  error_c_relpath = find_relative_path(os.getcwd(), C_ERROR_IMAGES_URL)
  error_c_images = correct_relative_path(sort_error_graph_func(error_c_relpath))
  plot_input_plane = plot_input_plane_3d()
  plot_output_surface = plot_output_surface_3d(dataset["X"], dataset["y"])
  return render_template("linear.html", image_url=[least_squares_url, gradient_descent_url],
                          defination_images = defination_images, 
                          scatter_plots = scatter_dataset, 
                          c_err_img = error_c_images, 
                          m_err_img = error_m_images, 
                          input_plane = plot_input_plane,
                          output_surface = plot_output_surface)

@app.post("/update_plot")
def update_plot():
  data = request.json
  m = float(data["m"])
  c = float(data["c"])
  dataset = get_cases()[0]
  url = user_line_plot(dataset['X'], dataset['y'], m, c)
  error_arr, error = user_line_error(dataset['X'], dataset['y'], m, c)
  print(url)
  return {"url": url, "error": error, "errorArray": error_arr}


app.run()
