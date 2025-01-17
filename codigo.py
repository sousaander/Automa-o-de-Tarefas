import pyautogui
import pandas as pd 
import time

pyautogui.PAUSE = 0.5

# Passo 1: Abrir o sistema da empresa

# abrir o google chrome
# apertar a tecla win
pyautogui.press("win")

# digitar o texto microsoft edge 
pyautogui.write("microsoft edge")

# apertar enter
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")



# pedir pro computador esperar 3 sgundos
time.sleep(3)

# Passo 2: Fazer Login
pyautogui.click(x=167, y=468)
pyautogui.write("sousaander@gmail.com")

pyautogui.press("tab")
pyautogui.write("minha senha aqui")


pyautogui.press("tab") #
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)
# Passo 4: Cadastrar 1 produto

for linha in tabela.index:
    pyautogui.click(x=148, y=334) # clicsr no 1º campo

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"] 
    pyautogui.write(marca)
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # str -> string = texto
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")  
    
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")

    pyautogui.press("enter") #apertar o btao de enviar

    # numero positivo = scroll para cima
    # numero negativo = scroll para baixo
    pyautogui.scroll(10000)
    
    # Passo 5: Repetir o passo 4 até acabar todos os produtos