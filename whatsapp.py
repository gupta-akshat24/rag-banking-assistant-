from twilio.rest import Client
import os

def send_whatsapp_message(to_number, message):
    """
    Send WhatsApp message using Twilio API
    """
    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )

    formatted_message = f"""
    🏦 *Banking Assistant Response*
    ─────────────────────────
    {message}
    ─────────────────────────
    _Powered by RAG Banking Assistant_
    """

    client.messages.create(
        from_=f"whatsapp:{os.getenv('TWILIO_WHATSAPP_NUMBER')}",
        to=f"whatsapp:{to_number}",
        body=formatted_message
    )

    return True
