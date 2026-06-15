from whatsapp import send_text, send_image, send_video

# ─── URLs de mídia ────────────────────────────────────────────────────────────

VIDEOS = {
    "dor_ouvido":     "https://drive.google.com/uc?export=download&id=1QPE_uQnDFDGcUgKcp5KM5fETXr2burp9",
    "febre":          "https://drive.google.com/uc?export=download&id=15aP50Z42B0FeC08H92j610ezP_j3wAkK",
    "gripe":          "https://drive.google.com/uc?export=download&id=1RJ5ZL16v1y9UeJVw2r9rNpPs7dsqFbiq",
    "mordida_animal": "https://drive.google.com/uc?export=download&id=1Uqi2f5hcNopD8cxK5IcdB91N3TiQFmix",
    "saudacao":       "https://drive.google.com/uc?export=download&id=1KD0qd_Aj9cqpP8imUmimE2_2w7sgpO7P",
    "resolver_casa":  "https://drive.google.com/uc?export=download&id=19vegUwH3UziDO4SbKaBMzQOa52b1HCFR",
    "sao_joao":       "https://drive.google.com/uc?export=download&id=1xD5KCghVy1C6gR287KF_JoQzf2ct032n",
    "urgencia":       "https://drive.google.com/uc?export=download&id=1bJmZ3ApHe58nLBpW-G2G9vyQ8NdPAvOb",
    "verao":          "https://drive.google.com/uc?export=download&id=11NpYHT8Zzcm-CMdHmomoFG9X1l0FSbP6",
}

IMAGENS = {
    "acidente_transito": "https://drive.google.com/uc?export=download&id=1b1Kb9vVGY9OIRSx4RRDw0iqdMhSSSZHB",
    "dor_cabeca":        "https://drive.google.com/uc?export=download&id=13kTZUn0CV3QLP_UJzm6zs4iMxdSLQiFr",
    "ferimento_arma":    "https://drive.google.com/uc?export=download&id=1-jYR76QCbpUM1hQ0WzERfqCcy6ioSh69",
    "gripe":             "https://drive.google.com/uc?export=download&id=1MQ88k1CjQogOjVhgz3wuKGWTGkkYgh2V",
    "inverno":           "PENDENTE",  # ← substitua pela URL do Drive
    "mordida_animal":    "https://drive.google.com/uc?export=download&id=15vd3TxmittyqmA2P0v4oL3A3OZc5cJaf",
    "queda_altura":      "https://drive.google.com/uc?export=download&id=1xKU5mojAjGbyxpz3rwDarSUWJimrumLX",
    "queimadura_casa":   "https://drive.google.com/uc?export=download&id=1oQgWzyjCJOkHXn9pQQOSQlto54hf43fv",
    "queimadura_grave":  "https://drive.google.com/uc?export=download&id=1OvpKsfB2O0RlLP7G2gJDZUb-6sEFkq8u",
    "sangramento":       "https://drive.google.com/uc?export=download&id=1IJ0Q4u4ytQg38z-hireM70-7Bwomi88O",
    "sao_joao":          "https://drive.google.com/uc?export=download&id=1f6FgEKFrbLtfpAKt_iFMU8zlt1Qv_hqp",
    "traumatismo":       "PENDENTE",  # ← substitua pela URL do Drive
    "verao":             "https://drive.google.com/uc?export=download&id=1_ml424TkbwvESRLMlSP-5OK3uiIR0fBr",
}

LINKS = {
    "upa":    "📍 Encontre a UPA mais próxima:\nhttps://www.google.com/maps/search/UPA+próxima+de+mim",
    "ubs":    "📍 Encontre a UBS mais próxima:\nhttps://www.google.com/maps/search/UBS+próxima+de+mim",
    "trauma": "📍 Encontre o Hospital de Trauma mais próximo:\nhttps://www.google.com/maps/search/Hospital+de+Trauma+próximo+de+mim",
}

# ─── Árvore de navegação ──────────────────────────────────────────────────────

NODES = {
    "1":  {"texto": "MENU PRINCIPAL\n\nEscolha um número abaixo e daremos continuidade ao seu atendimento. ☺", "pai": "parent", "tipo": 1},
    "2":  {"texto": "Triagem de urgência: é Trauma ou não é?", "pai": "parent", "tipo": 2},
    "3":  {"texto": "Como posso resolver em casa", "pai": "parent", "tipo": 2},
    "4":  {"texto": "Receber notificações sobre cuidados com a saúde", "pai": "parent", "tipo": 2},
    "76": {"texto": "Atendimento mais próximo", "pai": "parent", "tipo": 2},

    # ── Triagem (2) ───────────────────────────────────────────────────────────
    "5":  {"texto": "Triagem de urgência: é Trauma ou não é?\n\nIrei te ajudar a identificar isso. Responda algumas perguntas rápidas:", "pai": "2", "tipo": 1},
    "6":  {"texto": "Como saber se minha situação é uma emergência de Trauma?", "pai": "2", "tipo": 2},
    "7":  {"texto": "O que é considerado caso de Trauma?", "pai": "2", "tipo": 2},
    "8":  {"texto": "Casos que não são de Trauma", "pai": "2", "tipo": 2},

    # ── Como saber se é trauma (6) ────────────────────────────────────────────
    "17": {"texto": "Vou te ajudar a identificar isso. Responda algumas perguntas rápidas:", "pai": "6", "tipo": 1},
    "18": {"texto": "Você sofreu algum acidente, queda, pancada forte ou colisão?", "pai": "6", "tipo": 2},
    "19": {"texto": "Há sangramento intenso que não para?", "pai": "6", "tipo": 2},
    "20": {"texto": "A pessoa está inconsciente, confusa ou com dificuldade de respirar?", "pai": "6", "tipo": 2},

    "27": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "18", "tipo": 1},
    "30": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "19", "tipo": 1},
    "33": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "20", "tipo": 1},

    # ── O que é trauma (7) ────────────────────────────────────────────────────
    "21": {"texto": "Casos de Trauma incluem:", "pai": "7", "tipo": 1},
    "22": {"texto": "Acidentes de trânsito (carro, moto, bicicletas...)", "pai": "7", "tipo": 2},
    "23": {"texto": "Quedas de altura (escada, telhado, andaimes...)", "pai": "7", "tipo": 2},
    "24": {"texto": "Queimaduras extensas ou de grau elevado", "pai": "7", "tipo": 2},
    "25": {"texto": "Ferimentos por arma de fogo ou arma branca", "pai": "7", "tipo": 2},
    "26": {"texto": "Traumatismo cranioencefálico (pancada na cabeça)", "pai": "7", "tipo": 2},
    "65": {"texto": "Mordida por animais peçonhentos", "pai": "7", "tipo": 2},

    "54": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "22", "tipo": 1},
    "55": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "23", "tipo": 1},
    "56": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "24", "tipo": 1},
    "57": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "25", "tipo": 1},
    "58": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "26", "tipo": 1},
    "66": {"texto": "⚠️ Esse caso exige atendimento no Hospital de Trauma.", "pai": "65", "tipo": 1},

    # ── Não é trauma (8) ──────────────────────────────────────────────────────
    "37": {"texto": "Aqui iremos orientar e direcionar caso o seu atendimento não seja de Trauma.", "pai": "8", "tipo": 1},
    "38": {"texto": "Febre alta", "pai": "8", "tipo": 2},
    "39": {"texto": "Dor de ouvido", "pai": "8", "tipo": 2},
    "40": {"texto": "Sintomas de gripe", "pai": "8", "tipo": 2},
    "41": {"texto": "Dor de cabeça há dois dias", "pai": "8", "tipo": 2},
    "42": {"texto": "Onde fica a UPA mais próxima daqui?", "pai": "8", "tipo": 2},

    "43": {"texto": "Para febre, consulte uma UBS ou UPA dependendo da gravidade.", "pai": "38", "tipo": 1},
    "50": {"texto": "Dor de ouvido normalmente não é Trauma. Procure uma UBS ou UPA.", "pai": "39", "tipo": 1},
    "51": {"texto": "Para gripe sem complicações, repouso e hidratação em casa. Se piorar, procure uma UPA.", "pai": "40", "tipo": 1},
    "52": {"texto": "Para dores de cabeça sem trauma, procure uma UPA ou UBS.", "pai": "41", "tipo": 1},
    "53": {"texto": "Veja abaixo como encontrar atendimento próximo a você:", "pai": "42", "tipo": 1},

    # ── Resolver em casa (3) ──────────────────────────────────────────────────
    "9":  {"texto": "Primeiros socorros para ferimentos leves:", "pai": "3", "tipo": 1},
    "10": {"texto": "Me queimei com água quente. Como tratar?", "pai": "3", "tipo": 2},
    "11": {"texto": "Me machuquei e está sangrando.", "pai": "3", "tipo": 2},
    "12": {"texto": "Fui mordido(a) por um animal. O que faço?", "pai": "3", "tipo": 2},

    "59": {"texto": "Para queimaduras leves: água corrente por 10–20 min. NÃO use gelo, manteiga ou creme dental.", "pai": "10", "tipo": 1},
    "60": {"texto": "Lave o ferimento, pressione com pano limpo por 5–10 min e cubra com curativo estéril.", "pai": "11", "tipo": 1},
    "61": {"texto": "Lave o ferimento, identifique o animal e observe por 10 dias. Se necessário, vá ao Pronto Socorro.", "pai": "12", "tipo": 1},

    # ── Notificações sazonais (4) ─────────────────────────────────────────────
    "13": {"texto": "Cuidados sazonais por época do ano.", "pai": "4", "tipo": 1},
    "14": {"texto": "Quais cuidados devo ter no verão?", "pai": "4", "tipo": 2},
    "15": {"texto": "Como evitar doenças respiratórias no inverno?", "pai": "4", "tipo": 2},
    "16": {"texto": "Cuidados com a festa de São João.", "pai": "4", "tipo": 2},

    "62": {"texto": "No verão: hidrate-se, evite sol entre 10h–16h, use protetor solar FPS 30+.", "pai": "14", "tipo": 1},
    "63": {"texto": "No inverno: lave as mãos, evite aglomerações, use máscara se gripado(a) e vacine-se.", "pai": "15", "tipo": 1},
    "64": {"texto": "Na festa: cuidado com fogueiras, fogos de artifício, álcool e ambientes superlotados.", "pai": "16", "tipo": 1},
}

# ─── Funções de mídia ─────────────────────────────────────────────────────────

def _trauma(phone):
    send_video(phone, VIDEOS["urgencia"], "🚨 Dirija-se imediatamente ao Hospital de Trauma!")
    send_text(phone, LINKS["trauma"])

def _trauma_acidente(phone):
    send_image(phone, IMAGENS["acidente_transito"])
    send_video(phone, VIDEOS["urgencia"], "🚨 Dirija-se imediatamente ao Hospital de Trauma!")
    send_text(phone, LINKS["trauma"])

def _trauma_queda(phone):
    send_image(phone, IMAGENS["queda_altura"])
    send_video(phone, VIDEOS["urgencia"], "🚨 Dirija-se imediatamente ao Hospital de Trauma!")
    send_text(phone, LINKS["trauma"])

def _trauma_queimadura(phone):
    send_image(phone, IMAGENS["queimadura_grave"])
    send_video(phone, VIDEOS["urgencia"], "🚨 Dirija-se imediatamente ao Hospital de Trauma!")
    send_text(phone, LINKS["trauma"])

def _trauma_arma(phone):
    send_image(phone, IMAGENS["ferimento_arma"])
    send_video(phone, VIDEOS["urgencia"], "🚨 Dirija-se imediatamente ao Hospital de Trauma!")
    send_text(phone, LINKS["trauma"])

def _trauma_cranio(phone):
    send_image(phone, IMAGENS["traumatismo"])
    send_video(phone, VIDEOS["urgencia"], "🚨 Dirija-se imediatamente ao Hospital de Trauma!")
    send_text(phone, LINKS["trauma"])

def _trauma_animal(phone):
    send_image(phone, IMAGENS["mordida_animal"])
    send_video(phone, VIDEOS["urgencia"], "🚨 Dirija-se imediatamente ao Hospital de Trauma!")
    send_text(phone, LINKS["trauma"])

def _febre(phone):
    send_video(phone, VIDEOS["febre"], "ℹ️ Informações sobre febre")
    send_text(phone, LINKS["upa"])

def _dor_ouvido(phone):
    send_video(phone, VIDEOS["dor_ouvido"], "ℹ️ Informações sobre dor de ouvido")
    send_text(phone, LINKS["ubs"])

def _gripe(phone):
    send_video(phone, VIDEOS["gripe"], "ℹ️ Informações sobre gripe")
    send_image(phone, IMAGENS["gripe"])
    send_text(phone, LINKS["upa"])

def _dor_cabeca(phone):
    send_image(phone, IMAGENS["dor_cabeca"])
    send_text(phone, LINKS["upa"])

def _busca_upa(phone):
    send_text(phone, LINKS["upa"])
    send_text(phone, LINKS["ubs"])

def _queimadura_casa(phone):
    send_image(phone, IMAGENS["queimadura_casa"])
    send_video(phone, VIDEOS["resolver_casa"], "🏠 Como tratar em casa")

def _sangramento(phone):
    send_image(phone, IMAGENS["sangramento"])
    send_video(phone, VIDEOS["resolver_casa"], "🏠 Como tratar em casa")

def _mordida_animal(phone):
    send_image(phone, IMAGENS["mordida_animal"])
    send_video(phone, VIDEOS["mordida_animal"], "🐾 O que fazer após uma mordida")
    send_video(phone, VIDEOS["resolver_casa"], "🏠 Como tratar em casa")

def _verao(phone):
    send_image(phone, IMAGENS["verao"])
    send_video(phone, VIDEOS["verao"])

def _inverno(phone):
    send_image(phone, IMAGENS["inverno"])

def _sao_joao(phone):
    send_image(phone, IMAGENS["sao_joao"])
    send_video(phone, VIDEOS["sao_joao"])

def _atendimento_mais_proximo(phone):
    send_text(phone, LINKS["upa"])
    send_text(phone, LINKS["ubs"])
    send_text(phone, LINKS["trauma"])

MIDIA_POR_NO = {
    # Trauma genérico (perguntas de triagem)
    "27": _trauma, "30": _trauma, "33": _trauma,
    # Trauma com imagem específica
    "54": _trauma_acidente,
    "55": _trauma_queda,
    "56": _trauma_queimadura,
    "57": _trauma_arma,
    "58": _trauma_cranio,
    "66": _trauma_animal,
    # Não é trauma
    "43": _febre,
    "50": _dor_ouvido,
    "51": _gripe,
    "52": _dor_cabeca,
    "53": _busca_upa,
    # Resolver em casa
    "59": _queimadura_casa,
    "60": _sangramento,
    "61": _mordida_animal,
    # Sazonais
    "62": _verao,
    "63": _inverno,
    "64": _sao_joao,
    # Atendimento mais próximo
    "76": _atendimento_mais_proximo,
}

# ─── Índice pai → filhos ──────────────────────────────────────────────────────

def _build_children():
    children = {}
    for node_id, node in NODES.items():
        if node["tipo"] == 2:
            children.setdefault(node["pai"], []).append(node_id)
    return children

CHILDREN = _build_children()

# ─── Estado ───────────────────────────────────────────────────────────────────

user_state: dict = {}

def get_state(phone):
    return user_state.get(phone, {"etapa": "novo", "contexto": None, "historico": []})

def set_state(phone, state):
    user_state[phone] = state

# ─── Navegação ────────────────────────────────────────────────────────────────

def get_content_node(parent_id):
    for node_id, node in NODES.items():
        if node["pai"] == parent_id and node["tipo"] == 1:
            return node_id
    return None


def exibir_menu(phone, node_id, historico):
    node = NODES.get(node_id)
    if not node:
        send_text(phone, "❌ Opção não encontrada. Digite *menu* para recomeçar.")
        return

    send_text(phone, node["texto"])

    if node_id in MIDIA_POR_NO:
        MIDIA_POR_NO[node_id](phone)

    opcoes = CHILDREN.get(node_id, [])
    if opcoes:
        linhas = ["*Escolha uma opção:*\n"]
        for i, filho_id in enumerate(opcoes, start=1):
            linhas.append(f"{i}️⃣ {NODES[filho_id]['texto']}")
        linhas.append("\nResponda com o *número* da opção.")
        send_text(phone, "\n".join(linhas))
        set_state(phone, {"etapa": "aguardando_opcao", "contexto": node_id, "historico": historico})
    else:
        send_text(phone, "━━━━━━━━━━━━━━\nDigite *menu* para voltar ao início ou *voltar* para a opção anterior.")
        set_state(phone, {"etapa": "folha", "contexto": node_id, "historico": historico})


def handle_opcao(phone, escolha, contexto, historico):
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
    conteudo_id = get_content_node(filho_id)

    if conteudo_id:
        send_text(phone, NODES[conteudo_id]["texto"])
        if conteudo_id in MIDIA_POR_NO:
            MIDIA_POR_NO[conteudo_id](phone)
        subopcoes = CHILDREN.get(filho_id, [])
        if subopcoes:
            linhas = ["*Escolha uma opção:*\n"]
            for i, sub_id in enumerate(subopcoes, start=1):
                linhas.append(f"{i}️⃣ {NODES[sub_id]['texto']}")
            linhas.append("\nResponda com o *número* da opção.")
            send_text(phone, "\n".join(linhas))
            set_state(phone, {"etapa": "aguardando_opcao", "contexto": filho_id, "historico": novo_historico})
        else:
            send_text(phone, "━━━━━━━━━━━━━━\nDigite *menu* para voltar ao início ou *voltar* para a opção anterior.")
            set_state(phone, {"etapa": "folha", "contexto": filho_id, "historico": novo_historico})
    else:
        exibir_menu(phone, filho_id, novo_historico)


def ir_para_menu_principal(phone):
    send_text(phone, NODES["1"]["texto"])
    opcoes = CHILDREN.get("parent", [])
    linhas = ["*Escolha uma opção:*\n"]
    for i, filho_id in enumerate(opcoes, start=1):
        linhas.append(f"{i}️⃣ {NODES[filho_id]['texto']}")
    linhas.append("\nResponda com o *número* da opção.")
    send_text(phone, "\n".join(linhas))
    set_state(phone, {"etapa": "aguardando_opcao", "contexto": "parent", "historico": []})


# ─── Dispatcher ───────────────────────────────────────────────────────────────

def process_message(phone, body):
    state     = get_state(phone)
    etapa     = state.get("etapa", "novo")
    contexto  = state.get("contexto")
    historico = state.get("historico", [])
    texto     = body.strip().lower()

    print(f"[Bot] {phone} | etapa={etapa} | contexto={contexto} | msg='{texto}'")

    if texto == "voltar":
        if historico:
            exibir_menu(phone, historico[-1], historico[:-1])
        else:
            ir_para_menu_principal(phone)
        return

    if texto in ("menu", "inicio", "início", "oi", "olá", "ola", "reiniciar", "0"):
        send_text(phone, "👋 Bem-vindo(a) de volta!")
        ir_para_menu_principal(phone)
        return

    if etapa == "novo":
        send_text(phone, "👋 Olá! Bem-vindo(a) ao *Bot EVA* — seu assistente de saúde.")
        send_video(phone, VIDEOS["saudacao"], "Assista nossa apresentação!")
        ir_para_menu_principal(phone)
        return

    if etapa == "aguardando_opcao" and contexto:
        handle_opcao(phone, texto, contexto, historico)
        return

    if etapa == "folha":
        send_text(phone, "Digite *menu* para voltar ao início ou *voltar* para a opção anterior.")
        return

    send_text(phone, "Não entendi. Digite *menu* para recomeçar.")