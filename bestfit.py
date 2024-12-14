import tkinter as tk
from tkinter import messagebox

# Function to perform Best Fit memory allocation
def best_fit(blocks, processes):
    for process in processes:
        best_block = None
        best_block_size = float('inf')

        # Find the best fit block for each process
        for block in blocks:
            if block['size'] >= process['size'] and block['size'] - process['size'] < best_block_size:
                best_block = block
                best_block_size = block['size'] - process['size']

        if best_block:
            best_block['size'] -= process['size']  # Allocate memory
            process['allocated_to'] = best_block['id']  # Assign process to block
        else:
            process['allocated_to'] = None  # No allocation

# Function to update the UI with allocation details
def update_ui():
    try:
        # Get block sizes from the entry fields
        blocks = [
            {'id': 1, 'size': int(entry_block1.get())},
            {'id': 2, 'size': int(entry_block2.get())},
            {'id': 3, 'size': int(entry_block3.get())},
            {'id': 4, 'size': int(entry_block4.get())},
            {'id': 5, 'size': int(entry_block5.get())}
        ]

        # Get process sizes from the entry fields
        processes = [
            {'name': 'A', 'size': int(entry_process_a.get()), 'allocated_to': None},
            {'name': 'B', 'size': int(entry_process_b.get()), 'allocated_to': None},
            {'name': 'C', 'size': int(entry_process_c.get()), 'allocated_to': None}
        ]

        # Perform memory allocation
        best_fit(blocks, processes)

        # Update the result display
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Memory Block Allocation:\n")
        for process in processes:
            if process['allocated_to']:
                result_text.insert(tk.END, f"Process {process['name']} is allocated to Block {process['allocated_to']}\n")
            else:
                result_text.insert(tk.END, f"Process {process['name']} could not be allocated.\n")
        result_text.insert(tk.END, "\nRemaining Memory Blocks:\n")
        for block in blocks:
            result_text.insert(tk.END, f"Block {block['id']}: {block['size']} KB\n")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

# Create the main window
root = tk.Tk()
root.title("Best Fit Memory Allocation")

# Create the input fields and labels for memory blocks
tk.Label(root, text="Enter Memory Block Sizes (KB)").grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(root, text="Block 1:").grid(row=1, column=0)
entry_block1 = tk.Entry(root)
entry_block1.grid(row=1, column=1)
tk.Label(root, text="Block 2:").grid(row=2, column=0)
entry_block2 = tk.Entry(root)
entry_block2.grid(row=2, column=1)
tk.Label(root, text="Block 3:").grid(row=3, column=0)
entry_block3 = tk.Entry(root)
entry_block3.grid(row=3, column=1)
tk.Label(root, text="Block 4:").grid(row=4, column=0)
entry_block4 = tk.Entry(root)
entry_block4.grid(row=4, column=1)
tk.Label(root, text="Block 5:").grid(row=5, column=0)
entry_block5 = tk.Entry(root)
entry_block5.grid(row=5, column=1)

# Create the input fields and labels for processes
tk.Label(root, text="Enter Process Sizes (KB)").grid(row=6, column=0, columnspan=2, pady=5)
tk.Label(root, text="Process A:").grid(row=7, column=0)
entry_process_a = tk.Entry(root)
entry_process_a.grid(row=7, column=1)
tk.Label(root, text="Process B:").grid(row=8, column=0)
entry_process_b = tk.Entry(root)
entry_process_b.grid(row=8, column=1)
tk.Label(root, text="Process C:").grid(row=9, column=0)
entry_process_c = tk.Entry(root)
entry_process_c.grid(row=9, column=1)

# Create the button to perform the allocation
btn_allocate = tk.Button(root, text="Allocate Memory", command=update_ui)
btn_allocate.grid(row=10, column=0, columnspan=2, pady=10)

# Create the text box to display the result
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=11, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
