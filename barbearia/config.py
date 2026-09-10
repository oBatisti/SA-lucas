# config.py
# Credenciais de acesso ao banco de dados MySQL.
# Centralizadas aqui para facilitar a manutencao e a troca de ambiente.

CONFIG_BD = {
    "host": "localhost",      # endereco do servidor MySQL
    "user": "root",           # usuario do MySQL Workbench
    "password": "root",           # senha do usuario (padrao vazio no Workbench)
    "database": "barbearia"   # nome do banco criado pelo banco.sql
}
