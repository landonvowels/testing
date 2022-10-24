import pytest
import System

username = 'calyam'
password =  '#yeet'
profuser = 'goggins'
profpass = 'augurrox'


def test_multlogin(grading_system):
    username = 'calyam'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)
    grading_system.login(profuser, profpass)
    if grading_system.users[profuser]['role'] != grading_system.usr.name:
        assert False
    
    
    


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
