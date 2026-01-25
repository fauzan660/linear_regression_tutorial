import os


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

