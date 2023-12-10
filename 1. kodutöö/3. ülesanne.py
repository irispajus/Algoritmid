def rekursiivne_fibonacci(n): 
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rekursiivne_fibonacci(n - 1) + rekursiivne_fibonacci(n - 2)

try:
    n = int(input("Sisestage mitmendat Fibonacci numbrit soovite: "))
    if n < 0:
        print("Sisestage positiivne täisarv.")
    else:
        vastus = rekursiivne_fibonacci(n)
        print(f"{n}. Fibonacci number on {vastus}")
except ValueError:
    print("Sisestage positiivne täisarv!")
