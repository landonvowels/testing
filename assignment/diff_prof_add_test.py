import pytest
import Professor
import System

profUser = 'goggins'
profPass = 'augurrox'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    gradingSystem.login(profUser,profPass)
    return gradingSystem


def test_add_student(grading_system):
    grading_system.usr.add_student('yted91', 'comp_sci')
    grading_system.reload_data()
    grading_system.login('yted91',"imoutofpasswordnames")
    if "comp_sci" in grading_system.usr.users['yted91']['courses']:
        assert True
