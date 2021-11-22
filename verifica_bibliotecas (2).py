"""
Esse script instala as bibliotecas que iremos utilizar nos próximos exemplos.
Obs: requer conexão com a Internet!!!!
"""

import pip

def import_or_install(pac):
    try:
        __import__(pac)
    except ImportError:
        pip.main(['install', pac])    

bibliotecas = ["dash", "dash_core_components", "dash_html_components", "dash_bootstrap_components",
               "dash_table", "express", "numpy"]


for b in bibliotecas:
    import_or_install(b)

print("Bibliotecas instaladas")