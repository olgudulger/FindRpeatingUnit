import numpy as np

def check(a, b, indexes):
    x_row = indexes[0]
    x_col = indexes[1]
    b_rows, b_cols = b.shape
    a_slice = a[x_row : x_row + b_rows, :][:, x_col : x_col + b_cols]
    if a_slice.shape != b.shape:
        return False
    return (a_slice == b).all()

def find_slice(big_array, small_array):
    indexes = np.argwhere(big_array == small_array[0,0])
    for x in indexes:
        if check(big_array, small_array, x):
            return True
    else:
        return False
