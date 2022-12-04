import math
import sys

from util import generate_random_array
from time import monotonic
import uuid


def partition(array, low, high):
    """

    :param array:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    try:
        pivot = array[high]

        outer = low-1
        for inner in range(low, high):
            if array[inner] < pivot:
                outer += 1
                temp = array[outer]
                array[outer] = array[inner]
                array[inner] = temp

        temp = array[outer+1]
        array[outer+1] = array[high]
        array[high] = temp
        # print("New Sorted Array : ", array)
        return outer+1
    except Exception as e:
        print("Error in partition() function : ", e)
        return


def quick_sort(array, low, high):
    """

    :param array:
    :param low:
    :param high:
    :return:
    """
    try:
        if low < high:
            pivot = partition(array, low, high)
            quick_sort(array, low, pivot-1)
            quick_sort(array, pivot+1, high)
        else:
            return
    except Exception as e:
        print("Error in quick_sort() call : ", e)
        return


if __name__ == "__main__":
    print(sys.setrecursionlimit(2000000))
    for it in range(10):
        run_metrics = ()
        run_metrics = list(run_metrics)
        run_metrics.append(str(uuid.uuid4()))
        run_metrics.append(it)
        array_size = 50000
        while array_size <= 200000:
            randomized_array = generate_random_array(array_size)
            input_write_path = './io/quick_sort/'+(str(array_size)+"_input_"+str(it)+".txt")
            with open(input_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            start = monotonic()
            quick_sort(randomized_array, 0, array_size-1)
            end = monotonic()
            elapsed_time = end - start

            output_write_path = './io/quick_sort/'+(str(array_size)+"_output_"+str(it)+".txt")
            with open(output_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            print("Time taken to sort ",array_size," elements, using Quick Sort = ", elapsed_time, " seconds")
            run_metrics.append(elapsed_time)
            array_size += 25000
