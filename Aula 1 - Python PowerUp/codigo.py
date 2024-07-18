# pip install pyautogui
# pip install pandas openpyxl numpy

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - combinação de teclas (Ctrl + C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

# configuração de tempo de espera após cada comando pyautogui
pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no sistema
# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # faz a pausa de 3s apenas nesse lugar

# Passo 2 - Fazer login
pyautogui.click(x=4760, y=615)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("teste@teste.com")

time.sleep(3)

pyautogui.press("tab")
pyautogui.write("sdfsdf")
pyautogui.click(x=4740, y=848)

time.sleep(3)

# Passo 3 - Importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - Cadastrar o produto

for linha in tabela.index:

    # codigo
    pyautogui.click(x=4709, y=446)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo) # ou pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # preco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "custo"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    # botão de enviar
    pyautogui.press("enter")

    # voltar tela pro topo
    pyautogui.scroll(5000)

# Passo 5 - Repetir até acabar a lista de produtos
