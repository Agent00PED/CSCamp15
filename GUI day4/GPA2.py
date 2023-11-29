import tkinter as tk

def calculate_grade():
    total_marks = int(entry_total_marks.get())
    obtained_marks = int(entry_obtained_marks.get())
    percentage = obtained_marks / total_marks * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    label_grade.config(text="Your grade is: {}".format(grade))

# Create a new window
window = tk.Tk()
window.title("Grade Calculator")

# Create labels and entries for total and obtained marks
label_total_marks = tk.Label(text="Enter Total Marks:")
label_total_marks.pack()
entry_total_marks = tk.Entry()
entry_total_marks.pack()

label_obtained_marks = tk.Label(text="Enter Obtained Marks:")
label_obtained_marks.pack()
entry_obtained_marks = tk.Entry()
entry_obtained_marks.pack()

# Create a button to calculate grade
button_calculate = tk.Button(text="Calculate Grade", command=calculate_grade)
button_calculate.pack()

# Create a label to display the grade
label_grade = tk.Label(text="")
label_grade.pack()

# Run the window
window.mainloop()