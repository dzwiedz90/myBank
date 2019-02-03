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
	for x in data:
		print('\n')
		print('id: ', x[0],)
		print('name: ', x[1],)
		print('surname: ', x[2],)
		print('account_number: ', x[4],)
		print('account_balance: ', x[5],)
	input()