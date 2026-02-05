import os
import os
from api.service.math_utils import sort_error_graph_func


STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "static", "image")
DEFINITION_DIR = os.path.join(STATIC_DIR, "definitions")
M_ERROR_DIR    = os.path.join(STATIC_DIR, "m_err_carousel")
C_ERROR_DIR    = os.path.join(STATIC_DIR, "c_err_carousel")

def correct_relative_path(relative_path_list):
    return ([
    {
        "path": rel.replace("static/", ""),
        "name": os.path.splitext(os.path.basename(rel))[0]
    }
    for rel in relative_path_list
    ])

def find_relative_path(start, destination):
    file_set = set()
    for dir_, _, files in os.walk(destination):
        for file_name in files:
            rel_dir = os.path.relpath(dir_, start)
            rel_file = os.path.join(rel_dir, file_name)
            file_set.add(rel_file)
    return file_set 

def get_definition_images():
    return correct_relative_path(find_relative_path(os.getcwd(), DEFINITION_DIR))

def get_m_error_images():
    return correct_relative_path(sort_error_graph_func(find_relative_path(os.getcwd(), M_ERROR_DIR)))

def get_c_error_images():
    return correct_relative_path(sort_error_graph_func(find_relative_path(os.getcwd(), C_ERROR_DIR)))