# test_example.py
import pytest
from flask import render_template
import bcrypt
from src.domain.User import User, Roles
from flask_jwt_extended import create_access_token
from unittest.mock import patch
from src.DatabaseConfig import db  # Import db here


def test_user_registration(test_client):
    with patch('src.rest.AccountResource.send_activation_mail') as mock_send_mail:
        response = test_client.post('/api/register', json={
            'email': 'yassine442@gmail.com',
            'password': 'ValidPassw0rd!'
        })

    assert response.status_code == 201
    # To test if the the activation mail was sent only once
    mock_send_mail.assert_called_once()


def test_user_login(test_client):
    
    access_token = "Bearer " + create_access_token(identity='yassine442@gmail.com')
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }

    response = test_client.post('/api/login', json={
        'email': 'yassine442@gmail.com',
        'password': 'ValidPassw0rd!'
    })

    assert response.status_code == 200
    assert 'access_token' in response.json
    assert response.json['is_confirmed'] is False
    assert response.json['has_infos'] is False

# User confirmation success scenario
def test_user_confirmation(test_client):
    with patch('src.rest.AccountResource.confirm_token') as mock_confirm_token:
        mock_confirm_token.return_value = 'test@example.com'

        user = User(email='test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=False)
        user.save_to_db()

        response = test_client.get('/api/confirm/testtoken')

        # Render the expected activation.html template content
        with test_client.application.app_context():
            expected_content = render_template('activated.html')

        assert response.status_code == 200
        assert expected_content.encode() == response.data

        # Check if the user is confirmed
        updated_user = User.find_by_email('test@example.com')
        assert updated_user.is_confirmed

#  User not found: The email decoded from the token does not correspond to any user in the database.
def test_user_not_found(test_client):
    with patch('src.rest.AccountResource.confirm_token') as mock_confirm_token:
        mock_confirm_token.return_value = 'nonexistent@example.com'

        response = test_client.get('/api/confirm/testtoken')

        assert response.status_code == 404
        assert response.json['message'] == "Utilisateur non trouvé"

# Invalid token: The token provided is invalid or expired.
def test_invalid_token(test_client):
    with patch('src.rest.AccountResource.confirm_token') as mock_confirm_token:
        mock_confirm_token.side_effect = Exception("Invalid token")

        response = test_client.get('/api/confirm/invalidtoken')

        assert response.status_code == 400
        assert response.json['message'] == "Le lien de confirmation est invalide ou a expiré"

# User already confirmed: The user has already confirmed their email
def test_user_already_confirmed(test_client):
    with patch('src.rest.AccountResource.confirm_token') as mock_confirm_token:
        mock_confirm_token.return_value = 'already_user@example.com'

        user = User(email='already_user@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True)
        user.save_to_db()

        response = test_client.get('/api/confirm/testtoken')

        assert response.status_code == 200

        with test_client.application.app_context():
            expected_content = render_template('activated.html')
        assert expected_content.encode() in response.data

        updated_user = User.find_by_email('already_user@example.com')
        assert updated_user.is_confirmed

# User is found and not confirmed, and the activation email is successfully sent.
def test_user_new_confirmation_mail(test_client):
    with patch('src.rest.AccountResource.send_activation_mail') as mock_send_mail:
        user = User(email='user_new@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=False)
        user.save_to_db()

        access_token = create_access_token(identity=user.email)
        response = test_client.get('/api/resend', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json['message'] == "Un nouvel email de confirmation a été envoyé"
        mock_send_mail.assert_called_once_with(user)

# User is not found.
def test_resend_email_user_not_found(test_client):
    access_token = create_access_token(identity='user_nonexistent@example.com')
    response = test_client.get('/api/resend', headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 404
    assert response.json['message'] == "Utilisateur non trouvé"

# User is already confirmed.
def test_resend_email_already_confirmed(test_client):
    user = User(email='user_confirmed@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True)
    user.save_to_db()

    access_token = create_access_token(identity=user.email)
    response = test_client.get('/api/resend', headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 400
    assert response.json['message'] == "Votre compte est déjà activé"

# There is an error while sending the activation email.
def test_resend_email_failure_sending(test_client):
    with patch('src.rest.AccountResource.send_activation_mail', side_effect=Exception("Mail server error")) as mock_send_mail:
        user = User(email='error@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=False)
        user.save_to_db()

        access_token = create_access_token(identity=user.email)
        response = test_client.get('/api/resend', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json['message'] == "Impossible d'envoyer le mail"
        mock_send_mail.assert_called_once_with(user)

# User reset password with success
def test_forgot_password_success(test_client):
    with patch('src.rest.AccountResource.send_reset_mail') as mock_send_mail:
        user = User(email='mail_forgotten@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True)
        user.save_to_db()

        response = test_client.post('/api/forgot-password', json={'email': user.email})

        assert response.status_code == 200
        assert response.json['message'] == "Un email de réinitialisation de mot de passe a été envoyé"
        mock_send_mail.assert_called_once_with(user)

# reset password but user is not in the db
def test_forgot_password_user_not_found(test_client):
    response = test_client.post('/api/forgot-password', json={'email': 'nonexistent_in_db@example.com'})

    assert response.status_code == 404
    assert response.json['message'] == "Utilisateur non trouvé"

# User get valid token scenario
def test_reset_password_get_success(test_client):
    with patch('src.rest.AccountResource.confirm_token') as mock_confirm_token:
        mock_confirm_token.return_value = 'reset_pw@example.com'

        user = User(email='reset_pw@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True)
        user.save_to_db()

        response = test_client.get('/api/reset-password/testtoken')

        assert response.status_code == 200
        with test_client.application.app_context():
            expected_content = render_template('resetPassword.html')

        assert expected_content.encode() in response.data