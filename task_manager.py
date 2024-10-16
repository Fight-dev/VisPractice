import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите задачу.")

def remove_task():
    selected_index = task_list.curselection()
    if selected_index:
        del tasks[selected_index[0]]
        update_list()

def toggle_completion():
    selected_index = task_list.curselection()
    if selected_index:
        tasks[selected_index[0]]["completed"] = not tasks[selected_index[0]]["completed"]
        update_list()

def update_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        task_list.insert(tk.END, f"{'[x]' if task['completed'] else '[ ]'} {task['task']}")

root = tk.Tk()
root.title("Менеджер задач")

task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

remove_button = tk.Button(root, text="Удалить задачу", command=remove_task)
remove_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

complete_button = tk.Button(root, text="Отметить как выполненную", command=toggle_completion)
complete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

task_list = tk.Listbox(root, width=50, height=10)
task_list.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
