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
			logIn(loginID, password)
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
	cur.execute("SELECT users.id, name, surname, password, account_number, account_balance FROM users, accounts WHERE accounts.users_id=users.id AND users.id = '%s'" % login)
	
	data = cur.fetchall()
	length = len(data)
	try:
		data1 = data[0]
		data2 = data[1]
		print(data1)
		print(data2)
		
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
		print(idData)
		print(nameData)
		print(surnameData)
		print(passwordData)
		print(accNumberData)
		print(accBalanceData)
		print(idData2)
		print(nameData2)
		print(surnameData2)
		print(passwordData2)
		print(accNumberData2)
		print(accBalanceData2)
	except IndexError:
		for x in data:
			idData = data[0]
			nameData = data[1]
			surnameData = data[2]
			passwordData = data[3]
			accNumberData = data[4]
			accBalanceData = data[5]
	
		print(idData)
		print(nameData)
		print(surnameData)
		print(passwordData)
		print(accNumberData)
		print(accBalanceData)
		
	input()