def primeNumbers():
    for numb in range(100):
        if numb > 1:
            for i in range(2, numb):
                if(numb % i) == 0:
                    break
            else:
                print(numb)
primeNumbers()