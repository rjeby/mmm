# test_user.py
import pytest
from src.domain.User import User, Roles

# Unit tests for the User class
class TestUser:

    def test_find_by_email(self, test_client):
        # Create a user
        user = User(email='test1@example.com', password='password123', role=Roles.USER)
        user.save_to_db()

        # Retrieve user by email
        retrieved_user = User.find_by_email('test1@example.com')

        assert retrieved_user == user
        assert retrieved_user.role == Roles.USER

    def test_find_all(self, test_client):
        # Add multiple users
        for i in range(1, 6):
            user = User(email=f'user{i}@example.com', password='password123', role=Roles.USER)
            user.save_to_db()

        # Retrieve all users
        retrieved_users = User.find_all(page=1, per_page=5)

        assert len(retrieved_users) == 5
        for user in retrieved_users:
            assert user.role == Roles.USER

    def test_update_db(self, test_client):
        # Create and retrieve an existing user
        user = User(email='test2@example.com', password='password123', role=Roles.USER)
        user.save_to_db()
        retrieved_user = User.find_by_email('test2@example.com')

        # Update user attributes
        retrieved_user.password = 'newpassword123'
        retrieved_user.role = Roles.ADMIN
        retrieved_user.update_db()

        updated_user = User.find_by_id(retrieved_user.id)

        assert updated_user.password == 'newpassword123'
        assert updated_user.role == Roles.ADMIN

    def test_delete_from_db(self, test_client):
        # Create and retrieve an existing user
        user = User(email='test3@example.com', password='password123', role=Roles.USER)
        user.save_to_db()
        retrieved_user = User.find_by_email('test3@example.com')

        # Delete user from the database
        retrieved_user.delete_from_db()

        # Retrieve user from the database
        retrieved_user = User.find_by_email('test3@example.com')

        assert retrieved_user is None
