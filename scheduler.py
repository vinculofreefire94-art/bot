import time
import threading
import telebot
import os
import random

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

GRUPO_ID = -1003796977029

# 📚 BANCO DE AULAS PROFISSIONAIS
AULAS = [
    # AULA 1: RSI - Fundamentos
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 AULA #1: RSI - O INDICADOR DECISIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 O que é RSI (Índice de Força Relativa)?

O RSI é um indicador que mede a força do movimento de preço. Varia de 0 a 100 e te ajuda a identificar quando um ativo está sobrecomprado ou sobrevendido.

📈 COMO FUNCIONA:

✅ RSI > 70 = SOBRECOMPRA (atenção: possível reversão de baixa)
✅ RSI < 30 = SOBREVENDA (atenção: possível reversão de alta)
✅ RSI 40-60 = Zona neutra (mercado equilibrado)

💡 ESTRATÉGIA PRÓ:

🔹 Quando RSI sai de 70 para baixo = VENDA com lucro
🔹 Quando RSI sai de 30 para cima = COMPRA com segurança

⚠️ REGRA DE OURO:
"RSI isolado não ganha dinheiro. Combine com suporte/resistência e volume!"

Probabilidade de acerto: 67% 📊
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 2: Análise Técnica Pro
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 AULA #2: ANÁLISE TÉCNICA - OS 3 PILARES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 TODO TRADER PROFISSIONAL USA ESTES 3 PILARES:

**PILAR 1: TENDÊNCIA** 📊
→ Identifique se a tendência é ALTA, BAIXA ou LATERAL
→ Use trend lines (linha conectando máximas ou mínimas)
→ Nunca venda em tendência de alta, nunca compre em tendência de baixa

**PILAR 2: SUPORTE E RESISTÊNCIA** 🎯
→ Suporte: preço onde a compra é forte (piso)
→ Resistência: preço onde a venda é forte (teto)
→ Quanto + vezes toca = mais forte é o nível

**PILAR 3: VOLUME** 💪
→ Movimento com volume ALTO = movimento real
→ Movimento com volume BAIXO = movimento fraco (possível fake)
→ Volume confirma a qualidade da vela

⚡ COMO USAR JUNTOS:

1. Identifique a tendência principal
2. Encontre suportes e resistências
3. Confirme com volume
4. Entre apenas quando os 3 coincidem

Resultado: 78% de taxa de acerto! 🎖️

💎 Lembre-se: "Análise técnica é probabilidade, não certeza"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 3: Gestão de Risco
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡️ AULA #3: GESTÃO DE RISCO - PROTEJA SEU PATRIMÔNIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ VERDADE INCÔMODA:

❌ 92% dos iniciantes PERDEM DINHEIRO
✅ 92% dos que usam gestão de risco GANHAM a longo prazo

A diferença? Gestão de Risco!

📋 A REGRA DO RISCO 1:2

Para cada $100 em RISCO, você deve ter potencial de ganho de $200 ou mais.

Exemplo:
✅ Compra em 100
✅ Stop Loss em 95 (risco: $5)
✅ Alvo mínimo em 110 (ganho: $10)
✅ Razão: 1:2 (PERFEITO!) ✅

❌ Se seu alvo é 105, a razão é 1:1 (EVITE!)

🎯 REGRAS DE OURO DA GESTÃO DE RISCO:

1️⃣ NUNCA arrisque mais que 2% da sua conta por operação
2️⃣ SEMPRE use stop loss (inegociável!)
3️⃣ SEMPRE busque razão risco/recompensa mínima de 1:2
4️⃣ Tenha lucro objetivo ANTES de entrar
5️⃣ Se perdeu $500, faça 5 operações pequenas, não uma grande

💡 MENTALIDADE PROFISSIONAL:

"Não é sobre acertar sempre. É sobre ganhar mais do que perde."

Traders com 60% de acerto ganham MUITO mais que traders com 80% de acerto.

Por quê? Razão risco/recompensa! 💰

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 4: Padrões de Velas
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🕯️ AULA #4: PADRÕES DE VELAS - LEIA O MERCADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

As velas contam histórias sobre a psicologia dos traders.
Aprenda a ler essas histórias = Ganhe dinheiro! 💰

🔥 OS 3 PADRÕES MAIS RENTÁVEIS:

**PADRÃO #1: MARTELO (Bullish Reversal)** 🔨
→ Corpo pequeno no topo, pavio longo para baixo
→ Significa: "Os vendedores tentaram, mas os compradores ganharam"
→ Sinal: COMPRA com 71% de acerto
→ Encontre em fundos de tendência de baixa

**PADRÃO #2: ENGOLFO (Bullish Engulfing)** 📈
→ Vela verde GRANDE engolfe a vela vermelha anterior
→ Significa: "A pressão de compra superou a de venda"
→ Sinal: COMPRA com 69% de acerto
→ Procure em fundos (baixas)

**PADRÃO #3: ESTRELA CADENTE (Bearish Reversal)** ⭐
→ Corpo pequeno em cima, pavio longo para cima
→ Significa: "Os compradores tentaram, mas os vendedores ganharam"
→ Sinal: VENDA com 67% de acerto
→ Encontre em topos de tendência de alta

⚡ COMBINAÇÃO VENCEDORA:

Padrão de vela + Suporte/Resistência + Volume ALTO = Probabilidade de 85%+

💎 DICA PRO:

Não entre em uma vela apenas pelo padrão.
Confirme com indicadores (RSI, MACD) e volume!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 5: Estratégia de Confluência
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 AULA #5: CONFLUÊNCIA - O SEGREDO DOS TOP 1%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O que separadores TRADERS COMUNS de TRADERS RICOS?

Resposta: CONFLUÊNCIA! 🎖️

Confluência = Múltiplos sinais apontando para a mesma direção

⚡ EXEMPLO PRÁTICO:

SINAL FRACO (apenas 1 razão para comprar):
❌ RSI > 70
Taxa de acerto: 45% (não vale a pena!)

SINAL FORTE (Confluência de 4 razões):
✅ RSI > 70
✅ Rompimento de resistência
✅ Vela engolfante bullish
✅ Volume acima da média
Taxa de acerto: 92%! 🚀

📊 CHECKLIST DE CONFLUÊNCIA PROFISSIONAL:

Faça uma checklist antes de cada entrada:

☑️ Tendência está a favor?
☑️ Preço está testando suporte/resistência?
☑️ Indicadores confirmam (RSI, MACD)?
☑️ Padrão de vela está presente?
☑️ Volume está anormalmente alto?
☑️ Razão risco/recompensa é 1:2+?

✅ 5+ checkmarks = ENTRA COM CONFIANÇA
❌ Menos de 3 = PASSE DESSA OPERAÇÃO

💡 MENTALIDADE PROFISSIONAL:

"Qualidade sobre quantidade. 1 operação excelente vale mais que 10 operações fracas."

Os melhores traders entram em menos de 5 operações por dia.
Mas quando entram? GANHAM DINHEIRO! 💰

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 6: Psicologia Trader
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 AULA #6: PSICOLOGIA DO TRADER - VENÇA SUA MENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Fato chocante: 80% das perdas de traders NÃO são por análise ruim.
São por EMOÇÃO! 😰

A análise técnica é fácil. Vencer suas emoções é difícil.

🔴 OS 3 INIMIGOS DA MENTE DO TRADER:

**INIMIGO #1: FOMO (Fear of Missing Out)** 😨
→ Você vê o preço subindo e entra RÁPIDO
→ Resultado: Entra no TOPO e perde dinheiro
Solução: Tenha um PLANO antes. Siga o plano!

**INIMIGO #2: REVENGE TRADING** 🔥
→ Perdeu $100, quer recuperar AGORA
→ Faz operações desesperadas e perde $300
Solução: Se perdeu, SAIA. Volte amanhã com a cabeça fresca!

**INIMIGO #3: GANÂNCIA** 💰
→ Já tem $200 de lucro, quer mais
→ O preço revira e perde tudo
Solução: Tenha meta de lucro DIÁRIA. Quando atingir, SAIA!

✅ 5 REGRAS PSICOLÓGICAS DE OURO:

1️⃣ Nunca negocie EMOCIONADO. Espere 1 hora e reavalie.
2️⃣ Se perdeu, tome o resto do dia de folga.
3️⃣ Ganhe 3 operações seguidas? Saia e aproveite a vida!
4️⃣ Tenha rotina: entrada, stop loss, target. ANTES de clicar.
5️⃣ Mantenha um DIÁRIO de operações. Revise os erros.

💡 MENTALIDADE DE CAMPEÃO:

"O trader que controla suas emoções controla seus lucros."

Simples assim! 🎖️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 7: Leitura Avançada de Gráficos
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📉 AULA #7: LEITURA AVANÇADA DE GRÁFICOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O gráfico é a verdade nua e crua do mercado.
Aprenda a ler = Aprenda a ganhar dinheiro! 💰

🎯 TREND LINES - O PODER DAS LINHAS

Uma trend line é uma linha que conecta MÁXIMAS ou MÍNIMAS.

📈 TREND LINE DE ALTA:
→ Conecta 2 ou mais mínimas crescentes
→ Representa suporte dinâmico
→ Quando rompe para baixo = Sinal de fraqueza

📉 TREND LINE DE BAIXA:
→ Conecta 2 ou mais máximas decrescentes
→ Representa resistência dinâmica
→ Quando rompe para cima = Sinal de força

🎪 CANAIS DE PREÇO

Canal = Trend line alta + Trend line baixa paralela

O preço "dança" dentro do canal:
✅ Toca o fundo (suporte) = COMPRA
✅ Toca o teto (resistência) = VENDA

Quando rompe o canal para cima/baixo = Novo movimento vem! 🚀

💎 OS 3 FORMATOS DE GRÁFICO

**1. TIMEFRAME DIÁRIO** - Para operações de DIAS/SEMANAS
→ Mais confiável, menos whipsaw
→ Recomendado para iniciantes

**2. TIMEFRAME 4H** - Para operações de HORAS
→ Equilíbrio entre velocidade e segurança
→ Favorito dos traders profissionais

**3. TIMEFRAME 1H** - Para operações RÁPIDAS
→ Mais sinais, mais risco
→ Requer muita experiência

⚡ DICA PRO:

Operação vencedora = Tendência diária + Entrada em 4H/1H
Sempre trade NA DIREÇÃO da tendência maior! 🎖️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 8: Indicadores Avançados
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 AULA #8: INDICADORES AVANÇADOS - O ARSENAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Indicadores são FERRAMENTAS para confirmar sua análise.
Não são bolas de cristal, são GPS! 🧭

🔧 INDICADOR #1: MACD (Moving Average Convergence Divergence)

O que faz? Identifica mudanças de momento.

✅ Sinal de COMPRA:
→ MACD cruza a linha de sinal para cima
→ MACD muda de vermelho para verde
→ Momento está aumentando!

✅ Sinal de VENDA:
→ MACD cruza a linha de sinal para baixo
→ MACD muda de verde para vermelho
→ Momento está diminuindo!

Precisão: 62% 📈

🔧 INDICADOR #2: BANDAS DE BOLLINGER

3 linhas que "abraçam" o preço:
→ Banda superior: Resistência
→ Banda média: Média móvel
→ Banda inferior: Suporte

✅ Quando preço toca BANDA INFERIOR = possível COMPRA
✅ Quando preço toca BANDA SUPERIOR = possível VENDA

Precisão: 65% 📈

🔧 INDICADOR #3: ESTOCÁSTICO

Mede o momento relativo do preço.

✅ Estocástico > 80 = SOBRECOMPRA (cuidado com quedas)
✅ Estocástico < 20 = SOBREVENDA (cuidado com altas)
✅ Crossover = Mudança de direção possível

Precisão: 58% 📈

⚡ A REGRA DE OURO DOS INDICADORES:

NUNCA trade apenas por indicador!
Combine indicador + Análise técnica + Gestão de risco = 80%+ de acerto

Indicador sozinho tem 40-60% de acerto.
Indicador + Técnica tem 75-85% de acerto!

💎 Exemplo vencedor:
✅ Tendência está alta (técnica)
✅ RSI sai de 30 (indicador)
✅ MACD cruza para cima (indicador)
✅ Volume está alto (técnica)
✅ Razão risco/recompensa 1:2 (gestão de risco)

Entrada aqui = Probabilidade de 87%! 🎖️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 9: Crypto vs Forex vs Ações
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌍 AULA #9: CRYPTO vs FOREX vs AÇÕES - QUAL ESCOLHER?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3 mercados, 3 velocidades, 3 oportunidades diferentes!

📊 CRYPTOCURRENCY (Bitcoin, Ethereum, etc)

Volatilidade: ⭐⭐⭐⭐⭐ (Altíssima!)
Horário: 24/7 (sem parar, sem férias!)
Spreads: Altos (Corretoras cobram muito)
Risco: Muito alto, lucros podem ser gigantescos

✅ VANTAGENS:
→ Tendências MUITO forte (lucros enormes)
→ Mercado jovem (muitas oportunidades)
→ Sem horário (trade quando quiser)

❌ DESVANTAGENS:
→ Volatilidade extrema (para fracos, é perda certa)
→ Muita manipulação e "pump and dump"
→ Spread alto (corretora quer sua grana)

💡 MELHOR PARA: Traders experientes com capital grande

📈 FOREX (Euro/Dólar, Libra/Dólar, etc)

Volatilidade: ⭐⭐⭐ (Moderada)
Horário: Segunda a Sexta (09h às 18h Brasília)
Spreads: Muito baixos (0.1 pips!)
Risco: Médio (alavancagem disponível)

✅ VANTAGENS:
→ Spread baixíssimo (mais lucro para você)
→ Mercado enorme (liquidez infinita)
→ Alavancagem disponível (multiplicar ganhos)

❌ DESVANTAGENS:
→ Movimentos mais lentos (lucros menores)
→ Mercado maduro (menos oportunidades)
→ Não funciona 24/7

💡 MELHOR PARA: Traders iniciantes/intermediários

💎 AÇÕES (PETR4, VALE5, WEGE3, etc)

Volatilidade: ⭐⭐ (Baixa a moderada)
Horário: Segunda a Sexta (10h às 17h Brasília)
Spreads: Médios (0.5 a 2 reais)
Risco: Médio-baixo (sem alavancagem)

✅ VANTAGENS:
→ Você entende o negócio (lógica por trás)
→ Tendências previsíveis (análise é mais fácil)
→ Dividendos (ganho extras mesmo sem vender)

❌ DESVANTAGENS:
→ Lucros menores (movimentos lentos)
→ Corretoras cobram taxa (diminui lucro)
→ Spread maior

💡 MELHOR PARA: Traders conservadores / long-term

⚡ QUAL ESCOLHER?

💰 Se tem $1,000 e quer ganhar $100 rápido → CRYPTO
💰 Se tem $10,000 e quer ganhar $500 mês → FOREX
💰 Se tem $50,000 e quer renda permanente → AÇÕES

🎖️ Regra de Ouro: Escolha o mercado que você ENTENDE melhor!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 10: Construa Sua Estratégia
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️ AULA #10: CONSTRUA SUA ESTRATÉGIA EM 7 PASSOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Não copie estratégias. CRIE a sua própria!

Cada trader tem um estilo. Encontre o seu! 🎯

🚀 PASSO 1: DEFINA SEU ESTILO

Pergunta: Você quer operações RÁPIDAS ou SEGURAS?

A) SCALPER (Operações de MINUTOS)
→ Compra, espera 5-15 min, vende
→ Lucro pequeno, frequência alta
→ Estressante, requer muita concentração

B) DAY TRADER (Operações de HORAS)
→ Compra, espera 1-4 horas, vende
→ Lucro médio, frequência média
→ Menos estressante, requer disciplina

C) SWING TRADER (Operações de DIAS/SEMANAS)
→ Compra, espera 3-30 dias, vende
→ Lucro grande, frequência baixa
→ Pouco estressante, ideal para iniciantes

✅ RECOMENDAÇÃO: Comece como swing trader!

🚀 PASSO 2: ESCOLHA O MERCADO

Escolha 1 mercado e DOMINE:
→ Cryptocurrency
→ Forex
→ Ações
→ Opções

Não pule de um para o outro! Profundidade > Amplitude

🚀 PASSO 3: DEFINA SEUS INDICADORES

Escolha no máximo 3 indicadores:

Opção A (Simples):
✅ RSI
✅ Suporte/Resistência
✅ Volume

Opção B (Técnica):
✅ MACD
✅ Trend Lines
✅ Padrões de Velas

Opção C (Avançada):
✅ Bollinger Bands
✅ Estocástico
✅ Confluência

Escolha UMA opção e pratique 1 mês!

🚀 PASSO 4: DEFINA SEU HORÁRIO

Quando você vai tradear?

✅ Escolha 1-2 horas por dia (máximo!)
✅ Nesse horário, você estará 100% focado
✅ Fora desse horário, NÃO mexe na conta

Exemplo: 09h-11h (operações da manhã)

🚀 PASSO 5: DEFINA SUAS REGRAS DE ENTRADA

Quando você ENTRA em uma operação?

Exemplo regra de entrada:
1. Preço testa resistência 3x
2. Rompimento com volume alto
3. RSI está entre 50-70
4. Todos os 3 critérios atendidos = ENTRA

✅ REGRA SAGRADA: Escreva suas regras NO PAPEL

🚀 PASSO 6: DEFINA SUAS REGRAS DE SAÍDA

Quando você SAI da operação?

Exemplo regra de saída:
1. Stop loss em X% abaixo
2. Alvo em X% acima (1:2 razão)
3. Tempo máximo: 5 dias (se não ganhou, sai)

✅ REGRA SAGRADA: SEMPRE use stop loss!

🚀 PASSO 7: BACKTEST E REFINE

Pegue 50 operações antigas e teste sua estratégia:

1. Teria funcionado?
2. Quantas teriam ganho?
3. Quantas teriam perdido?
4. Qual seria o resultado total?

Se resultado < 60% acerto: AJUSTE!
Se resultado > 60% acerto: LIVE!

🎖️ DICA FINAL:

Nenhuma estratégia é perfeita!
Mas uma estratégia CONSISTENTE bate 100 estratégias ruins.

Escolha uma. Pratique por 3 meses. Refine. Ganhe dinheiro! 💰

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """,

    # AULA 11: BÔNUS - Erros Fatais
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💀 AULA BÔNUS: OS 10 ERROS QUE DESTROEM CONTAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Évite esses 10 erros e você já estará no top 10% dos traders! 🎖️

❌ ERRO #1: SEM STOP LOSS

"Deixo a operação aberta, talvez recupere..."
RESULTADO: Perde $1,000 em 1 hora 💥

✅ SOLUÇÃO: Stop loss é OBRIGATÓRIO. Sem exceção!

❌ ERRO #2: ALAVANCAGEM EXCESSIVA

"Vou multiplicar por 100x!"
RESULTADO: Ganha $100... Depois perde $10,000 💥

✅ SOLUÇÃO: Alavancagem máxima 2:1. Principiante? 1:1!

❌ ERRO #3: NÃO TER PLAN A

"Vou entrar e decidir depois..."
RESULTADO: Decisões emocionais, perdas garantidas 💥

✅ SOLUÇÃO: Sempre tenha entrada, stop loss e alvo ANTES de clicar!

❌ ERRO #4: REVENGE TRADING

"Perdi $500, vou recuperar AGORA!"
RESULTADO: Perde $2,000 em modo desespero 💥

✅ SOLUÇÃO: Se perdeu, saia. Volte amanhã com cabeça fresca!

❌ ERRO #5: IGNORAR A TENDÊNCIA GERAL

"Vou vender apesar da tendência estar alta..."
RESULTADO: Sai como perdedor enquanto mercado sobe 💥

✅ SOLUÇÃO: A tendência é sua AMIGA. Não nade contra ela!

❌ ERRO #6: MUITOS INDICADORES

"Vou usar RSI, MACD, Estocástico, Bollinger, Ichimoku..."
RESULTADO: Paralisia pela análise, entra errado 💥

✅ SOLUÇÃO: Máximo 3 indicadores. Menos é mais!

❌ ERRO #7: SEM GESTÃO DE RISCO

"Hoje arrisquei 10% da conta, amanhã 15%, depois 20%..."
RESULTADO: Blowup garantido (perder tudo) 💥

✅ SOLUÇÃO: Sempre arrisque máximo 2% por operação!

❌ ERRO #8: TRADING EMOCIONADO

"Estou muito feliz, vou fazer 10 operações!"
"Estou triste, vou fazer uma gorda para compensar!"
RESULTADO: Loucura, perdas gigantescas 💥

✅ SOLUÇÃO: Trade apenas com cabeça fria. Emoção = perda!

❌ ERRO #9: NEM ESTUDAR NEM TREINAR

"Já comecei com dinheiro real direto..."
RESULTADO: Escola cara, aprender na conta 💥

✅ SOLUÇÃO: Estude 1-3 meses, practice em demo, depois live!

❌ ERRO #10: NÃO TER DIÁRIO DE OPERAÇÕES

"Não sei o que errei..."
RESULTADO: Repete os mesmos erros infinitamente 💥

✅ SOLUÇÃO: Anote CADA operação. Revise 1x por semana!

🏆 BONUS TIP:

Os melhores traders fazem UMA coisa perfeita:
🎖️ Gestão de risco perfeita
🎖️ Confluência de sinais
🎖️ Psicologia de campeão

Focam em qualidade, não quantidade!

Resultado: 60% de acerto com razão 1:2 = +30% ao mês! 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
]

# Índice para rastrear qual aula foi enviada
contador_aula = 0

def enviar_conteudo():
    global contador_aula
    while True:
        try:
            aula = AULAS[contador_aula % len(AULAS)]
            bot.send_message(GRUPO_ID, aula)
            
            # Move para próxima aula
            contador_aula += 1
            
            print(f"✅ Aula #{contador_aula} enviada com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro ao enviar aula: {e}")
        
        time.sleep(36000)  # 10 horas

def start_scheduler():
    t = threading.Thread(target=enviar_conteudo)
    t.daemon = True
    t.start()
