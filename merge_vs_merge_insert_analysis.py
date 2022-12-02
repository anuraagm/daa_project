import matplotlib.pyplot as plt
import ast

if __name__ == "__main__":
    print("Analysing the results of Merge Sort vs Merge Insert Sort runs :")

    merge_sort_write_path = './io/merge_sort/comparison2_output.txt'
    merge_insert_sort_write_path = './io/merge_insert_sort/comparison2_output.txt'

    with open(merge_sort_write_path, 'r') as f:
        merge_sort_result = ast.literal_eval(f.read())

    with open(merge_insert_sort_write_path, 'r') as f:
        merge_insert_sort_result = ast.literal_eval(f.read())

    merge_sort_result = {int(k): float(v) for k, v in merge_sort_result.items()}
    merge_insert_sort_result = {int(k): float(v) for k, v in merge_insert_sort_result.items()}

    merge_sort_list = merge_sort_result.items()
    m_numbers, m_time_taken = zip(*merge_sort_list)

    merge_insert_sort_list = merge_insert_sort_result.items()
    mi_numbers, mi_time_taken = zip(*merge_insert_sort_list)

    fig, ax = plt.subplots()
    line_up, = ax.plot(m_numbers, m_time_taken, label='Merge Sort')
    line_down, = ax.plot(mi_numbers, mi_time_taken, label='Merge-Insert Sort')
    ax.legend([line_up, line_down], ['Merge Sort', 'Merge-Insert Sort'])
    plt.xlabel("Number of elements to sort")
    plt.ylabel("Time taken in seconds")
    plt.savefig("./io/metrics_images/merge_vs_merge_insert.png")
    plt.show()
