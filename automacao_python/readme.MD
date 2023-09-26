# Automação de Cadastro de Produtos

Este repositório contém um script de automação desenvolvido para realizar o cadastro de produtos em um sistema empresarial. O script segue um conjunto específico de passos para efetuar o cadastro de produtos em massa, com base no layout dessa empresa ficticia. 

<hr>

## Créditos e Anotações

Este código foi desenvolvido com base em uma aula do Intensivo de Python oferecido pela [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/). Também deixei anotações pessoais no código a fins de estudo e referência.

<hr>

## Passos do Projeto

O projeto consiste nos seguintes passos:

1. **Entrar no sistema da empresa:**
   - URL: [https://dlp.hashtagtreinamentos.com/python/intensivao/login](https://dlp.hashtagtreinamentos.com/python/intensivao/login)

2. **Fazer login:**
   - Preencher o e-mail e a senha e efetuar o login no sistema.

3. **Importar a base de produtos:**
   - Carregar a base de dados de produtos a serem cadastrados a partir de um arquivo CSV.

4. **Cadastrar 1 produto:**
   - Realizar o cadastro de um produto na plataforma.

5. **Repetir o cadastro para todos os produtos:**
   - Automatizar o processo de cadastro para todos os produtos listados no arquivo CSV.

<hr>

## Comandos Principais do PyAutoGUI

Este script utiliza a biblioteca PyAutoGUI para realizar a automação. Abaixo estão os principais comandos PyAutoGUI usados:

- `pyautogui.write`: Escrever um texto.
- `pyautogui.press`: Pressionar uma tecla.
- `pyautogui.click`: Clicar em alguma parte da tela.
- `pyautogui.hotkey`: Combinação de teclas.
- `pyautogui.position()`: Pegar a posição do mouse na tela (útil com `time.sleep` e `print`).
- `pyautogui.scroll(5000)`: Controlar o scroll do mouse (números positivos para cima, números negativos para baixo).

<hr>

## Configuração do Ambiente Virtual

Antes de executar o script, siga estas etapas:

1. **Clone este repositório:**
   
   ```bash
   git clone git@github.com:ThiagoKalac/Python_Learning_Hub.git

2. **Navegue até o diretório da aula:**
     ```bash
     cd Python_Learning_Hub/automacao_python 
     ```
3. **Crie e ative um ambiente virtual (recomendado):**
     ```bash
     python -m venv venv 
     source venv/bin/activate  # No Windows: venv\Scripts\activate
     ```
4. **Instale as dependências Python:**
     ```bash
     pip install -r requirements.txt
     ```
5. **Execute o script:**
     ```bash
     python main.py
     ```
     
