---
name: omnx-copy-gerar-angulos
description: "Gera e ranqueia ângulos de anúncio (a linha de ataque que muda uma crença do comprador, antes de qualquer headline) a partir do produto, do público e da pesquisa disponível, com nota por critério, prova que falta e ganchos de exemplo. Use quando pedirem 'ângulos de anúncio', 'ângulos para testar', 'por onde atacar esse produto', 'ideias de abordagem para a campanha', 'o que testar no criativo', 'gera ângulos a partir dessa pesquisa'. Entrega uma lista ranqueada com os 3 primeiros testes. Não use para escrever o anúncio, a página ou o e-mail prontos (rita), para montar oferta, preço ou garantia (bento), para ganchos de VSL (otto), nem para pautas e aberturas de conteúdo orgânico (cami)."
---

# Gerar ângulos de anúncio

Um ângulo é um plano para mudar uma crença do comprador: liga um desejo que ele já tem a um motivo crível para acreditar e reduz o principal receio. A headline vem depois. Esta skill entrega a lista de ângulos e a ordem de teste.

## Como falar com a pessoa

Ela pode nunca ter usado IA. No começo da conversa, diga em duas linhas o que você faz. Faça uma pergunta por vez. Explique termo técnico em meia frase (ângulo, gancho, criativo). Nunca peça para ela digitar comando: quem roda o script é você. Termine cada resposta com o próximo passo.

## Quando não usar

| Pedido | Quem resolve |
|---|---|
| Pesquisa de voz do cliente, anúncio, página ou e-mail prontos, checagem de promessa | agente Rita |
| Oferta, preço, bônus, garantia | agente Bento |
| Ganchos e roteiro de VSL | agente Otto |
| Pauta, Reels e frases de abertura orgânicas | agente Cami |

## Passos

1. **Junte o material.** Precisa de: o que é o produto, para quem, o que a pessoa quer resolver, o que já existe de prova (número real, depoimento autorizado, demonstração), restrições (o que não pode ser dito) e concorrentes ou alternativas. Se ela trouxe pesquisa (avaliações, comentários, respostas de clientes), use as palavras dela. Pergunte só o que falta, uma coisa por vez, no máximo quatro perguntas. Sem resposta, siga com o que tem e marque o que ficou em aberto.
2. **Marque a base.** Pesquisa real é fala de cliente, avaliação, comentário ou dado com origem identificável; cite a origem como a pessoa informou. Ângulo que não veio disso é **hipótese**: sem pesquisa nenhuma, todos são; com pesquisa parcial, marque um a um com `"hipotese": true`.
3. **Gere 8 ângulos viáveis** (ou o número pedido) de pelo menos 4 tipos diferentes. Se a pessoa pediu uma promessa que não se sustenta, ela entra como item extra na lista, com a nota real, sem contar nos 8:
   intensificar o problema · mostrar como funciona · comparar com o que já falhou para a pessoa · chamar por identidade · liderar pela prova · ponto de vista contrário ao senso comum · custo escondido · velocidade ou conveniência · reduzir o risco · comparação com os pares · momento ou época do ano.
4. **Dê nota de 1 a 5** em seis critérios:

   | Critério (chave) | 1 | 5 |
   |---|---|---|
   | Força do desejo (`desejo`) | seria bom ter | tira o sono, urgente |
   | Encaixe com o que o público já acredita (`crenca`) | exige outra visão de mundo | ele já quase concorda |
   | Diferença dos concorrentes (`novidade`) | todos dizem igual | ninguém diz |
   | Prova disponível hoje (`prova`) | nenhuma | prova forte em mãos |
   | Segurança da promessa (`seguranca`) | promessa arriscada | fato verificável |
   | Facilidade de mostrar em imagem ou cena (`visual`) | abstrato | dá para filmar |

   `prova` mede a prova **do que o ângulo afirma**: 1 nenhuma, 2 só indício (a dor existe, mas falta mostrar a solução), 3 um caso real ou dado parcial, 4 vários casos, 5 prova forte. Prova que a pessoa não mostrou vale 1. Nos demais critérios, 2 a 4 são graus entre as duas pontas.
5. **Ranqueie por script.** Grave um JSON temporário fora da pasta da skill:
   `{"pesquisa": true, "angulos": [{"nome": "...", "tipo": "...", "notas": {"desejo": 4, "crenca": 3, "novidade": 3, "prova": 2, "seguranca": 5, "visual": 4}}]}`
   e rode `python3 "<pasta desta skill>/scripts/ranquear_angulos.py" <arquivo>`. `<pasta desta skill>` é a pasta onde está este `SKILL.md`. Use a ordem e o `status` que ele devolver; não refaça a conta de cabeça.
6. **Entregue** no formato abaixo e pergunte qual dos três primeiros a pessoa quer levar adiante.

## Regras

- Trabalhe com desejo que já existe. Ângulo que exige que o mercado passe a querer algo novo sai da lista e é trocado por outro.
- Comentário de terceiro serve de pesquisa. Em anúncio, use a ideia como fala geral, nunca como depoimento de alguém.
- Nada de prova, número, depoimento ou resultado inventado. No gancho, escreva `[número real]` ou `[depoimento autorizado]` quando faltar.
- Status `vetado` (segurança até 2): fica fora dos testes, mesmo com nota alta. Sem promessa de ganho financeiro, cura ou resultado garantido, sem urgência falsa.
- Status `precisa_de_prova` (prova até 2): só entra nos testes depois que a pessoa conseguir a prova listada.
- Sem imitar pessoa real e sem ofender quem compra.

## Formato da entrega

Se houve promessa vetada a pedido da pessoa, avise antes da tabela, em duas linhas, com o motivo e a alternativa.

Tabela: posição, ângulo, tipo, total sobre 30, status.

Depois, para cada um dos 3 primeiros com status `testar` (se forem menos, detalhe os que houver e diga qual prova libera o próximo):

- **De onde veio:** o sinal de mercado (trecho de pesquisa com fonte, ou "hipótese").
- **Crença que muda:** de "..." para "...".
- **Por que acreditar:** o mecanismo, ou seja, o motivo crível.
- **Prova:** o que já existe e o que falta.
- **Objeção que trata.**
- **2 ganchos de exemplo** e o formato sugerido (vídeo curto, imagem, carrossel).
- **Risco:** o que pode dar problema com o público ou com a plataforma, como promessa de ganho, tema de saúde ou texto que aponta a situação pessoal de quem lê. Oriente a conferir as regras atuais da plataforma.

Para os demais, uma linha: nome, status, crença que muda e o que falta.

Feche com o próximo passo: qual testar primeiro e o que conseguir antes.

## Se der erro

Se o script apontar nota fora de 1 a 5 ou critério faltando, corrija o JSON e rode de novo. Sem Python na máquina: some à mão, confira duas vezes e avise. Produto sem nenhuma informação: não gere; peça o básico.

## Outro sistema operacional

O script usa só a biblioteca padrão do Python 3. Adapte e conte o que funcionou de verdade:

- **Python:** `python3` (macOS, Linux), `py -3` ou `python` (Windows). Sem Python, não instale nada só para isso.
- **Pasta pessoal:** `~` é `%USERPROFILE%` no Windows. Caminho com espaço vai entre aspas.
- **Arquivo temporário:** use a pasta temporária do sistema (`$TMPDIR`, `/tmp` ou `%TEMP%`).
- **Instalar no Windows:** copie esta pasta para `%USERPROFILE%\.claude\skills\omnx-copy-gerar-angulos`.

## Outra ferramenta (Codex e outras)

Compatível com Claude Code, Codex e outras ferramentas de agentes, em Mac, Windows e Linux. Se a pessoa pedir para instalar
fora do Claude Code, a IA dela adapta na hora, testa no computador dela e conta o que realmente funcionou:
