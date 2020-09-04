import datetime

class Main:
	def __init__(self):
		self.weeks = [None] * 53
		today = datetime.date.today()
		self.startDayOfWeek = datetime.date.today().strftime('%A')
		self.startingWeekNumber = datetime.date(today.year,today.month,today.day).isocalendar()[1]

	class Week:
		def __init__(self, budget = float('inf')):
			self.weekDays = [None] * 7
			self.weekTotal = 0
			self.weekBudget = budget
			self.startDate = datetime.date.today()
			self.lastDate = self.startDate + datetime.timedelta(6)

		class Day:
			def __init__(self):
				self.expenses = []
				self.dailyTotal = 0

			class Expense:
				def __init__(self, expenseName, expenseAmount):
					self.name = expenseName
					self.amount = expenseAmount

			def addExpense(self, expenseName, expenseAmount):
				newExpense = self.Expense(expenseName, expenseAmount)
				self.expenses.append(newExpense)
				self.dailyTotal += expenseAmount

		def getDayNumberFromDayName(self,dayName, startDayOfWeek):
			weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
			totalDaysInWeek = 7

			for startDayIndex in range(0, len(weekDays)):
				if weekDays[startDayIndex] == startDayOfWeek:
					break
			for index in range(0,7):
				if weekDays[(startDayIndex + index) % totalDaysInWeek] == dayName:
					break
			return index

		def addExpense(self, expenseName, expenseAmount, startDayOfWeek):
			currentDay = datetime.date.today().strftime('%A')
			index = self.getDayNumberFromDayName(currentDay, startDayOfWeek)

			if self.weekDays[index] == None:
				self.weekDays[index] = self.Day()

			if (self.weekTotal + expenseAmount > self.weekBudget):
				print()
				print("Warning !!!")
				print("Weekly budget ", self.weekBudget, " has exceeded")
				print("Current Week Total : ", self.weekTotal)
				print("Current Week Total After adding this Expense: ", (self.weekTotal + expenseAmount))
				print("########################################################")

				print("Do u still want to add this expense")
				print("Type 1 if 'Yes'")
				print("Type 2 if 'No'")
				try:
					choice = int(input())
					if choice == 1:
						self.weekDays[index].addExpense(expenseName, expenseAmount)
						print("Expense added successfully")
					elif choice == 2:
						print("Expense " + expenseName + " discarded successfully")
					else:
						print("Invalid choice")
				except:
					print("Input Numeric Value")
			else:
				self.weekDays[index].addExpense(expenseName, expenseAmount)
				print("Expense added successfully")
				self.weekTotal += expenseAmount;

	def getDetailsOfNWeek(self,n):
		today = datetime.date.today()
		currentWeekNumber = datetime.date(today.year,today.month,today.day).isocalendar()[1] - self.startingWeekNumber

		print()
		print('*************************************************')
		if currentWeekNumber - n + 1 >= 0:
			print("Week reports of ", n, " week is :-")
		else:
			print("Only ", (currentWeekNumber + 1) , " weeks data is available")
		for i in range(max(currentWeekNumber - n, 0), currentWeekNumber + 1):
			week = self.weeks[i]
			if week == None:
				print()
				print("Week Number : ", (i + 1))
				print("Week Total : 0.0")
				print("Duration of Week : N.A.")
				print()
				continue
			print()
			print("Week Number : ", (i + 1))
			print("Week Total : ", week.weekTotal)
			print("Duration of Week : ", week.startDate, " to ", week.lastDate)
			print()
			print("Daily expenses List")

			for j in range(0, len(week.weekDays)):
				if week.weekDays[j] == None:
				    print("Day ", week.startDate + datetime.timedelta(j//1), ": 0.0")
				else:
					print("Day ", week.startDate + datetime.timedelta(j//1), ": ", week.weekDays[j].dailyTotal)
			print()

	def addExpense(self, expenseName, expenseAmount):
		today = datetime.date.today()
		weekNumber = datetime.date(today.year,today.month,today.day).isocalendar()[1] - self.startingWeekNumber

		if self.weeks[weekNumber] is None:
			print("Do you want to set a budget for this week")
			print("Type 1 if 'Yes'")
			print("Type 2 if 'No'")
			try:
				choice = int(input())
				if choice == 1:
					print("Enter budget")
					self.budget = float(input())
					self.weeks[weekNumber] = self.Week(self.budget)
					print("Budget added successfully")
				elif choice == 2:
					self.weeks[weekNumber] = self.Week()
				else:
					print("Invalid choice")
				currentWeek = self.weeks[weekNumber]
				currentWeek.addExpense(expenseName, expenseAmount,self.startDayOfWeek)
			except:
				print("Input Numeric Value")
		else:
			currentWeek = self.weeks[weekNumber]
			currentWeek.addExpense(expenseName, expenseAmount, self.startDayOfWeek)

expenseManager = Main()
status = True
while status:
	print()
	print("########################################################")
	print("Choose : ")
	print("1. Add an Expense")
	print("2. Get details of N week/s")
	print("3. Exit")
	print()
	try:
		choice = int(input())
		if choice == 1:
			print("Enter Name of the Expense ")
			expenseName = input()
			print("Enter Expense Amount")
			expenseAmount = float(input())
			expenseManager.addExpense(expenseName, expenseAmount)
			print()
		elif choice == 2:
			print("Enter Number of weeks")
			n = int(input())
			expenseManager.getDetailsOfNWeek(n)
			print()
		elif choice == 3:
			status = False
		else:
			print("Invalid choice")
			print()
	except:
		print("Input Numeric Value")

