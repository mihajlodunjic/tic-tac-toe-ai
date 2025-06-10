# Tic-Tac-Toe sa Botom (Minimax algoritam)

Ova igra predstavlja proširenu verziju popularne igre **Tic-Tac-Toe (Iks-Oks)**, omogućavajući prilagođavanje veličine table i broja simbola u nizu potrebnih za pobedu. Igra se igra protiv bota koji koristi **Minimax algoritam sa Alpha-Beta odsecanjem** za donošenje optimalnih poteza.

## Karakteristike

- Prilagodljiva veličina table (`MxN`)
- Prilagodljiv broj simbola potrebnih za pobedu (`K`)
- Igrač igra kao **X**, bot kao **O**
- Bot koristi **Minimax algoritam** sa evaluacijom pozicije i Alpha-Beta odsecanjem
- Provera pobede u svim pravcima (horizontalno, vertikalno, obe dijagonale)
- Detekcija nerešenog rezultata
- Mogućnost ponavljanja partije

## Kako pokrenuti

1. Pokrenite skriptu u Python okruženju (verzija 3.x):

```bash
python tic_tac_toe.py
```
## Unesite sledeće podatke kada se od vas zatraže:

 - Broj redova table (npr. 3)
 - Broj kolona table (npr. 3)
 - Broj simbola u nizu za pobedu (npr. 3)
 - Ko igra prvi – unesite X (vi) ili O (bot)
 - Igrajte tako što unosite red i kolonu za vaš potez (brojevi počinju od 1).

## Struktura koda
 - inicijalizacija_igre() – Inicijalizuje praznu tablu i broj simbola potrebnih za pobedu
 - odigraj_potez() – Postavlja potez na tablu, sa proverom validnosti 
 - proveri_trenutno_stanje() – Detektuje pobedu, nerešeno ili nastavak igre
 - oceni_stanje_igre() – Heuristička funkcija za evaluaciju pozicije
 - vrati_najbolji_potez() – Minimax funkcija sa Alpha-Beta odsecanjem
 - prikazi_tablu() – Prikazuje trenutno stanje table u konzoli

 Ovaj projekat je edukativnog karaktera i može poslužiti kao osnova za dalje eksperimente sa veštačkom inteligencijom u igrama.