def multiplicar(a, b):
    def es_numero(x):
        return isinstance(x, (int, float))

    # Si ambos son listas
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Las listas deben tener la misma longitud.")
        return [x * y for x, y in zip(a, b)]

    # Si uno es lista y el otro número
    elif isinstance(a, list) and es_numero(b):
        return [x * b for x in a]
    elif isinstance(b, list) and es_numero(a):
        return [a * y for y in b]

    # Si ambos son números
    elif es_numero(a) and es_numero(b):
        return a * b

    else:
        raise TypeError("Los argumentos deben ser números o listas de números.")