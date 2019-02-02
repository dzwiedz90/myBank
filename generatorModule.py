#Program odczytujący dane z czujek meteorologicznych
import os
import sys
import time
import generatorDefs


def generator():
	os.system('cls')

	choose = 0
	while choose!= 1:
		choose1 = choose
		print('#######################################')
		print('#######                          ######')
		print('#######         generator        ######')
		print('#######                          ######')
		print('#######################################')
		print(' ')
		print('(C) by bear Wszystkie prawa zastrzeżone')
		print(' ')
		print('1. Generuj PESEL')
		print('2. Generuj numer konta')
		print('3. Wróć do myBank')
		print('4. Zamknij program')
		inputChoose = input('Wybierz działanie: ')
		if inputChoose == '1':
			pesel = generatorDefs.peselGenerator()
			print(pesel)
			input('Wciśnij enter, aby kontynuować...')
		elif inputChoose == '2':
			account = generatorDefs.accountNumberGenerator()
			print(account)
			input('Wciśnij enter, aby kontynuować...')
		elif inputChoose == '3':	
			break
		elif inputChoose == '4':
			sys.exit(0)
		os.system('cls')