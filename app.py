from flask import Flask, render_template,session,request,redirect,url_for

from flask_mail import Mail, Message
import random
import string
app= Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'barammanik@gmail.com'
app.config['MAIL_PASSWORD'] = 'hiyy cjhq qmwh gdfn'
app.config['MAIL_DEFAULT_SENDER'] = 'barammanik@gmail.com'

mail = Mail(app)



@app.route("/")
def index():
    return render_template(
        "base.html"
    )
    
@app.route("/send_message", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not name or not email or not message:
        return "All fields are required", 400

    try:
        msg = Message(
            subject=f"New message from {name}",
            recipients=["barammanik@gmail.com"],  
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)
        return "Message sent successfully!"
    except Exception as e:
        print("Error sending mail:", e)
        return "Failed to send message", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway এর PORT ব্যবহার করবে
    app.run(host="0.0.0.0", port=port)
