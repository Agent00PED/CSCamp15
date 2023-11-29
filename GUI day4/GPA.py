import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('GPA Calculator')

root.geometry("900x250")
app = tk.Tk()

#Label subject
subject1 = ttk.Label(root,text= 'Enter marks in 1st subject : ')
subject1.grid(row=0, column=0)
subject1.config(font=("Courier", 12))

subject2 = ttk.Label(root,text= 'Enter marks in 2nd subject : ')
subject2.grid(row=1, column=0)
subject2.config(font=("Courier", 12))

subject3 = ttk.Label(root,text= 'Enter marks in 3rd subject : ')
subject3.grid(row=2, column=0)
subject3.config(font=("Courier", 12))

subject4 = ttk.Label(root,text= 'Enter marks in 4th subject : ')
subject4.grid(row=3, column=0)
subject4.config(font=("Courier", 12))

subject5 = ttk.Label(root,text= 'Enter marks in 5th subject : ')
subject5.grid(row=4, column=0)
subject5.config(font=("Courier", 12))

subject6 = ttk.Label(root,text= 'Enter marks in 6th subject : ')
subject6.grid(row=5, column=0)
subject6.config(font=("Courier", 12))

mine = ttk.Label(root, text='Powered By Powerrr')
mine.grid(row=10, column=4)
mine.configure(foreground='green')

#Label credit hours
credit1_hour = ttk.Label(root,text='Enter Credit Hours :')
credit1_hour.grid(row=0, column=3)
credit1_hour.config(font=("Courier",12))

credit2_hour = ttk.Label(root,text='Enter Credit Hours :')
credit2_hour.grid(row=1, column=3)
credit2_hour.config(font=("Courier",12))

credit3_hour = ttk.Label(root,text='Enter Credit Hours :')
credit3_hour.grid(row=2, column=3)
credit3_hour.config(font=("Courier",12))

credit4_hour = ttk.Label(root,text='Enter Credit Hours :')
credit4_hour.grid(row=3, column=3)
credit4_hour.config(font=("Courier",12))

credit5_hour = ttk.Label(root,text='Enter Credit Hours :')
credit5_hour.grid(row=4, column=3)
credit5_hour.config(font=("Courier",12))

credit6_hour = ttk.Label(root,text='Enter Credit Hours :')
credit6_hour.grid(row=5, column=3)
credit6_hour.config(font=("Courier",12))

#Entry Box&Variables
subject1_var = tk.IntVar()
subject1_entry = ttk.Entry(root, width=10, textvariable= subject1_var)
subject1_entry.grid(row=0, column=1)

subject2_var = tk.IntVar()
subject2_entry = ttk.Entry(root, width=10, textvariable= subject1_var)
subject2_entry.grid(row=1, column=1)

subject3_var = tk.IntVar()
subject3_entry = ttk.Entry(root, width=10, textvariable= subject1_var)
subject3_entry.grid(row=2, column=1)

subject4_var = tk.IntVar()
subject4_entry = ttk.Entry(root, width=10, textvariable= subject1_var)
subject4_entry.grid(row=3, column=1)

subject5_var = tk.IntVar()
subject5_entry = ttk.Entry(root, width=10, textvariable= subject1_var)
subject5_entry.grid(row=4, column=1)

subject6_var = tk.IntVar()
subject6_entry = ttk.Entry(root, width=10, textvariable= subject1_var)
subject6_entry.grid(row=5, column=1)

quit = ttk.Button(root,text='Quit', command=root.destroy)
quit.grid(row=8, column=0)

#Entry Box credit hours
credit1_var = tk.IntVar()
credit1_entry = ttk.Entry(root, width=10, textvariable = credit1_var)
credit1_entry.grid(row=0, column= 4)

credit2_var = tk.IntVar()
credit2_entry = ttk.Entry(root, width=10, textvariable = credit2_var)
credit2_entry.grid(row=1, column= 4)

credit3_var = tk.IntVar()
credit3_entry = ttk.Entry(root, width=10, textvariable = credit3_var)
credit3_entry.grid(row=2, column= 4)

credit4_var = tk.IntVar()
credit4_entry = ttk.Entry(root, width=10, textvariable = credit4_var)
credit4_entry.grid(row=3, column= 4)

credit5_var = tk.IntVar()
credit5_entry = ttk.Entry(root, width=10, textvariable = credit5_var)
credit5_entry.grid(row=4, column= 4)

credit6_var = tk.IntVar()
credit6_entry = ttk.Entry(root, width=10, textvariable = credit6_var)
credit6_entry.grid(row=5, column= 4)

#Generate result
def calculate():
    sub1 = subject1_var.get()
    sub2 = subject2_var.get()
    sub3 = subject3_var.get()
    sub4 = subject4_var.get()
    sub5 = subject5_var.get()
    sub6 = subject6_var.get()

    #Check Code 1
    if sub1 < 50:
        sub1 = 0
    elif sub1 == 50:
        sub1 == 2.00
    elif sub1 == 51:
        sub1 == 2.05
    elif sub1 == 52:
        sub1 == 2.10
    elif sub1 == 53:
        sub1 == 2.15
    elif sub1 == 54:
        sub1 == 2.20
    elif sub1 == 55:
        sub1 == 2.25
    elif sub1 == 56:
        sub1 == 2.30
    elif sub1 == 57:
        sub1 == 2.35
    elif sub1 == 58:
        sub1 == 2.40
    elif sub1 == 59:
        sub1 == 2.45
    elif sub1 == 60:
        sub1 == 2.50
    elif sub1 == 61:
        sub1 == 2.55
    elif sub1 == 62:
        sub1 == 2.60
    elif sub1 == 63:
        sub1 == 2.65
    elif sub1 == 64:
        sub1 == 2.70
    elif sub1 == 65:
        sub1 == 2.75
    elif sub1 == 66:
        sub1 == 2.80
    elif sub1 == 67:
        sub1 == 2.85
    elif sub1 == 68:
        sub1 == 2.90
    elif sub1 == 69:
        sub1 == 2.95
    elif sub1 == 70:
        sub1 == 3.00
    elif sub1 == 71:
        sub1 == 3.05
    elif sub1 == 72:
        sub1 == 3.10
    elif sub1 == 73:
        sub1 == 3.15
    elif sub1 == 74:
        sub1 == 3.20
    elif sub1 == 75:
        sub1 == 3.25
    elif sub1 == 76:
        sub1 == 3.30
    elif sub1 == 77:
        sub1 == 3.35
    elif sub1 == 78:
        sub1 == 3.40
    elif sub1 == 79:
        sub1 == 3.45
    elif sub1 == 80:
        sub1 == 3.50
    elif sub1 == 81:
        sub1 == 3.55
    elif sub1 == 82:
        sub1 == 3.60
    elif sub1 == 83:
        sub1 == 3.65
    elif sub1 == 84:
        sub1 == 3.70
    elif sub1 == 85:
        sub1 == 3.75
    elif sub1 == 86:
        sub1 == 3.80
    elif sub1 == 87:
        sub1 == 3.85
    elif sub1 == 88:
        sub1 == 3.90
    elif sub1 == 89:
        sub1 == 3.95
    elif sub1 >= 90 and sub1 <=100:
        sub1 == 4.00
    else:
        sub1_error = ttk.Label(root, text= 'Invalid Input')
        sub1_error.grid(row=0, column=2)
        sub1_error.configure(foreground='Red')

    #Check Code 2
    if sub2 < 50:
        sub2 = 0
    elif sub2 == 50:
        sub2 == 2.00
    elif sub2 == 51:
        sub2 == 2.05
    elif sub2 == 52:
        sub2 == 2.10
    elif sub2 == 53:
        sub2 == 2.15
    elif sub2 == 54:
        sub2 == 2.20
    elif sub2 == 55:
        sub2 == 2.25
    elif sub2 == 56:
        sub2 == 2.30
    elif sub2 == 57:
        sub2 == 2.35
    elif sub2 == 58:
        sub2 == 2.40
    elif sub2 == 59:
        sub2 == 2.45
    elif sub2 == 60:
        sub2 == 2.50
    elif sub2 == 61:
        sub2 == 2.55
    elif sub2 == 62:
        sub2 == 2.60
    elif sub2 == 63:
        sub2 == 2.65
    elif sub2 == 64:
        sub2 == 2.70
    elif sub2 == 65:
        sub2 == 2.75
    elif sub2 == 66:
        sub2 == 2.80
    elif sub2 == 67:
        sub2 == 2.85
    elif sub2 == 68:
        sub2 == 2.90
    elif sub2 == 69:
        sub2 == 2.95
    elif sub2 == 70:
        sub2 == 3.00
    elif sub2 == 71:
        sub2 == 3.05
    elif sub2 == 72:
        sub2 == 3.10
    elif sub2 == 73:
        sub2 == 3.15
    elif sub2 == 74:
        sub2 == 3.20
    elif sub2 == 75:
        sub2 == 3.25
    elif sub2 == 76:
        sub2 == 3.30
    elif sub2 == 77:
        sub2 == 3.35
    elif sub2 == 78:
        sub2 == 3.40
    elif sub2 == 79:
        sub2 == 3.45
    elif sub2 == 80:
        sub2 == 3.50
    elif sub2 == 81:
        sub2 == 3.55
    elif sub2 == 82:
        sub2 == 3.60
    elif sub2 == 83:
        sub2 == 3.65
    elif sub2 == 84:
        sub2 == 3.70
    elif sub2 == 85:
        sub2 == 3.75
    elif sub2 == 86:
        sub2 == 3.80
    elif sub2 == 87:
        sub2 == 3.85
    elif sub2 == 88:
        sub2 == 3.90
    elif sub2 == 89:
        sub2 == 3.95
    elif sub2 >= 90 and sub2 <=100:
        sub2 == 4.00
    else:
        sub2_error = ttk.Label(root, text= 'Invalid Input')
        sub2_error.grid(row=0, column=2)
        sub2_error.configure(foreground='Red')

    #Check Code 3
    if sub3 < 50:
        sub3 = 0
    elif sub3 == 50:
        sub3 == 2.00
    elif sub3 == 51:
        sub3 == 2.05
    elif sub3 == 52:
        sub3 == 2.10
    elif sub3 == 53:
        sub3 == 2.15
    elif sub3 == 54:
        sub3 == 2.20
    elif sub3 == 55:
        sub3 == 2.25
    elif sub3 == 56:
        sub3 == 2.30
    elif sub3 == 57:
        sub3 == 2.35
    elif sub3 == 58:
        sub3 == 2.40
    elif sub3 == 59:
        sub3 == 2.45
    elif sub3 == 60:
        sub3 == 2.50
    elif sub3 == 61:
        sub3 == 2.55
    elif sub3 == 62:
        sub3 == 2.60
    elif sub3 == 63:
        sub3 == 2.65
    elif sub3 == 64:
        sub3 == 2.70
    elif sub3 == 65:
        sub3 == 2.75
    elif sub3 == 66:
        sub3 == 2.80
    elif sub3 == 67:
        sub3 == 2.85
    elif sub3 == 68:
        sub3 == 2.90
    elif sub3 == 69:
        sub3 == 2.95
    elif sub3 == 70:
        sub3 == 3.00
    elif sub3 == 71:
        sub3 == 3.05
    elif sub3 == 72:
        sub3 == 3.10
    elif sub3 == 73:
        sub3 == 3.15
    elif sub3 == 74:
        sub3 == 3.20
    elif sub3 == 75:
        sub3 == 3.25
    elif sub3 == 76:
        sub3 == 3.30
    elif sub3 == 77:
        sub3 == 3.35
    elif sub3 == 78:
        sub3 == 3.40
    elif sub3 == 79:
        sub3 == 3.45
    elif sub3 == 80:
        sub3 == 3.50
    elif sub3 == 81:
        sub3 == 3.55
    elif sub3 == 82:
        sub3 == 3.60
    elif sub3 == 83:
        sub3 == 3.65
    elif sub3 == 84:
        sub3 == 3.70
    elif sub3 == 85:
        sub3 == 3.75
    elif sub3 == 86:
        sub3 == 3.80
    elif sub3 == 87:
        sub3 == 3.85
    elif sub3 == 88:
        sub3 == 3.90
    elif sub3 == 89:
        sub3 == 3.95
    elif sub3 >= 90 and sub3 <=100:
        sub3 == 4.00
    else:
        sub3_error = ttk.Label(root, text= 'Invalid Input')
        sub3_error.grid(row=0, column=2)
        sub3_error.configure(foreground='Red')
    
    #Check Code 4
    if sub4 < 50:
        sub4 = 0
    elif sub4 == 50:
        sub4 == 2.00
    elif sub4 == 51:
        sub4 == 2.05
    elif sub4 == 52:
        sub4 == 2.10
    elif sub4 == 53:
        sub4 == 2.15
    elif sub4 == 54:
        sub4 == 2.20
    elif sub4 == 55:
        sub4 == 2.25
    elif sub4 == 56:
        sub4 == 2.30
    elif sub4 == 57:
        sub4 == 2.35
    elif sub4 == 58:
        sub4 == 2.40
    elif sub4 == 59:
        sub4 == 2.45
    elif sub4 == 60:
        sub4 == 2.50
    elif sub4 == 61:
        sub4 == 2.55
    elif sub4 == 62:
        sub4 == 2.60
    elif sub4 == 63:
        sub4 == 2.65
    elif sub4 == 64:
        sub4 == 2.70
    elif sub4 == 65:
        sub4 == 2.75
    elif sub4 == 66:
        sub4 == 2.80
    elif sub4 == 67:
        sub4 == 2.85
    elif sub4 == 68:
        sub4 == 2.90
    elif sub4 == 69:
        sub4 == 2.95
    elif sub4 == 70:
        sub4 == 3.00
    elif sub4 == 71:
        sub4 == 3.05
    elif sub4 == 72:
        sub4 == 3.10
    elif sub4 == 73:
        sub4 == 3.15
    elif sub4 == 74:
        sub4 == 3.20
    elif sub4 == 75:
        sub4 == 3.25
    elif sub4 == 76:
        sub4 == 3.30
    elif sub4 == 77:
        sub4 == 3.35
    elif sub4 == 78:
        sub4 == 3.40
    elif sub4 == 79:
        sub4 == 3.45
    elif sub4 == 80:
        sub4 == 3.50
    elif sub4 == 81:
        sub4 == 3.55
    elif sub4 == 82:
        sub4 == 3.60
    elif sub4 == 83:
        sub4 == 3.65
    elif sub4 == 84:
        sub4 == 3.70
    elif sub4 == 85:
        sub4 == 3.75
    elif sub4 == 86:
        sub4 == 3.80
    elif sub4 == 87:
        sub4 == 3.85
    elif sub4 == 88:
        sub4 == 3.90
    elif sub4 == 89:
        sub4 == 3.95
    elif sub4 >= 90 and sub4 <=100:
        sub4 == 4.00
    else:
        sub4_error = ttk.Label(root, text= 'Invalid Input')
        sub4_error.grid(row=0, column=2)
        sub4_error.configure(foreground='Red')

    #Check Code 5
    if sub5 < 50:
        sub5 = 0
    elif sub5 == 50:
        sub5 == 2.00
    elif sub5 == 51:
        sub5 == 2.05
    elif sub5 == 52:
        sub5 == 2.10
    elif sub5 == 53:
        sub5 == 2.15
    elif sub5 == 54:
        sub5 == 2.20
    elif sub5 == 55:
        sub5 == 2.25
    elif sub5 == 56:
        sub5 == 2.30
    elif sub5 == 57:
        sub5 == 2.35
    elif sub5 == 58:
        sub5 == 2.40
    elif sub5 == 59:
        sub5 == 2.45
    elif sub5 == 60:
        sub5 == 2.50
    elif sub5 == 61:
        sub5 == 2.55
    elif sub5 == 62:
        sub5 == 2.60
    elif sub5 == 63:
        sub5 == 2.65
    elif sub5 == 64:
        sub5 == 2.70
    elif sub5 == 65:
        sub5 == 2.75
    elif sub5 == 66:
        sub5 == 2.80
    elif sub5 == 67:
        sub5 == 2.85
    elif sub5 == 68:
        sub5 == 2.90
    elif sub5 == 69:
        sub5 == 2.95
    elif sub5 == 70:
        sub5 == 3.00
    elif sub5 == 71:
        sub5 == 3.05
    elif sub5 == 72:
        sub5 == 3.10
    elif sub5 == 73:
        sub5 == 3.15
    elif sub5 == 74:
        sub5 == 3.20
    elif sub5 == 75:
        sub5 == 3.25
    elif sub5 == 76:
        sub5 == 3.30
    elif sub5 == 77:
        sub5 == 3.35
    elif sub5 == 78:
        sub5 == 3.40
    elif sub5 == 79:
        sub5 == 3.45
    elif sub5 == 80:
        sub5 == 3.50
    elif sub5 == 81:
        sub5 == 3.55
    elif sub5 == 82:
        sub5 == 3.60
    elif sub5 == 83:
        sub5 == 3.65
    elif sub5 == 84:
        sub5 == 3.70
    elif sub5 == 85:
        sub5 == 3.75
    elif sub5 == 86:
        sub5 == 3.80
    elif sub5 == 87:
        sub5 == 3.85
    elif sub5 == 88:
        sub5 == 3.90
    elif sub5 == 89:
        sub5 == 3.95
    elif sub5 >= 90 and sub5 <=100:
        sub5 == 4.00
    else:
        sub5_error = ttk.Label(root, text= 'Invalid Input')
        sub5_error.grid(row=0, column=2)
        sub5_error.configure(foreground='Red')

    #Check Code 6
    if sub6 < 50:
        sub6 = 0
    elif sub6 == 50:
        sub6 == 2.00
    elif sub6 == 51:
        sub6 == 2.05
    elif sub6 == 52:
        sub6 == 2.10
    elif sub6 == 53:
        sub6 == 2.15
    elif sub6 == 54:
        sub6 == 2.20
    elif sub6 == 55:
        sub6 == 2.25
    elif sub6 == 56:
        sub6 == 2.30
    elif sub6 == 57:
        sub6 == 2.35
    elif sub6 == 58:
        sub6 == 2.40
    elif sub6 == 59:
        sub6 == 2.45
    elif sub6 == 60:
        sub6 == 2.50
    elif sub6 == 61:
        sub6 == 2.55
    elif sub6 == 62:
        sub6 == 2.60
    elif sub6 == 63:
        sub6 == 2.65
    elif sub6 == 64:
        sub6 == 2.70
    elif sub6 == 65:
        sub6 == 2.75
    elif sub6 == 66:
        sub6 == 2.80
    elif sub6 == 67:
        sub6 == 2.85
    elif sub6 == 68:
        sub6 == 2.90
    elif sub6 == 69:
        sub6 == 2.95
    elif sub6 == 70:
        sub6 == 3.00
    elif sub6 == 71:
        sub6 == 3.05
    elif sub6 == 72:
        sub6 == 3.10
    elif sub6 == 73:
        sub6 == 3.15
    elif sub6 == 74:
        sub6 == 3.20
    elif sub6 == 75:
        sub6 == 3.25
    elif sub6 == 76:
        sub6 == 3.30
    elif sub6 == 77:
        sub6 == 3.35
    elif sub6 == 78:
        sub6 == 3.40
    elif sub6 == 79:
        sub6 == 3.45
    elif sub6 == 80:
        sub6 == 3.50
    elif sub6 == 81:
        sub6 == 3.55
    elif sub6 == 82:
        sub6 == 3.60
    elif sub6 == 83:
        sub6 == 3.65
    elif sub6 == 84:
        sub6 == 3.70
    elif sub6 == 85:
        sub6 == 3.75
    elif sub6 == 86:
        sub6 == 3.80
    elif sub6 == 87:
        sub6 == 3.85
    elif sub6 == 88:
        sub6 == 3.90
    elif sub6 == 89:
        sub6 == 3.95
    elif sub6 >= 90 and sub6 <=100:
        sub6 == 4.00
    else:
        sub3_error = ttk.Label(root, text= 'Invalid Input')
        sub3_error.grid(row=0, column=2)
        sub3_error.configure(foreground='Red')

app.mainloop()