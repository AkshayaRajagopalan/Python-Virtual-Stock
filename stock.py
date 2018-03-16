from tkinter import*

root = Tk()
w=Label(root,text="Stock Check")
w.pack()
stock = []

class remove(object):
    def __init__(self):
        self.remid = 0;
        self.remc = 0;
        self.present = False
    def removing(self):
        while True:
            self.remid = simpledialog.askstring("ID", "Enter the ID of the product you want to remove: ")
            for i in stock:
                if i[0] == self.remid:
                    self.present = True
                    stock.remove(i)
                    messagebox.showinfo("Success!", "Product successfully removed!")
                    print (stock)
                    break
            if self.present == False:
                messagebox.showinfo("Error!", "The ID you entered is not present in stock!! \n Try again!")
            else:
                break

        while True:
            self.remc =  simpledialog.askstring("What Next?","Enter 1 if you want to remove more items, enter 2 if you want to go to the main menu: ")
            if self.remc not in ['1','2']:
                messagebox.showinfo("Error", "Incorrect value entered! Try again!")
            else:
                break


class edit(object):
    def __init__(self):
        self.editc = 0
        self.editid = 0
        self.cedit = 0
        self.present = False
        self.editpara = ""
        self.choice1 = 0;
        self.editname = "";
    def editing(self):
        self.editc = simpledialog.askstring("Choice"," 1 - change name \n 2 - change id  \n 3 - change number in stock \n Select the appropriate option: ")
        if self.editc not in ['1','2','3','4','5']:
            messagebox.showinfo("Error", "Enter a valid option!!")
        elif self.editc == '1':
            self.changename()
        elif self.editc == '2':
            self.changeid()
        elif self.editc == '3':
            self.changestock()
        while True:
            self.cedit =  simpledialog.askstring("What Next?","Enter 1 if you want to edit more, enter 2 if you want to go to the main menu: ")
            if self.cedit not in ['1','2']:
                messagebox.showinfo("Error", "Incorrect value entered! Try again!")
            else:
                break
    def changename(self):
        while True:
            self.editid = simpledialog.askstring("Enter ID","Enter the ID of the product: ")
            for i in stock:
                if i[0] == self.editid:
                    self.present = True
                    self.editpara = simpledialog.askstring("Name","Enter the name you want to change it to: ")
                    i[1] = self.editpara
                    messagebox.showinfo("Success!", "The name was updated!!")
                    print (stock)
                    break

            if self.present == False:
                messagebox.showinfo("Error!", "The ID you entered is not present in stock!! \n Try again!")
            else:
                self.present = False
                break

    def changeid(self):
        while True:
            self.editname = simpledialog.askstring("Name","Enter the name of the product: ")
            for i in stock:
                if i[1] == self.editname:
                    self.present = True
                    self.editpara = simpledialog.askstring("ID","Enter the new ID: ")
                    i[0] = self.editpara
                    messagebox.showinfo("Success!", "The ID was updated!")
                    print (stock)
                    break
            if self.present == False:
                messagebox.showinfo("Error!", "The name of the product you entered is not present in stock!! \n Try again!")
            else:
                self.present = False
                break

    def changestock(self):
        while True:
            self.editid = simpledialog.askstring("ID", "Enter the ID of the product: ")
            for i in stock:
                if i[0] == self.editid:
                    self.present = True
                    while True:
                        self.editpara = simpledialog.askstring("Number", "Enter the number by which you want to alterthe stock \n If you want to decrease the count, include a negative sign before your number : ")
                        if int(i[3]) + int(self.editpara) < 0:
                            messagebox.showinfo("Error!", "Not enough products to remove \n Try again!")
                        else:
                            i[3] = str(int(i[3])+int(self.editpara))
                            messagebox.showinfo("Success!", "Number of products was updated")
                            print (stock)
                            break
                    break
            if self.present == False:
                messagebox.showinfo("Error!", "The ID of the product you entered was not available \n Try again")
            else:
                self.present = False
                break
                               

class add(object):
    def __init__(self):
        self.name = "";
        self.price = 0.0;
        self.id = 0;
        self.number = 0;
        self.manday = 0;
        self.manmonth = 0;
        self.manyear = 0;
        self.exmonth = 0;
        self.exyear = 0;
        self.exday = 0;
        self.c = 0;
    def adding(self):
        
            stocksub = [0,0,0,0,0,0,0,0,0]; 
            messagebox.showinfo("Instructions", "Enter the stock specifications as the message boxes pop up!")
            self.name = simpledialog.askstring("Name","Name of the product: ")
            stocksub[1] = self.name
            self.id = simpledialog.askstring("ID","product ID: ")
            for i in stock:
                if i[0] == self.id:
                    while True:
                        choice = simpledialog.askstring("Already Exists","A product with the same ID already exists!! \n If you want to try again, press 0 \n If you want to go to the main menu, press 1 : ")
                        if choice == 0:
                            break
                        elif choice == 1:
                            Choice.input()
                        else:
                            messagebox.showinfo("Error", "Enter a valid number")
                        
                    break
                
                        
            self.price = simpledialog.askstring("Price", "Enter the price of the item: " )
                
            self.number = simpledialog.askstring("Number of stock","Number of product: ")
            while True:
                self.exmonth = simpledialog.askstring("Month","Expiry month(number): ")
                if int(self.exmonth) >12 or int(self.exmonth)<1:
                    messagebox.showinfo("Error", "Enter a valid month between 1 and 12")
                else:
                    break
            
            self.exyear = simpledialog.askstring("Year","Enter Expiry year(number): ")
            while True:
                self.manday = simpledialog.askstring("Day","Manufacture date(day): ")
                if int(self.manday) >30 or int(self.manday)<1:
                    messagebox.showinfo("Error", "Enter a valid date between 1 and 30")
                else:
                    break
            while True:
                self.manmonth = simpledialog.askstring("Month","Manufacture month(number): ")
                if int(self.manmonth) >12 or int(self.manmonth)<1:
                    messagebox.showinfo("Error", "Enter a valid month between 1 and 12")
                else:
                    break
            
            self.manyear = simpledialog.askstring("Year","Enter current year(number): ")
                   
                    
            stocksub[0] = self.id
            stocksub[1] = self.name
            stocksub[2] = self.price
            stocksub[3] = self.number
            stocksub[4] = self.manday
            stocksub[5] = self.manmonth
            stocksub[6] = self.manyear
            stocksub[7] = self.exmonth
            stocksub[8] = self.exyear
            stock.append(stocksub)
            print (stock)
                
            while True:
                self.c =  simpledialog.askstring("What Next?","Enter 1 if you want to add more, enter 2 if you want to go to the main menu: ")
                if self.c not in ['1','2']:
                     messagebox.showinfo("Error", "Incorrect value entered! Try again!")
                else:
                    break

class display(object):
    def __init__(self):
        self.disid = 0
        self.disc = 0
        self.disstr = ""
    def displaying(self):
        while True:
            self.disid = simpledialog.askstring("ID", "Enter the ID of the product you want to display: ")
            for i in stock:
                if i[0] == self.disid:
                    self.present = True
                    self.disstr = "Product and corresponding details: \n Name: "+i[1]+" \n ID: "+i[0]+" \n Price: "+i[2]+"$ \n Pieces left: "+i[3]+" \n Manufactured Date: "+i[4]+"/"+i[5]+"/"+i[6]+" \n Expiry Date: "+i[7]+"/"+i[8]+" \n"
                    messagebox.showinfo("Details",self.disstr)
                    break
            if self.present == False:
                messagebox.showinfo("Error!", "The ID of the product you entered was not available \n Try again")
            else:
                self.present = False
                break
        
        while True:
            self.disc =  simpledialog.askstring("What Next?","Enter 1 if you want to display another item, enter 2 if you want to go to the main menu: ")
            if self.disc not in ['1','2']:
                messagebox.showinfo("Error", "Incorrect value entered! Try again!")
            else:
                break

class Choice(add,edit,remove,display):
    def __init__(self):
        add.__init__(self)
        edit.__init__(self)
        remove.__init__(self)
        display.__init__(self)
        self.choice= 0;
    def input(self):
        while True:
            self.choice = simpledialog.askstring("Choice","'1 - to add an item \n 2 - to remove an item \n 3 - to edit an item \n 4 - to view a particular item and its properties \n 0 - to exit \n Enter your choice: ")
            if self.choice not in ['0','1','2','3','4']:
                messagebox.showinfo("Error", "Invalid Input!! Please try again.")
            elif self.choice == '1':
                while True:
                    self.adding()
                    if self.c == '2':
                        break
            elif self.choice == '2':
                while True:
                    self.removing()
                    if self.remc == '2':
                        break
            elif self.choice == '3':
                while True:
                    self.editing()
                    if self.cedit == '2':
                        break
            elif self.choice == '4':
                while True:
                    self.displaying()
                    if self.disc == '2':
                        break
            elif self.choice == '0':
                messagebox.showinfo("Done!", "Successfully finished adding and managing virtual stock!!!")
                break

object1 = Choice()
object1.input()

    


