from time import strftime
from tkinter import Label,Tk

# configuration of digital clock window
window = Tk()
window.title("") # title of digital clock is empty
window.geometry("200x80") # geometry of digital clock can be fixed from here 
window.configure(bg = "green")# colour can be set from here
window.resizable(False,False)# window size can not be set manually by user
# here clock_label define the outer geometry of digital clock include colour,type etc.
clock_label = Label(window, bg = "black", fg = "cyan", font =( "arial",30,"bold"), relief = "flat" )
clock_label.place(x = 20, y = 20)
# def function here work for to update time of digital clock in every 80 milliseconds
def update_label():
    current_time = strftime("%H: %M: %S\n %d-%m-%y")
    clock_label.configure(text = current_time )
    clock_label.after("80", update_label)
    clock_label.pack(anchor = "center")




update_label()
window.mainloop()


# End of function:)
