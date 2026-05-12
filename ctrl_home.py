"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if 'user_id' not in session:
         return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template
    
@bp.route("/dashboard") # cria uma rota para navegador http://127.0.0.1:5000/dashboard
def dashboard(): # função que gerencia rota
    """ Painel de vendas"""
    #remova o login
    
    vendas: list = [
        {"mes":"Janeiro", "valortotal" :139519.19},
        {"mes":"Fevereiro", "valortotal" :149629.18},
        {"mes":"Março", "valortotal" :159989.16},
        {"mes":"Abril", "valortotal" :169419.19},
        {"mes":"Maio", "valortotal" :179599.17},
        {"mes":"Junho", "valortotal" :189439.19},
        {"mes":"Julho", "valortotal" :199519.20},
        {"mes":"Agosto", "valortotal" :239329.17},
        {"mes":"Setembro", "valortotal" :249509.19},
        {"mes":"Outubro", "valortotal" :259539.18},
        {"mes":"Novembro", "valortotal" :269710.19},
        {"mes":"Dezembro", "valortotal" :279815.20},


    ] #fim lista vendas
    
    return render_template("dashboard/index.html", title="Painel de Vendas", vendas=vendas) # Renderiza um template