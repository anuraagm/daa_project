from insertion_sort import insertion_sort
from merge_sort import merge_sort
from util import generate_random_array
from time import monotonic
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Part 1 : Comparison between Insertion Sort and Merge Sort\n\n")
    run_result = []
    insertion_sort_result = {}
    merge_sort_result = {}
    max_num = 1
    max_start = 1
    for run_it in range(1000):
        print("Iteration : ", run_it)
        breakpoint_size = max_start
        array_size = max_start
        check_flag = 0
        while True:
            randomized_array = generate_random_array(array_size)

            insertion_sort_time_array = []
            start = monotonic()
            sorted_array = insertion_sort(randomized_array)
            end = monotonic()
            insertion_sort_time = end - start
            insertion_sort_time_array.append(insertion_sort_time)
            mean_insertion_sort_time = sum(insertion_sort_time_array) / len(insertion_sort_time_array)

            if array_size not in insertion_sort_result.keys():
                insertion_sort_result[array_size] = mean_insertion_sort_time
            else:
                insertion_sort_result[array_size] = (insertion_sort_result[array_size] + mean_insertion_sort_time) / 2

            merge_sort_time_array = []
            start = monotonic()
            merge_sort(randomized_array, 0, randomized_array.size-1)
            end = monotonic()
            merge_sort_time = end - start
            merge_sort_time_array.append(merge_sort_time)
            mean_merge_sort_time = sum(merge_sort_time_array) / len(merge_sort_time_array)

            if array_size not in merge_sort_result.keys():
                merge_sort_result[array_size] = mean_merge_sort_time
            else:
                merge_sort_result[array_size] = (merge_sort_result[array_size] + mean_merge_sort_time) / 2

            if mean_insertion_sort_time > mean_merge_sort_time:
                breakpoint_size = array_size-1
                if breakpoint_size > max_num:
                    max_num = breakpoint_size
                    max_start += 1
                break

            check_flag += 1
            array_size += 1

        if check_flag > 1:
            print("Insertion sort performs better than Merge sort until the array size is : ", breakpoint_size)
            run_result.append(breakpoint_size)
    if len(run_result) > 0:
        avg_array_size = sum(run_result) / len(run_result)
        print("Average number of elements, where insertion sort beats merge sort : ", avg_array_size)

    insertion_sort_write_path = './io/insertion_sort/comparison1_output.txt'
    merge_sort_write_path = './io/merge_sort/comparison1_output.txt'

    with open(insertion_sort_write_path, 'w') as f:
        f.write(str(insertion_sort_result))

    with open(merge_sort_write_path, 'w') as f:
        f.write(str(merge_sort_result))

    plt.hist(run_result, bins=10)
    plt.gca().set(title='Insertion Sort Limit Frequency Histogram', xlabel='Number of elements', ylabel='Frequency')
    plt.savefig("./io/metrics_images/element_limit_for_insertion.png")
    plt.show()
