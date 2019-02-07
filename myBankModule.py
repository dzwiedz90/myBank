import os
import sys
import sqlite3



def myBankModule():
	os.system('cls')

	choose = 0
	while choose!= 1:
		choose1 = choose
		print('#######################################')
		print('#######                          ######')
		print('#######       myBankModule       ######')
		print('#######                          ######')
		print('#######################################')
		print(' ')
		print('(C) by bear Wszystkie prawa zastrzeżone')
		print(' ')
		print('1. Zaloguj się')
		print('2. Wróć do myBank')
		print('3. Zamknij program')
		inputChoose = input('Wybierz działanie: ')
		if inputChoose == '1':
			loginID = input('Podaj login(id): ')
			password = input('Podaj hasło: ')#ustwaić na hasło aby nie wyświetlało
			try:
				logIn(loginID, password)
			except IndexError:
				print('Wprowadzono niepoprawny znak!')
				print('dupa5')
				input('Wciśnij enter, aby kontynuować...')
		elif inputChoose == '2':	
			break
		elif inputChoose == '3':
			sys.exit(0)
		else: 
			print('Wprowadzono niepoprawny znak!')
			print('dupa4')
			input('Wciśnij enter, aby kontynuować...')
		os.system('cls')
		
		
def databaseQuery(login):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	#Skrócić selecta tylko do id i pass, oraz skrócić try\except
	cur.execute("SELECT users.id, name, surname, password, account_number, account_balance FROM users, accounts WHERE accounts.users_id=users.id AND users.id = '%s'" % login)
	
	data = cur.fetchall()
	length = len(data)
#Do wywalenia do osobnej funkcji
	try:
		data1 = data[0]
		data2 = data[1]
		
		
		for x in data1:
			idData = data1[0]
			nameData = data1[1]
			surnameData = data1[2]
			passwordData = data1[3]
			accNumberData = data1[4]
			accBalanceData = data1[5]
		for x in data2:
			idData2 = data2[0]
			nameData2 = data2[1]
			surnameData2 = data2[2]
			passwordData2 = data2[3]
			accNumberData2 = data2[4]
			accBalanceData2 = data2[5]
	except IndexError:
		data3 = data[0]
		for x in data3:
			idData = data3[0]
			nameData = data3[1]
			surnameData = data3[2]
			passwordData = data3[3]
			accNumberData = data3[4]
			accBalanceData = data3[5]
	
	if length>=2:
		return length, idData, nameData, surnameData, passwordData, accNumberData, accBalanceData, idData2, nameData2, surnameData2, passwordData2, accNumberData2, accBalanceData2
	else:
		return length, idData, nameData, surnameData, passwordData, accNumberData, accBalanceData,
	
def logIn(login, password):

	data = databaseQuery(login)
	
	length = data[0]
	if length >= 2:
		idData = data[1]
		nameData = data[2]
		surnameData = data[3]
		passwordData = data[4]
		accNumberData = data[5]
		accBalanceData = data[6]
		idData2 = data[7]
		nameData2 = data[8]
		surnameData2 = data[9]
		passwordData2 = data[10]
		accNumberData2 = data[11]
		accBalanceData2 = data[12]
	else:
		idData = data[1]
		nameData = data[2]
		surnameData = data[3]
		passwordData = data[4]
		accNumberData = data[5]
		accBalanceData = data[6]
		
	loginFrom = str(login)
	passswordFrom = str(password)
	loginData = str(idData)
	passwordData = str(passwordData)
		
	if (loginFrom == loginData) and (passswordFrom == passwordData):
		print('Zalogowano!')
		input()
		loggedIn(login)
	else:
		print('Wprowadzono nieprawidłowe dane logowania!')
		input()
					
			
def loggedIn(login):
	os.system('cls')

	choose = 0
	while choose!= 1:
		data = databaseQuery(login)
	
		length = data[0]
		if length >= 2:
			idData = data[1]
			nameData = data[2]
			surnameData = data[3]
			passwordData = data[4]
			accNumberData = data[5]
			accBalanceData = data[6]
			idData2 = data[7]
			nameData2 = data[8]
			surnameData2 = data[9]
			passwordData2 = data[10]
			accNumberData2 = data[11]
			accBalanceData2 = data[12]
		else:
			idData = data[1]
			nameData = data[2]
			surnameData = data[3]
			passwordData = data[4]
			accNumberData = data[5]
			accBalanceData = data[6]
		
		choose1 = choose
		print('#######################################')
		print('#######                          ######')
		print('#######       myBankModule       ######')
		print('#######                          ######')
		print('#######################################')
		print(' ')
		print('(C) by bear Wszystkie prawa zastrzeżone')
		print(' ')
		if length>=2:
			print('+---------------------------------------')
			print('| Login           |  '+str(idData))
			print('| Imię i nazwisko |  '+str(nameData)+' '+str(surnameData))
			print('| Numer konta     |  '+str(accNumberData))
			print('| Stan konta      |  '+str(accBalanceData))
			print('----------------------------------------')
			print('+---------------------------------------')
			print('| Login           |  '+str(idData2))
			print('| Imię i nazwisko |  '+str(nameData2)+' '+str(surnameData2))
			print('| Numer konta     |  '+str(accNumberData2))
			print('| Stan konta      |  '+str(accBalanceData2))
			print('----------------------------------------')
		else:
			print('+---------------------------------------')
			print('| Login           |  '+str(idData))
			print('| Imię i nazwisko |  '+str(nameData)+' '+str(surnameData))
			print('| Numer konta     |  '+str(accNumberData))
			print('| Stan konta      |  '+str(accBalanceData))
			print('----------------------------------------')		
		print('1. Wykonaj przelew')
		print('2. Historia operacji')
		print('3. Wyloguj')
		print('4. Zamknij program')
		inputChoose = input('Wybierz działanie: ')
		if inputChoose == '1':
			transferMoney()
		elif inputChoose == '2':
			accountStatement(login)
		elif inputChoose == '3':	
			break
		elif inputChoose == '4':
			sys.exit(0)
		else: 
			print('Wprowadzono niepoprawny znak!')
			print('dupa3')
			input('Wciśnij enter, aby kontynuować...')
		os.system('cls')
		
		
def transferMoney():
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	
	os.system('cls')

	choose = 0
	while choose!= 1:
		choose1 = choose
		print('#######################################')
		print('#######                          ######')
		print('#######       myBankModule       ######')
		print('#######                          ######')
		print('#######################################')
		print(' ')
		print('(C) by bear Wszystkie prawa zastrzeżone')
		print(' ')
		print('1. Wybierz konto')
		print('2. Wróć')
		print('3. Zamknij program')
		inputChoose = input('Wybierz działanie: ')
		if inputChoose == '1':
			accNumber = input('Wprowadź numer konta: ')
			moneyAmount = input('Wprowadź kwotę do przelania: ')
			accNumberIN = int(accNumber)
			print(accNumberIN)
			print('ddupa')
			moneyAmountIN = float(moneyAmount)
			print(moneyAmountIN)
			print(type(moneyAmountIN))
			print('dddupa')
			cur.execute("SELECT account_number, account_balance FROM accounts WHERE account_number = '%s'" % accNumberIN)
			print('ddddupa')
			data = cur.fetchall()
			print(data)
			for x in data:
				accNumberData = data[0][0]
				accBalanceData = data[0][1]
			print(accNumberData)
			print(accBalanceData)
			print(type(accBalanceData))
			try:
				accBalanceIN = [accBalanceData]
				acc = accBalanceIN[0]
				acc.replace(',', ".")
				accB = int(acc)
				print(type(acc))
				print('True')
			except ValueError:
				print('False')
				input()
			moneyToSend = accBalanceIN - moneyAmountIN
			print(moneyToSend)
			print('ddddddupa')
			input()
			cur.executemany("INSERT INTO accounts VALUES('%s') WHERE account_number = '%s';", moneyToSend, accNumberIN)
			print('dupa')
			input()
		elif inputChoose == '2':	
			break
		elif inputChoose == '3':
			sys.exit(0)
		else: 
			print('Wprowadzono niepoprawny znak!')
			print('dupa2')
			input('Wciśnij enter, aby kontynuować...')
		os.system('cls')
			
def accountStatement():
	print('dupa')