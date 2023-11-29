import tkinter as tk
from tkinter import messagebox
from tkinter import *

def calculate_grade():
    score = (score_entry.get())
    if(not score.isdigit()):
         messagebox.showwarning("คะแนนไม่ถูกต้อง","กรุณากรอกตัวเลข")
    elif int(score) >= 101: 
         messagebox.showwarning("คะแนนไม่ถูกต้อง", "กรุณากรอกคะแนนระหว่าง 0-100")
    elif int(score) >= 80:
        grade = "A"
    elif int(score) >= 75:
        grade = "B+"
    elif int(score) >= 70:   
        grade = "B"
    elif int(score) >= 65:
        grade = "C+"
    elif int(score) >= 60:
        grade = "C"
    elif int(score) >= 55:
        grade = "D+"
    elif int(score) >= 50:
        grade = "D"
    else:
        grade = "F"
    result_label.config(text=f"คะแนน {score} จะได้เกรด {grade}")

app = tk.Tk()
app.iconbitmap('emoji.ico')#title picture
app.title('เรือวาฬขาว')
app.geometry("300x200")
app.resizable(False, False)
app.configure(bg='#CCFFFF')

score_label = tk.Label(app, text="กรอกคะแนน🐋", font=("Arial", 14), bg='#CCFFFF')
score_label.pack(pady=10)

score_entry = tk.Entry(app, font=("Arial", 14))
score_entry.pack()

calculate_button = tk.Button(app, text="คำนวณเกรด", font=("Arial", 14), bg='#4caf50', fg='#CCFFFF', 
                    activebackground='#3e8e41', activeforeground='#CCFFFF', command=calculate_grade)
calculate_button.pack(pady=10)

result_label = tk.Label(app, font=("Arial", 14), bg='#CCFFFF')
result_label.pack()

app.mainloop()