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
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template


@bp.route("/dashboard") # cria uma rota para navegador http://127.0.0.1:5000/dashboard
def dashboard(): # função que gerencia rota deve ser única
    """ Painel de vendas"""
    # remova o login
    import locale
    # define a localização para portugues brasileiro 
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    vendas : list = [
         {"mes" :"janeiro", "total":139519.19 },
         {"mes" :"fevereiro", "total":149519.19 },
         {"mes" :"Março", "total":159519.19 },
         {"mes" :"abril", "total":169519.19 },
         {"mes" :"maio", "total":179519.19 },
         {"mes" :"junho", "total":189519.19 },
         {"mes" :"julho", "total":199519.19 },           
         {"mes" :"agosto", "total":20519.19 },
         {"mes" :"setembro", "total":219519.19 },
         {"mes" :"outubro", "total":229519.19 },
         {"mes" :"novembro", "total":239519.19 },
         {"mes" :"dezembro", "total":249519.19 },
    ] #fim lista vendas           

    return render_template("dashboard/index.html" , title="Painel de vendas", vendas=vendas, locale=locale) # Renderiza um template