def get_goldbach(n):
    # Pentru a avea o solutie, parametrul dat trebuie sa respecte conditiile: n > 3 si n % 2 == 0 ( sa fie par )
    for i in range(int(n), 1, -1):
        if test_get_goldbach(i):
            for j in range(3, int(i)+1, 2):
                if test_get_goldbach(j) and int(i)+int(j)==int(n):
                    print(i, end = " ")
                    print(j)
                    return
    print("NU SE VERIFICA")

def test_get_goldbach(n):
    if int(n) < 2: return False
    for i in range(2, int(n) // 2 + 1):
        if int(n) % int(i) == 0: return False
    return True

def get_newton_sqrt(n, steps):
    x=n
    x0=2
    while steps:
        steps=int(steps)-1
        root=float(0.5)*(float(x)+float(n)/float(x))
        if test_get_newton_sqrt(root, x, x0) == True:
            break
        x=float(root)
    return float(root)

def test_get_newton_sqrt(root, x, x0):
    if float(abs(float(root) - float(x))) < float(x0):
        return True
    return False

if __name__ == '__main__':
    while True:
        print("Optiuni:")
        print("1. Conjunctura lui Goldbach")
        print("2. Calcularea radicalului folosind metoda lui Newton")
        print("3. Termina programul")
        option = input("Scrie numarul aferent optiunii: ")

        if option == "1":
            n = input("Introdu numarul: ")
            get_goldbach(n)

        if option == "2":
            n = input("Introdu numarul: ")
            steps = input("Introdu numarul de pasi: ")
            print("Solutia este:", end = " ")
            print(get_newton_sqrt(n, steps))

        if option == "3":
            break
        print()
    exit(0)