def calculate(entrada):
    entrada = entrada.strip()
    if not entrada:
        raise ValueError("Entrada vacía")
    # Validar las operaciones
    if not any(op in entrada for op in ['+', '-', '*', '/']):
        raise SyntaxError("Operación no soportada")


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
        
    elif '-' in entrada:
        partes = entrada.split('-')  # Corregido
        if len(partes) != 2:
            raise SyntaxError("Sintaxis inválida para la resta")
        try:
            num1 = float(partes[0].strip())
            num2 = float(partes[1].strip())
            return num1 - num2
        except ValueError:
            raise ValueError("Entrada inválida")

    elif '*' in entrada:
            partes = entrada.split('*')
            if len(partes) != 2:
                raise SyntaxError("Sintaxis inválida para la multiplicación")
            try:
                num1 = float(partes[0].strip())
                num2 = float(partes[1].strip())
                return num1 * num2
            except ValueError:
                raise ValueError("Entrada inválida")
    elif '/' in entrada:
        partes = entrada.split('/')
        if len(partes) != 2:
            raise SyntaxError("Sintaxis inválida para la división")
        try:
            num1 = float(partes[0].strip())
            num2 = float(partes[1].strip())
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            return num1 / num2
        except ValueError:
            raise ValueError("Entrada inválida")
    else:
        raise NotImplementedError("Operación no implementada")
