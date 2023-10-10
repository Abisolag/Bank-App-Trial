import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = 'root', password = 'Aderinoye234$', database = 'MOBILE_BANK')
import random
import sys
cursor = myconn.cursor()
class bank:
    def __init__(self):
        print("WELCOME TO STANDARD BANK")
        self.start()

    def start(self):#Function for landing page
        self.decision = input("""ENTER WHAT OPERATION DO YOU WANT TO PERFORM\n
                               1. CREATE ACCOUNT\n2. LOG IN\n3. DEPOSIT\n4. HOMEPAGE\n5. EXIT: """)
        if self.decision == "1":
            self.create()
        elif self.decision == "2":
            self.login()
        elif self.decision == "3":
            self.deposit()
        elif self.decision == "4":
            self.home()
        elif self.decision == "5":
            sys.exit()
        else:
            print("INVALID OPERATION")
            self.start()
    
    def create(self):#function for customers to create an account
        self.info = ["fname", "lname", "Age", "Gender", "Address", "pwd", "Phonenumber","Email"]
        self.customer = []#Empty list
        for i in self.info:#interation for details asked from users
            information = input(f"Enter your {i}: ")
            while i == "Phonenumber" and len (information) != 11:
                print("NUMBER MUST BE 11 DIGIT")
            
            self.customer.append(information)
        self.Account=self.customer[6][1:]
        self.customer.append(self.Account)
        self.BVN = random. randrange(200036574, 3256782901)
        self.customer.append(self.BVN)
        self.Balance = 0
        self.customer.append(self.Balance)
        print(self.customer)#appended all information into an empty list
        self.sel()
    
    def sel(self):#function to insert details into each bank table on the database
        self.bnk = print("\nFirstbank\nAccessbank\nBankphb: ")
        self.decide = input("Enter Preferred Bank: ").title()
        if self.decide == "Firstbank":
            self.querry = "INSERT INTO Firstbank(fname, lname, Age, Gender, Address, pwd,  phonenumber, Email, Account, BVN, Balance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
            self.committing()
        elif self.decide == "Accessbank":
            self.querry = "INSERT INTO Accessbank(fname, lname, Age, Gender, Address, pwd,  phonenumber, Email, Account, BVN, Balance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
            self.committing()
        elif self.decide == "Bankphb":
            self.querry = "INSERT INTO Bankphb(fname, lname, Age, Gender, Address, pwd,  phonenumber, Email, Account, BVN, Balance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
            self.committing()
        else:
            print("BANK NOT AVALABILE")
            self.sel()

    def committing(self):#function to fetch details of users from database
        self.val = tuple(self.customer)
        cursor.execute(self.querry, self.val)
        myconn.commit()
        print("REGISTRATION SUCCESSFUL")
        self.start()

    def login(self):#login function
        self.email = input("Enter your Email: ").strip()
        self.password = input("Enter your password: ").strip()
        self.banking = input("Enter your bank: ").title()
        if self.banking == "Firstbank":
            self.query = "SELECT * FROM Firstbank WHERE Email = %s"
            self.confirm()
        elif self.banking == "Accessbank":                                      #To select correct email from database
            self.query = "SELECT * FROM Accessbank WHERE Email = %s"
            self.confirm()
        elif self.banking =="Bankphb":
            self.query = "SELECT * FROM Bankphb WHERE Email = %s"
            self.confirm()
        else:
            print("BANK NOT AVALABILE")
            self.login()

    def confirm (self):
        self.val = (self.email,)
        cursor.execute(self.query, self.val)#To confirm entry is in alignment with details in the database
        self.giver = cursor.fetchone()
        if self.email == self.giver[8] and self.password == self.giver[6]:
           print("LOGIN SUCCESSFUL")
           self.home()
        else:
            print("LOGIN FAILED")
            self.login()

    def home(self):#function for homepage
        print("CHOOSE THE TRANSCATION YOU LIKE TO PERFORM\n1. To Deposit\n2. Transfer Money\n3. Buy Airtime\n4. Buy Data\n5. Pay Utility\n6. ENTER ANY KEY TO ExiT")
        self.op = input(">>>: ")
        if self.op == "1":
            self.deposit()
        elif self.op == "2":
            self.Transfer_Money()
        elif self.op == "3":
            self.buy_airtime()
        elif self.op == "4":
            self.buydata()
        elif self.op == "5":
            self.utility()
        else:
             sys.exit()
    
    def deposit (self):#function for deposit
        print("WELCOME")
        self.receiver = input("Enter account number: ")
        self.choice = input("Enter Prefer Bank;\n ENTER 1 for Firstbank\n ENTER 2 FOR Accessbank\n ENTER 3 FOR Bankphb :")
        if self.choice == "1":
            self.acc = "SELECT * FROM Firstbank WHERE Account = %s"
            self.quer = "UPDATE Firstbank SET Balance =%s WHERE Account = %s "
            self.confirmation()                                                     #self.acc= to locate the users account in the database
        elif self.choice == "2":                                                    #self.quer= to set cuurrent balance of user
            self.acc = "Select * FROM Accessbank WHERE Account = %s"
            self.quer = "UPDATE Accessbank SET Balance =%s WHERE Account = %s"
            self.confirmation()
        elif self.choice == "3":
            self.acc = "Select * FROM Bankphb WHERE Account = %s"
            self.quer = "UPDATE Bankphb SET Balance =%s WHERE Account = %s"
        else:
            print("OPTION NOT FOUND")
            self.deposit()

    def confirmation(self):
        self.val = (self.receiver,)
        cursor.execute(self.acc, self.val)
        self.result = cursor.fetchone()
        if self.result:
            print(f"You are making a deposit of {self.amount} to {self.result[1]} {self.result[2]}")
            self.amount = int(input("Enter the amount to deposit: "))
            self.new_amount = self.result[-1] + self.amount
            self.val = (self.new_amount, self.receiver)
            cursor.execute(self.quer, self.val)             #Setting new balance to users account
            myconn.commit()
            print(f"{self.amount} sent successfully to {self.result[1]} {self.result[2]}")
            self.start()
        else:
            print("NO RECORD MATCH YOUR ACCOUNT DETAILS")
            self.deposit()
    
    def Transfer_Money(self):#function to make transfer
        self.ch = input("Choose the bank you want to send money to;\n ENTER 1 for Firstbank\n ENTER 2 FOR Accessbank\n ENTER 3 FOR Bankphb: ")
        if self.ch == "1":
                self.out = input("Enter account of receiver: ")
                if self.out == self.giver[9]:
                    print("MONEY CANNOT BE SENT TO YOUR ACCOUNT")
                    self.Transfer_Money()
                else:
                    self.query = "SELECT * FROM Firstbank where account = %s"
                    self.querry2 = "UPDATE Firstbank SET Balance = %s WHERE account = %s"
                    self.money()
        elif self.ch == "2":
            self.out = input("Enter account of receiver: ")
            if self.out == self.giver[9]:
                    print("MONEY CANNOT BE SENT TO YOUR ACCOUNT")
                    self.Transfer_Money()
            else:
                self.query = "SELECT * FROM Accessbank where account = %s"
                self.querry2 = "UPDATE Accessbank SET Balance = %s WHERE account = %s"
                self.money()
        elif self.ch == "3":
            self.out = input("Enter account of receiver: ")
            if self.out == self.giver[9]:
                    print("MONEY CANNOT BE SENT TO YOUR ACCOUNT")
                    self.Transfer_Money()
            else:
                self.query = "SELECT * FROM Bankphb where account = %s"
                self.querry2 = "UPDATE Bankphb SET Balance = %s WHERE account = %s"
                self.money()
        else:
            print("OPTION NOT AVALABILE")
            self.start()
    def money (self):
        self.val = (self.out,)
        cursor.execute(self.query, self.val)
        self.result = cursor.fetchone()
        if self.result:
            self.amount = int(input("Enter the amount to send: "))
            if self.amount > self.giver[-1]:
                print("INSUCCFIENT AMOUNT")
                self.money()
            else:
                self.new_amount = self.result[-1] + self.amount
                self.balance = self.giver[-1] - self.amount
                self.val = (self.new_amount, self.out)
                cursor.execute(self.querry2, self.val)
                myconn.commit()
                print(f"{self.amount} sent successfully to {self.result[1]} {self.result[2]}")
                self.deduct()
        else:
            print("NO RECORD MATCH YOUR ACCOUNT DETAILS")
            self.Transfer_Money()

    def deduct(self):#function to deduct money from users balance
        if self.banking == 'Firstbank':
            self.querry =  "UPDATE Firstbank SET Balance = %s WHERE Email = %s "#to update balance
            self.val = (self.balance,self.email)
            cursor.execute(self.querry,self.val)
            myconn.commit()
        elif self.banking == 'Accessbank':
            self.querry =  "UPDATE Accessbank SET Balance = %s WHERE Email = %s "
            self.val = (self.balance,self.email)
            cursor.execute(self.querry,self.val)
            myconn.commit()
        elif self.banking == 'Bankphb':
            self.querry =  "UPDATE Bankphb SET Balance = %s WHERE Email = %s "
            self.val = (self.balance,self.email)
            cursor.execute(self.querry,self.val)
            myconn.commit()
        print(f"{self.amount} has been deducted from your account.")
        self.home()

    def buy_airtime(self):#function to buy airtime
        self.val = (self.email,)
        cursor.execute(self.query, self.val)
        self.giver = cursor.fetchone()
        self.network = ['Mtn','Glo','Airtel', '9mobile']
        self.phonenumber = input('Enter Phonenumber: ')
        while len(self.phonenumber) != 11:
            print('Phone number is not 11')
            self.phonenumber = input('Enter Phonenumber: ')
        else:
            self.net = input("""Enter the network you want to buy: """)
            while self.net not in self.network:
                print('NETWORK NOT FOUND')
                net = input("""Enter the network you want to buy: """)
            else:
                self.airtime_money()

    def airtime_money(self):#function to buy airtime 
        self.val = (self.email,)
        cursor.execute(self.query, self.val)
        self.giver = cursor.fetchone()
        self.air = int(input("Enter the amount you want to buy: "))
        if self.giver[-1] < self.air:
            print("INSUCCIFIENT BALANCE")
            self.airtime_money()
        else:
            self.balance = self.giver[-1] - self.air #deducting balance from inputted amount
            if self.banking == "Firstbank":
                self.uquery = "UPDATE Firstbank SET Balance = %s where Account = %s"
                self.val2 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val2)
                myconn.commit()
                print(f"You have successfully purchase {self.air} worth of airtime")
                self.home()
            elif self.banking == "Accessbank":
                self.uquery = "UPDATE Accessbank SET Balance =%s where Account = %s"
                self.val2 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val2)
                myconn.commit()
                print(f"You have successfully purchase {self.air} worth of airtime")
                self.home()
            elif self.banking == "Bankphb":
                self.uquery = "UPDATE Bankphb SET Balance =%s where Account = %s"
                self.val2 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val2)
                myconn.commit()
                print(f"You have successfully purchase {self.air} worth of airtime")
                self.home()
            else:
                print("NO RECORD FOUND")
    def data(self):#function to buy data
        self.val = (self.email,)
        cursor.execute(self.query, self.val)
        self.giver = cursor.fetchone()
        self.network = ['Mtn','Glo','Airtel', '9mobile']
        self.phonenumber = input('Enter Phonenumber: ')
        while len(self.phonenumber) != 11:
            print('Phone number is not 11')
            self.phonenumber = input('Enter Phonenumber: ')
        else:
            self.net = input("""Enter the network you want to buy: """)
            while self.net not in self.network:
                print('NETWORK NOT FOUND')
                net = input("""Enter the network you want to buy: """)
            else:
                self.buydata()
    def buydata(self):
        self.options = input ("Select 1 to buy data: ").strip()
        if self.options == "1":
            print("""
                    1. N100 for 100MB
                    2. N150 for 150MB
                    3. N200 for 250MB""")
            opt1 = input ("Select Option: ").strip()
            if opt1 == "1":
                print("Your subscription for 100MB is Successful ")
                self.air = 100
                self.condata()
            elif opt1 == "2":
                print("Your subscription for 150MB is Successful ")
                self.air = 150
                self.condata()
            elif opt1 == "3":
                self.air = 200
                self.condata()
                print("Your subscription for 250MB is successful")
            else:
                print("INVALID OPERATION")
                self.buydata()
    def condata(self):
        self.val = (self.email,)
        cursor.execute(self.query, self.val)
        self.giver = cursor.fetchone()
        self.balance = self.giver[-1] - self.air
        if self.banking == "Firstbank":
                self.uquery = "UPDATE Firstbank SET Balance = %s where Account = %s"
                self.val3 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val3)
                myconn.commit()
                print(f"You have successfully purchase {self.air} worth of airtime")
                self.home()
        elif self.banking == "Accessbank":
                self.uquery = "UPDATE Accessbank SET Balance =%s where Account = %s"
                self.val3 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val3)
                myconn.commit()
                print(f"You have successfully purchase {self.air} worth of airtime")
                self.home()
        elif self.banking == "Bankphb":
                self.uquery = "UPDATE Bankphb SET Balance =%s where Account = %s"
                self.val3 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val3)
                myconn.commit()
                print(f"You have successfully purchase {self.air} worth of data")
                self.home()
        else:
            print("NO DATA PLAN FOUND")
            self.data()
    
    def utility(self):#function to pay for utility bills
        self.val = (self.email,)
        cursor.execute(self.query, self.val)
        self.giver = cursor.fetchone()
        self.choice = input("Enter 1 TO PAY FOR TV SUBSCRIPTION\n ENTER 2 TO PAY FOR WATER BILL")
        if self.choice == "1":
            print("Enter: 1. DSTV\n2. STARTIMES\n3. GOTV")
            self.tv = input(">>>>: ")
            if self.tv == "1":
                print("YOUR DSTV SUBSCRIPTION IS SUCCESSFUL")
                self.pay = 10000
            elif self.choice == "2":
                print("PAYMENT FOR WATER BILL IS SUCCESSFUL")
                self.pay = 10000
            else:
                self.home()
    def uticon(self):
        self.val = (self.email,)
        cursor.execute(self.query, self.val)
        self.giver = cursor.fetchone()
        self.balance = self.giver[-1] - self.pay
        if self.banking == "Firstbank":
                self.uquery = "UPDATE Firstbank SET Balance = %s where Account = %s"
                self.val3 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val3)
                myconn.commit()
                self.home()
        elif self.banking == "Accessbank":
                self.uquery = "UPDATE Accessbank SET Balance =%s where Account = %s"
                self.val3 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val3)
                myconn.commit()
                self.home()
        elif self.banking == "Bankphb":
                self.uquery = "UPDATE Bankphb SET Balance =%s where Account = %s"
                self.val3 = (self.balance, self.giver[9])
                cursor.execute(self.uquery, self.val3)
                myconn.commit()
                self.home()
        else:
            print("NO UTILITY PLAN FOUND")
            self.home()      
bank()