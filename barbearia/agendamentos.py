# agendamentos.py
import mysql.connector

from .banco import conectar
from .models import Agendamento


def listar_agendamentos():
    """Retorna a lista de objetos Agendamento, ordenados por data e horario."""
    conexao = None
    cursor = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM agendamentos ORDER BY data, horario"
        cursor.execute(sql)
        lista = []
        for tupla in cursor.fetchall():
            lista.append(Agendamento.reverte_tupla(tupla))
        return lista
    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos: {erro}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def buscar_agendamento(id):
    """Retorna um objeto Agendamento pelo id, ou None se nao existir."""
    conexao = None
    cursor = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM agendamentos WHERE id = %s"
        cursor.execute(sql, (id,))
        tupla = cursor.fetchone()
        if tupla:
            return Agendamento.reverte_tupla(tupla)
        return None
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar agendamento: {erro}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def listar_por_status(status):
    """Retorna os agendamentos que possuem um status especifico."""
    conexao = None
    cursor = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM agendamentos WHERE status = %s ORDER BY data, horario"
        cursor.execute(sql, (status,))
        lista = []
        for tupla in cursor.fetchall():
            lista.append(Agendamento.reverte_tupla(tupla))
        return lista
    except mysql.connector.Error as erro:
        print(f"Erro ao listar por status: {erro}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
