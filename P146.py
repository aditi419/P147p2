from tkinter import *
root = Tk()
root.title('Fibonacci Sum')
root.geometry('300x400')

entry = Entry(root)
root.place(relx=0.5,rely=0.2,anchor=CENTER)

label = 'Fibonacci Series'
label.place(relx=0.5,rely=0.3,anchor=CENTER)
label2 = ''
label2.place(relx=0.5,rely=0.4,anchor=CENTER)

def stuff():
    userInput = int(entry.get())
    
    firstNum = 0
    secNum = 1
    counter = 0
    sum1 = 0
    sum2 = 0
    
    while counter <= userInput:
        label['text'] += str(sum1) + ' '
        label2['text'] = 'Fibonacci Sum: ' + str(sum2)
        
        counter = counter + 1
        firstNum = secNum
        secNum = sum1
        sum1 = firstNum + secNum
        sum2 = sum2 + sum1

btn = Button(root,text='Show Fibonacci Series',command=stuff)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()