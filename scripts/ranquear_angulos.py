#!/usr/bin/env python3
"""Soma as notas dos ângulos, aplica as regras de veto e imprime o ranking em JSON.

Uso: ranquear_angulos.py <arquivo.json>

Entrada: {"pesquisa": true, "angulos": [{"nome": "...", "tipo": "...", "hipotese": false, "notas": {...}}]}
"hipotese" é opcional: marca um ângulo que não veio da pesquisa, mesmo quando há pesquisa.
Critérios: desejo, crenca, novidade, prova, seguranca, visual (1 a 5).
Biblioteca padrão do Python 3.8 em diante. Só lê.
"""
import json
import sys
from pathlib import Path

CRITERIOS = ("desejo", "crenca", "novidade", "prova", "seguranca", "visual")
MINIMO_DE_TIPOS = 4


def imprimir(dados):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(dados, ensure_ascii=False, indent=2))


def validar(dados):
    erros = []
    angulos = dados.get("angulos") if isinstance(dados, dict) else None
    if not isinstance(angulos, list) or not angulos:
        return ["O arquivo precisa ter uma lista 'angulos' com pelo menos um item."]
    if "pesquisa" in dados and not isinstance(dados["pesquisa"], bool):
        erros.append("'pesquisa' deve ser true ou false.")
    vistos = set()
    for i, a in enumerate(angulos, 1):
        nome = a.get("nome") if isinstance(a, dict) else None
        rotulo = nome if isinstance(nome, str) and nome.strip() else "item %d" % i
        if not isinstance(nome, str) or not nome.strip():
            erros.append("%s: falta 'nome' em texto." % rotulo)
        elif nome.casefold() in vistos:
            erros.append("%s: nome repetido." % rotulo)
        else:
            vistos.add(nome.casefold())
        if not isinstance(a, dict) or not isinstance(a.get("tipo"), str) or not a["tipo"].strip():
            erros.append("%s: falta 'tipo' em texto." % rotulo)
        if isinstance(a, dict) and "hipotese" in a and not isinstance(a["hipotese"], bool):
            erros.append("%s: 'hipotese' deve ser true ou false." % rotulo)
        notas = a.get("notas") if isinstance(a, dict) else None
        if not isinstance(notas, dict):
            erros.append("%s: falta 'notas'." % rotulo)
            continue
        for c in CRITERIOS:
            v = notas.get(c)
            if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 5:
                erros.append("%s: nota '%s' deve ser inteira de 1 a 5 (veio %r)." % (rotulo, c, v))
    return erros


def status_de(notas):
    if notas["seguranca"] <= 2:
        return "vetado"
    if notas["prova"] <= 2:
        return "precisa_de_prova"
    return "testar"


def ranquear(dados):
    com_pesquisa = dados.get("pesquisa") is True
    itens = []
    for a in dados["angulos"]:
        n = a["notas"]
        itens.append({
            "nome": a["nome"],
            "tipo": a["tipo"],
            "total": sum(n[c] for c in CRITERIOS),
            "status": status_de(n),
            "base": "pesquisa" if com_pesquisa and not a.get("hipotese") else "hipotese",
            "notas": {c: n[c] for c in CRITERIOS},
        })
    ordem = {"testar": 0, "precisa_de_prova": 1, "vetado": 2}
    itens.sort(key=lambda x: (ordem[x["status"]], -x["total"], -x["notas"]["prova"], -x["notas"]["desejo"], x["nome"].casefold()))
    for pos, item in enumerate(itens, 1):
        item["posicao"] = pos
    tipos = {" ".join(i["tipo"].split()).casefold() for i in itens}
    avisos = []
    if len(itens) >= MINIMO_DE_TIPOS and len(tipos) < MINIMO_DE_TIPOS:
        avisos.append("Pouca variedade: %d tipos diferentes; o mínimo é %d." % (len(tipos), MINIMO_DE_TIPOS))
    if not com_pesquisa:
        avisos.append("Sem pesquisa real: todos os ângulos são hipótese.")
    if not any(i["status"] == "testar" for i in itens):
        avisos.append("Nenhum ângulo pronto para teste: consiga a prova listada ou reescreva.")
    elif sum(i["status"] == "testar" for i in itens) < 3:
        avisos.append("Menos de 3 ângulos prontos para teste.")
    return {
        "maximo": len(CRITERIOS) * 5,
        "total_de_angulos": len(itens),
        "tipos_diferentes": len(tipos),
        "contagem_por_status": {s: sum(i["status"] == s for i in itens) for s in ordem},
        "avisos": avisos,
        "ranking": itens,
    }


def main():
    if len(sys.argv) != 2:
        imprimir({"erro": "Uso: ranquear_angulos.py <arquivo.json>"})
        return 2
    try:
        dados = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    except OSError as e:
        imprimir({"erro": "Não consegui ler o arquivo: %s" % e})
        return 2
    except ValueError as e:
        imprimir({"erro": "O arquivo não é um JSON válido: %s" % e})
        return 2
    erros = validar(dados)
    if erros:
        imprimir({"erro": "Corrija os itens antes de ranquear.", "problemas": erros})
        return 2
    imprimir(ranquear(dados))
    return 0


if __name__ == "__main__":
    sys.exit(main())
