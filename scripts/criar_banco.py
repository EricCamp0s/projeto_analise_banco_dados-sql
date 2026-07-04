"""
Executar Consultas SQL - Versão Simplificada
Autor: Eric Campos Teixeira
"""

import sqlite3
import pandas as pd
import os

print("=" * 50)
print("🚀 EXECUTANDO CONSULTAS SQL")
print("=" * 50)

# ============================================================
# CONFIGURAÇÕES
# ============================================================

# Caminhos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.dirname(SCRIPT_DIR)

PASTA_DATABASE = os.path.join(PROJETO_DIR, 'database', '')
PASTA_OUTPUTS = os.path.join(PROJETO_DIR, 'outputs', '')
CAMINHO_DB = os.path.join(PASTA_DATABASE, 'vendas.db')

# Criar pasta outputs se não existir
os.makedirs(PASTA_OUTPUTS, exist_ok=True)

print(f"📁 Banco: {CAMINHO_DB}")
print(f"📁 Outputs: {PASTA_OUTPUTS}")

# Verificar se o banco existe
if not os.path.exists(CAMINHO_DB):
    print(f"❌ ERRO: Banco de dados não encontrado em: {CAMINHO_DB}")
    print("   Execute primeiro: python scripts/criar_banco.py")
    exit()

# ============================================================
# CONSULTAS SQL (diretamente no código)
# ============================================================

consultas = [
    {
        'nome': 'consulta_01_vendas_por_filial',
        'descricao': 'Total de vendas por filial',
        'sql': '''
            SELECT 
                branch,
                SUM(total_price) AS total_vendas,
                COUNT(*) AS total_transacoes,
                AVG(total_price) AS ticket_medio
            FROM vendas
            GROUP BY branch
            ORDER BY total_vendas DESC
        '''
    },
    {
        'nome': 'consulta_02_vendas_por_cidade',
        'descricao': 'Total de vendas por cidade',
        'sql': '''
            SELECT 
                city,
                SUM(total_price) AS total_vendas,
                COUNT(*) AS total_transacoes
            FROM vendas
            GROUP BY city
            ORDER BY total_vendas DESC
        '''
    },
    {
        'nome': 'consulta_03_top_10_produtos',
        'descricao': 'Top 10 produtos mais vendidos por faturamento',
        'sql': '''
            SELECT 
                product_name,
                product_category,
                SUM(quantity) AS total_quantidade,
                SUM(total_price) AS total_vendas
            FROM vendas
            GROUP BY product_name
            ORDER BY total_vendas DESC
            LIMIT 10
        '''
    },
    {
        'nome': 'consulta_04_top_10_categorias',
        'descricao': 'Top 10 categorias por faturamento',
        'sql': '''
            SELECT 
                product_category,
                SUM(total_price) AS total_vendas,
                COUNT(*) AS total_transacoes,
                AVG(unit_price) AS preco_medio
            FROM vendas
            GROUP BY product_category
            ORDER BY total_vendas DESC
            LIMIT 10
        '''
    },
    {
        'nome': 'consulta_05_membros_vs_normais',
        'descricao': 'Comparação Membros vs Normais',
        'sql': '''
            SELECT 
                customer_type,
                COUNT(*) AS total_transacoes,
                SUM(total_price) AS total_vendas,
                AVG(total_price) AS ticket_medio,
                SUM(quantity) AS total_quantidade
            FROM vendas
            GROUP BY customer_type
        '''
    },
    {
        'nome': 'consulta_06_analise_por_genero',
        'descricao': 'Análise por Gênero',
        'sql': '''
            SELECT 
                gender,
                COUNT(*) AS total_transacoes,
                SUM(total_price) AS total_vendas,
                AVG(total_price) AS ticket_medio,
                SUM(quantity) AS total_quantidade
            FROM vendas
            GROUP BY gender
        '''
    },
    {
        'nome': 'consulta_07_ticket_medio_por_categoria',
        'descricao': 'Ticket médio por categoria',
        'sql': '''
            SELECT 
                product_category,
                AVG(total_price) AS ticket_medio,
                MIN(total_price) AS ticket_minimo,
                MAX(total_price) AS ticket_maximo,
                COUNT(*) AS total_transacoes
            FROM vendas
            GROUP BY product_category
            ORDER BY ticket_medio DESC
        '''
    },
    {
        'nome': 'consulta_08_top_10_reward_points',
        'descricao': 'Produtos que mais geraram pontos de recompensa',
        'sql': '''
            SELECT 
                product_name,
                product_category,
                SUM(reward_points) AS total_pontos,
                AVG(reward_points) AS pontos_medios,
                COUNT(*) AS total_transacoes
            FROM vendas
            WHERE reward_points > 0
            GROUP BY product_name
            ORDER BY total_pontos DESC
            LIMIT 10
        '''
    },
    {
        'nome': 'consulta_09_preco_por_categoria',
        'descricao': 'Análise de preço por categoria',
        'sql': '''
            SELECT 
                product_category,
                COUNT(*) AS total_produtos,
                MIN(unit_price) AS preco_minimo,
                MAX(unit_price) AS preco_maximo,
                ROUND(AVG(unit_price), 2) AS preco_medio
            FROM vendas
            GROUP BY product_category
            ORDER BY preco_medio DESC
        '''
    },
    {
        'nome': 'consulta_10_faixa_preco',
        'descricao': 'Distribuição de vendas por faixa de preço',
        'sql': '''
            SELECT 
                CASE 
                    WHEN unit_price < 5 THEN 'Baixo (até R$5)'
                    WHEN unit_price < 15 THEN 'Médio (R$5-R$15)'
                    ELSE 'Alto (acima de R$15)'
                END AS faixa_preco,
                COUNT(*) AS total_transacoes,
                SUM(total_price) AS total_vendas,
                AVG(total_price) AS ticket_medio
            FROM vendas
            GROUP BY faixa_preco
            ORDER BY total_vendas DESC
        '''
    }
]

# ============================================================
# EXECUTAR CONSULTAS
# ============================================================

print(f"\n📝 {len(consultas)} consultas para executar")
print("-" * 50)

# Conectar ao banco
conn = sqlite3.connect(CAMINHO_DB)

for i, consulta in enumerate(consultas, 1):
    try:
        print(f"\n📊 {i}. {consulta['descricao']}")
        
        # Executar consulta
        df = pd.read_sql_query(consulta['sql'], conn)
        
        # Salvar CSV
        caminho_csv = os.path.join(PASTA_OUTPUTS, f"{consulta['nome']}.csv")
        df.to_csv(caminho_csv, index=False, encoding='utf-8-sig')
        
        print(f"   ✅ {len(df)} registros salvos em: {consulta['nome']}.csv")
        
    except Exception as e:
        print(f"   ❌ ERRO: {e}")

# Fechar conexão
conn.close()

# ============================================================
# RESUMO FINAL
# ============================================================

print("\n" + "=" * 50)
print("✅ EXECUÇÃO CONCLUÍDA!")
print("=" * 50)

# Listar arquivos gerados
print("\n📁 Arquivos gerados em:", PASTA_OUTPUTS)

try:
    arquivos = os.listdir(PASTA_OUTPUTS)
    if arquivos:
        for arquivo in sorted(arquivos):
            print(f"   - {arquivo}")
    else:
        print("   ❌ Nenhum arquivo encontrado!")
except Exception as e:
    print(f"   ❌ Erro ao listar arquivos: {e}")