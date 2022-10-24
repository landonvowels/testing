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


def test_on_time(grading_system):
    course = grading_system.usr.all_courses['software_engineering']['assignments']
    due_date = course['assignment1']['due_date']
    onTimeBool = grading_system.usr.check_ontime("1/2/20",due_date)
    if onTimeBool is True:
        assert False
    onTimeBool = grading_system.usr.check_ontime("12/29/20",due_date)
    if onTimeBool is False:
        assert True
