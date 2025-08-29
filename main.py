"""CODIGO CREADO POR RAMSES QUINTANILLA"""
from tkinter import *
from tkinter import StringVar


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
    valor_convertir = valor_inicial.get()
    valor_decimal = float(binarioDecimal(valor_convertir))
    valor_hexadecimal = binarioHexadecimal(valor_decimal)

    Frame(root, bg="#FFFFFF", width=454, height=35).place(x=23, y=250)
    Frame(root, bg="#FFFFFF", width=454, height=35).place(x=23, y=340)

    Label(root, bg="#FFFFFF", fg="#373B4F", text=valor_decimal, font=("Arial", 18)).place(x=23, y=252)
    Label(root, bg="#FFFFFF", fg="#373B4F", text=valor_hexadecimal, font=("Arial", 18)).place(x=23, y=342)

root = Tk()
root.geometry('500x600')
root.resizable(False, False)
root.title('Transformador de Bases Numericas')

valor_inicial = StringVar()

Frame(root, bg="#373B4F", height=200, width=500).place(x=0, y=0)
Frame(root, bg="#373B4F", height=50, width=500).place(x=0, y=550)
Frame(root, bg="#C7C7C7", height=350, width=500).place(x=0, y=200)
Label(root, text="CONVERSOR DE BASES", font=("Arial", 28), bg="#373B4F", fg="#FFFFFF").place(x=25, y=35)
Label(root, text="NOTA: PARA INGRESAR NUMEROS CON DECIMALES USE PUNTO", font=("Arial", 10), bg="#373B4F", fg="#FFFFFF").place(x=20, y=165)
Label(root, text="Ingrese el numero en binario", font=("Arial", 15), bg="#373B4F", fg="#FFFFFF").place(x=20, y=95)
Entry(root, textvariable=valor_inicial, width=30, font=("Arial", 20), fg="#373B4F").place(x=23, y=127)

Label(root, text="VALOR DECIMAL", font=("Arial", 15), bg="#C7C7C7", fg="#373B4F").place(x=20, y=220)
Frame(root, bg="#FFFFFF", width=454, height=35).place(x=23, y=250)

Label(root, text="VALOR HEXADECIMAL", font=("Arial", 15), bg="#C7C7C7", fg="#373B4F").place(x=20, y=310)
Frame(root, bg="#FFFFFF", width=454, height=35).place(x=23, y=340)

Button(root, bg="#373B4F", fg="#FFFFFF", text="CONVERTIR", command=main, font=("Arial", 15),pady=2).place(x=180, y=400)

root.mainloop()