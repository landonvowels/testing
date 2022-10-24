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


def test_create_assignment_(grading_system):
    grading_system.usr.create_assignment("assignment100", "1/1/70", "software_engineering")
    grading_system.reload_data()
    if "assignment100" in grading_system.usr.all_courses["software_engineering"]["assignments"]:
        assert True
