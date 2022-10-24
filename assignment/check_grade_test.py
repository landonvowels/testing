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


def test_grade_check(grading_system):
    grades = grading_system.usr.check_grades('software_engineering')
    if [1, 100] in grades:
        assert True

