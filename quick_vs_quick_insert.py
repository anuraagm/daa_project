from quick_insert_sort import quick_insert_sort
from quick_sort import quick_sort
from util import generate_random_array
from time import monotonic
import uuid
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    print("Part 4 : Comparison between Quick Sort and Quick-Insert Sort\n\n")
    run_result = []
    quick_sort_result = {}
    quick_insert_sort_result = {}
    for run_it in range(25):
        print("Iteration : ", run_it)
        array_size = 100000
        while array_size <= 300000:
            randomized_array = generate_random_array(array_size)

            run_id = str(uuid.uuid4()).split()[0]

            quick_sort_time_array = []
            start = monotonic()
            quick_sort(randomized_array, 0, randomized_array.size - 1)
            end = monotonic()
            quick_sort_time = end - start
            quick_sort_time_array.append(quick_sort_time)
            mean_quick_sort_time = sum(quick_sort_time_array) / len(quick_sort_time_array)
            # print("QS time : ", mean_quick_sort_time)

            if array_size not in quick_sort_result.keys():
                quick_sort_result[array_size] = mean_quick_sort_time
            else:
                quick_sort_result[array_size] = (quick_sort_result[array_size] + mean_quick_sort_time) / 2

            quick_insert_sort_time_array = []
            start = monotonic()
            quick_insert_sort(randomized_array, 0, randomized_array.size-1, 1)
            end = monotonic()
            quick_insert_sort_time = end - start
            quick_insert_sort_time_array.append(quick_insert_sort_time)
            mean_quick_insert_sort_time = sum(quick_insert_sort_time_array) / len(quick_insert_sort_time_array)
            # print("QIS time : ", mean_quick_insert_sort_time)

            if array_size not in quick_insert_sort_result.keys():
                quick_insert_sort_result[array_size] = mean_quick_insert_sort_time
            else:
                quick_insert_sort_result[array_size] = (quick_insert_sort_result[array_size] +
                                                        mean_quick_insert_sort_time) / 2

            array_size += 25000

    quick_insert_sort_write_path = 'io/quick_insert_sort/comparison3_output.txt'
    quick_sort_write_path = './io/quick_sort/comparison3_output.txt'

    with open(quick_insert_sort_write_path, 'w') as f:
        f.write(str(quick_insert_sort_result))

    with open(quick_sort_write_path, 'w') as f:
        f.write(str(quick_sort_result))
