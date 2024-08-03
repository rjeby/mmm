from flask_mail import Mail, Message
from flask import render_template, url_for
from src.config import Config
from itsdangerous import URLSafeTimedSerializer

mail = Mail()


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    return serializer.dumps(email, salt=Config.SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        email = serializer.loads(
            token, salt=Config.SECURITY_PASSWORD_SALT, max_age=expiration
        )
    except:
        return False
    return email


def send_activation_mail(user):
    token = generate_confirmation_token(user.email)
    confirm_url = url_for("account-resource_confirm_email", token=token, _external=True)
    html = render_template("activation.html", confirm_url=confirm_url)
    subject = "Confirmez votre inscription au programme MMMenus"
    send_mail(subject, user.email, html)


def send_reset_mail(user):
    token = generate_confirmation_token(user.email)
    reset_url = url_for("account-resource_reset_password", token=token, _external=True)
    html = render_template("resetEmail.html", reset_url=reset_url)
    subject = "Réinitialisation du Mot de Passe"
    send_mail(subject, user.email, html)


def send_mail(subject, recipient, body):
    msg = Message(
        subject=subject, sender=Config.MAIL_DEFAULT_SENDER, recipients=[recipient]
    )
    msg.html = body
    mail.send(msg)
