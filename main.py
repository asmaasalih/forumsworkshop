class ATM:

	def __init__(self,balance,bank_name):
		self.balance = balance
		self.bank_name = bank_name
		self.withdrawals_list = []

	def show_withdrawals(self):
		for withdrawal in self.withdrawals_list:
			print("withdrawal: "+str(withdrawal))
			


	def print_information(self):
		print("Welcome to "+ self.bank_name)
		print("current balance: " + str(self.balance))


	def check_balance(self , request):	
		if self.balance < request:
			print("Can't give you all this money !!")

		elif request < 0:
			print("More than zero plz!")

	

	def withdraw(self, request):
		self.withdrawals_list.append(request)

		if self.balance > request:
			self.balance = self.balance - request

			while request > 0:

				if request >= 100:
					request -= 100
					print("give 100")

				elif request >= 50:
					request -= 50
					print("give 50")

				elif request >= 10:
					request -= 10
					print("give 10")

				else:
					request -= 5
					print("give 5")
		return self.balance			
	 
		    
	
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "islamy bank")
atm2 = ATM(balance2, "baraka bank")

atm1.print_information()
atm1.check_balance(300)
atm1.withdraw(300)

atm1.print_information()
atm1.check_balance(250)
atm1.withdraw(250)

atm1.show_withdrawals()

atm2.print_information()
atm2.check_balance(500)
atm2.withdraw(500)

atm2.print_information()
atm2.check_balance(455)
atm2.withdraw(455)

atm2.show_withdrawals()