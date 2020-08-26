# Importing the required libraries
from tkinter import * 
import sentences
import difflib

time_left = 10

# Defining the countdown function
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timeLabel.config(text="Time Left: "+ str(time_left))
        timeLabel.after(1000, countdown)
        
    # Tasks to be done after countdown ends
    if time_left == 0:
        timeLabel.destroy()
        writing_text.destroy()
        typingarea.destroy()
        wordCount = Label(textvariable=totalwords, font="comicsasms 10", pady=20)
        wordCount.pack(side=LEFT, anchor="nw")

        correctwords = Label(textvariable=correct_words, font="comicsasms 10", pady=20,)
        correctwords.pack(side=LEFT, anchor="sw")

# Defining the function for counting words
def results(event):
    var = str(typingarea.get(1.0, END))
    var = var.split() 
    totalwords.set(f"Your typing speed was {len(var)} WPM (Words per minute)") 
    var2 = str(writing_text)
    var2.split()

if __name__ == "__main__":
    
    # Making the parent window
    root = Tk()
    root.title("Typing Test")
    root.geometry("700x500")

    # Setting the icon and Heading
    # root.wm_iconbitmap("icon.ico")
    Label(text="Typing Test", font="lucida 30 bold").pack()

    # Adding the start button
    start_btn = Button(text="START", command=lambda:[start_btn.pack_forget(), countdown(), 
    typingarea.delete(1.0,END)])
    start_btn.pack()

    # Countdown label
    timeLabel = Label(root, text = "Time left: " + str(time_left), font = ('Helvetica', 20))          
    timeLabel.pack(anchor="w") 

    # Making the scrollbar
    scrollbar = Scrollbar(root)
    scrollbar.pack(fill=Y, side=RIGHT)

    # Text to be written by user
    writing_text = Listbox(root, height=6, font=" calibri 14", yscrollcommand=scrollbar.set)
    writing_text.pack(fill=X, pady=30)

    # Using sentences from 'sentences.py'
    for i in sentences.sentences:
        writing_text.insert(END, i)

    # Variable for storing words
    totalwords = StringVar()
    correct_words = StringVar()

    # Making The typing area
    typingarea = Text(root, height=5, font="calibri 14")
    typingarea.pack(fill=X)
    typingarea.focus_set()

    scrollbar.config(command=writing_text.yview)
    # scrollbar2.config(command=correctwords.xview)

    # Binding the events
    typingarea.bind("<KeyRelease>", results)

    root.mainloop()
