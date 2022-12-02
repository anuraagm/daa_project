import math
from util import generate_random_array
from time import monotonic
import uuid


def merge_insert(array, low, mid, high):
    """

    :param array:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    try:
        if array[low:high+1].size > 25:
            i = low
            j = mid + 1
            aux = []
            while i <= mid and j <= high:
                if array[i] <= array[j]:
                    aux.append(array[i])
                    i += 1
                else:
                    aux.append(array[j])
                    j += 1
            while i <= mid:
                aux.append(array[i])
                i += 1
            while j <= high:
                aux.append(array[j])
                j += 1
            it_aux = 0
            it_arr = low
            while it_arr <= high:
                array[it_arr] = aux[it_aux]
                it_arr += 1
                it_aux += 1
        else:
            for i in range(1, len(array[low:high+1])):
                if array[i] >= array[i - 1]:
                    continue
                for j in range(i):
                    if array[i] < array[j]:
                        array[j], array[j + 1:i + 1] = array[i], array[j:i]
                        break
    except Exception as e:
        print("Error in merge() function : ", e)
        return


def merge_insert_sort(array, low, high):
    """

    :param array:
    :param low:
    :param high:
    :return:
    """
    try:
        if low < high:
            mid = math.floor((low + high) / 2)
            merge_insert_sort(array, low, mid)
            merge_insert_sort(array, mid+1, high)
            merge_insert(array, low, mid, high)
        else:
            return
    except Exception as e:
        print("Error in merge_sort() call : ", e)
        return


if __name__ == "__main__":

    for it in range(10):
        run_metrics = ()
        run_metrics = list(run_metrics)
        run_metrics.append(str(uuid.uuid4()))
        run_metrics.append(it)
        array_size = 500000
        while array_size <= 2000000:
            randomized_array = generate_random_array(array_size)
            input_write_path = './io/merge_insert_sort/'+(str(array_size)+"_input_"+str(it)+".txt")
            with open(input_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            start = monotonic()
            merge_insert_sort(randomized_array, 0, array_size-1)
            end = monotonic()
            elapsed_time = end - start

            output_write_path = './io/merge_insert_sort/'+(str(array_size)+"_output_"+str(it)+".txt")
            with open(output_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            print("Time taken to sort ",array_size," elements, using Merge Insert Sort = ", elapsed_time, " seconds")
            run_metrics.append(elapsed_time)
            array_size += 250000
