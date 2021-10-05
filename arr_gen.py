import random

def rand_arr_gen(len_arr):
    return [random.randint((-10)**9, 10**9) for _ in range(len_arr)]

def sorted_arr_gen(len_arr):
    return [i for i in range(len_arr)]

def backward_sorted_arr_gen(len_arr):
    return [len_arr - i for i in range(len_arr)]

def set_arr_gen(len_arr):
    return [random.randint(1, 3) for _ in range(len_arr)]


if __name__ == "__main__":
    lst_sum = 0
    for _ in range(3):
        lst = set_arr_gen(2**15)
        lst_sum += sum(lst)
    avg = lst_sum / (3 * 2**15)
    print(avg)