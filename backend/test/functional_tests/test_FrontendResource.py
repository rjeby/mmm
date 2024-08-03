# test/functional_tests/test_FrontendResource.py
import pytest
from unittest.mock import patch
from src.domain.User import User, Roles
from src.domain.Inscrit import Inscrit
from src.domain.Preferences import Preferences
from src.domain.MembreFamille import MembreFamille
from flask_jwt_extended import create_access_token


def test_formulaire_inscription_post_success(test_client):
    user = User(email='form_test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True, has_infos=False)
    user.save_to_db()

    access_token = create_access_token(identity=user.email)
    inscrits_json = {
        "prenom": "Abdo",
        "genre": "homme",
        "annee_naissance": 2001,
        "taille": 180,
        "poids": 70,
        "activite_legere": "0 min",
        "activite_moyenne": "30 min",
        "activite_elevee": "60 min",
        "perdre_poids": "Non",
        "code_postal": "38400"
    }

    response = test_client.post('/api/formulaire-inscription', json=inscrits_json, headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 201
    assert response.json['prenom'] == "Abdo"
    assert response.json['genre'] == "homme"


def test_inscrit_infos_get_success(test_client):
    user = User(email='inscrit_get_test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True, has_infos=True)
    user.save_to_db()
    inscrit = Inscrit(user_id=user.id, prenom="John", genre="homme", annee_naissance=1990, taille=180, poids=90, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="Yes", code_postal="90000")
    inscrit.save_to_db()

    access_token = create_access_token(identity=user.email)

    response = test_client.get('/api/mes-infos', headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200
    assert response.json['prenom'] == "John"
    assert response.json['genre'] == "homme"

def test_inscrit_infos_put_success(test_client):
    user = User(email='inscrit_put_test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True, has_infos=True)
    user.save_to_db()
    inscrit = Inscrit(user_id=user.id, prenom="Ibrahimovich", genre="homme", annee_naissance=1988, taille=180, poids=90, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="Yes", code_postal="90000")
    inscrit.save_to_db()

    access_token = create_access_token(identity=user.email)
    updated_json = {
        "prenom": "Jane",
        "genre": "femme"
    }

    response = test_client.put('/api/mes-infos', json=updated_json, headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200
    assert response.json['message'] == "Inscrit mis à jour avec succès"
    updated_inscrit = user.inscrit
    assert updated_inscrit.prenom == "Jane"
    assert updated_inscrit.genre == "femme"

def test_inscrit_preferences_get_success(test_client):
    user = User(email='preference_get_test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True, has_infos=True)
    user.save_to_db()
    inscrit = Inscrit(user_id=user.id, prenom="Ibrahimovich", genre="homme", annee_naissance=1988, taille=180, poids=90, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="Yes", code_postal="90000")
    inscrit.save_to_db()
    preferences = Preferences(inscrit_id=inscrit.id, type_alimentation="Méditerranéenne", difficulte_menu="Facile")
    preferences.save_to_db()

    access_token = create_access_token(identity=user.email)

    response = test_client.get('/api/mes-preferences', headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200
    assert response.json['type_alimentation'] == "Méditerranéenne"
    assert response.json['difficulte_menu'] == "Facile"

def test_inscrit_preferences_put_success(test_client):
    user = User(email='preference_put_test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True, has_infos=True)
    user.save_to_db()
    inscrit = Inscrit(user_id=user.id, prenom="Ibrahimovich", genre="homme", annee_naissance=1988, taille=180, poids=90, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="Yes", code_postal="90000")
    inscrit.save_to_db()
    preferences = Preferences(inscrit_id=inscrit.id, type_alimentation="Méditerranéenne", difficulte_menu="Facile")
    preferences.save_to_db()

    access_token = create_access_token(identity=user.email)
    updated_json = {
        "type_alimentation": "Végétarienne",
        "difficulte_menu": "Moyenne"
    }

    response = test_client.put('/api/mes-preferences', json=updated_json, headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200
    assert response.json['message'] == "Préférences mises à jour avec succès"
    updated_preferences = Preferences.find_by_inscrit_id(inscrit.id)
    assert updated_preferences.type_alimentation == "Végétarienne"
    assert updated_preferences.difficulte_menu == "Moyenne"


def test_inscrit_famille_get_success(test_client):
    user = User(email='famille_get_test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True, has_infos=True)
    user.save_to_db()
    inscrit = Inscrit(user_id=user.id, prenom="Ibrahimovich", genre="homme", annee_naissance=1988, taille=180, poids=90, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="Yes", code_postal="90000")
    inscrit.save_to_db()
    member1 = MembreFamille(inscrit_id=inscrit.id, prenom="Marie", genre="femme", annee_naissance=2010, taille=140, poids=40, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="No")
    member2 = MembreFamille(inscrit_id=inscrit.id, prenom="Bob", genre="homme", annee_naissance=2008, taille=150, poids=50, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="No")
    member1.save_to_db()
    member2.save_to_db()

    access_token = create_access_token(identity=user.email)

    response = test_client.get('/api/ma-famille', headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['prenom'] == "Marie"
    assert response.json[1]['prenom'] == "Bob"

def test_inscrit_famille_put_success(test_client):
    user = User(email='famille_put_test@example.com', password='ValidPassw0rd', role=Roles.USER, is_confirmed=True, has_infos=True)
    user.save_to_db()
    inscrit = Inscrit(user_id=user.id, prenom="Ibrahimovich", genre="homme", annee_naissance=1988, taille=180, poids=90, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="Yes", code_postal="90000")
    inscrit.save_to_db()
    member1 = MembreFamille(inscrit_id=inscrit.id, prenom="Alice", genre="femme", annee_naissance=2010, taille=140, poids=40, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="No")
    member2 = MembreFamille(inscrit_id=inscrit.id, prenom="Bob", genre="homme", annee_naissance=2008, taille=150, poids=50, activite_legere="0 min", activite_moyenne="30 min", activite_elevee="60 min", perdre_poids="No")
    member1.save_to_db()
    member2.save_to_db()

    access_token = create_access_token(identity=user.email)
    updated_json = [
        {"prenom": "Charlie", "genre": "homme", "annee_naissance": 2012, "taille": 130, "poids": 35, "activite_legere": "0 min", "activite_moyenne": "30 min", "activite_elevee": "60 min", "perdre_poids": "No"},
        {"prenom": "Dana", "genre": "femme", "annee_naissance": 2006, "taille": 160, "poids": 55, "activite_legere": "0 min", "activite_moyenne": "30 min", "activite_elevee": "60 min", "perdre_poids": "No"}
    ]

    response = test_client.put('/api/ma-famille', json=updated_json, headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200
    assert response.json['message'] == "Membres de la famille mis à jour avec succès"
    updated_family = user.inscrit.membres_famille
    assert updated_family[0].prenom == "Charlie"
    assert updated_family[1].prenom == "Dana"
