def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a: float, b: float) -> float:
    return a ** b

if __name__ == "__main__":
    print(sumar(2, 3))          # 5
    print(restar(5, 1))         # 4
    print(multiplicar(4, 2))    # 8
    print(dividir(10, 2))       # 5.0
    print(potencia(2, 2))       # 4