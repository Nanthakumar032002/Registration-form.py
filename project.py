from tkinter import *
root = Tk()
root.geometry('600x400')

def getvals():
    print('Successfull')


#heading
Label(root, text='Python Registration Form',font ='ar 20 bold').grid(row = 0,column =3)

#field name
Name = Label(root,text='Name')
Phone = Label(root,text='Phone')
Gender= Label(root,text='Gender')
Emergency= Label(root,text='Emergency')
Paymentmood = Label(root,text='Paymentmood')

# show the label using the grid fuction
Name.grid(row = 1, column =2)
Phone.grid(row =2 , column =2)
Gender.grid(row =3 , column =2)
Emergency.grid(row = 4, column =2)
Paymentmood.grid(row =5 , column =2)

#create some variable

Namevalue =StringVar
Phonevalue =IntVar
Gendervalue =StringVar
Emergencyvalue =StringVar
Paymentmoodvalue =StringVar
checkvalue =IntVar

# create entry field

nameentry = Entry(root, textvariable=Namevalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Emergencyentry = Entry(root, textvariable=Emergencyvalue)
Paymentmoodentry = Entry(root, textvariable=Paymentmoodvalue)

#packing entry fields
nameentry.grid(row=1, column=3)
Phoneentry.grid(row=2, column=3)
Genderentry.grid(row=3, column=3)
Emergencyentry.grid(row=4, column=3)
Paymentmoodentry.grid(row=5, column=3)


#creating checkbox
checkbtn = Checkbutton (text ='remember me ?', variable= checkvalue)
checkbtn.grid(row=6, column= 3)


#sumbit button
Button(text='sumbit',command = getvals).grid(row =7, column=3)

root.mainloop() 
