from sort_algos import *
import arr_gen
import time
from copy import copy
import matplotlib.pyplot as plt

def experiment(num):
    if num == 1:
        arr_type = "arr_gen.rand_arr_gen"
    elif num == 2:
        arr_type = "arr_gen.sorted_arr_gen"
    elif num == 3:
        arr_type = "arr_gen.backward_sorted_arr_gen"
    elif num == 4:
        arr_type = "arr_gen.set_arr_gen"
    else:
        raise ValueError("Experiment has only 4 types from 1 to 4")
    num_experiment(arr_type)
    

def num_experiment(arr_type: str):
    algos =  ["insertion_sort", "selection_sort", "shell_sort", "merge_sort"]
    insertion_sort_time, selection_sort_time, shell_sort_time, merge_sort_time = [], [], [], []
    insertion_sort_compar, selection_sort_compar, shell_sort_compar, merge_sort_compar = [], [], [], []
    arr_power = [i for i in range(7, 16)]
    num_compar = 0
    for power in range(7, 16):      # proceed with experiment for array with a given length of power 2
        arr = eval(f"{arr_type}(2**{power})")      #generate array according to experiment
        for algo in algos:
            lst = copy(arr)         # create copy of array since list is a mutable type. Not to change the initial
            now = time.time()
            eval(f"{algo}_compar.append({algo}(lst)[1])")      # sort copy of array and remember number of comparisons
            algo_time = time.time() - now
            eval(f"{algo}_time.append({algo_time})")        # remember time of work
            print(f"{algo} took {time.time() - now} seconds for 2**{power} elements")
        print("-"*100)
    
    time_chart(insertion_sort_time, selection_sort_time, shell_sort_time, merge_sort_time, arr_power, 1)
    time_chart(insertion_sort_compar, selection_sort_compar, shell_sort_compar, merge_sort_compar, arr_power, 2)

def time_chart(insertion_info: list, selection_info: list, shell_info: list, merge_info: list, arr_power: list, type_of_chart):
    plt.plot(arr_power, merge_info, label="Mergesort")
    plt.plot(arr_power, insertion_info, label="Insertion sort")
    plt.plot(arr_power, shell_info, label="Shellsort")
    plt.plot(arr_power, selection_info, label="Selection sort")
    if type_of_chart == 1:
        plt.title("Algorithm time of work chart")
        plt.ylabel("Algorithm time in seconds")
    else:
        plt.title("Algorithm number of comparisons chart")
        plt.ylabel("Algorithm number of comparisons")
    plt.xlabel("Length of the array in power of 2")
    plt.yscale("log")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    experiment(1)