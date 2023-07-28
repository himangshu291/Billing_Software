# ---------------------------CREATED BY Himangshu Chandra Das---------------------------------
from tkinter import *               #tkinter is used to make a powerful GUI application
from tkinter import ttk             #It'll used to make a stylish entry field 
from PIL import Image,ImageTk,ImageFilter       #pip install pillowpip install pillow
import random,os
from tkinter import messagebox
import tempfile                     #importing tempfile for printing 
from time import strftime
import mysql.connector as Myconn              # mysql.connector is a driver where mysql is a package and connector is a class


class Bill_App:
    def __init__(self,root):                                #constructor of Bill_App class
        self.root=root                                      #Initialize root
        self.root.geometry("1530x800+0+0")                                #geometry is used for width(1530) and height(800) x & y axis(0,0)
        self.root.title("Billing Software")                          # Name of the window is root
        self.conn=self.connect()        # connect method called during object initialization
        
        #====================================================Variables============================================================

        self.c_name=StringVar()
        self.c_ph=StringVar()
        self.bill_no=StringVar()
        bill=random.randint(1000,9999)
        self.bill_no.set(bill)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        #=================================================Product Categories List===========================================================
        
        self.category=["Select Option","Staples","Snacks","Fruits & Vegetables","Beverages"]
        
        self.SubCatstaples=["Dals","Rice","Atta,Flours & Sooji","Edible Oils","Masalas"]
        self.Dals=["Moong Dal 1kg","Chana Dal 1kg","Masoor Dal 1kg","Matar Dal 1kg"]
        self.price_moong=130
        self.price_chana=77
        self.price_masoor=120
        self.price_matar=180
        
        self.Rice=["Fortune Basmati Rice 1kg","Fortune Biriyani Basmati Rice 1kg","Fortune Ratna Rice 1kg"]
        self.price_basmati=80
        self.price_biriyani=130
        self.price_ratna=50
        
        self.Atta=["Aashirvaad Wheat Atta 1 kg","Maida 1 kg","Besan 1kg"]
        self.price_wheat=50
        self.price_maida=42
        self.price_besan=76
        
        self.oils=["Fortune Mustard Oil 1L","Fortune Refined Sunflower Oil 1L"]
        self.price_mustard=150
        self.price_refined=125
        
        self.masalas=["Sunrise Turmeric Powder 100 g","Sunrise Meat Masala 50g","Sunrise Chilli Powder 100g","Sunrise Jeera Powder"]
        self.price_turmeric=22
        self.price_meat=42
        self.price_chilli=50
        self.price_jeera=50
        
        self.SubCatSnacks=["Biscuits & Cookies","Noodle & Pasta","Snacks & Namkeen","Chocolates & Candies"]
        
        self.biscuits=["Marie 100g","Good Day 100g","Nutri Choice 50g","Oreo 50g"]
        self.price_marie=10
        self.price_good=10
        self.price_nutri=10
        self.price_oreo=10
        
        self.noodle=["Maggie 70g","Yippee Noodles 60g","Pasta 60g"]
        self.price_maggie=10
        self.price_yippe=10
        self.price_pasta=10
        
        self.snacks=["Kurkure","Lays","Uncle chips","Bingo","Bhujia"]
        self.price_kurkure=10
        self.price_lays=10
        self.price_uncle=10
        self.price_bingo=10
        self.price_bhujia=10
        
        self.choco=["kitkat","Dairy Milk","Munch","5 Star"]
        self.price_kitkat=10
        self.price_dairy=10
        self.price_munch=10
        self.price_star=10
        
        
        self.SubCatFruit=["Fresh Fruits","Fresh Vegetables"]
        
        self.FreshFruit=["Apple 500g","Mango 1kg","Orange 1kg","Mosambi 1kg"]
        self.price_apple=90
        self.price_mango=50
        self.price_orange=130
        self.price_mosabmi=60
        
        self.FreshVeg=["Onion 1kg","Potato 1kg","Chilli 100g","Ginger 200g"]
        self.price_onion=20
        self.price_potato=25
        self.price_chilli=30
        self.price_ginger=50
        
        self.SubCatBeverages=["Tea & Coffe","Cold Drinks","Health Drinks"]
        
        self.tea=["Tata Tea 100g","Red Label Tea 50g","Nescafe Instant Coffee 50 g"]
        self.price_tata=90
        self.price_red=50
        self.price_nescafe=140
        
        self.coldDrinks=["Sprite 600ml","Fanta 600ml","Slice 600ml","Pepsi 600ml"]
        self.price_sprite=38
        self.price_fanta=38
        self.price_slice=38
        self.price_pepsi=38
        
        self.healthDrinks=["Horlicks 750g","Bournvita 750g"]
        self.price_horlicks=330
        self.price_bournvita=296
        
        
        #=================================================Image===========================================================#
        #Image_1
        img=Image.open("Images/fruit.jpg")                           #Open the image
        img=img.resize((510,130), Image.LANCZOS)                  #Resize the image. ANTIALIAS is used to convert higher level image to lower level image. use LANCZOS instead of ANTIALIAS
        self.photoimg=ImageTk.PhotoImage(img)                       #ImageTk is used to convert photo to image
        
        #Show the fruit image on the window using label
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=520,height=130)
        
        #Image_2
        img_2=Image.open("Images/grocery.jpg")                           
        img_2=img_2.resize((510,130), Image.LANCZOS)                  
        self.photoimg_2=ImageTk.PhotoImage(img_2)                      
        
        #Show the grocery image on the window using label
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=510,y=0,width=510,height=130)
        
        #Image_3
        img_3=Image.open("Images/vege.jpg")                           
        img_3=img_3.resize((510,130), Image.LANCZOS)                  
        self.photoimg_3=ImageTk.PhotoImage(img_3)                      
        
        #Show the shopping image on the window using label
        lbl_img_3=Label(self.root,image=self.photoimg_3)
        lbl_img_3.place(x=1020,y=0,width=510,height=130)
        
         #=================================================TITLE===========================================================#
        #lbl is used for giving the label
        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")       #inside the window so self.root
        lbl_title.place(x=0,y=130,width=1530,height=45)             #show the label on the window
        
        
        #================================================= TIME ===========================================================#
        def time():
            string=strftime("%H:%M:%S %p")          #strftime is a format which consists Hour,Minute,Second and p=pm or am
            lbl.config(text=f"Time:{string}")                 
            lbl.after(1000, time)                   #1000=1s, count the time after every 1s(1s,2s,3s...)
        
        lbl= Label(lbl_title, font=("times new roman",16,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=180,height=45)
        time()
        
        #================================================= Main Frame===========================================================#
        #frame is used as a container
        Main_Frame = Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        
        #=================================================Customer Label Frame with entry field===========================================================#
        
        #In a LabelFrame we can add text but in Frame, we can't add
        #Add the frame inside the Main_Frame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",14,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)             #y=5 because this is in Main_frame 
        
        #stick parameter tells which side of the "cell" the widget will "stick" to. widget is centered in its cell
        # Mobile_no.
        self.lbl_mbl=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mbl.grid(row=0,column=0,sticky=W,padx=5,pady=2)              #we need to add row & column so grid
                                 
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_ph,font=("times new roman",10,"bold"),width=24)    # Many stylish field are there inside ttk 
        self.entry_mob.grid(row=0,column=1)
        
        # Customer_name
        self.lbl_Name=Label(Cust_Frame,text="Customer Name",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Name.grid(row=1,column=0,sticky=W,padx=5,pady=2)              
                                 
        self.entry_name=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",10,"bold"),width=24)    
        self.entry_name.grid(row=1,column=1,sticky=W,padx=5,pady=2)       
        
        # Email
        self.lbl_Email=Label(Cust_Frame,text="Email",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Email.grid(row=2,column=0,sticky=W,padx=5,pady=2)              
                                 
        self.entry_Email=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",10,"bold"),width=24)    
        self.entry_Email.grid(row=2,column=1,sticky=W,padx=5,pady=2)  
        
        
        #=================================================Product Label Frame with combobox===========================================================#
        #textvariable is used to set the variable
        
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",14,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=600,height=140)
        
        #=================Category==============
        self.lbl_category=Label(Product_Frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_category.grid(row=0,column=0,sticky=W,padx=5,pady=2)               #This is new frame so row column will start from beginning
        
        # Create combobox
        self.combo_category=ttk.Combobox(Product_Frame,value=self.category,font=("times new roman",10,"bold"),width=28,state="readonly")  #All the value of category will cme
        self.combo_category.current(0)                  #current is used to show the index value on the combobox
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2) 
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)        #After selecting ComboBox it'll call the Categories function
        
        #================Sub Category=============
        self.lbl_SubCategory=Label(Product_Frame,text="Sub Category",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_SubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)               
        
        self.combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=("times new roman",10,"bold"),width=28,state="readonly")         
        #value=[""] because we don't know which value will come through the sub category into the product name. Whom I select that'll come, don't need to specify 
        self.combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2) 
        self.combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        
        #================Product Name===============
        self.lbl_Product_Name=Label(Product_Frame,text="Product Name",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Product_Name.grid(row=2,column=0,sticky=W,padx=5,pady=2)               
        
        self.combo_Product_Name=ttk.Combobox(Product_Frame,value=[""],textvariable=self.product,font=("times new roman",10,"bold"),width=28,state="readonly")    
        self.combo_Product_Name.grid(row=2,column=1,sticky=W,padx=5,pady=2) 
        self.combo_Product_Name.bind("<<ComboboxSelected>>",self.price)
        
        #===============Price=================
        self.lbl_Price=Label(Product_Frame,text="Price",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Price.grid(row=0,column=2,sticky=W,padx=5,pady=2)               
        
        self.combo_Price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",10,"bold"),width=20,state="readonly")    
        self.combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2) 
        
        #==============Qty==================
        self.lbl_Qty=Label(Product_Frame,text="Qty",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)               
        
        self.Entry_Qty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",10,"bold"),width=22)    
        self.Entry_Qty.grid(row=1,column=3,sticky=W,padx=5,pady=2) 
        
        
        #================================================= Middle Frame ======================================================================#
        
        middleFrame = Frame(Main_Frame,bd=10)
        middleFrame.place(x=10,y=150,width=970,height=340)
        
        #================================================= Images inside Middle Frame ======================================================================#
        
        #Image_1
        Img=Image.open("Images/shopping.jpg")                           
        Img=Img.resize((480,315),Image.LANCZOS)                  
        self.photoImg=ImageTk.PhotoImage(Img)                      
        
        #Show the grocery image on the window using label
        lbl_Img=Label(middleFrame,image=self.photoImg)
        lbl_Img.place(x=0,y=0,width=480,height=315)
        
        #Image_2
        Img_1=Image.open("Images/supermarket.jpg")                           
        Img_1=Img_1.resize((470,315), Image.LANCZOS)                  
        self.photoImg_1=ImageTk.PhotoImage(Img_1)                      
        
        #Show the shopping image on the window using label
        lbl_Img_1=Label(middleFrame,image=self.photoImg_1)
        lbl_Img_1.place(x=480,y=0,width=470,height=315)
        
        
        #================================================= Search Frame======================================================================#
        
        search_Frame=Frame(Main_Frame,bd=2,bg="#e0e0e0")               #All the Buttons border is 2
        search_Frame.place(x=990,y=5,width=510,height=40)
        
        #===============Bill Number=============
        
        self.lblBill=Label(search_Frame,text="Bill Number",font=("times new roman",12,"bold"),bg="yellow",fg="red",bd=4)
        self.lblBill.grid(row=0,column=0,sticky=W,padx=2,pady=2)               
        
        #==========Bill number Entry field=======
        
        self.Entry_bill=ttk.Entry(search_Frame,textvariable=self.search_bill,font=("times new roman",10,"bold"),width=26)    
        self.Entry_bill.grid(row=0,column=1,sticky=W,padx=5,pady=2) 
        
        #===============Search button=======
        self.search_btn=Button(search_Frame,command=self.find_bill,text="Search",font=("times new roman",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.search_btn.grid(row=0,column=2)  
        
        #=================================================  Frame Bill Area= ================================================================#
        
        RightFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",14,"bold"),bg="white",fg="red")
        RightFrame.place(x=990,y=45,width=510,height=510)
        
        #=================================================Scroll bar===========================================================#
        
        scroll_y=Scrollbar(RightFrame,orient=VERTICAL)
        self.textarea=Text(RightFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))      #Text field inside right frame
        scroll_y.pack(side=RIGHT,fill=Y)                        #fill the scrollbar in Y-axis and right side
        scroll_y.config(command=self.textarea.yview)            # Config() function, used to simply change the text on a label.
        self.textarea.pack(fill=BOTH,expand=1)                  #The textarea will be filled in the both side and expand fully.
        
        #================================================= Bill Counter Label Frame ==========================================================#
        
        #================================================== Entry Field ========================================================
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",14,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)
    
        #Sub Total
        self.lbl_Sub_Total=Label(Bottom_Frame,text="Sub Total",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Sub_Total.grid(row=0,column=0,sticky=W,padx=5,pady=2)               
        
        self.Entry_Sub_Total=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",10,"bold"),width=26)    
        self.Entry_Sub_Total.grid(row=0,column=1,sticky=W,padx=5,pady=2) 
        
        # Gov. Tax
        self.lbl_tax=Label(Bottom_Frame,text="Gov Tax",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)               
        
        self.Entry_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",10,"bold"),width=26)    
        self.Entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2) 
        
        # Total
        self.lbl_Total=Label(Bottom_Frame,text="Total",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Total.grid(row=2,column=0,sticky=W,padx=5,pady=2)               
        
        self.Entry_Sub_Total=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("times new roman",10,"bold"),width=26)    
        self.Entry_Sub_Total.grid(row=2,column=1,sticky=W,padx=5,pady=2) 
        
        #=================================================Button Frame===========================================================#
        #Frame is like a container
        #command is used to call the function through the button

        btn_Frame=Frame(Bottom_Frame,bd=2,bg="#e0e0e0")               #All the Buttons border is 2
        btn_Frame.place(x=320,y=15)
        
        #================Add to Cart===================
        self.BtnAddToCart=Button(btn_Frame,command=self.AddItems,height=2,text="Add to Cart",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)        
        
        #=================Generate Bill===================
        self.Btngenerate=Button(btn_Frame,command=self.generate_bill,height=2,text="Generate Bill",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate.grid(row=0,column=1)        
        
        #=================Save Bill===================
        self.BtnSave=Button(btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)        
        
        #=================Print===================
        self.BtnPrint=Button(btn_Frame,command=self.print,height=2,text="Print",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)        
        
        #=================Clear===================
        self.BtnClear=Button(btn_Frame,height=2,command=self.clear,text="Clear",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)        

        #=================Exit===================
        self.BtnExit=Button(btn_Frame,command=self.root.destroy,height=2,text="Exit",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)    
        self.welcome()
        
    #=================================================DB connection===========================================================#
    
    def connect(self):
        try:
            # Replace the placeholders with your actual MySQL database credentials
            self.conn = Myconn.connect(
                host="localhost",
                user="root",
                password="Himangshu@12345",
                database="Billing_db"
            )
            if self.conn.is_connected():
                print("Connected to MySQL database!")
                return self.conn
        except Exception as e:
            print("Error connecting to MySQL:", e)
            return None
        
        
        self.l=[]
    # #=================================================Create Welcome Page in Bill Area===========================================================#
     
    def welcome(self):
       self.textarea.delete(1.0,END)                #delete(1.0,END) is used to delete all the contents inside the field.
       self.textarea.insert(END,"\t\tWelcome to DAS Super Market")
       self.textarea.insert(END,f"\n Bill Number:\t{self.bill_no.get()}")
       self.textarea.insert(END,f"\n Customer Name:\t{self.c_name.get()}")
       self.textarea.insert(END,f"\n Mobile Number:\t{self.c_ph.get()}")
       self.textarea.insert(END,f"\n Customer Email:\t{self.c_email.get()}")
        
        
       self.textarea.insert(END,"\n=====================================================")
       self.textarea.insert(END,"\n Products\t\t\t\tQty\t\tPrice")    
       self.textarea.insert(END,"\n=====================================================\n")
       
        
    #=================================================Add the items===========================================================#
    
    def AddItems(self):
        print("Adding the items...")
        Tax=1
        self.n=self.qty.get()*self.prices.get()                 #Total price for a particular product
        self.l.append(self.n)                                   #List of all the products price                   
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the Product Name!")     #For showing error message import messagebox
        else:
            myconn_cursor=self.conn.cursor()
            insert_query=("insert into Bills values(%s,%s,%s,%s)")              #In place of %s we will insert actual value
            insert_value=(1000,"9749470744","Himangshu",500)
            myconn_cursor.execute(insert_query,(self.bill_no.get(),self.c_ph.get(),self.c_name.get(),self.total.get()))  
            self.conn.commit()                                           #commit() is used to save the record inside the database. Without commit it cannot be saved or inserted.

            print(myconn_cursor.rowcount,"Record inserted Successfully!")

            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t\t {self.qty.get()}\t\t{self.n}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
        
    #=================================================Generate Bill===========================================================#
    
    def generate_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add Product to the Cart for generating bill!") 
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))          #self.l=List of all the products price 
            self.textarea.delete(1.0,END)
            self.welcome()     
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=====================================================")
            
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")                
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n=====================================================")
    
     #=================================================Save Bill===========================================================#
    
    def save_bill(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                # Save data to the database using SQL queries
                query = "INSERT INTO bills (bill_number,customer_ph,customer_name, total_amount) VALUES (%s, %s, %s, %s)"
                data = (self.bill_no.get(),self.c_ph.get(), self.c_name.get(), self.total.get())
                cursor.execute(query, data)
                self.conn.commit()
                cursor.close()
                print("Bill data saved to MySQL database!")
            except Exception as e:
                print("Error saving bill to MySQL:", e)
        else:
            print("MySQL connection is not established.")
            
    # def save_bill(self):
    #     op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
    #     if op>0:
    #         self.bill_data = self.textarea.get(1.0,END)
    #         f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
    #         f1.write(self.bill_data)
    #         op=messagebox.showinfo("Saved,",f"Bill No: {self.bill_no.get()} saved successfully.")
    #         f1.close()
           
    # =================================================Print===========================================================#
    
    def print(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')            #tempfile is imported. mktemp is needed for the format
        open(filename,'w').write(q)                 #Open the file in write mode
        os.startfile(filename,"print")                      #startfile method is used to pass the files
         
    #=================================================Search===========================================================#
    
    def find_bill(self):
        found="no"
        for i in os.listdir("Bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.textarea.delete(1.0,END)
                for j in f1:
                    self.textarea.insert(END,j)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error! Invalid Bill Number")
            
    #=================================================Clear===========================================================
        
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_ph.set("")
        bill=random.randint(1000,9999)
        self.bill_no.set(str(bill))
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]              #List of all product prices
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()
      

          
    def Categories(self,event=""):                      #Instead of event you can write anything. Just need to pass the arguments otherwise it'll show error.  
        
        #============================= By selecting category value, automatic show the sub categories of it ==============================================#
        
        if self.combo_category.get()=="Staples":             # To Add validation first get the category value
            self.combo_SubCategory.config(value=self.SubCatstaples)         # Add the sub category value of staples to the sub category combobox
            self.combo_SubCategory.current(0)                               # current will show the value of index 0 on the sub category combobox
        
        if self.combo_category.get()=="Snacks":             
            self.combo_SubCategory.config(value=self.SubCatSnacks)         
            self.combo_SubCategory.current(0)   

        if self.combo_category.get()=="Fruits & Vegetables":             
            self.combo_SubCategory.config(value=self.SubCatFruit)         
            self.combo_SubCategory.current(0)  
        
        if self.combo_category.get()=="Beverages":             
            self.combo_SubCategory.config(value=self.SubCatBeverages)         
            self.combo_SubCategory.current(0)  
    
    
    def Product_add(self,event=""):
    
     #====================================================Adding Product of Staples===============================================================
    
        if self.combo_SubCategory.get()=="Dals":
            self.combo_Product_Name.config(value=self.Dals)
            self.combo_Product_Name.current(0)
            
        if self.combo_SubCategory.get()=="Rice":
            self.combo_Product_Name.config(value=self.Rice)
            self.combo_Product_Name.current(0)
        
        if self.combo_SubCategory.get()=="Atta,Flours & Sooji":
            self.combo_Product_Name.config(value=self.Atta)
            self.combo_Product_Name.current(0)
            
        if self.combo_SubCategory.get()=="Edible Oils":
            self.combo_Product_Name.config(value=self.oils)
            self.combo_Product_Name.current(0)
            
        if self.combo_SubCategory.get()=="Masalas":
            self.combo_Product_Name.config(value=self.masalas)
            self.combo_Product_Name.current(0)
    
     #====================================================Adding Product of Snacks===============================================================
    
        if self.combo_SubCategory.get()=="Biscuits & Cookies":
            self.combo_Product_Name.config(value=self.biscuits)
            self.combo_Product_Name.current(0)
        
        if self.combo_SubCategory.get()=="Noodle & Pasta":
            self.combo_Product_Name.config(value=self.noodle)
            self.combo_Product_Name.current(0)
        
        if self.combo_SubCategory.get()=="Snacks & Namkeen":
            self.combo_Product_Name.config(value=self.snacks)
            self.combo_Product_Name.current(0)
            
        if self.combo_SubCategory.get()=="Chocolates & Candies":
            self.combo_Product_Name.config(value=self.choco)
            self.combo_Product_Name.current(0)
    
     #====================================================Adding Product of Fruits & Vegetables===============================================================
        
        if self.combo_SubCategory.get()=="Fresh Fruits":
            self.combo_Product_Name.config(value=self.FreshFruit)
            self.combo_Product_Name.current(0)
            
        if self.combo_SubCategory.get()=="Fresh Vegetables":
            self.combo_Product_Name.config(value=self.FreshVeg)
            self.combo_Product_Name.current(0)
            
        
     #====================================================Adding Product of Beverages===============================================================
   
        if self.combo_SubCategory.get()=="Tea & Coffe":
            self.combo_Product_Name.config(value=self.tea)
            self.combo_Product_Name.current(0)
        
        if self.combo_SubCategory.get()=="Cold Drinks":
            self.combo_Product_Name.config(value=self.coldDrinks)
            self.combo_Product_Name.current(0)
        
        if self.combo_SubCategory.get()=="Health Drinks":
            self.combo_Product_Name.config(value=self.healthDrinks)
            self.combo_Product_Name.current(0)
            
            
    def price(self,event=""):
        
        #====================================================set the product price===============================================================
        
        #=================Dals================
        if self.combo_Product_Name.get()=="Moong Dal 1kg":
            self.combo_Price.config(value=self.price_moong)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product_Name.get()=="Chana Dal 1kg":
            self.combo_Price.config(value=self.price_chana)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product_Name.get()=="Masoor Dal 1kg":
            self.combo_Price.config(value=self.price_masoor)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Matar Dal 1kg":
            self.combo_Price.config(value=self.price_matar)
            self.combo_Price.current(0)
            self.qty.set(1)
       
        #=================Rice================
        if self.combo_Product_Name.get()=="Fortune Basmati Rice 1kg":
            self.combo_Price.config(value=self.price_basmati)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product_Name.get()=="Fortune Biriyani Basmati Rice 1kg":
            self.combo_Price.config(value=self.price_biriyani)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Fortune Ratna Rice 1kg":
            self.combo_Price.config(value=self.price_ratna)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        #=================Atta,Flours & Sooji================
        if self.combo_Product_Name.get()=="Aashirvaad Wheat Atta 1 kg":
            self.combo_Price.config(value=self.price_wheat)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Maida 1 kg":
            self.combo_Price.config(value=self.price_maida)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Besan 1kg":
            self.combo_Price.config(value=self.price_besan)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        #=================Edible Oils================
        if self.combo_Product_Name.get()=="Fortune Mustard Oil 1L":
            self.combo_Price.config(value=self.price_mustard)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Fortune Refined Sunflower Oil 1L":
            self.combo_Price.config(value=self.price_refined)
            self.combo_Price.current(0)
            self.qty.set(1)
             
        #=================Masalas================
        if self.combo_Product_Name.get()=="Sunrise Turmeric Powder 100 g":
            self.combo_Price.config(value=self.price_turmeric)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Sunrise Meat Masala 50g":
            self.combo_Price.config(value=self.price_meat)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Sunrise Chilli Powder 100g":
            self.combo_Price.config(value=self.price_chilli)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Sunrise Jeera Powder":
            self.combo_Price.config(value=self.price_jeera)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        #=================Biscuits & Cookies================
        if self.combo_Product_Name.get()=="Marie 100g":
            self.combo_Price.config(value=self.price_marie)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Good Day 100g":
            self.combo_Price.config(value=self.price_good)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Nutri Choice 50g":
            self.combo_Price.config(value=self.price_nutri)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product_Name.get()=="Oreo 50g":
            self.combo_Price.config(value=self.price_oreo)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        #=================Noodle & Pasta================
        if self.combo_Product_Name.get()=="Maggie 70g":
            self.combo_Price.config(value=self.price_maggie)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Yippee Noodles 60g":
            self.combo_Price.config(value=self.price_yippe)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Pasta 60g":
            self.combo_Price.config(value=self.price_pasta)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        #=================Snacks & Namkeen================
        if self.combo_Product_Name.get()=="Kurkure":
            self.combo_Price.config(value=self.price_kurkure)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Lays":
            self.combo_Price.config(value=self.price_lays)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Uncle chips":
            self.combo_Price.config(value=self.price_uncle)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Bingo":
            self.combo_Price.config(value=self.price_bingo)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Bhujia":
            self.combo_Price.config(value=self.price_bhujia)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        #=================Chocolates & Candies================
        if self.combo_Product_Name.get()=="kitkat":
            self.combo_Price.config(value=self.price_kitkat)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Dairy Milk":
            self.combo_Price.config(value=self.price_dairy)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Munch":
            self.combo_Price.config(value=self.price_munch)
            self.combo_Price.current(0)
            self.qty.set(1)
        0
        if self.combo_Product_Name.get()=="5 Star":
            self.combo_Price.config(value=self.price_star)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        #=================Fresh Fruits================
        if self.combo_Product_Name.get()=="Apple 500g":
            self.combo_Price.config(value=self.price_apple)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Mango 1kg":
            self.combo_Price.config(value=self.price_mango)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product_Name.get()=="Orange 1kg":
            self.combo_Price.config(value=self.price_orange)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Mosambi 1kg":
            self.combo_Price.config(value=self.price_mosabmi)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        #=================Fresh Vegetables================
        if self.combo_Product_Name.get()=="Onion 1kg":
            self.combo_Price.config(value=self.price_onion)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Potato 1kg":
            self.combo_Price.config(value=self.price_potato)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Chilli 100g":
            self.combo_Price.config(value=self.price_chilli)
            self.combo_Price.current(0)
            self.qty.set(1)
    
        if self.combo_Product_Name.get()=="Ginger 200g":
            self.combo_Price.config(value=self.price_ginger)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        #=================Tea & Coffe===============
        if self.combo_Product_Name.get()=="Tata Tea 100g":
            self.combo_Price.config(value=self.price_tata)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Red Label Tea 50g":
            self.combo_Price.config(value=self.price_red)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product_Name.get()=="Nescafe Instant Coffee 50 g":
            self.combo_Price.config(value=self.price_nescafe)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        #=================Cold Drinks================
        if self.combo_Product_Name.get()=="Sprite 600ml":
            self.combo_Price.config(value=self.price_sprite)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Fanta 600ml":
            self.combo_Price.config(value=self.price_fanta)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Slice 600ml":
            self.combo_Price.config(value=self.price_slice)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Pepsi 600ml":
            self.combo_Price.config(value=self.price_pepsi)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        #=================Health Drinks================
        if self.combo_Product_Name.get()=="Horlicks 750g":
            self.combo_Price.config(value=self.price_horlicks)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        if self.combo_Product_Name.get()=="Bournvita 750g":
            self.combo_Price.config(value=self.price_bournvita)
            self.combo_Price.current(0)
            self.qty.set(1)
            
            
            
            
if __name__ == "__main__":
    root=Tk()
    obj=Bill_App(root)                          #Creating object of a class and pass the root
    root.mainloop()                             #until we don't closed the window the mainloop is executed