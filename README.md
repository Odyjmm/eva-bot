# 🤖 Bot EVA — Assistente de Saúde via WhatsApp

Bot de triagem de saúde para WhatsApp desenvolvido em Python, capaz de orientar pacientes sobre urgências, primeiros socorros e encaminhamento para UBS ou hospital de Trauma.

---

## 📁 Estrutura do projeto

```
eva-bot/
├── main.py          → Servidor Flask + webhook
├── bot.py           → Lógica de navegação e fluxo de conversa
├── whatsapp.py      → Funções de envio (texto, imagem, vídeo, localização)
├── requirements.txt → Dependências Python
└── .env.example     → Modelo de variáveis de ambiente
```

---

## ⚙️ Pré-requisitos

- Python 3.10 ou superior
- Conta gratuita no [Twilio](https://twilio.com)
- Conta gratuita no [ngrok](https://ngrok.com)

---

## 🚀 Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/eva-bot.git
cd eva-bot
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

Edite o `.env`:

```
ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_NUMBER=whatsapp:+14155238886
PORT=5000
```

> As credenciais estão disponíveis no painel do Twilio em **Account Info**.

### 4. Inicie o servidor

```bash
python main.py
```

### 5. Exponha o servidor com ngrok

Em outro terminal:

```bash
ngrok http 5000
```

Copie a URL gerada, ex: `https://abc123.ngrok-free.app`

### 6. Configure o webhook no Twilio

1. Acesse [console.twilio.com](https://console.twilio.com)
2. Vá em **Messaging → Try it out → Send a WhatsApp message**
3. Conecte seu número ao sandbox enviando a mensagem indicada para `+1 415 523 8886`
4. Em **Sandbox Settings**, cole no campo **"When a message comes in"**:
   ```
   https://abc123.ngrok-free.app/webhook
   ```
5. Clique em **Save**

### 7. Teste

Mande qualquer mensagem para `+1 415 523 8886` no WhatsApp e o bot responderá.

---

## 💬 Comandos disponíveis

| Comando | Ação |
|---|---|
| `oi` / `olá` / `menu` | Reinicia e exibe o menu principal |
| `voltar` | Retorna ao nível anterior do menu |
| `0` | Volta ao menu principal |

---

## 🛠️ Personalização

Para editar o fluxo de triagem, altere o dicionário `NODES` em `bot.py`. Cada nó tem:

- `texto` → mensagem enviada ao usuário
- `pai` → ID do nó pai (`"parent"` para raiz)
- `tipo` → `1` = conteúdo informativo, `2` = opção de menu

