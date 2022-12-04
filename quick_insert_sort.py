import math

from util import generate_random_array
from time import monotonic
import uuid
import sys


def insertion_sort(array):
    """

    :param array:
    :return:
    """
    try:
        # print("IS method used")
        if len(array) > 1:
            for i in range(1, len(array)):
                if array[i] >= array[i - 1]:
                    continue
                for j in range(i):
                    if array[i] < array[j]:
                        array[j], array[j + 1:i + 1] = array[i], array[j:i]
                        break
    except Exception as e:
        print("Error in insertion sort part : ",e)


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
        return outer+1
    except Exception as e:
        print("Error in partition() function : ", e)
        return


def quick_insert_sort(array, low, high, pivot_count):
    """

    :param array:
    :param low:
    :param high:
    :param pivot_count:
    :return:
    """
    try:
        if low < high:
            pivot_count += 1
            # print("The Pivot Count : ", pivot_count)
            if pivot_count >= 0.012 * array.size:
                # print("The Pivot Count : ", pivot_count)
                insertion_sort(array)
            else:
                pivot = partition(array, low, high)
                pivot_count += 1
                quick_insert_sort(array, low, pivot-1, pivot_count)
                pivot_count += 1
                quick_insert_sort(array, pivot+1, high, pivot_count)
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
        array_size = 10
        while array_size <= 2000:
            randomized_array = generate_random_array(array_size)
            input_write_path = './io/quick_insert_sort/'+(str(array_size)+"_input_"+str(it)+".txt")
            with open(input_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            start = monotonic()
            quick_insert_sort(randomized_array, 0, array_size-1, 0)
            end = monotonic()
            elapsed_time = end - start

            output_write_path = './io/quick_insert_sort/'+(str(array_size)+"_output_"+str(it)+".txt")
            with open(output_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            print("Time taken to sort ",array_size," elements, using Quick Insert Sort = ", elapsed_time, " seconds")
            run_metrics.append(elapsed_time)
            array_size += 25000
