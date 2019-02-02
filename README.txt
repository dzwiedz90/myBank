Aplikacja bankowa kliencka + serwer
Klient loguje siê do aplikacja za pomoc¹ loginu i has³a, w aplikacji mo¿e sprawdzic szczegó³y dot. swojego konta i wykonaæ
operacje.
Aplikacja serwerowa komunikuje siê z baz¹, w której przetrzymywane s¹ dane, sprawdza poprawnoœæ logowania, przekazuje dane do 
aplikacji klienckiej, wykonuje operacje zlecone przez klienta.

- modu³ tworzenia u¿ytkownika(dodatkowy/opcjonalny), 2 u¿ytkowników bêdzie domyœlnie utworzonych, modu³ pozwoli dodaæ wiêksz¹ iloœæ u¿ytkowników
- modu³ bankomat/wp³atomat - zmiana stanu œrodków na koncie - symulacja wyp³acania lub wp³acania œrodków na konto
- modu³ klienta - operacje na koncie, sprawdzenie stanu, wyci¹g operacji do pliku, przesy³anie operacij/zadañ do serwera
- modu³ serwer - wykonywanie operacji/zadañ przesy³anych z modu³u klienta, przechowywanie/modyfikacja danych w bazie
- baza, tabele:
    *u¿ytkownicy: id, imie, nazwisko, miasto, kod pocztowy, ulica+nrdomu, pesel
    *konta: id_user (obcy z u¿ytkownicy - id), nr_konta, typ_konta, has³o
    *stan konta: id_user(obcy z u¿ytkownicy - id), nr_konta, stan_konta
 - generator - modu³ dodatkowy do generowania numeru pesel i numeru konta