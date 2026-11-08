# omnx-copy-gerar-angulos

Guia visual: abra o `COMO-FUNCIONA.html` desta pasta (dois cliques; funciona sem internet).

A partir do produto, do público e da pesquisa disponível, gera ângulos de anúncio (a linha de ataque que muda uma crença do comprador, antes de qualquer headline), dá nota por critério e entrega a ordem de teste, com a prova que falta e ganchos de exemplo.

## O que ela não faz

- Não escreve o anúncio pronto, a página ou o e-mail: isso é do agente **Rita**.
- Não monta oferta, preço ou garantia (**Bento**), ganchos de VSL (**Otto**) nem pauta orgânica (**Cami**).
- Não inventa prova: sem pesquisa, cada ângulo sai marcado como hipótese. Promessa arriscada é vetada.

## Como instalar

**Direto do GitHub:** no Claude Code, diga: "Instale a skill a partir de https://github.com/Empire-Business/omnx-copy-gerar-angulos". Para atualizar, diga: "Atualize a skill a partir de https://github.com/Empire-Business/omnx-copy-gerar-angulos". A IA baixa e copia os arquivos.

Se você já baixou esta pasta:

1. Abra o Claude Code (no aplicativo do Claude, aba **Code**, ambiente **Local**).
2. Escreva: **"Instale a skill que está nesta pasta: `<caminho desta pasta>`"**.
3. Você vai ver a IA copiando os arquivos. Não precisa digitar comando nenhum.
4. Abra uma conversa nova e faça um pedido, como nos exemplos abaixo.

### Instalar à mão

- **Mac ou Linux:** rode `bash install.sh` a partir desta pasta. A skill é copiada para `~/.claude/skills/omnx-copy-gerar-angulos`.
- **Windows:** copie esta pasta para `%USERPROFILE%\.claude\skills\omnx-copy-gerar-angulos`, ou peça para a IA fazer isso. O `install.sh` não é usado no Windows.
- Funciona em Mac, Windows e Linux, no Claude Code e no Codex. Na instalação, a própria IA faz as adaptações necessárias para o seu computador.

Funciona em Mac, Windows e Linux, no Claude Code e no Codex. Na instalação, a própria IA faz as adaptações necessárias para o seu computador.

## Como pedir

- "Gera ângulos de anúncio para o meu curso, com base nesse material."
- "Por onde eu ataco esse produto? Quero testar 3 caminhos."
- "O que testar no criativo dessa campanha?"

## O que tem na pasta

| Arquivo | Para que serve |
|---|---|
| `SKILL.md` | o passo a passo que a IA segue |
| `scripts/ranquear_angulos.py` | soma as notas, aplica os vetos e ordena; só lê |
| `COMO-FUNCIONA.html` | guia visual |
| `install.sh` | instalação no Mac ou Linux |

## Versões

- 1.0 (08/11/2026): primeira versão.
