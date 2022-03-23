import tkinter
import tkinter.messagebox

class PizzaGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x300')
        self.main_window.title("Caleb's Pizzeria")

        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.forth_frame = tkinter.Frame(self.main_window)
        self.fifth_frame = tkinter.Frame(self.main_window)

        #Order Name
        self.name = tkinter.Label(self.first_frame, text = "Enter an name for your order:")
        def name(self):
            self.entry_name = tkinter.Entry(self.first_frame, width=15)
            return self.entry_name

        #Toppings
        self.toppings = tkinter.Label(self.second_frame, text = 'Toppings:')
        
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

        #pack frames
        self.first_frame.pack(side='top', anchor=tkinter.NW)
        
        self.second_frame.pack()
        '''
        self.third_frame.pack(side='top')
        self.forth_frame.pack(side='top')
        self.fifth_frame.pack(side='top')
        '''
        #pack Labels
        self.name.pack(side='left')
        

        #pack Entry
        self.entry_name.pack(side='top')
        
        #main buttons
        self.paybutton = tkinter.Button(self.main_window, text = 'Pay', command = self.Cal_Price)
        self.quitbutton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        #pack main buttons
        self.paybutton.pack(side='bottom')
        self.quitbutton.pack(side='bottom')


        tkinter.mainloop()
        

    def Cal_Price(self):
        
        total = 0
        if self.cb_pep_var == 1:
            total += 1
        if self.cb_pineapple_var == 1:
            total += 1.5
        if self.cb_onion_var == 1:
            total += .5
        
        self.message =  "\nYour total is: " + str(total)
        tkinter.messagebox.showinfo('Receipt', self.message)
        


pizza = PizzaGUI()