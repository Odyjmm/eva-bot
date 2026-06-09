import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from bot import process_message

load_dotenv()

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Recebe mensagens do Twilio.
    O Twilio envia um form POST com os campos 'From' e 'Body'.
    """
    phone = request.form.get("From", "")   # ex: whatsapp:+5583999999999
    body  = request.form.get("Body", "").strip()

    print(f"[Webhook] Mensagem de {phone}: '{body}'")

    # Remove o prefixo "whatsapp:" para usar internamente
    phone_clean = phone.replace("whatsapp:", "")

    process_message(phone_clean, body)

    # Twilio exige uma resposta TwiML (pode ser vazia pois enviamos pelo cliente)
    resp = MessagingResponse()
    return str(resp), 200


@app.route("/", methods=["GET"])
def health():
    return "Bot EVA rodando!", 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"[Server] Iniciando na porta {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)
