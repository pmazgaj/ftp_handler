"""
Zlecę wykonanie skryptu w Pythonie 2.7, który:
1. Zaloguje się na serwer ftp
2. Sprawdzi datę i godzinę modyfikacji pliku
3. Jeśli plik jest starszy niz X godzin względem czasu komputera,
na którym uruchomiony został program, to skrypt powinien wysłać powiadomienie na e-maila.
4. Powiadomienie email

Skrypt powinien być konfigurowany wewnątrz kodu w łatwy sposób i zawierać:
- adres serwera ftp w postaci nazwy domeny
- nazwę użytkownika ftp
- hasło użytkownika ftp
- ścieżkę wraz z nazwą pliku sprawdzanego
- przesunięcie czasowe X wyrażone w godzinach
- adres serwera smtp w postaci nazwy domeny
- nazwę użytkownika smtp
- hasło użytkownika smtp
- adres nadawcy maila
- adres odbiorcy maila
- temat maila
- treść e-maila

"""

