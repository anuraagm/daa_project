import matplotlib.pyplot as plt
import ast

if __name__ == "__main__":
    print("Analysing the results of Quick Sort vs Quick Insert Sort runs :")

    quick_sort_write_path = './io/quick_sort/comparison3_output.txt'
    quick_insert_sort_write_path = './io/quick_insert_sort/comparison3_output.txt'

    with open(quick_sort_write_path, 'r') as f:
        quick_sort_result = ast.literal_eval(f.read())

    with open(quick_insert_sort_write_path, 'r') as f:
        quick_insert_sort_result = ast.literal_eval(f.read())

    quick_sort_result = {int(k): float(v) for k, v in quick_sort_result.items()}
    quick_insert_sort_result = {int(k): float(v) for k, v in quick_insert_sort_result.items()}

    quick_sort_list = quick_sort_result.items()
    q_numbers, q_time_taken = zip(*quick_sort_list)

    quick_insert_sort_list = quick_insert_sort_result.items()
    qi_numbers, qi_time_taken = zip(*quick_insert_sort_list)

    fig, ax = plt.subplots()
    line_up, = ax.plot(q_numbers, q_time_taken, label='Quick Sort')
    line_down, = ax.plot(qi_numbers, qi_time_taken, label='Quick-Insert Sort')
    ax.legend([line_up, line_down], ['Quick Sort', 'Quick-Insert Sort'])
    plt.xlabel("Number of elements to sort")
    plt.ylabel("Time taken in seconds")
    plt.savefig("./io/metrics_images/quick_vs_quick_insert.png")
    plt.show()
