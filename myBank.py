#Program odczytujący dane z czujek meteorologicznych
import os
import sys
import time
import generatorModule
import databaseActions
import usersModule
import myBankModule



databaseActions.createDatabase()

def myBank():
	os.system('cls')

	choose = 0
	while choose!= 1:
		choose1 = choose
		print('#######################################')
		print('#######                          ######')
		print('#######          myBank          ######')
		print('#######                          ######')
		print('#######################################')
		print(' ')
		print('(C) by bear Wszystkie prawa zastrzeżone')
		print(' ')
		print('1. Uruchom moduł generator')
		print('2. Uruchom moduł tworzenia użytkownika / wyświetlenia użytkowników')
		print('3. Uruchom moduł bankomat/wpłatomat')
		print('4. Uruchom moduł klienta myBank')
		print('5. Wyjdź')
		inputChoose = input('Wybierz działanie: ')
		if inputChoose == '1':
			generatorModule.generator()
		elif inputChoose == '2':
			usersModule.usersModule()
		elif inputChoose == '3':
			print('bankomat/wpłatomat')
			input()
		elif inputChoose == '4':
			myBankModule.myBankModule()
		elif inputChoose == '5':	
			sys.exit(0)
		else: 
			print('Wprowadzono niepoprawny znak!')
			input('Wciśnij enter, aby kontynuować...')
		os.system('cls')

myBank()