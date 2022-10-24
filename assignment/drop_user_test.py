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


def test_drop_student(grading_system):
    grading_system.usr.drop_student('yted91', 'software_engineering')
    grading_system.reload_data()
    grading_system.login('yted91',"imoutofpasswordnames")
    if "software_engineering" in grading_system.usr.users['yted91']['courses']['software_engineering']:
        assert False
