import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np


def figure_to_svg(fig):
    stream = BytesIO()
    # Added: Disable XML declaration and SVG namespace
    # Removed: background='#FFFFFF' since it is the default
    fig.savefig(stream, format="svg")
    qr = stream.getvalue().decode('utf-8')
    return qr


def figure_to_plot(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    url = f"data:image/png;base64,{data}"
    return url


def figure_to_plot_3d(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    url = f"data:image/png;base64,{data}"
    return url