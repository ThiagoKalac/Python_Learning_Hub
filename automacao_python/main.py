"""
     Passo a passo para o projeto.
     Passo 1: Entrar no sistema da empresa
          url: https://dlp.hashtagtreinamentos.com/python/intensivao/login
     Passo 2: Fazer login
     Passo 3: Importar a base de produtos
     Passo 4: Cdastrar 1 produto
     Passo 5: Repetir o cadastro para todos produtos

"""
# --- Comandos principais do pyautogui ---
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# pyautogui.position() -> pegar posição do mouse na tela  | macete é usar com o time.sleep mais o print.
""" 
     time.sleep(5) 
     print(pyautogui.position())
"""
# pyautogui.scroll(5000) -> controlar o scroll do mouse, numeros positivos fazem a barra subir e negativos fazem ela baixar 

import pyautogui
import pandas
import time

pyautogui.PAUSE = 1 # Comando para o gerar 1 segundo para execusão de um comando e outro do pyautogui

# 1 - Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# 2 - Entrar no site 
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# 3 - Esperar site carregar
time.sleep(3) # lib interna do python intera para controle de tempo.

# 4 - Fazer Login
pyautogui.click(x=1076, y=403)
pyautogui.write('thiago@mail.com')
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('enter')

# 5  - Esperar o login do sistema

time.sleep(3)

# 6 - Import "base de dados" de produtos

tabela = pandas.read_csv("produtos.csv") #está lendo o arquivo em excell.

# 7 - Repetir a tarefa de execussão da tarefa de cadastro 

for linha_tabela in range(len(tabela)):
     
     pyautogui.click(x=1017, y=280)

     # tabela.loc[linha_tabela, coluna] 
     # dentro da tabela ele localiza a linha (numero) e a coluna (nome/str) o nome precisa estar exatamete igual está na tabela.
     codigo_produto = tabela.loc[linha_tabela, "codigo"]  
     marca_produto = tabela.loc[linha_tabela, "marca"]
     tipo_produto = tabela.loc[linha_tabela, "tipo"]
     categoria_produto = tabela.loc[linha_tabela, "categoria"]
     preco_unitario_produto = tabela.loc[linha_tabela, "preco_unitario"]
     custo_produto = tabela.loc[linha_tabela, "custo"]
     observacao_produto = tabela.loc[linha_tabela, "obs"]

     # preenchendo os campos
     pyautogui.write(str(codigo_produto))
     pyautogui.press('tab')
     pyautogui.write(str(marca_produto))
     pyautogui.press('tab')
     pyautogui.write(str(tipo_produto))
     pyautogui.press('tab')
     pyautogui.write(str(categoria_produto))
     pyautogui.press('tab')
     pyautogui.write(str(preco_unitario_produto))
     pyautogui.press('tab')
     pyautogui.write(str(custo_produto))
     pyautogui.press('tab')
     
     if not pandas.isna(observacao_produto):
          pyautogui.write(str(observacao_produto))
          
     pyautogui.press('tab')
     pyautogui.press('enter')

     pyautogui.scroll(5000)










