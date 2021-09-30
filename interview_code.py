def licz(wejscie):
    """
    Ta funkcja wylicza wynik działania oparty o Odwrotną Notację Polską.
    :param wejscie: string, zawiera elementy potrzebne do wyliczenia wyniku operacji matemaatycznej.
    Zawiera liczby całkowite i operacje które mają być na tych liczbach wykonane.

    Szczegóły implementacji (source): https://pl.wikipedia.org/wiki/Odwrotna_notacja_polska

    :return: float, wynik działania
    """

    # zdefiniować operacje arytmetyczne
    # wejscie = string
    # rozbicie wejscie na elementy, separator to spacja
    # przejść element po elemencie
    # jeżeli napotkam operacje arytmetyczną wykonać działanie na ostatnich dwóch elementach kolekcji
    # jeżeli element nie jest operacją matematyczną, dodać do kolekcji

    operacje = ['+', '-', '/', '*'] # todo czy może to być słownik z wartościami odnoszącymi się do __add__, __mul__ itd

    operacje = {
        '+': '__add__',
        '-': '__sub__',
        '*': '__mul__' # ,
        # '/': '__div__'
        ## pierwiastek DONE
        ## customowe funkcje w których jest trzy lub wiećęj elementów DONE
        ## swoje operatory DONE
        ## elementy większe niż float - co wtedy
    }

    elementy = wejscie.split(' ')

    rezultaty = list()

    for el in elementy:
        if el in operacje:
            elem2 = rezultaty.pop()
            elem1 = rezultaty.pop()
            try:
                rezultaty.append(getattr(elem1, operacje[el])(elem2))
            except ZeroDivisionError as e:
                raise e('Zgłoszono błąd związany z dzieleniem wyrażenia przez zero. Błędne działanie: ') ## todo customowy tekst
        else:
            rezultaty.append(float(el))

    return rezultaty.pop()


if __name__ == "__main__":
    print('licz 2 3 +', licz('2 3 +'))
    assert licz('2 3 +') == 5
    assert licz('1 2 3 + +') == 6
    print(licz('5 1 2 + 4 * + 3 -'))
    assert licz('5 1 2 + 4 * + 3 -') == 14
    # print(licz('1 0 /'))

# import a
# wynik = a('2 3 5 + /')