import pytest
from django.contrib.auth.models import User
from cakestore.forms import RegisterUserForm

@pytest.mark.django_db  # Mark this test to use the database
class TestRegisterUserForm:
    
    def test_register_user_form_valid(self):
        """Test that the form is valid with correct data."""
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123'
        }
        form = RegisterUserForm(data=data)
        assert form.is_valid()  # Form should be valid

    def test_register_user_form_invalid_email(self):
        """Test that the form is invalid with an invalid email."""
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalidemail',  # Invalid email
            'password1': 'securepassword123',
            'password2': 'securepassword123'
        }
        form = RegisterUserForm(data=data)
        assert not form.is_valid()  # Form should be invalid
        assert 'email' in form.errors  # Email field should be in errors

    def test_register_user_form_passwords_mismatch(self):
        """Test that the form is invalid if passwords do not match."""
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'securepassword123',
            'password2': 'differentpassword'  # Mismatched password
        }
        form = RegisterUserForm(data=data)
        assert not form.is_valid()  # Form should be invalid
        assert form.errors['password2'] == ['The two password fields didn’t match.']  # Check for specific error

    def test_register_user_form_no_data(self):
        """Test that the form is invalid with no data."""
        form = RegisterUserForm(data={})
        assert not form.is_valid()  # Form should be invalid
        assert 'username' in form.errors  # Username field should be in errors
        assert 'password1' in form.errors  # Password1 field should be in errors
        assert 'password2' in form.errors  # Password2 field should be in errors

    def test_form_fields_widget_attributes(self):
        """Test that form fields have the correct widget attributes."""
        form = RegisterUserForm()
        assert form.fields['username'].widget.attrs['class'] == 'form-control'
        assert form.fields['first_name'].widget.attrs['class'] == 'form-control'
        assert form.fields['last_name'].widget.attrs['class'] == 'form-control'
        assert form.fields['email'].widget.attrs['class'] == 'form-control'
        assert form.fields['password1'].widget.attrs['class'] == 'form-control'
        assert form.fields['password2'].widget.attrs['class'] == 'form-control'
