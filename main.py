"""CODIGO CREADO POR RAMSES QUINTANILLA"""

def binarioHexadecimal(valor_convertir):
    valor_entero = int(valor_convertir)
    valor_decimal = valor_convertir - valor_entero

    valores_hexadecimal = "0123456789ABCDEF"
    res_hexadecimal = ""
    res_hexadecimal_decimal = ""

    while valor_entero > 0:
        resto = valor_entero % 16
        res_hexadecimal = valores_hexadecimal[resto] + res_hexadecimal
        valor_entero //= 16

    if valor_decimal > 0:
        itera = 0
        while valor_decimal > 0 and itera < 10:
            valor_decimal *= 16
            digito = int(valor_decimal)
            res_hexadecimal_decimal += valores_hexadecimal[digito]
            valor_decimal -= digito
            itera += 1
        if res_hexadecimal != 0 and res_hexadecimal != "":
            return f'{res_hexadecimal}.{res_hexadecimal_decimal}'
        else:
            return f'0.{res_hexadecimal_decimal}'
    return res_hexadecimal if res_hexadecimal else 0


def binarioDecimal(valor_convertir):
    if '.' in valor_convertir:
        valor_completo = valor_convertir.split('.')
        valor_entero = valor_completo[0]
        valor_decimal = valor_completo[1]
    else:
        valor_entero = valor_convertir

    res_entero = 0
    res_decimal = 0

    for i, digito in enumerate(reversed(valor_entero)):
        if digito == '1':
            res_entero += 2**i

    if '.' in valor_convertir:
        for i, digito in enumerate(valor_decimal):
            if digito == '1':
                res_decimal += 2**(-(i+1))
        return res_entero + res_decimal
    return res_entero


def main():
    #AGREGAR VERIFICACIONES Y GUI
    print("PARA LOS VALORES CON DECIMALES USAR PUNTO")
    print("")
    valor_convertir = 0
    valor_convertir = input("Ingrese el numero en binario: ")
    print("")
    print(f'El resultado de {valor_convertir} en BINARIO a DECIMAL ES:')
    valor_decimal = float(binarioDecimal(valor_convertir))
    print(valor_decimal)

    print(f'El resultado de {valor_convertir} en BINARIO a HEXADECIMAL ES:')
    print(binarioHexadecimal(valor_decimal))


main()