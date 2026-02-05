from api.model.datasets import get_cases
from api.service.plotting import (
    plot_scatter, user_line_plot, plot_input_plane_3d, plot_output_surface_3d, plotly_gd_line_3d
)
from api.service.math_utils import user_line_error, sort_error_graph_func
from api.service.least_squares import least_squares_regression
from api.service.gradient_descent import gradient_descent_regression
from api.service.path_utils import get_definition_images, get_m_error_images, get_c_error_images

def get_plot_page_data():
    cases = get_cases()
    dataset = cases[0]

    least_squares_url = least_squares_regression(dataset["X"], dataset["y"])
    gradient_descent_url = gradient_descent_regression(dataset["X"], dataset["y"])

    scatter_plots = [plot_scatter(case["X"], case["y"], case["name"]) for case in cases]

    return {
        "image_url": [least_squares_url, gradient_descent_url],
        "defination_images": get_definition_images(),
        "scatter_plots": scatter_plots,
        "c_err_img": get_c_error_images(),
        "m_err_img": get_m_error_images(),
        "input_plane": plot_input_plane_3d(),
        "output_surface": plot_output_surface_3d(dataset["X"], dataset["y"])
    }

def update_user_line(data):
    try:
        m = float(data.get("m"))
        c = float(data.get("c"))
    except (TypeError, ValueError):
        return {"error": "Invalid input"}

    dataset = get_cases()[0]
    url = user_line_plot(dataset["X"], dataset["y"], m, c)
    error_arr, error = user_line_error(dataset["X"], dataset["y"], m, c)

    return {"url": url, "error": error, "errorArray": error_arr}

def live_descent_3d():
    cases = get_cases()
    dataset = cases[0]
    return plotly_gd_line_3d(dataset["X"], dataset["y"])