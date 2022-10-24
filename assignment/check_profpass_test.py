import pytest
import System


username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'



def test_check_password(grading_system):
    test = grading_system.check_password(username,profPass)
    test2 = grading_system.check_password(profUser,profPass)
    
    
    if test != test2:
        assert False

    


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
