# banco.py
# Responsavel por abrir a conexao com o MySQL usando as credenciais do config.py.

import mysql.connector  # biblioteca oficial do conector MySQL para Python

from .config import CONFIG_BD  # importa as credenciais centralizadas


def conectar():
    """Abre e retorna uma conexao com o banco de dados da barbearia."""
    conexao = mysql.connector.connect(**CONFIG_BD)  # conecta com as credenciais
    return conexao
