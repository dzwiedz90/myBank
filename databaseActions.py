import sqlite3



# def conn():
	#połączenie z bazą
	# conn = sqlite3.connect('example.db')
	#utworzenie kursora
	# cur = conn.cursor()

#Utworzenie bazy danych i wypełnienie jej danymi
def createDatabase():
	#polączenie z bazą danych
	conn = sqlite3.connect('example.db')

	#tworzenie tabeli
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS users;")
	cur.execute("""
		CREATE TABLE IF NOT EXISTS users (
			id INTEGER PRIMARY KEY ASC,
			name varchar(250) NOT NULL,
			surname varchar(250) NOT NULL,
			password varchar(250) NOT NULL,
			city varchar(250) NOT NULL,
			post_code varchar(250) NOT NULL,
			street_home_number varchar(250) NOT NULL,
			pesel BIGINT NOT NULL
		)""")
	cur.execute("DROP TABLE IF EXISTS accounts;")
	cur.execute("""
		CREATE TABLE IF NOT EXISTS accounts (
			id INTEGER PRIMARY KEY ASC,
			account_number INTEGER NOT NULL,
			account_balance varchar(250) NOT NULL,
			users_id INTEGER NOT NULL,
			FOREIGN KEY(users_id) REFERENCES users(id)
		)""")
		
		
	# tupla "users" zawiera tuple z danymi poszczególnych użytkowników
	usersData = (
		(None, 'Tomasz', 'Nowak', '1234', 'Poznań', '60-320', 'Bukowska 1/2', '53515564843'),
		(None, 'Alfred', 'Szymczak', '1234', 'Gorzów Wlkp.', '66-400', 'Stilonowa 13/8', '74300625537'),
		(None, 'Jan', 'Kowalski', '1234', 'Warszawa', '01-020', 'Marszałowska 121/12', '38300020761')
	)	

	#wstawiam rekordy do tabeli
	cur.executemany('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?);', usersData)



	# tupla "accountsData" zawiera tuple z danymi poszczególnych kont
	accountsData = (
		(None, '162472', '36589.99', '1'),
		(None, '244685', '12260.87', '2'),
		(None, '805054', '87329.63', '3'),
		(None, '545152', '5345.09', '1')
	)

	#wstawiam rekordy do tabeli
	cur.executemany('INSERT INTO accounts VALUES(?,?,?,?)', accountsData)

	# zatwierdzamy zmiany w bazie
	conn.commit()




def readData():
	#"""Funkcja pobiera i wyświetla dane z bazy."""
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	cur.execute(
		"""
		SELECT users.id, name, surname, password, city, post_code, street_home_number, pesel, account_number, account_balance
		FROM users, accounts
		WHERE accounts.users_id=users.id
		""")
	data = cur.fetchall()
	for x in data:
		print('\n')
		print('id: ', x[0],)
		print('name: ', x[1],)
		print('surname: ', x[2],)
		print('password: ', x[3],)
		print('city: ', x[4],)
		print('post_code: ', x[5],)
		print('street/home_number: ', x[6],)
		print('pesel: ', x[7],)
		print('account_number: ', x[8],)
		print('account_balance: ', x[9],)

	
def createUser(name, surname, password, city, postCode, street, pesel, accountNumber, accountBalance, usersID):
	
	
	
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	
	usersData = (
		(None, name, surname, password, city, postCode, street, pesel)
	)	

	#wstawiam rekordy do tabeli
	cur.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?);', usersData)
	
	
	# tupla "accountsData" zawiera tuple z danymi poszczególnych kont
	accountsData = (
		(None, accountNumber, accountBalance, usersID)
	)
	
	#wstawiam rekordy do tabeli
	cur.execute('INSERT INTO accounts VALUES(?, ?, ?, ?);', accountsData)
	
	# zatwierdzamy zmiany w bazie
	conn.commit()