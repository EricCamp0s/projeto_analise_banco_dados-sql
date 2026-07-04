# 🗄️ Análise de Dados com SQL

![SQL](https://img.shields.io/badge/SQL-SQLite-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)

## 🎯 Objetivo do Projeto

Este projeto demonstra habilidades em **SQL** para análise de dados, utilizando um banco de dados SQLite com dados de vendas. O objetivo é responder perguntas de negócio através de consultas analíticas.

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Finalidade |
|------------|------------|
| **SQLite** | Banco de dados relacional |
| **Python** | Conexão e automação |
| **SQL** | Consultas analíticas |
| **Pandas** | Manipulação de resultados |

## 📁 Estrutura do Repositório


## 📊 Consultas SQL Criadas

| Consulta | Pergunta de Negócio |
|----------|---------------------|
| 01 | Qual filial vende mais? |
| 02 | Qual cidade tem maior faturamento? |
| 03 | Quais produtos geram mais receita? |
| 04 | Quais categorias são mais lucrativas? |
| 05 | Membros compram mais que clientes normais? |
| 06 | Homens ou mulheres compram mais? |
| 07 | Quais categorias tem os maiores tickets? |
| 08 | Quais produtos geram mais pontos de recompensa? |
| 09 | Qual é a distribuição de preços por categoria? |
| 10 | Como as vendas se distribuem por faixa de preço? |

## 🔍 Como Reproduzir o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/[SEU-USUARIO]/projeto3-analise-sql.git
cd projeto3-analise-sql

## 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows

## 3. Instale as dependências
```bash
pip install -r requirements.txt

## 4. Crie o banco de dados
```bash
python scripts/criar_banco.py

## 5. Execute as consultas
```bash
python scripts/executar_consultas.py

## 6. Veja os resultados
Os arquivos CSV estarão na pasta outputs/.

## 7. Para consultar resultados direto no terminal
No seu terminal digite 
```bash 
type outputs\o_nome_do_arquivo_que_quer.csv