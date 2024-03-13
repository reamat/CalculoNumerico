import sys
import os
import re

def casa_brackets(text, sub=b"{"):
    if sub not in text or b"}" not in text :
        return -1, -1
    pos_ini = text.find(sub) + len(sub) - 1
    pos = pos_ini+1
    count = 1
    while count > 0 and pos < len(text):
        # print(pos, text[pos], count)
        if text[pos] in b'{':
            count += 1
        elif text[pos] in b'}':
            count -= 1
        pos += 1
    return pos_ini, pos


def limpa_isif(texto, tipo=b'py'):
    tags = [rb"isoctave", rb"ispython", rb"isscilab", rb"ishtml"]
    
    expr = rb"\\if(" + b"|".join([t for t in tags if tipo not in t]) + rb").*?\\fi\b" 

    res = re.split(expr, texto, flags=re.DOTALL|re.MULTILINE)
    novo_texto = b"".join([r for i, r in enumerate(res) if i %2 == 0])
    return novo_texto


def extrai_exercicios(arq, exer, exeresol, exemplo, tipo):
    texto = b""

    blocos = ([rb"exer", rb"resp"] if exer else [])\
           + ([rb"exeresol", rb"resol"] if exeresol else [])\
           + ([rb"ex"] if exemplo else [])
    aberturas = [rb"\begin{" + l + rb"}" for l in blocos]
    fechamentos = [rb"\end{" + l + rb"}" for l in blocos]
    tags = [rb"\chapter{", rb"\section{", rb"\subsection{"]
    contagem = 0
    dentro_de_bloco = False
    with open(arq, 'rb') as f: 
        texto_cru = limpa_isif(f.read(), tipo)
    #    texto_cru = f.read()
        for i, linha in enumerate(texto_cru.splitlines()):
            if linha.startswith(b"%"):
                continue
            linha += b"\n"

            if any([s in linha for s in tags]):
                texto += linha

            if any([s in linha for s in aberturas]):
                dentro_de_bloco = True
                contagem = contagem + 1

            if dentro_de_bloco:
                if linha.strip() != b'':
                    texto += linha
            else:  
                pass
                # texto += lida_com_if(linha, i) 
                    

            if any([s in linha for s in fechamentos]):
                dentro_de_bloco = False
    
    if contagem == 0:
        print("0000", arq)
        if rb"\chapter{" in texto:
            texto = rb"\addtocounter{chapter}{1}"
            contagem = 1
            
    # return contagem, texto.decode() if contagem > 0 else ""
    return contagem, limpa_secoes_vazias(texto.decode()) if contagem > 0 else ""


def abre_arquivos(receita, tipo):
    texto = ""
    with open("main.tex", "rb") as f:
        for linha in f.readlines():
            if linha.strip()[0:9] == rb"\include{":
                s, e = casa_brackets(linha)
                arq = linha[s+1 : e-1].decode() + ".tex"
                print(r"%Extraindo de " + arq)
                texto = texto + r"%%%% Extraído de " + arq + "\n"
                contagem, conteudo = extrai_exercicios(arq, *receita, tipo)
                texto = texto + conteudo
    return texto


def limpa_secoes_vazias(texto):
    ltags = [r"\subsection", r"\section", r"\chapter", r"%%%% Extraído de"]
    for n in range(2):
        tag = ltags[n]
        tags = ltags[n:]
        linhas = texto.splitlines() + [""]
        
        texto = ""
        for i, linha in enumerate(linhas):
            if (tag in linha and all(t not in linhas[i+1] for t in tags) and linhas[i+1] != "") or tag not in linha:
                texto += "\n" + linha
            elif tag in linha:
                texto += r"\stepcounter{" + tag[1:] + r"}"
                print("Seção vazia")

    return texto.strip()
        


### main
cabecalho = r"""\documentclass[10pt]{book}
\input preambulo.tex
%\setlength{\headheight}{30pt}
\geometry{a4paper, total={170mm, 257mm}, left=20mm, top=20mm, textwidth=170mm}
\pagestyle{plain}
\usepackage{xr}
\externaldocument{main}
\begin{document}"""

if len(sys.argv) < 2:
    tipo = "sci"
else:
    tipo = sys.argv[1]

receitas = [(f"exercicios_resolvidos-{tipo}.tex",         (False, True,  False)),
            (f"exercicios-{tipo}.tex",                    (True,  False, False)),
            (f"exercicios_todos-{tipo}.tex",              (True,  True,  False)),
#            ("exercicios_todos_com_exemplos.tex", (True,  True,  True ))
]

tipo = tipo.encode()
for arq, receita in receitas:
    if receita[0] or receita[2]:
        rodape = r"\include{respostas}" + '\n' + r"\end{document}"
    else:
        rodape = r"\end{document}"

    texto = cabecalho + abre_arquivos(receita, tipo) + rodape
    with open(arq, "w") as f:
        f.write(texto)

# print(texto)
