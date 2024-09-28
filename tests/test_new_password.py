import string
import random
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_equaling():
    for i in range(100):
        integ = random.randint(1,100)
        password = generate_password(integ)
        assert len(password) == integ


def test_compare():
    for i in range(10):
        first = generate_password(3)
        second = generate_password(3)
        assert first != second
