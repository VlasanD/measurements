import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from benchmarks import *


def generate_graph(selected_option):
    # Clear the previous graph
    for widget in graph_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots()
    results = data.get(selected_option, {})
    averages = []

    for name, values in results.items():
        y = values
        if y:
            average_value = sum(y)/len(y)
            averages.append(average_value)
            if selected_option == 'Context Switch' or selected_option == 'Thread Creation':
                ax.bar(name, math.log(average_value) , label=f"{name} (Average: {average_value:.2f})")
            else:
                ax.bar(name, average_value , label=f"{name} (Average: {average_value:.2f})")


    ax.set_xlabel("Language")
    if selected_option == 'Context Switch' or 'Thread Creation':
        ax.set_ylabel("Log Time(microseconds)")
    else:
        ax.set_ylabel("Time(microseconds)")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Update the layout
    graph_frame.update_idletasks()


def execute_button_click():
    selected_option = dropdown.get()
    generate_graph(selected_option)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Performance Measurement in C++, Python, and Rust")
    root.minsize(width=450, height=450)

    data = {
        'Dynamic Allocation': dynamic_alloc,
        'Static Memory Access': static_access,
        'Dynamic Memory Access': dynamic_access,
        'Thread Creation': threads,
        'Context Switch': context,
        'Thread Migration': migration
    }

    x = [i for i in range(NO_TESTS)]

    options = list(data.keys())

    dropdown = ttk.Combobox(root, values=options)
    dropdown.set(options[0])
    dropdown.pack(pady=10)

    execute_button = tk.Button(root, text="Execute", command=execute_button_click)
    execute_button.pack(pady=10)

    # Frame to hold the graph
    graph_frame = tk.Frame(root)
    graph_frame.pack(expand=1, fill="both")

    root.mainloop()
