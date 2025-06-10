from math import inf as beskonacno

def inicijalizacija_igre():
    redovi = int(input("Unesite broj redova za tablu: "))
    kolone = int(input("Unesite broj kolona za tablu: "))
    simboli_u_nizu = int(input("Unesite broj simbola u nizu potrebnih za pobedu: "))
    
    stanje_igre = [[' ' for _ in range(kolone)] for _ in range(redovi)]
    return stanje_igre, simboli_u_nizu

def odigraj_potez(stanje, igrac, red, kolona):
    if 0 <= red < len(stanje) and 0 <= kolona < len(stanje[0]) and stanje[red][kolona] == ' ':
        stanje[red][kolona] = igrac
    else:
        print("Neispravan potez! Izaberite ponovo.")
        while True:
            red = int(input("Unesite broj reda: ")) - 1
            kolona = int(input("Unesite broj kolone: ")) - 1
            if 0 <= red < len(stanje) and 0 <= kolona < len(stanje[0]) and stanje[red][kolona] == ' ':
                break
            else:
                print("Nevažeći potez! Izaberite ponovo.")

def kopiraj_stanje_igre(stanje):
    return [red[:] for red in stanje]

def proveri_trenutno_stanje(stanje_igre, simboli_u_nizu):

    # Provera redova za pobedu
    for i in range(len(stanje_igre)):
        for j in range(len(stanje_igre[0]) - simboli_u_nizu + 1):
            if all(simbol == 'X' for simbol in stanje_igre[i][j:j + simboli_u_nizu]) or all(simbol == 'O' for simbol in stanje_igre[i][j:j + simboli_u_nizu]):
                return stanje_igre[i][j], "Gotovo"

    # Provera kolona za pobedu
    for i in range(len(stanje_igre[0])):
        for j in range(len(stanje_igre) - simboli_u_nizu + 1):
            if all(stanje_igre[j + k][i] == 'X' for k in range(simboli_u_nizu)) or all(stanje_igre[j + k][i] == 'O' for k in range(simboli_u_nizu)):
                return stanje_igre[j][i], "Gotovo"

    # Provera dijagonala za pobedu
    for i in range(len(stanje_igre) - simboli_u_nizu + 1):
        for j in range(len(stanje_igre[0]) - simboli_u_nizu + 1):
            if all(stanje_igre[i + k][j + k] == 'X' for k in range(simboli_u_nizu)) or all(stanje_igre[i + k][j + k] == 'O' for k in range(simboli_u_nizu)):
                return stanje_igre[i][j], "Gotovo"

    for i in range(len(stanje_igre) - simboli_u_nizu + 1):
        for j in range(simboli_u_nizu - 1, len(stanje_igre[0])):
            if all(stanje_igre[i + k][j - k] == 'X' for k in range(simboli_u_nizu)) or all(stanje_igre[i + k][j - k] == 'O' for k in range(simboli_u_nizu)):
                return stanje_igre[i][j], "Gotovo"

    # Provera da li je nerešeno
    flag_nereseno = all(simbol != ' ' for red in stanje_igre for simbol in red)
    if flag_nereseno:
        return None, "Nerešeno"

    return None, "Nije Gotovo"

def prikazi_tablu(stanje_igre):
    for red in stanje_igre:
        print('|'.join(str(simbol) for simbol in red))
        print('-' * (2 * len(red) - 1))

def oceni_stanje_igre(stanje, igrac, simboli_u_nizu):
    rezultat = 0
    protivnik = 'X' if igrac == 'O' else 'O'

    for i in range(len(stanje)):
        broj_simbola_igraca = stanje[i].count(igrac)
        broj_simbola_protivnika = stanje[i].count(protivnik)

        if broj_simbola_igraca > 0 and broj_simbola_protivnika == 0:
            rezultat += 10 ** broj_simbola_igraca
        elif broj_simbola_protivnika > 0 and broj_simbola_igraca == 0:
            rezultat -= 10 ** broj_simbola_protivnika

        rezultat += broj_simbola_igraca - broj_simbola_protivnika

    for i in range(len(stanje)):
        for j in range(len(stanje[0]) - simboli_u_nizu + 1):
            if all(stanje[i][j + k] == igrac for k in range(simboli_u_nizu)):
                rezultat += 10 ** simboli_u_nizu
            elif all(stanje[i][j + k] == protivnik for k in range(simboli_u_nizu)):
                rezultat -= 10 ** simboli_u_nizu

    for i in range(len(stanje[0])):
        for j in range(len(stanje) - simboli_u_nizu + 1):
            if all(stanje[j + k][i] == igrac for k in range(simboli_u_nizu)):
                rezultat += 10 ** simboli_u_nizu
            elif all(stanje[j + k][i] == protivnik for k in range(simboli_u_nizu)):
                rezultat -= 10 ** simboli_u_nizu

    for i in range(len(stanje) - simboli_u_nizu + 1):
        for j in range(len(stanje[0]) - simboli_u_nizu + 1):
            if all(stanje[i + k][j + k] == igrac for k in range(simboli_u_nizu)):
                rezultat += 10 ** simboli_u_nizu
            elif all(stanje[i + k][j + k] == protivnik for k in range(simboli_u_nizu)):
                rezultat -= 10 ** simboli_u_nizu

    for i in range(len(stanje) - simboli_u_nizu + 1):
        for j in range(simboli_u_nizu - 1, len(stanje[0])):
            if all(stanje[i + k][j - k] == igrac for k in range(simboli_u_nizu)):
                rezultat += 10 ** simboli_u_nizu
            elif all(stanje[i + k][j - k] == protivnik for k in range(simboli_u_nizu)):
                rezultat -= 10 ** simboli_u_nizu

    return rezultat


def vrati_najbolji_potez(stanje, igrac, simboli_u_nizu, dubina, alfa=-beskonacno, beta=beskonacno):
    pobednik, gotovo = proveri_trenutno_stanje(stanje, simboli_u_nizu)
    if gotovo == "Gotovo" and pobednik == 'O':
        return 10 ** simboli_u_nizu, 0
    elif gotovo == "Gotovo" and pobednik == 'X':
        return -10 ** simboli_u_nizu, 0
    elif gotovo == "Nerešeno":
        return 0, 0

    
    elif dubina == 0:
        return oceni_stanje_igre(stanje, 'O', simboli_u_nizu), 0
    
    potezi = []
    prazna_polja = [(i, j) for i in range(len(stanje)) for j in range(len(stanje[0])) if stanje[i][j] == ' ']

    for prazno_polje in prazna_polja:
        potez = {'index': prazno_polje}
        novo_stanje = kopiraj_stanje_igre(stanje)
        odigraj_potez(novo_stanje, igrac, prazno_polje[0], prazno_polje[1])

        if igrac == 'O':
            rezultat, _ = vrati_najbolji_potez(novo_stanje, 'X', simboli_u_nizu, dubina - 1, alfa, beta)
            potez['ocena'] = rezultat
            alfa = max(alfa, rezultat)
        else:
            rezultat, _ = vrati_najbolji_potez(novo_stanje, 'O', simboli_u_nizu, dubina - 1, alfa, beta)
            potez['ocena'] = rezultat
            beta = min(beta, rezultat)

        potezi.append(potez)

        if alfa >= beta:
            break  #Odsecanje preostalih grana

    if igrac == 'O':
        najbolja_ocena = -beskonacno
        for potez in potezi:
            if potez['ocena'] > najbolja_ocena:
                najbolja_ocena = potez['ocena']
                najbolji_potez = potez['index']
    else:
        najbolja_ocena = beskonacno
        for potez in potezi:
            if potez['ocena'] < najbolja_ocena:
                najbolja_ocena = potez['ocena']
                najbolji_potez = potez['index']

    return najbolja_ocena, najbolji_potez


ponovo_igraj = 'D'
while ponovo_igraj.upper() == 'D':
    stanje_igre, simboli_u_nizu = inicijalizacija_igre()
    trenutno_stanje = "Nije Gotovo"
    print("\nNova igra!")
    prikazi_tablu(stanje_igre)
    izbor_igraca = input("Izaberite koji igrač prvi igra - X (vi) ili O (bot): ")
    pobednik = None

    if izbor_igraca.upper() == 'X':
        trenutni_indeks_igraca = 0
    else:
        trenutni_indeks_igraca = 1

    while trenutno_stanje == "Nije Gotovo":
        if trenutni_indeks_igraca == 0:  #Potez igrača
            red = int(input("Unesite broj reda: ")) - 1
            kolona = int(input("Unesite broj kolone: ")) - 1
            odigraj_potez(stanje_igre, 'X', red, kolona)
        else:  #Potez bota
            _, izbor_bloka = vrati_najbolji_potez(stanje_igre, 'O', simboli_u_nizu, dubina=3)
            odigraj_potez(stanje_igre, 'O', izbor_bloka[0], izbor_bloka[1])
            print("Bot igra potez: " + str((izbor_bloka[0] + 1, izbor_bloka[1] + 1)))

        prikazi_tablu(stanje_igre)
        pobednik, trenutno_stanje = proveri_trenutno_stanje(stanje_igre, simboli_u_nizu)
        if pobednik is not None:
            print(str(pobednik) + " je pobedio!")
        else:
            trenutni_indeks_igraca = (trenutni_indeks_igraca + 1) % 2

        if trenutno_stanje == "Nerešeno":
            print("Nerešeno!")

    ponovo_igraj = input('Želite li ponovo da igrate? Ako da, kliknite D: ')


