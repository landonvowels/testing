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


def test_view_assignment(grading_system):
    assignments = grading_system.usr.view_assignments("software_engineering")
    if [0, "1/1/20"] in assignments:
        assert True
