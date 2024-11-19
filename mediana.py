def mediana(numbers):
    if len(numbers) % 2 == 0:
        med = ((numbers[int(len(numbers) / 2 + 1 / 2)] + numbers[int(len(numbers) / 2 - 1 / 2)]) / 2)
    else:
        med = numbers[int(len(numbers) / 2)]
    print('Mediana z {} liczb : {} to {}'.format(len(numbers), numbers, med))
def numbersinput(x):
    if type(x) == list or type(x) == tuple:
        liczba = 1
        x = [None]
        print('Wpisz K jesli wpisales już wszystkie liczby')
        warunek = True
        while warunek == True:
            for i in x:
                i = input(('wprowadz liczbe nr {} >>>> '.format(liczba)))
                liczba = liczba + 1
                if i == 'K':
                    warunek = False
                else:
                    x.append(i)
        x.remove(x[0])
        x = sorted([float(i) for i in x])
        return list(x)

if __name__ == '__main__':
    x = []
    x = numbersinput(x)
    mediana(x)
