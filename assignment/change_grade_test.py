import pytest
import Staff
import System

profUser = 'goggins'
profPass = 'augurrox'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    gradingSystem.login(profUser,profPass)
    return gradingSystem

def test_change_grade(grading_system):
    grading_system.usr.change_grade('yted91',"cloud_computing", "assignment1", "100")
    grading_system.reload_data()
    grades = grading_system.usr.check_grades("yted91", "cloud_computing")
    if [1, 100] in grades:
        assert True
