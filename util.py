import numpy as np


def swap(array, pos1, pos2):
    """

    :param array:
    :param pos1:
    :param pos2:
    :return:
    """
    try:
        temp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = temp
        return array
    except Exception as e:
        print("Error swapping : ",e)
        return []


def generate_random_array(array_length):
    """

    :param array_length:
    :return:
    """

    try:
        random_array = np.random.randint(100, size=array_length)
        return random_array
    except Exception as e:
        print("Error generating random array : \n", e)
        return []