from merge_insert_sort import merge_insert_sort
from merge_sort import merge_sort
from util import generate_random_array
from time import monotonic
import uuid


if __name__ == '__main__':
    print("Part 2 : Comparison between Merge Sort and Merge-Insert Sort\n\n")
    run_result = []
    merge_sort_result = {}
    merge_insert_sort_result = {}
    for run_it in range(25):
        print("Iteration : ", run_it)
        array_size = 500000
        while array_size < 2000000:
            randomized_array = generate_random_array(array_size)

            run_id = str(uuid.uuid4()).split()[0]

            merge_sort_time_array = []
            start = monotonic()
            merge_sort(randomized_array, 0, randomized_array.size - 1)
            end = monotonic()
            merge_sort_time = end - start
            merge_sort_time_array.append(merge_sort_time)
            mean_merge_sort_time = sum(merge_sort_time_array) / len(merge_sort_time_array)

            if array_size not in merge_sort_result.keys():
                merge_sort_result[array_size] = mean_merge_sort_time
            else:
                merge_sort_result[array_size] = (merge_sort_result[array_size] + mean_merge_sort_time) / 2

            merge_insert_sort_time_array = []
            start = monotonic()
            merge_insert_sort(randomized_array, 0, randomized_array.size-1)
            end = monotonic()
            merge_insert_sort_time = end - start
            merge_insert_sort_time_array.append(merge_insert_sort_time)
            mean_merge_insert_sort_time = sum(merge_insert_sort_time_array) / len(merge_insert_sort_time_array)

            if array_size not in merge_insert_sort_result.keys():
                merge_insert_sort_result[array_size] = mean_merge_insert_sort_time
            else:
                merge_insert_sort_result[array_size] = (merge_insert_sort_result[array_size] +
                                                        mean_merge_insert_sort_time) / 2

            array_size += 250000

    merge_insert_sort_write_path = 'io/merge_insert_sort/comparison2_output.txt'
    merge_sort_write_path = './io/merge_sort/comparison2_output.txt'

    with open(merge_insert_sort_write_path, 'w') as f:
        f.write(str(merge_insert_sort_result))

    with open(merge_sort_write_path, 'w') as f:
        f.write(str(merge_sort_result))
