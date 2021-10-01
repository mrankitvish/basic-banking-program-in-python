class Account:
    
##function for changing account password
    def changePass(self):
        print("----------------------------------------")
        def oldPassword():
            password1=input("Enter your old password: ")
            return password1
        def newPassword():
            password2=input("New password: ")
            return password2
        
        while True:
            myoldPass=self.password
            oldPassword=oldPassword()
            newPassword=newPassword()
            if myoldPass==oldPassword:
                self.password=newPassword   
                print("**********Password has been changed!*********")
                break
            else:
                print("Password does not matched!-Check your password again!")
                print('')
                print("**************Thanks for using me!********************")
                print('')
                break

#Initializing object variables 
    def __init__(self,fname,lname):
        print("----------------------------------------")
        def accNumber():
            accNumber=int(input("Enter your account number: "))
            return accNumber
        def balance():
            balance=int(input("Enter your account balance: "))
            return balance
        def password1():
            password1=input("Enter your password: ")
            return password1
        def password2():
            password2=input("comfirm password: ")
            return password2

        password1=password1()
        password2=password2()
        while True:
            if password1==password2:
                self.fname=fname
                self.lname=lname
                self.balance=balance()
                self.accountNumber=accNumber()
                self.password=password2
                print('')
                print("*********Account Created Successfully!***********")
                print('')
                break
            else:
                print("Password does not matched!-Check your password again!")
                break

#function for withdraw amount 
    def withdraw(self):
        print("------------------Withdraw---------------------")
        def password1():
            password1=input("Enter your password: ")
            return password1
        def password2():
            password2=input("comfirm password: ")
            return password2

        password1=password1()
        password2=password2()
        
        while True:
            if password1==password2:

                def amount():
                    amount=int(input("Enter amount: "))
                    return amount
                amount=amount()
                if amount==0:
                    print(f"You have insuficant balance!: {amount}")
                elif amount=='':
                    print(f'Invalid input!: {amount}')
                elif amount<0:
                    print(f'Invalid input!: {amount}')
                else:
                    self.balance=self.balance-amount
                    print('')
                    print(f"*********You have been withdrawn {amount} Successfully!***********")
                    print('')

                print("----------------------------------------")
                print(f'Your account number: {self.accountNumber}')
                print(f'Availval balance: {self.balance}')
                print("----------------------------------------")
                break
            else:
                print("Password does not matched!")
                print('')
                print("**************Thanks for using me!********************")
                print('')
                break

#function for deposit amount            
    def deposit(self):
        print("-----------------Deposit---------------------")
        def amount():
            amount=int(input("Enter amount: "))
            return amount
        amount=amount()
        if amount==0:
            print(f"Invalid input!: {amount}")
        elif amount=='':
            print(f'Invalid input!: {amount}')
        elif amount<0:
            print(f'Invalid input!: {amount}')
        else:
            self.balance=self.balance+amount
            print('')
            print(f"*********You have been deposited {amount} Successfully!***********")
            print('')
        print("----------------------------------------")
        print(f'Your account number: {self.accountNumber}')
        print(f'Availval balance: {self.balance}')
        print("----------------------------------------")

#function for show account details
    def show(self):
        def password1():
            password1=input("Enter your password: ")
            return password1
        def password2():
            password2=input("comfirm password: ")
            return password2
        password1=password1()
        password2=password2()
       
        while True:
            if password1==password2:
                print("---------------Account Details---------------------")
                print(f'Name: {self.fname} {self.lname}')
                print(f'Your account number: {self.accountNumber}')
                print(f'Availval balance: {self.balance}')
                print(f'Password: {self.password}')
                break
               
            else:
                print("Password does not matched!")
                print('')
                print("**************Thanks for using me!********************")
                print('')
                break

#Navigator
def navigate():
    while True:
        print('---------------------------------')
        print("1.Create account: ")
        print("2.Withdraw: ")
        print("3.Deposit: ")
        print("4.Show account details: ")
        print("5.Change your password")
        print("6.Exit:")
        print('---------------------------------')
        choice=int(input("Enter your choice: "))
        if choice==1:
            fname=input('Enter your First Name:')
            lname=input('Enter your Last Name: ')
            full_name = fname+'_'+lname
            full_name=Account(fname,lname)
            print('')
            
        elif choice==2:
            full_name.withdraw()
            print('')
        elif choice==3:
            full_name.deposit()
            print('')
        elif choice==4:
            full_name.show()
            print('')
        elif choice==5:
            full_name.changePass()
            print('')
        elif choice==6:
            print('')
            print("**************Thanks for using me!********************")
            print('')
            break

navigate()