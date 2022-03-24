import tkinter
from tkinter import font
import tkinter.messagebox



class PizzaGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x300')
        self.main_window['background']='#ebe6dd'
        self.main_window.title("Caleb's Pizzeria")
        #self.font = tkinter.font.Font(family = 'Times', size = 20, weight = 'bold')

        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
      

        #Order Name
        self.name = tkinter.Label(self.first_frame, text = "Enter an name for your order:")
        self.entry_name = tkinter.Entry(self.first_frame, width=15)
        

        #Toppings
        self.toppings = tkinter.Label(self.second_frame, text = 'Toppings:', font = 'Times')
        
        self.cb_pep_var = tkinter.IntVar()
        self.cb_pineapple_var = tkinter.IntVar()
        self.cb_onion_var = tkinter.IntVar()

        self.cb_pep_var.set(0)
        self.cb_pineapple_var.set(0)
        self.cb_onion_var.set(0)

        self.cb_pep_box = tkinter.Checkbutton(self.second_frame, text =       'Pepperoni ($1.00):', variable=self.cb_pep_var)
        self.cb_pineapple_box = tkinter.Checkbutton(self.second_frame, text = 'Pineapple ($1.50): ', variable=self.cb_pineapple_var)
        self.cb_onion_box = tkinter.Checkbutton(self.second_frame, text =     'Onion       ($0.50):  ', variable=self.cb_onion_var)

        #pack checkboxes
        self.toppings.pack()
        self.cb_pep_box.pack()
        self.cb_pineapple_box.pack()
        self.cb_onion_box.pack()

        #crust
        #radio buttons
        self.crust = tkinter.Label(self.third_frame, text = 'Crust:', font='Times')
        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.third_frame, text = 'Thin              ', variable= self.radio_var, value= 1)
        self.rb2 = tkinter.Radiobutton(self.third_frame, text = 'Thick ($1.99)', variable= self.radio_var, value= 2)

        self.rb1.select()
        #pack radio buttons
        self.crust.pack(side='top')
        self.rb1.pack()
        self.rb2.pack()
        


        #pack frames
        self.first_frame.pack(side='top', anchor=tkinter.NW)
        
        self.second_frame.pack()
        
        self.third_frame.pack(side='top')
 
        #pack Labels
        self.name.pack(side='left')
        

        #pack Entry
        self.entry_name.pack(side='top')
        
        #main buttons
        self.paybutton = tkinter.Button(self.main_window, text = 'Pay', command = self.Calc_Price, font = 'Impact')
        self.quitbutton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        #pack main buttons
        self.quitbutton.pack(side='bottom')
        self.paybutton.pack(side='bottom')
        


        tkinter.mainloop()
        

    def Calc_Price(self):
        name = self.entry_name.get()
        
        self.total = 0
        
        if self.cb_pep_var.get() == 1:
            self.total += 1
        if self.cb_pineapple_var.get() == 1:
            self.total += 1.5
        if self.cb_onion_var.get() == 1:
            self.total += .5

        if self.radio_var.get() == 2:
            self.total += 1.99
        
        
        self.message =  name + "\nYour total is: $" + str(format(self.total, '.2f'))
        tkinter.messagebox.showinfo('Receipt', self.message)
        


pizza = PizzaGUI()