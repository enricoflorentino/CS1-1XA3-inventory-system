## Enrico Florentino
## 400062052
## Final Project, 1XA3 
## April 9, 2017

from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox


listofitems = dict () #dictionary of items that are to contain every item in the inventory

class Item:
    
    ## Initializes the item with the components in the parameters ##
    def __init__(self,item_number,quantity,item_name,item_location,item_info):
        
        self.item_number = item_number
        self.quantity = quantity
        self.item_name = item_name
        self.item_location = item_location
        self.item_info = item_info

        
    ## These functions will RETURN the item's specific component dependent on whichever one is called ##
    def display_item_number(self): return self.item_number
    def display_quantity(self): return self.quantity
    def display_item_name(self): return self.item_name
    def display_item_location(self): return self.item_location
    def display_item_info(self): return self.item_info
    
    ## These functions will update the item's specific component ##
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    def update_item_name(self, new_item_name):
        self.item_name = new_item_name
    def update_item_location(self, new_item_location):
        self.item_location = new_item_location
    def update_item_info(self, new_item_info):
        self.item_info = new_item_info

def exit(): #function will close the inventory upon request
    if messagebox.askquestion(title="Confirmation",message="Do you wish to proceed?"):
        root.destroy()


def clearentries(): #function only has the purpose of clearing entries when the button is pressed
    item_numberV.set("")
    quantityV.set("")
    item_nameV.set("")
    item_locationV.set("")
    item_infoV.set("")
    
def addnewitem(): # function will add item to inventory using the class Item 


    # These configures set the labels back to their original context if anything was changed due to errors
    label1.configure(background="grey")
    label1.configure(text="Item Number:")
    label2.configure(background="grey")
    label2.configure(text="Quantity:")
    label3.configure(background="grey")
    label3.configure(text="Item Name:")
    label4.configure(background="grey")
    label4.configure(text="Item Location:")
    label5.configure(background="grey")
    label5.configure(text="Item Description:")



    
    # These if/elifs check if any of the entry fields are blank and notifies the user
    
    if item_numberV.get() == "" or item_numberV.get() == None: 
        label1.configure(background="red")
        label1.configure(text="Enter an Item Number")
        item_number_entry.focus_set()
        pass
    elif quantityV.get() == "" or quantityV.get() == None:
        label2.configure(background="red")
        label2.configure(text="Enter the Quantity")
        quantity_entry.focus_set()
        pass
    elif item_nameV.get() == "" or item_nameV.get() == None:
        label3.configure(background="red")
        label3.configure(text="Enter the Item Name")
        item_name_entry.focus_set()
        pass
    elif item_locationV.get() == "" or item_locationV.get() == None:
        label4.configure(background="red")
        label4.configure(text="Enter the Item Location")
        item_location_entry.focus_set()
        pass
    elif item_infoV.get() == "" or item_infoV.get() == None:
        label5.configure(background="red")
        label5.configure(text="Enter the Item's Description")
        item_description_entry.focus_set()
        pass

        
    elif item_numberV.get() in listofitems: #If item number is already in inventory, notify user
        label1.configure(background="red")
        label1.configure(text="Already in Inventory")
        item_number_entry.focus_set()
        
        # Sets the entry fields to blank
        item_numberV.set("")
        quantityV.set("")
        item_nameV.set("")
        item_locationV.set("")
        item_infoV.set("")
        pass
    else:
        #Puts the new item into the inventory, with the key being the item number
        listofitems[item_numberV.get()]=Item(item_numberV.get(),quantityV.get(),item_nameV.get(),item_locationV.get(),item_infoV.get())
        messagebox.showinfo(message='Item added successfully!')
        #Sets the entry fields to blank
        item_numberV.set("")
        quantityV.set("")
        item_nameV.set("")
        item_locationV.set("")
        item_infoV.set("")


def searchforitem(): # function that will fill in inventory using the class Item
    
    
    # These configures set the labels back to their original context if anything was changed due to errors
    label1.configure(background="grey")
    label1.configure(text="Item Number:")
    label2.configure(background="grey")
    label2.configure(text="Quantity:")
    label3.configure(background="grey")
    label3.configure(text="Item Name:")
    label4.configure(background="grey")
    label4.configure(text="Item Location:")
    label5.configure(background="grey")
    label5.configure(text="Item Description:")
    
    
    tempword=item_numberV.get()
    if tempword in listofitems:
        quantityV.set("")
        item_nameV.set("")
        item_locationV.set("")
        item_infoV.set("")
        # Fills in each field to the appropriate inventory item
        quantityV.set(listofitems[tempword].display_quantity())
        item_nameV.set(listofitems[tempword].display_item_name())
        item_locationV.set(listofitems[tempword].display_item_location())
        item_infoV.set(listofitems[tempword].display_item_info())
    else:
        #If the item number that was being searched for is not an actual item, clears the entry and does not show any components
        item_numberV.set("")
        label1.configure(background="red")
        label1.configure(text="Not in Inventory")
        item_number_entry.focus_set()
        pass
    
def updatecurrentitem():
    # These configures set the labels back to their original context if anything was changed due to errors
    label1.configure(background="grey")
    label1.configure(text="Item Number:")
    label2.configure(background="grey")
    label2.configure(text="Quantity:")
    label3.configure(background="grey")
    label3.configure(text="Item Name:")
    label4.configure(background="grey")
    label4.configure(text="Item Location:")
    label5.configure(background="grey")
    label5.configure(text="Item Description:")
    
    
    if item_numberV.get() in listofitems:
        #Updates each item component to whatever was in the entry field at the time the update button was pressed
        listofitems[item_numberV.get()].update_quantity(quantityV.get())
        listofitems[item_numberV.get()].update_item_name(item_nameV.get())
        listofitems[item_numberV.get()].update_item_location(item_locationV.get())
        listofitems[item_numberV.get()].update_item_info(item_infoV.get())
        
        #Sets the entry fields to blank
        item_numberV.set("")
        quantityV.set("")
        item_nameV.set("")
        item_locationV.set("")
        item_infoV.set("")
    else:
        #If the item number that was being searched for is not an actual item, clears the entry and does not show any components
        item_numberV.set("")
        label1.configure(background="red")
        label1.configure(text="Not in Inventory")
        item_number_entry.focus_set()
        pass
    
def savedatatofile(): #This function will transfer the contents of all the items of the inventory system and place it in a text file
    # These configures set the labels back to their original context if anything was changed due to errors
    label1.configure(background="grey")
    label1.configure(text="Item Number:")
    label2.configure(background="grey")
    label2.configure(text="Quantity:")
    label3.configure(background="grey")
    label3.configure(text="Item Name:")
    label4.configure(background="grey")
    label4.configure(text="Item Location:")
    label5.configure(background="grey")
    label5.configure(text="Item Description:")
    
    if len(listofitems) == 0: #If there are no items, do not do anything
        pass
    else:
        root.withdraw() #Closes the Inventory Management window temporarily
        file_path = filedialog.askopenfilename() #Opens up the interface to be able to select the text file we are writing the contents to
        newfile=open(file_path,"w")
        
        for key in listofitems: #For each element in the dictionary, print out its contents on each line
            bigstring=key+","+listofitems[key].display_quantity()+","+listofitems[key].display_item_name()+","+listofitems[key].display_item_location()+","+listofitems[key].display_item_info()
            newfile.write(bigstring+"\n")
        newfile.close() #Closes the text file
        root.deiconify() #Opens back  up the Inventory Management System 

def loadfromfile(): #This function will transfer the contents of a text file that contains item elements into the inventory system 
    
    # These configures set the labels back to their original context if anything was changed due to errors
    label1.configure(background="grey")
    label1.configure(text="Item Number:")
    label2.configure(background="grey")
    label2.configure(text="Quantity:")
    label3.configure(background="grey")
    label3.configure(text="Item Name:")
    label4.configure(background="grey")
    label4.configure(text="Item Location:")
    label5.configure(background="grey")
    label5.configure(text="Item Description:")

    root.withdraw()
    file_path2 = filedialog.askopenfilename()
    readingfile=open(file_path2,"r")

    listofnewitems=readingfile.readlines() #makes a list of the textfile, each line(item) being one element
    for i in range(len(listofnewitems)):
        listofnewitems[i]=listofnewitems[i].replace("\n","")
    for i in range(len(listofnewitems)): #Creates a new item based on each line of string in the text file that was given
        templist=listofnewitems[i].split(",")
        listofitems[templist[0]]=Item(templist[0],templist[1],templist[2],templist[3],templist[4]) 
    readingfile.close() #Closes the text file
    root.deiconify() #Opens back  up the Inventory Management System 


def deletefromlist(): # This function will delete the specified item (based on item number) from the list of items
    
    # These configures set the labels back to their original context if anything was changed due to errors
    label1.configure(background="grey")
    label1.configure(text="Item Number:")
    label2.configure(background="grey")
    label2.configure(text="Quantity:")
    label3.configure(background="grey")
    label3.configure(text="Item Name:")
    label4.configure(background="grey")
    label4.configure(text="Item Location:")
    label5.configure(background="grey")
    label5.configure(text="Item Description:")
    
    
    if item_numberV.get() in listofitems: #If the Item is inventory, deletes the item from the dictionary of items
        if messagebox.askquestion(title="Confirmation",message="Do you wish to proceed?"):
            del listofitems[item_numberV.get()]
            item_numberV.set("")
            quantityV.set("")
            item_nameV.set("")
            item_locationV.set("")
            item_infoV.set("")
    else:
        #If the item number that was being searched for is not an actual item, clears the entry and does not show any components
        item_numberV.set("")
        label1.configure(background="red")
        label1.configure(text="Not in Inventory")
        pass
    

    
## GUI Aspect of Project ## 

root=Tk()
root.title("RestEasy: Inventory Management")

mainframe=ttk.Frame(root, relief=SUNKEN, borderwidth=5)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Variables #

item_numberV = StringVar() 
quantityV = StringVar()
item_nameV = StringVar()
item_locationV = StringVar()
item_infoV = StringVar()


myFont = Font(family="MS Serif",size=12)


# Item Number entry text field and label
item_number_entry=ttk.Entry(mainframe,width=15,text=item_numberV,font=myFont)
item_number_entry.grid(row=0,column=2,columnspan=1,sticky=(W,E))

label1=ttk.Label(mainframe,text='Item Number:',background='grey',font=myFont)
label1.grid(row=0,column=0,columnspan=2,sticky=(W,E,S),padx=5)

#Quantity entry text field and label
quantity_entry=ttk.Entry(mainframe,width=15,text=quantityV,font=myFont)
quantity_entry.grid(row=1,column=2,columnspan=1,sticky=(W,E))

label2=ttk.Label(mainframe,text='Quantity:',background='grey',font=myFont)
label2.grid(row=1,column=0,columnspan=2,sticky=(W,E,S),padx=5)

#Item name entry text field and label
item_name_entry=ttk.Entry(mainframe,width=15,text=item_nameV,font=myFont)
item_name_entry.grid(row=2,column=2,columnspan=2,sticky=(W,E))

label3=ttk.Label(mainframe,text='Item Name:',background='grey',font=myFont)
label3.grid(row=2,column=0,columnspan=2,sticky=(W,E,S),padx=5)

#Item location entry text field and label
item_location_entry=ttk.Entry(mainframe,width=15,text=item_locationV,font=myFont)
item_location_entry.grid(row=3,column=2,columnspan=2,sticky=(W,E))

label4=ttk.Label(mainframe,text='Item Location:',background='grey',font=myFont)
label4.grid(row=3,column=0,columnspan=2,sticky=(W,E,S),padx=5)

#Item description entry text field and label
item_description_entry=ttk.Entry(mainframe,width=30,text=item_infoV,font=myFont)
item_description_entry.grid(row=4,column=2,columnspan=2,sticky=(W,E))

label5=ttk.Label(mainframe,text='Item Description:',background='grey',font=myFont)
label5.grid(row=4,column=0,columnspan=2,sticky=(W,E,S),padx=5)

#New button that will transfer data from ALL entry fields and add item to inventory
newbutton = ttk.Button(mainframe,text="New",command=addnewitem)
newbutton.grid(row=5,column=0,columnspan=1,sticky=(W,E,S),pady=15)

#Search button that will take the value in the Item Number text field and find the other componenents of that item
searchbutton = ttk.Button(mainframe,text="Search",command=searchforitem)
searchbutton.grid(row=5,column=1,columnspan=1,sticky=(W,E,S),pady=15)

#Deletes the item based on the data in the Item Number field 
deletebutton = ttk.Button(mainframe,text="Delete",command=deletefromlist)
deletebutton.grid(row=5,column=3,columnspan=1,sticky=(W,E,S),pady=15)

#Update button that will update the components of an item based on the Item Number Text Field
updatebutton = ttk.Button(mainframe,text="Update",command=updatecurrentitem)
updatebutton.grid(row=5,column=2,columnspan=1,sticky=(W,E,S),pady=15)

#Clear button that will clear the contents of the entries
clearbutton = ttk.Button(mainframe,text="Clear Entries",command=clearentries)
clearbutton.grid(row=0,column=3,rowspan=2,columnspan=2)


#Save Data button that write the current inventory items into a text file, use GUI selection for this 
savedatabutton = ttk.Button(mainframe,text="Save Data",command=savedatatofile)
savedatabutton.grid(row=6,column=0,columnspan=1,sticky=(W,E,S))

#Load Data button that will take contents from a text file and put it in the list of items
loadbutton = ttk.Button(mainframe,text="Load Data",command=loadfromfile)
loadbutton.grid(row=6,column=1,columnspan=1,sticky=(W,E,S))

#Exit button that will exit the program when the button is pressed
exitbutton = ttk.Button(mainframe,text="Exit",command=exit)
exitbutton.grid(row=6,column=3,columnspan=1,sticky=(W,E,S))


# Start up GUI
root.mainloop()
