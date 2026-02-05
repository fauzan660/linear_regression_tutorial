from flask import Blueprint, render_template, request
from api.service.holder import get_plot_page_data, update_user_line, live_descent_3d

home_bp = Blueprint("home", __name__)

@home_bp.route('/')
def welcome():
    return "Welcome to the Codecademy Calculator!"

@home_bp.route('/plot')
def plot():
    context = get_plot_page_data()
    return render_template("linear.html", **context)

@home_bp.post('/update-plot')
def update_plot():
    data = request.json
    response = update_user_line(data)
    return response

@home_bp.route('/live-descent')
def live_descent():
    response = live_descent_3d()
    return response