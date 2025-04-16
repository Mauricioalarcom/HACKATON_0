def calculate(entrada):
    entrada = entrada.strip()
    if not entrada:
        raise ValueError("Entrada vacía")

    # Solo permitimos la suma en esta implementación
    if '+' in entrada:
        partes = entrada.split('+')
        if len(partes) != 2:
            raise SyntaxError("Sintaxis inválida para la suma")
        try:
            num1 = float(partes[0].strip())
            num2 = float(partes[1].strip())
            return num1 + num2
        except ValueError:
            raise ValueError("Entrada inválida")
    else:
        raise NotImplementedError("Solo se permite la suma por ahora")


def procesar_entrada(entrada):
    entrada = entrada.strip()
    
    if '*' in entrada:
        partes = entrada.split('*')
        if len(partes) != 2:
            raise SyntaxError("Sintaxis inválida para la multiplicación")
        try:
            num1 = float(partes[0].strip())
            num2 = float(partes[1].strip())
            return num1 * num2
        except ValueError:
            raise ValueError("Entrada inválida: no se pudo convertir a número")
    else:
        raise NotImplementedError("Operación no implementada")
    #HAVE_
