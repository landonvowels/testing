import pytest
import System

username = 'calyam'
password =  '#yeet'

def test_login(grading_system):
    username = 'calyam'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
