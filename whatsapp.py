import os
from twilio.rest import Client

ACCOUNT_SID  = os.getenv("ACCOUNT_SID")
AUTH_TOKEN   = os.getenv("AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER", "whatsapp:+14155238886")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def _fmt(number: str) -> str:
    """Garante que o número esteja no formato whatsapp:+55..."""
    if not number.startswith("whatsapp:"):
        return f"whatsapp:{number}"
    return number


def send_text(to: str, message: str):
    """Envia uma mensagem de texto simples."""
    msg = client.messages.create(
        from_=TWILIO_NUMBER,
        to=_fmt(to),
        body=message,
    )
    print(f"[Twilio] Texto enviado → SID: {msg.sid}")
    return msg


def send_image(to: str, image_url: str, caption: str = ""):
    """Envia uma imagem com legenda opcional."""
    msg = client.messages.create(
        from_=TWILIO_NUMBER,
        to=_fmt(to),
        body=caption,
        media_url=[image_url],
    )
    print(f"[Twilio] Imagem enviada → SID: {msg.sid}")
    return msg


def send_video(to: str, video_url: str, caption: str = ""):
    """Envia um vídeo com legenda opcional."""
    msg = client.messages.create(
        from_=TWILIO_NUMBER,
        to=_fmt(to),
        body=caption,
        media_url=[video_url],
    )
    print(f"[Twilio] Vídeo enviado → SID: {msg.sid}")
    return msg


def send_location(to: str, lat: float, lng: float, name: str = "", address: str = ""):
    """
    Envia uma localização via Google Maps (Twilio não suporta location nativo).
    Envia o nome, endereço e link clicável do Maps.
    """
    maps_url = f"https://maps.google.com/?q={lat},{lng}"
    body = f"📍 *{name}*\n{address}\n{maps_url}"
    return send_text(to, body)


def send_menu(to: str, header: str, body: str, options: list, footer: str = ""):
    """
    Envia um menu numerado de opções via texto formatado.
    O Twilio sandbox não suporta botões interativos nativos,
    então usamos um menu textual numerado.

    Exemplo de options:
    [
        {"id": "1", "title": "Ver localização"},
        {"id": "2", "title": "Ver imagens"},
    ]
    """
    lines = [f"*{header}*\n", body, ""]
    for opt in options:
        lines.append(f"{opt['id']}️⃣ {opt['title']}")
    if footer:
        lines.append(f"\n_{footer}_")
    lines.append("\nResponda com o *número* da opção desejada.")

    return send_text(to, "\n".join(lines))
