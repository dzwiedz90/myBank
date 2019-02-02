import databaseActions
import os
import sys



def usersModule():
	os.system('cls')

	choose = 0
	while choose!= 1:
		choose1 = choose
		print('#######################################')
		print('#######                          ######')
		print('#######       Users module       ######')
		print('#######                          ######')
		print('#######################################')
		print(' ')
		print('(C) by bear Wszystkie prawa zastrzeżone')
		print(' ')
		print('1. Wyświetl istniejących użytkowników')
		print('2. Dodaj użytkownika')
		print('3. Wróć do myBank')
		print('4. Zamknij program')
		inputChoose = input('Wybierz działanie: ')
		if inputChoose == '1':
			databaseActions.readData()
			input('Wciśnij enter, aby kontynuować...')
		elif inputChoose == '2':
			name= input('Podaj imię: ')
			surname = input('Podaj nazwisko: ')
			password = input('Podaj hasło: ')
			city = input('Podaj miasto: ')
			postCode = input('Podaj kod pocztowy: ')
			street = input('Podaj ulicę: ')
			pesel = input('Podaj pesel(11 znaków): ')
			accountNumber = input('Podaj numer konta(6 znaków): ')
			accountBalance = input('Podaj stan środków:')
			usersID = input('Podaj id usera(kolejny wolny numer id/ niestety trzeba sprawdzić i podać ręcznie, domyślnie: 4):')
			databaseActions.createUser(name, surname, password, city, postCode, street, pesel, accountNumber, accountBalance, usersID)
			input('Wciśnij enter, aby kontynuować...')
		elif inputChoose == '3':	
			break
		elif inputChoose == '4':
			sys.exit(0)
		os.system('cls')