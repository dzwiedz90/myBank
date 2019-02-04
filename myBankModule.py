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
				input('Wciśnij enter, aby kontynuować...')
		elif inputChoose == '2':	
			break
		elif inputChoose == '3':
			sys.exit(0)
		else: 
			print('Wprowadzono niepoprawny znak!')
			input('Wciśnij enter, aby kontynuować...')
		os.system('cls')
		
def logIn(login, password):
	#"""Funkcja pobiera i wyświetla dane z bazy."""
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	#Skrócić selecta tylko do id i pass, oraz skrócić try\except
	cur.execute("SELECT users.id, name, surname, password, account_number, account_balance FROM users, accounts WHERE accounts.users_id=users.id AND users.id = '%s'" % login)
	
	data = cur.fetchall()
	length = len(data)
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
		
	except IndexError:
		data3 = data[0]
		for x in data3:
			idData = data3[0]
			nameData = data3[1]
			surnameData = data3[2]
			passwordData = data3[3]
			accNumberData = data3[4]
			accBalanceData = data3[5]
			
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
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute("SELECT users.id, name, surname, password, account_number, account_balance FROM users, accounts WHERE accounts.users_id=users.id AND users.id = '%s'" % login)
	
	data = cur.fetchall()
	length = len(data)
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
		if length>2:
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
			print('dupa')
		elif inputChoose == '2':
			print('dupa')
		elif inputChoose == '3':	
			break
		elif inputChoose == '3':
			sys.exit(0)
		else: 
			print('Wprowadzono niepoprawny znak!')
			input('Wciśnij enter, aby kontynuować...')
		os.system('cls')