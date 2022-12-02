import matplotlib.pyplot as plt
import ast

if __name__ == "__main__":
    print("Analysing the results of Insertion Sort vs Merge Sort runs :")

    insertion_sort_write_path = './io/insertion_sort/comparison1_output.txt'
    merge_sort_write_path = './io/merge_sort/comparison1_output.txt'

    with open(insertion_sort_write_path, 'r') as f:
        insertion_sort_result = ast.literal_eval(f.read())

    with open(merge_sort_write_path, 'r') as f:
        merge_sort_result = ast.literal_eval(f.read())

    insertion_sort_result = {int(k): float(v) for k, v in insertion_sort_result.items()}
    merge_sort_result = {int(k): float(v) for k, v in merge_sort_result.items()}

    insert_sort_list = insertion_sort_result.items()
    i_numbers, i_time_taken = zip(*insert_sort_list)

    merge_sort_list = merge_sort_result.items()
    m_numbers, m_time_taken = zip(*merge_sort_list)

    fig, ax = plt.subplots()
    line_up, = ax.plot(i_numbers, i_time_taken, label='Insertion Sort')
    line_down, = ax.plot(m_numbers, m_time_taken, label='Merge Sort')
    ax.legend([line_up, line_down], ['Insertion Sort', 'Merge Sort'])
    plt.xlabel("Number of elements to sort")
    plt.ylabel("Time taken in seconds")
    plt.savefig("./io/metrics_images/insert_vs_merge.png")
    plt.show()
