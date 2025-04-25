import psutil
import tkinter as tk
from tkinter import StringVar

def update_stats():
    # Get system stats
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    # Update labels
    cpu_var.set(f"CPU Usage: {cpu_usage}%")
    memory_var.set(f"Memory Usage: {memory_usage}%")
    disk_var.set(f"Disk Usage: {disk_usage}%")

    # Time to run again
    root.after(1000, update_stats)

# Overlay window
root = tk.Tk()
root.title("System Monitor")
root.geometry("200x100")
root.attributes('-topmost', True)  # Keep the window on top
root.overrideredirect(True)  # Remove window decorations
root.attributes('-transparentcolor', 'black')
root.configure(bg='black')

# StringVars for dynamic updates
cpu_var = StringVar()
memory_var = StringVar()
disk_var = StringVar()

# labels
cpu_label = tk.Label(root, textvariable=cpu_var, font=("Arial", 12, "bold"), fg="green", bg="black", anchor="w", justify="left")
cpu_label.pack(fill="x", pady=5)
memory_label = tk.Label(root, textvariable=memory_var, font=("Arial", 12, "bold"), fg="green", bg="black", anchor="w", justify="left")
memory_label.pack(fill="x", pady=5)
disk_label = tk.Label(root, textvariable=disk_var, font=("Arial", 12, "bold"), fg="green", bg="black", anchor="w", justify="left")
disk_label.pack(fill="x", pady=5)

# update stats
update_stats()

# Run
root.mainloop()