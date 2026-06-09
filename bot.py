from whatsapp import send_text, send_location

# ─── Árvore de navegação gerada do CSV ───────────────────────────────────────
# Formato: { id: {"texto": "...", "pai": "...", "tipo": 1|2} }

NODES = {
    "1":  {"texto": "MENU PRINCIPAL\n\nEscolha um número abaixo e daremos continuidade ao seu atendimento. ☺", "pai": "parent", "tipo": 1},
    "2":  {"texto": "Triagem de urgência: é Trauma ou não é?", "pai": "parent", "tipo": 2},
    "3":  {"texto": "Como posso resolver em casa", "pai": "parent", "tipo": 2},
    "4":  {"texto": "Receber notificações sobre cuidados com a saúde", "pai": "parent", "tipo": 2},
    "5":  {"texto": "Triagem de urgência: é Trauma ou não é?\n\nIrei te ajudar a identificar isso. Responda algumas perguntas rápidas:", "pai": "2", "tipo": 1},
    "6":  {"texto": "Como sabe se minha situação é uma emergência de Trauma?", "pai": "2", "tipo": 2},
    "7":  {"texto": "O que é considerado caso de Trauma?", "pai": "2", "tipo": 2},
    "8":  {"texto": "Direcionamento para casos que não são de Trauma.", "pai": "2", "tipo": 2},
    "9":  {"texto": "Primeiros socorros para ferimentos leves:", "pai": "3", "tipo": 1},
    "10": {"texto": "Me queimei com água quente. Como tratar?", "pai": "3", "tipo": 2},
    "11": {"texto": "Me machuquei e está sangrando.", "pai": "3", "tipo": 2},
    "12": {"texto": "Fui Mordido(a) por um animal. O que faço?", "pai": "3", "tipo": 2},
    "78": {"texto": "Atendimento encerrado", "pai": "3", "tipo": 2},
    "13": {"texto": "Cuidados sazonais por época do ano.", "pai": "4", "tipo": 1},
    "14": {"texto": "Quais cuidados devo ter no verão para evitar problemas de saúde?", "pai": "4", "tipo": 2},
    "15": {"texto": "Como evitar doenças respiratórias no inverno?", "pai": "4", "tipo": 2},
    "16": {"texto": "Cuidado com festa de São João.", "pai": "4", "tipo": 2},
    "17": {"texto": "Vou te ajudar a identificar isso. Responda algumas perguntas rápidas:", "pai": "6", "tipo": 1},
    "18": {"texto": "Você sofreu algum acidente, queda, pancada forte ou colisão?", "pai": "6", "tipo": 2},
    "19": {"texto": "Há sangramento intenso que não para?", "pai": "6", "tipo": 2},
    "20": {"texto": "A pessoa está inconsciente, confusa ou com dificuldade de respirar?", "pai": "6", "tipo": 2},
    "70": {"texto": "Envenenamento", "pai": "6", "tipo": 2},
    "71": {"texto": "Violência", "pai": "6", "tipo": 2},
    "72": {"texto": "Convulsão", "pai": "6", "tipo": 2},
    "73": {"texto": "Sinais de infarto", "pai": "6", "tipo": 2},
    "74": {"texto": "Sinais de AVC", "pai": "6", "tipo": 2},
    "75": {"texto": "Ferimento em objeto enferrujado", "pai": "6", "tipo": 2},
    "21": {"texto": "Casos de Trauma incluem:", "pai": "7", "tipo": 1},
    "22": {"texto": "Acidentes de trânsito (carro, moto, bicicletas...)", "pai": "7", "tipo": 2},
    "23": {"texto": "Quedas de altura (escada, telhado, andaimes...)", "pai": "7", "tipo": 2},
    "24": {"texto": "Queimaduras extensas ou de grau elevado", "pai": "7", "tipo": 2},
    "25": {"texto": "Ferimentos por arma de fogo ou arma branca", "pai": "7", "tipo": 2},
    "26": {"texto": "Traumatismo cranioencefálico (pancada na cabeça)", "pai": "7", "tipo": 2},
    "65": {"texto": "Mordida por animais peçonhentos", "pai": "7", "tipo": 2},
    "27": {"texto": "Se a resposta for sim para qualquer uma delas, dirija-se imediatamente para o hospital de Trauma.", "pai": "18", "tipo": 1},
    "28": {"texto": "Sim", "pai": "18", "tipo": 2},
    "29": {"texto": "Não", "pai": "18", "tipo": 2},
    "30": {"texto": "Se a resposta for sim para qualquer uma delas, dirija-se imediatamente para o hospital de Trauma.", "pai": "19", "tipo": 1},
    "31": {"texto": "Sim", "pai": "19", "tipo": 2},
    "32": {"texto": "Não", "pai": "19", "tipo": 2},
    "33": {"texto": "Se a resposta for sim para qualquer uma delas, dirija-se imediatamente para o hospital de Trauma.", "pai": "20", "tipo": 1},
    "34": {"texto": "Sim", "pai": "20", "tipo": 2},
    "35": {"texto": "Não", "pai": "20", "tipo": 2},
    "37": {"texto": "Aqui iremos orientar e direcionar caso o seu atendimento não seja de Trauma.", "pai": "8", "tipo": 1},
    "38": {"texto": "Febre alta", "pai": "8", "tipo": 2},
    "39": {"texto": "Dor de ouvido", "pai": "8", "tipo": 2},
    "40": {"texto": "Sintomas de gripe", "pai": "8", "tipo": 2},
    "41": {"texto": "Dor de cabeça há dois dias", "pai": "8", "tipo": 2},
    "42": {"texto": "Onde fica a UPA mais próxima daqui", "pai": "8", "tipo": 2},
    "43": {"texto": "Depende da situação:", "pai": "38", "tipo": 1},
    "44": {"texto": "Febre abaixo de 38°C", "pai": "38", "tipo": 2},
    "45": {"texto": "Febre entre 38°C e 39°C", "pai": "38", "tipo": 2},
    "46": {"texto": "Febre acima de 39°C ou com convulsão", "pai": "38", "tipo": 2},
    "47": {"texto": "Hidratação e antitérmico em casa", "pai": "44", "tipo": 1},
    "48": {"texto": "UBS", "pai": "45", "tipo": 1},
    "49": {"texto": "Pronto Socorro", "pai": "46", "tipo": 1},
    "50": {"texto": "Normalmente dor de ouvido não é considerada um caso de Trauma. Indicamos:\n\n• UBS mais próxima para consulta com clínico geral\n• Consulta com otorrinolaringologista\n• UPA se for fim de semana ou fora do horário comercial\n\nEvite inserir objetos no ouvido enquanto aguarda o atendimento.", "pai": "39", "tipo": 1},
    "51": {"texto": "Para gripe sem complicações:\n\n• UBS ou UPA da sua região ou a mais próxima\n• Em casa: repouso, hidratação, antitérmico (Paracetamol, Dipirona e Ibuprofeno) se necessário\n\n⚠️ Se tiver dificuldade para respirar, lábios azulados ou piora rápida vá ao pronto socorro.", "pai": "40", "tipo": 1},
    "52": {"texto": "Para dores de cabeça sem trauma, recomendamos:\n\n• UPA mais próxima\n• UBS durante o dia\n• Clínica geral\n\n⚠️ Se a dor for súbita, muito intensa ('a pior da vida') ou acompanhada de rigidez de nuca, vá ao pronto socorro.", "pai": "41", "tipo": 1},
    "53": {"texto": "Para encontrar a UPA mais próxima, você pode:\n\nhttps://docs.google.com/document/d/1-T5lxzdB9p0_MLVZxNEZHPxKpM4JyykzzPmj3zOPzsY/edit?usp=drivesdk\n\n• Ligar para o Disk Saúde: 136\n• Acessar o site da Secretaria Municipal de Saúde\n• Pesquisar no Google Maps por 'UPA próxima a mim'\n• Perguntar na recepção do hospital o endereço das unidades conveniadas.", "pai": "42", "tipo": 1},
    "54": {"texto": "⚠️ Esse caso exige atendimento no hospital de Trauma.", "pai": "22", "tipo": 1},
    "55": {"texto": "⚠️ Esse caso exige atendimento no hospital de Trauma.", "pai": "23", "tipo": 1},
    "56": {"texto": "⚠️ Esse caso exige atendimento no hospital de Trauma.", "pai": "24", "tipo": 1},
    "57": {"texto": "⚠️ Esse caso exige atendimento no hospital de Trauma.", "pai": "25", "tipo": 1},
    "58": {"texto": "⚠️ Esse caso exige atendimento no hospital de Trauma.", "pai": "26", "tipo": 1},
    "59": {"texto": "Para queimaduras leves (1° grau - vermelhidão):\n\n• Coloque água corrente por 10 a 20 minutos\n• NÃO use gelo, manteiga, creme dental ou pasta\n• NÃO estoure as bolhas\n\n⚠️ Queimaduras em rosto, mãos, genitais ou com bolhas grandes: Pronto Socorro imediato.", "pai": "10", "tipo": 1},
    "60": {"texto": "Para cortes superficiais, siga este passo a passo:\n\n• Lave o ferimento com água corrente e sabão neutro por 5 minutos\n• Pressione com um pano limpo por 5 a 10 minutos\n• Cubra com um curativo estéril\n\n⚠️ Se o sangramento não parar ou o corte for profundo, procure atendimento médico em um Pronto Socorro.", "pai": "11", "tipo": 1},
    "61": {"texto": "Após a mordida:\n\n• Lavar o ferimento em água corrente e sabão neutro\n• Identificar o animal: doméstico ou silvestre\n• Observar o animal por 10 dias e verificar sinais de raiva\n\n⚠️ Vá ao Pronto Socorro se não souber a procedência do animal ou se o ferimento for profundo.", "pai": "12", "tipo": 1},
    "62": {"texto": "No verão, atenção especial para:\n\n• Hidratação: beba pelo menos 2 litros de água por dia\n• Evite exposição ao sol entre as 10h e 16h\n• Use protetor solar FPS 30 ou maior\n• Alimentos: evite deixar comida fora da geladeira\n• Piscinas: observe regras de segurança e supervisione as crianças", "pai": "14", "tipo": 1},
    "63": {"texto": "Para reduzir o risco de doenças respiratórias:\n\n• Lave as mãos com frequência\n• Evite aglomerações em ambientes fechados\n• Não compartilhe itens pessoais\n• Use máscara se estiver gripado(a)\n• Vacine-se contra a gripe (especialmente crianças e idosos)", "pai": "15", "tipo": 1},
    "64": {"texto": "Durante as festas evite:\n\n• Acender fogueiras e brincadeiras ao redor\n• Cuidado ao manusear fogos — mantenha longe de crianças\n• Evite pendurar decorações próximas a fios de energia\n• Cuidado no consumo de álcool\n• Cuidado em ambientes superlotados", "pai": "16", "tipo": 1},
    "66": {"texto": "Escorpiões", "pai": "65", "tipo": 1},
    "67": {"texto": "Cobras", "pai": "65", "tipo": 2},
    "68": {"texto": "Aranhas", "pai": "65", "tipo": 2},
    "76": {"texto": "Atendimento mais próximo", "pai": "parent", "tipo": 2},
    "79": {"texto": "Aqui você confirma que o seu caso foi resolvido. ☺\n\nQualquer dúvida, inicie um novo atendimento.", "pai": "78", "tipo": 1},
}

# ─── Monta índice: pai → lista de filhos (opções) ────────────────────────────
def _build_children():
    children = {}
    for node_id, node in NODES.items():
        pai = node["pai"]
        if node["tipo"] == 2:
            children.setdefault(pai, []).append(node_id)
    return children

CHILDREN = _build_children()

# ─── Estado das conversas ─────────────────────────────────────────────────────
# Guarda: etapa, contexto atual e histórico para o comando "voltar"
user_state: dict = {}

def get_state(phone: str) -> dict:
    return user_state.get(phone, {"etapa": "novo", "contexto": None, "historico": []})

def set_state(phone: str, state: dict):
    user_state[phone] = state


# ─── Funções de navegação ─────────────────────────────────────────────────────

def get_content_node(parent_id: str) -> str | None:
    """Retorna o nó de conteúdo (tipo 1) filho de um pai, se existir."""
    for node_id, node in NODES.items():
        if node["pai"] == parent_id and node["tipo"] == 1:
            return node_id
    return None


def exibir_menu(phone: str, node_id: str, historico: list):
    """Envia o texto do nó e exibe as opções filhas se houver."""
    node = NODES.get(node_id)
    if not node:
        send_text(phone, "❌ Opção não encontrada. Digite *menu* para recomeçar.")
        return

    send_text(phone, node["texto"])

    opcoes = CHILDREN.get(node_id, [])
    if opcoes:
        linhas = ["*Escolha uma opção:*\n"]
        for i, filho_id in enumerate(opcoes, start=1):
            filho = NODES[filho_id]
            linhas.append(f"{i}️⃣ {filho['texto']}")
        linhas.append("\nResponda com o *número* da opção.")
        send_text(phone, "\n".join(linhas))
        set_state(phone, {"etapa": "aguardando_opcao", "contexto": node_id, "historico": historico})
    else:
        # Nó folha — sem mais opções
        send_text(phone, "━━━━━━━━━━━━━━\nDigite *menu* para voltar ao início ou *voltar* para a opção anterior.")
        set_state(phone, {"etapa": "folha", "contexto": node_id, "historico": historico})


def handle_opcao(phone: str, escolha: str, contexto: str, historico: list):
    """Processa a escolha numérica do usuário dentro de um contexto."""
    opcoes = CHILDREN.get(contexto, [])

    try:
        idx = int(escolha) - 1
        if idx < 0 or idx >= len(opcoes):
            raise ValueError
    except ValueError:
        send_text(phone, f"❌ Opção inválida. Escolha um número entre 1 e {len(opcoes)}.")
        return

    filho_id = opcoes[idx]
    novo_historico = historico + [contexto]

    # Se o filho tem nó de conteúdo (tipo 1) associado, envia o conteúdo
    # e depois verifica se esse conteúdo também tem filhos
    conteudo_id = get_content_node(filho_id)
    if conteudo_id:
        # Envia o texto do conteúdo
        send_text(phone, NODES[conteudo_id]["texto"])
        # Verifica se o filho (tipo 2) tem subopcoes
        subopcoes = CHILDREN.get(filho_id, [])
        if subopcoes:
            linhas = ["*Escolha uma opção:*\n"]
            for i, sub_id in enumerate(subopcoes, start=1):
                sub = NODES[sub_id]
                linhas.append(f"{i}️⃣ {sub['texto']}")
            linhas.append("\nResponda com o *número* da opção.")
            send_text(phone, "\n".join(linhas))
            set_state(phone, {"etapa": "aguardando_opcao", "contexto": filho_id, "historico": novo_historico})
        else:
            # Sem subopcoes — nó folha
            send_text(phone, "━━━━━━━━━━━━━━\nDigite *menu* para voltar ao início ou *voltar* para a opção anterior.")
            set_state(phone, {"etapa": "folha", "contexto": filho_id, "historico": novo_historico})
    else:
        exibir_menu(phone, filho_id, novo_historico)


def ir_para_menu_principal(phone: str):
    """Envia o menu principal do zero."""
    send_text(phone, NODES["1"]["texto"])
    opcoes_parent = CHILDREN.get("parent", [])
    linhas = ["*Escolha uma opção:*\n"]
    for i, filho_id in enumerate(opcoes_parent, start=1):
        filho = NODES[filho_id]
        linhas.append(f"{i}️⃣ {filho['texto']}")
    linhas.append("\nResponda com o *número* da opção.")
    send_text(phone, "\n".join(linhas))
    set_state(phone, {"etapa": "aguardando_opcao", "contexto": "parent", "historico": []})


# ─── Dispatcher principal ─────────────────────────────────────────────────────

def process_message(phone: str, body: str):
    state    = get_state(phone)
    etapa    = state.get("etapa", "novo")
    contexto = state.get("contexto")
    historico = state.get("historico", [])
    texto    = body.strip().lower()

    print(f"[Bot] {phone} | etapa={etapa} | contexto={contexto} | msg='{texto}'")

    # ── Comando: voltar ───────────────────────────────────────────────────────
    if texto == "voltar":
        if historico:
            contexto_anterior = historico[-1]
            novo_historico = historico[:-1]
            exibir_menu(phone, contexto_anterior, novo_historico)
        else:
            ir_para_menu_principal(phone)
        return

    # ── Comando: menu / reiniciar ─────────────────────────────────────────────
    if texto in ("menu", "início", "inicio", "oi", "olá", "ola", "reiniciar", "0"):
        send_text(phone, "👋 Bem-vindo(a) de volta!")
        ir_para_menu_principal(phone)
        return

    # ── Primeiro contato ──────────────────────────────────────────────────────
    if etapa == "novo":
        send_text(phone, "👋 Olá! Bem-vindo(a) ao *Bot EVA* — seu assistente de saúde.")
        ir_para_menu_principal(phone)
        return

    # ── Aguardando escolha de opção ───────────────────────────────────────────
    if etapa == "aguardando_opcao" and contexto:
        handle_opcao(phone, texto, contexto, historico)
        return

    # ── Nó folha — só aceita menu ou voltar ───────────────────────────────────
    if etapa == "folha":
        send_text(phone, "Digite *menu* para voltar ao início ou *voltar* para a opção anterior.")
        return

    send_text(phone, "Não entendi. Digite *menu* para recomeçar.")
