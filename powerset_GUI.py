import tkinter as tk
from tkinter import messagebox

# Function to generate the power set recursively
def powerset(input_set):
    if len(input_set) == 0:  # Base case: the power set of an empty set is a set containing the empty set
        return [set()]
    first_elem = input_set[0]  # Get the first element and the rest of the set
    rest = input_set[1:]
    
    rest_powerset = powerset(rest)  # Recursively compute the power set of the rest of the set
    
    # Combine the subsets: add the first element to each subset
    # in the power set of the rest of the set
    with_first_elem = [subset | {first_elem} for subset in rest_powerset]
    
    # Return the combination of both sets (with and without the first element)
    return rest_powerset + with_first_elem

# Function to parse the input string into a set of meaningful elements
def parse_input(input_string):
    # Split the string by commas, strip whitespace, and ignore empty strings
    return [element.strip() for element in input_string.split(',') if element.strip()]

# Function to handle the power set generation and display
def generate_powerset():
    user_input = input_entry.get().strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter elements separated by commas.")
        return

    input_set = parse_input(user_input)
    if not input_set:
        messagebox.showwarning("Input Error", "Input contains no valid elements. Please try again.")
        return
    
    result = powerset(input_set)
    
    # Format the result to replace empty set representation
    formatted_result = []
    for subset in result:
        if subset == set():
            formatted_result.append("∅")
        else:
            formatted_result.append(str(subset))
    
    # Display the formatted result
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "The power set is:\n")
    for subset in formatted_result:
        result_text.insert(tk.END, f"{subset}\n")

# Function to clear the input and results
def clear_inputs():
    input_entry.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

# Create the main tkinter window
root = tk.Tk()
root.title("Power Set Generator")

# Input section
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter elements (separated by commas):").grid(row=0, column=0, padx=5, pady=5)

input_entry = tk.Entry(input_frame, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Power Set", command=generate_powerset)
generate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_inputs)
clear_button.grid(row=0, column=1, padx=10)

# Output section with scrollbar
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

tk.Label(result_frame, text="Power Set Result:").pack(anchor="w")

# Create a text widget with a vertical scrollbar
scrollbar = tk.Scrollbar(result_frame)
result_text = tk.Text(result_frame, height=15, width=50, wrap="word", yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)

result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Footer
footer_label = tk.Label(root, text="Bagon | Fernandez | Fontanilla | Zapico")
footer_label.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
