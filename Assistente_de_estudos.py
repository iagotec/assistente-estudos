import json
from pathlib import Path

ARQUIVO_DADOS = Path("conteudos.json")


def carregar_conteudos():
    if not ARQUIVO_DADOS.exists():
        return []
    
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_conteudos(conteudos):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(conteudos, f, indent=4, ensure_ascii=False)


def adicionar_conteudo(titulo, texto):
    conteudos = carregar_conteudos()

    conteudo = {
        "titulo": titulo,
        "texto": texto
    }

    conteudos.append(conteudo)
    salvar_conteudos(conteudos)


def listar_conteudos():
    conteudos = carregar_conteudos()

    for i, c in enumerate(conteudos, start=1):
        print(f"{i}. {c['titulo']}")


def buscar_conteudo(palavra):
    conteudos = carregar_conteudos()
    resultados = []

    for c in conteudos:
        if palavra.lower() in c["texto"].lower():
            resultados.append(c)

    return resultados
