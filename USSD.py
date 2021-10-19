#GTBank USSD prototype using python
#ATTAHIRU JAFAR
#U17/FNS/CSC/1098


#I first define some functions that i will use frequently

def select():
	c = input("press 1 to go back to main menu or 2 to cancel: \n_______\n")
	if(c=="1"):
		main()

#i declared main as a function 
def main():
	print("enter GTBank USSD code: \n__________\n")
	ussd = input( )
#we need to enter the correct USSD for GTBank
	if(ussd=="737"or ussd=="*737#"):
		option=input("\n 1.Airtime-self\n 2.Airtime-others\n 3.Data\n 4.Transf-GTB\n 5.Transf-Others\n6.check balance:\n________\n")
		if(option == "1"):
			amount = input("\nenter amount: ")
		
			print("\n",amount,"amount of airtime was sent to your line\n")
			select()
		elif(option == "2"):
			third = input("\nenter the 3rd-party number: \n__________\n")
			if(len(third)==10):
				amount = input("enter amount: ")
				arg = "are you sure you want to send "+amount+" naira amount of airtime to "+third+"?\n 1.Yes\n 2.No:\n________\n"		
				assure = input(arg)
				if(assure == "1"):
					print(amount,"amount of airtime was sent to ",third,"\n")
					select()
				elif(assure == "2"):
					print("transaction cancelled")
					select()
				else:
					print("input error! try again later")
			else:
				print("mobile number must be 11 digits")
				select()
		elif(option == "3"):
			choice = input('purchase data for: \n 1.self\n 2.3rd party\n______\n')
			if(choice == "1"):
				data = input("\nselect MTN bundle: \n 1. 100MB 1day N100\n 2. 350MB 7days N300\n 3. 750MB 14days N500 \n 4. 1GB 1day N300\n 5. 1.5GB 30days N1000\n_______\n")
				if(data == "1"):
					arg = input("\nAre you sure you want to purchase MTN 100MB data for N100?\n 1. Yes\n 2. No\n__________\n")
					print("trasaction successful.")
					select()
				elif(data =="2"):
					arg = input("\nAre you sure you want to purchase MTN 350MB data for N300 valid for 7 days?\n 1. Yes\n 2. No\n__________\n")
					print("trasaction successful.")
					select()
				elif(data == "3"):
					arg = input("\nare you sure you want to purchase MTN 750MB data for N500 valid for 14 days?\n 1. Yes\n 2. No\n__________\n")
					print("trasaction successful.")
					select()
				elif(data == "4"):
					arg = input("are you sure you want to purchase MTN 1GB data for N300 valid for 1 day?\n 1. Yes\n 2. No\n___________\n")
					print("trasaction successful.")
					select()
				elif(data == "5"):
					arg = input("are you sure you want to purchase MTN 1.5GB data for N1000 valid for 30 days?\n 1. Yes\n 2. No\n__________\n")
					print("trasaction successful.")
					select()
				else:
					print("input error! try again")
					select()
			elif(choice == "2"):
					third = input("enter the 3rd party number\n__________\n")
					if(len(third)!=11):
						print("phone number must be 11")
						select()
					else:
							data = input("select MTN bundle: \n 1. 100MB 1day N100\n 2. 350MB 7days N300\n 3. 750MB 14days N500 \n 4. 1GB 1day N300\n 5. 1.5GB 30days N1000\n____________\n")
					if(data == "1"):
						arg = input("are you sure you want to send MTN 100MB data for N100?\n 1. Yes\n 2. No\n__________\n")
						print("trasaction successful.")
						select()
					elif(data =="2"):
						arg = input("are you sure you want to purchase MTN 350MB data for N300 valid for 7 days?\n 1. Yes\n 2. No\n__________\n")
						print("trasaction successful.")	
						select()
					elif(data == "3"):
						arg = input("are you sure you want to purchase MTN 750MB data for N500 valid for 14 days?\n 1. Yes\n 2. No\n__________\n")
						print("trasaction successful.")
						select()
					elif(data == "4"):
						arg = input("are you sure you want to purchase MTN 1GB data for N300 valid for 1 day?\n 1. Yes\n 2. No\n_____\n")
						print("trasaction successful.")
						select()
					elif(data == "5"):
						arg = input("are you sure you want to purchase MTN 1.5GB data for N1000 valid for 30 days?\n 1. Yes\n 2. No\n__________\n")
						print("trasaction successful.")
						select()
					else:
						print("input error! try again")
						select()
			else:
					print("wrong input, try again later.")
					select()
		elif(option == "4"):
					amount = eval(input("please enter amount:\n__________\n"))
					recipient = input("enter recipient account number: \n__________\n")
					if(len(recipient)!=10):
						print("account number must be 10 digits")
						select()
					else:
						alert = "enter your 737 PIN to comfirm transfer of NGN "+amount+" to "+recipient+" at N20 charges, enter 0 to cancel: \n__________\n"
						pin = input(alert)
						if(pin == "1089"):
							if(amount <= 10000):
								print("transaction successful!")
								select()
							else:
								print("insufficient fund!, your account balance is NGN10,000")
								select()
						elif(pin == "0"):
							print("transaction cancelled")
							select()
						else:
							print("wrong input, try again later")
							select()
		elif(option == "5"):
				amount = eval(input("please enter amount:\n__________\n"))
				recipient = input("enter recipient account number: \n__________\n")
				if(len(recipient)!=10):
					print("account number must be 10 digits")
					select()
				else:
					bank = input("please enter:\n 1. First Bank\n 2. Access(Diamond)\n 3. Access\n 4. Zenith\n 5. UBA \n 6. Ecobank\n 7. Polaris Bank\n 8. FCMB\n__________\n")
					alert = "enter your 737 PIN to comfirm transfer of NGN "+str(amount)+" to "+recipient+" at N20 charges, enter 0 to cancel: \n__________\n"
					pin = input(alert)
					if(pin == "1089"):
						if(amount <= 10000):
							print("transaction successful!")
							select()
						else:
									print("insufficient fund!, your account balance is NGN10,000")
									select()
					elif(pin == "0"):
							print("transaction cancelled")
							select()
					else:
							print("wrong input, try again later")
							select()
		elif(option=="6"):
					print("dear ATTAHIRU JAFAR, your account balance is NGN10,000")
					select()
					

	else:
		print("wrong USSD entered, try again")
		main()
		
		
		
#Here is the beginning of the code	
print("WELCOME TO ATTAHIRU JAFAR GTBank USSD prototype\n")

#i called upon my main function	
main()