# Python Insights - Analisando Dados com Python

Este repositório contém um case de estudo para analise de dados desenvolvido em Python com base em uma aula do Intensivo de Python oferecido pela [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/). 

<br>

Também deixei anotações pessoais no código a fins de estudo e referência.

<hr>

### Case - Cancelamento de Clientes

Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.

Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.

<hr>

## Passo a Passo

O projeto está dividido em etapas para facilitar a compreensão e a execução:

1. **Importar a Base de Dados**: Importe a base de dados fornecida.
2. **Visualizar a Base de Dados**: Visualize as primeiras linhas da tabela.
3. **Corrigir a Base de Dados**: Limpe os dados, removendo colunas desnecessárias e linhas com valores vazios.
4. **Primeira Análise do Cancelamento dos Clientes**: Observe a taxa de cancelamento dos clientes.
5. **Análise das Causas do Cancelamento dos Clientes**: Analise a duração dos contratos e agrupe informações relevantes.
6. **Motivos dos Cancelamentos**: Identifique os principais motivos para o cancelamento dos clientes.

<hr>

## Tecnologias Utilizadas

- Python
- Pandas
- Plotly (para criar os gráficos)
- Extesão do VsCode -> Jupyter

<hr>

## Configuração do Ambiente Virtual

Antes de executar o script, siga estas etapas:

1. **Clone este repositório:**
   
   ```bash
   git clone git@github.com:ThiagoKalac/Python_Learning_Hub.git

2. **Navegue até o diretório da aula:**
     ```bash
     cd Python_Learning_Hub/analise_dados 
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