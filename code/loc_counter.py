"""LOC counter"""
import os
from python_loc_counter import LOCCounter

PYTHON_PATH = "python_ex1.py"
JAVA_PATH = "HelloWorld.java"
PYTHON_RESULTS = r"..\metrics\python_loc_counter\python_loc_counter_results.txt"
JAVA_RESULTS = r"..\metrics\python_loc_counter\java_loc_counter_results.txt"


def loc(path):
    """calculate LOC"""
    counter = LOCCounter(path)
    loc_data = counter.getLOC()
    print("-----------------------------------------")
    print("File: ", path)
    for k in loc_data:
        print(f"{k}: {loc_data[k]}")
    return loc_data


def remove_open_files(file_path):
    """remove file if exists"""
    if os.path.exists(file_path):
        os.remove(file_path)


def loc_in_file(file_name,path):
    """write in file LOC"""
    data = loc(path) #loc_count results
    remove_open_files(file_name) # remove file if exists
    file_obj = open(file_name, "w")
    file_obj.write("--------"+path+" LOC-------\n")
    for k in data:
        file_obj.write(str(f"{k}: {data[k]}\n"))
    file_obj.close()


if __name__ == "__main__":
    loc_in_file(PYTHON_RESULTS,PYTHON_PATH)
    loc_in_file(JAVA_RESULTS,JAVA_PATH)
