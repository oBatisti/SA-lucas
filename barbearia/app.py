# app.py
# Aplicacao Flask do sistema de agendamentos da Barbearia Navalha de Ouro.
# Executar pela raiz: python main.py  e acessar http://127.0.0.1:5000

from flask import Flask, render_template  # micro-framework web e renderizador de templates

from .agendamentos import (listar_agendamentos, buscar_agendamento, listar_por_status)

app = Flask(__name__)  # cria a aplicacao Flask


@app.route("/")  # rota da pagina inicial
def inicio():
    agendamentos = listar_agendamentos()      # busca todos os agendamentos
    return render_template("index.html", agendamentos=agendamentos)


@app.route("/agendamentos")  # rota da listagem completa
def agendamentos():
    lista = listar_agendamentos()
    return render_template("agendamentos.html", agendamentos=lista)


@app.route("/agendamentos/status/<status>")  # rota com filtro por status
def agendamentos_por_status(status):
    lista = listar_por_status(status)         # filtra por Agendado/Concluido/Cancelado
    return render_template("agendamentos.html", agendamentos=lista, status=status)


@app.route("/agendamento/<int:id>")  # rota do detalhe de um agendamento
def detalhe(id):
    agendamento = buscar_agendamento(id)      # retorna o objeto ou None
    return render_template("detalhe.html", agendamento=agendamento)


if __name__ == "__main__":
    app.run(debug=True)  # permite executar este arquivo dentro do pacote
