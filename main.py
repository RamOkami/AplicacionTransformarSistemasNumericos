"""CODIGO CREADO POR RAMSES QUINTANILLA"""
from tkinter import *
from tkinter import messagebox
from tkinter import StringVar

def binarioOctal(valor_convertir):
    res_octal_entero = ""
    res_octal_decimal = ""
    res_octal = ""

    if '.' in valor_convertir:
        valor_completo = valor_convertir.split('.')
        valor_entero = valor_completo[0]
        valor_decimal = valor_completo[1]
    else:
        valor_entero = valor_convertir

    while len(valor_entero) % 3 != 0:
        valor_entero = '0' + valor_entero

    for i in range(0, len(valor_entero), 3):
        grupo = valor_entero[i:i + 3]
        decimal = 0
        for j, bit in enumerate(grupo):
            decimal += int(bit) * (2 ** (2 - j))
        res_octal_entero += str(decimal)

    if '.' in valor_convertir:
        bin_decimal = valor_decimal
        for _ in range(10):
            bin_decimal += '0' * ((3 - len(bin_decimal) % 3) % 3)
            grupo = bin_decimal[:3]
            decimal = int(grupo[0]) * 4 + int(grupo[1]) * 2 + int(grupo[2]) * 1
            res_octal_decimal += str(decimal)
            bin_decimal = bin_decimal[3:]
            if bin_decimal == '' or int(bin_decimal) == 0:
                break
        return f'{res_octal_entero}.{res_octal_decimal}'
    return res_octal_entero

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
    #AGREGAR VERIFICACIONES
    valor_convertir = valor_inicial.get()

    verificador = False
    valores_no_permitidos = ['2', '3', '4', '5', '6', '7', '8', '9']
    for i in valores_no_permitidos:
        if i in valor_convertir:
            verificador = True
            break

    if verificador:
        messagebox.showinfo("ERROR", f'SE HA INTRODUCIDO UN VALOR INVALIDO \nINTRODUCIR SOLO VALORES 0 Y 1')
        return


    valor_decimal = float(binarioDecimal(valor_convertir))
    valor_hexadecimal = binarioHexadecimal(valor_decimal)
    valor_octal = binarioOctal(valor_convertir)

    salida_decimal.config(state="normal")
    salida_hexadecimal.config(state="normal")
    salida_octal.config(state="normal")

    salida_decimal.delete(0, END)
    salida_decimal.insert(0, valor_decimal)

    salida_hexadecimal.delete(0, END)
    salida_hexadecimal.insert(0, valor_hexadecimal)

    salida_octal.delete(0, END)
    salida_octal.insert(0, valor_octal)

    for i in [salida_decimal, salida_hexadecimal, salida_octal]:
        i.config(state="readonly")


root = Tk()
root.geometry('500x600')
root.resizable(False, False)
root.title('Transformador de Bases Numericas')
root.iconbitmap('LogoOkami.ico')
root.config(bg="#C7C7C7")

valor_inicial = StringVar()

Frame(root, bg="#373B4F", height=200, width=500).place(x=0, y=0)
Frame(root, bg="#373B4F", height=50, width=500).place(x=0, y=550)
Label(root, text="CONVERSOR DE BASES", font=("Arial", 28), bg="#373B4F", fg="#FFFFFF").place(x=25, y=35)
Label(root, text="NOTA: PARA INGRESAR NUMEROS CON DECIMALES USE PUNTO", font=("Arial", 10), bg="#373B4F", fg="#FFFFFF").place(x=20, y=165)
Label(root, text="Ingrese el numero en binario", font=("Arial", 15), bg="#373B4F", fg="#FFFFFF").place(x=20, y=95)
Entry(root, textvariable=valor_inicial, width=30, font=("Arial", 20), fg="#373B4F").place(x=23, y=127)

Label(root, text="VALOR DECIMAL", font=("Arial", 15), bg="#C7C7C7", fg="#373B4F").place(x=20, y=220)
salida_decimal = Entry(root, state="readonly", width=30, font=("Arial", 20), fg="#373B4F")
salida_decimal.place(x=23, y=250)

Label(root, text="VALOR HEXADECIMAL", font=("Arial", 15), bg="#C7C7C7", fg="#373B4F").place(x=20, y=310)
salida_hexadecimal = Entry(root, state="readonly", width=30, font=("Arial", 20), fg="#373B4F")
salida_hexadecimal.place(x=23, y=340)

Label(root, text="VALOR OCTAL", font=("Arial", 15), bg="#C7C7C7", fg="#373B4F").place(x=20, y=400)
salida_octal = Entry(root, state="readonly", width=30, font=("Arial", 20), fg="#373B4F")
salida_octal.place(x=23, y=430)

Button(root, bg="#373B4F", fg="#FFFFFF", text="CONVERTIR", command=main, font=("Arial", 15),pady=2).place(x=180, y=490)

root.mainloop()