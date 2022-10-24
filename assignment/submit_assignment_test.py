import pytest
import Student
import System

username = 'hdjsr7'
password = 'pass1234'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    gradingSystem.login('hdjsr7','pass1234')
    return gradingSystem


def test_submit_assignment(grading_system):
    grading_system.usr.submit_assignment("software_engineering", "assignment1", "hi!", "01/01/70")
    assignments = grading_system.usr.view_assignments("software_engineering")
    if [0, "01/01/70"] in assignments:
        assert True
    else:
        assert False
