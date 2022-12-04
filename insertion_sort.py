from util import generate_random_array
from time import monotonic
import uuid


def insertion_sort(array):
    """

    :param array:
    :return:
    """

    try:
        if len(array) > 1:
            for i in range(1, array.size):
                if array[i] > array[i-1]:
                    continue
                else:
                    j = i-1
                    while array[i] < array[j] and j >= 0:
                        j -= 1
                    j += 1
                    temp = array[i]
                    array[j+1:i+1] = array[j:i]
                    array[j] = temp
    except Exception as e:
        print("Error in insertion sort function call : \n", e)
        return []


if __name__ == "__main__":

    for it in range(10):
        run_metrics = ()
        run_metrics = list(run_metrics)
        run_metrics.append(str(uuid.uuid4()))
        run_metrics.append(it)
        array_size = 8
        while array_size <= 20:
            randomized_array = generate_random_array(array_size)

            input_write_path = './io/insertion_sort/'+(str(array_size)+"_input_"+str(it)+".txt")
            with open(input_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            start = monotonic()
            insertion_sort(randomized_array)
            end = monotonic()
            elapsed_time = end - start
            output_write_path = './io/insertion_sort/'+(str(array_size)+"_output_"+str(it)+".txt")
            with open(output_write_path,'w') as f:
                for elem in randomized_array:
                    f.write(str(elem)+", ")

            print("Time taken to sort ",array_size," elements, using Insertion Sort = ", elapsed_time, " seconds")
            run_metrics.append(elapsed_time)
            array_size += 2500
