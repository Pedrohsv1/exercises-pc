abc = input().split()

A = float(abc[0])
B = float(abc[1])
C = float(abc[2])

isPossible = True

if A < B:
    A, B = B, A
if A < C:
    A, C = C, A
if B < C:
    B, C = C, B

if A >= B + C:
        print("NAO FORMA TRIANGULO")
        isPossible = False

if isPossible:    
    if A**2 > B**2 + C**2:
            print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
            print("TRIANGULO ACUTANGULO")

    if A**2 == B**2 + C**2:
            print("TRIANGULO RETANGULO")
    elif A == B == C:
            print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")