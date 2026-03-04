from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():

    incoming_msg = request.form.get("Body").lower()

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in ["hi", "hello"]:
        reply = (
            "Welcome to SRM SAP Assistant 🤖\n\n"
            "1 View universities\n"
            "2 Find best university\n"
            "3 SAP details\n"
            "4 Compare universities\n"
            "5 Estimate SAP cost\n"
        )
    else:
        reply = "Please type 'Hi' to start the SAP assistant."

    msg.body(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)