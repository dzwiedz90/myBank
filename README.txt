Aplikacja bankowa kliencka + serwer
Klient loguje si� do aplikacja za pomoc� loginu i has�a, w aplikacji mo�e sprawdzic szczeg�y dot. swojego konta i wykona�
operacje.
Aplikacja serwerowa komunikuje si� z baz�, w kt�rej przetrzymywane s� dane, sprawdza poprawno�� logowania, przekazuje dane do 
aplikacji klienckiej, wykonuje operacje zlecone przez klienta.

- modu� tworzenia u�ytkownika(dodatkowy/opcjonalny), 2 u�ytkownik�w b�dzie domy�lnie utworzonych, modu� pozwoli doda� wi�ksz� ilo�� u�ytkownik�w
- modu� bankomat/wp�atomat - zmiana stanu �rodk�w na koncie - symulacja wyp�acania lub wp�acania �rodk�w na konto
- modu� klienta - operacje na koncie, sprawdzenie stanu, wyci�g operacji do pliku, przesy�anie operacij/zada� do serwera
- modu� serwer - wykonywanie operacji/zada� przesy�anych z modu�u klienta, przechowywanie/modyfikacja danych w bazie
- baza, tabele:
    *u�ytkownicy: id, imie, nazwisko, miasto, kod pocztowy, ulica+nrdomu, pesel
    *konta: id_user (obcy z u�ytkownicy - id), nr_konta, typ_konta, has�o
    *stan konta: id_user(obcy z u�ytkownicy - id), nr_konta, stan_konta
 - generator - modu� dodatkowy do generowania numeru pesel i numeru konta