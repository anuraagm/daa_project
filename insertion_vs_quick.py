from util import generate_random_array
import matplotlib.pyplot as plt
import numpy as np


def check_nearly_sorted(array):
    """

    :param array:
    :return:
    """
    try:
        for i in range(array.size-2):
            if array[i] > array[i + 2]:
                return False
        return True
    except Exception as e:
        print("Error checking if nearly sorted : ",e)


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


def quick_sort(array, low, high, recursive_count, threshold_dict):
    """

    :param array:
    :param low:
    :param high:
    :param recursive_count:
    :param threshold_dict:
    :return:
    """
    try:
        if low < high:
            if check_nearly_sorted(array):
                if threshold_dict[array.size] == 0:
                    threshold_percent = (recursive_count * 100) / array.size
                    threshold_dict[array.size] = threshold_percent
                else:
                    threshold_percent = ((threshold_dict[array.size] + recursive_count) // 2 * 100) / array.size
                    threshold_dict[array.size] = threshold_percent
            pivot = partition(array, low, high)
            recursive_count += 1
            quick_sort(array, low, pivot-1, recursive_count, threshold_dict)
            recursive_count += 1
            quick_sort(array, pivot+1, high, recursive_count, threshold_dict)
        else:
            return
    except Exception as e:
        print("Error in quick_sort() call : ", e)
        return


def check_nearly_sorted(array):
    """

    :param array:
    :return:
    """
    try:
        # print("Entered Check Part")
        for i in range(array.size-2):
            if array[i] > array[i + 2]:
                return False
        return True
    except Exception as e:
        print("Error checking if nearly sorted : ",e)


if __name__ == '__main__':
    print("Part 3 : Finding where Insertion Sort can be used in Quick Sort\n\n")
    threshold_distribution = []
    for it in range(100):
        print("Iteration : ",it)
        start_size = 50000
        threshold_point = {}
        while start_size >= 2:
            threshold_point[start_size] = 0
            randomized_array = generate_random_array(start_size)
            check_nearly_sorted(randomized_array)
            quick_sort(randomized_array, 0, randomized_array.size-1, 0, threshold_point)
            start_size -= 10000

        threshold_list = [v for k, v in threshold_point.items()]
        l = np.array(threshold_list)
        new_threshold_list = l[(l > np.quantile(l, 0.1)) & (l < np.quantile(l, 0.9))].tolist()

        print("Threshold List : ",new_threshold_list)
        average_recursion_step = sum(new_threshold_list) / len(new_threshold_list)
        threshold_distribution.append(average_recursion_step)

    average_distribution = sum(threshold_distribution) / len(threshold_distribution)
    print("On average, when the recursive call count is ", average_distribution,
          "% the the size of the input array, the Array is nearly sorted and the "
          "Insertion Sort algorithm can be used.")
    plt.hist(threshold_distribution)
    plt.gca().set(title='Quick Sort Switch Value Frequency Histogram', xlabel='% of Recursions', ylabel='Frequency')
    plt.savefig("./io/metrics_images/recursion_threshold_for_quick_sort.png")
    plt.show()
