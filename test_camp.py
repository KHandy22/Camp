from unittest.mock import patch
import task1
import task2


# Task 1 Tests - Camp Registration Input

@patch('builtins.input', side_effect=[
    'Alice',
    'Johnson',
    '2012',
    '5',
    'Robert',
    'Johnson',
    '615-555-1234',
    '123 Main Street',
    'Clarksville',
    'TN',
    '37040'
])
def test_task1_sample1(mock_input, capsys):
    task1.main()
    captured = capsys.readouterr().out

    assert "Camper's Name: Alice Johnson" in captured
    assert "Birth Year: 2012" in captured
    assert "Camp Duration: 5 days" in captured
    assert "Parent's Name: Robert Johnson" in captured
    assert "Phone Number: 615-555-1234" in captured
    assert "123 Main Street" in captured
    assert "Clarksville, TN 37040" in captured


@patch('builtins.input', side_effect=[
    'Marcus',
    'Williams',
    '2015',
    '3',
    'Keisha',
    'Williams',
    '931-555-9876',
    '456 Oak Avenue',
    'Nashville',
    'TN',
    '37201'
])
def test_task1_sample2(mock_input, capsys):
    task1.main()
    captured = capsys.readouterr().out

    assert "Camper's Name: Marcus Williams" in captured
    assert "Birth Year: 2015" in captured
    assert "Camp Duration: 3 days" in captured
    assert "Parent's Name: Keisha Williams" in captured
    assert "Phone Number: 931-555-9876" in captured
    assert "456 Oak Avenue" in captured
    assert "Nashville, TN 37201" in captured


# Task 2 Tests - Type Conversion

def test_task2_birth_is_int():
    assert isinstance(task2.birth, int)


def test_task2_days_is_int():
    assert isinstance(task2.days, int)


def test_task2_first_is_str():
    assert isinstance(task2.first, str)


def test_task2_last_is_str():
    assert isinstance(task2.last, str)


def test_task2_p_first_is_str():
    assert isinstance(task2.p_first, str)


def test_task2_p_last_is_str():
    assert isinstance(task2.p_last, str)


def test_task2_phone_is_str():
    assert isinstance(task2.phone, str)


def test_task2_street_is_str():
    assert isinstance(task2.street, str)


def test_task2_city_is_str():
    assert isinstance(task2.city, str)


def test_task2_state_is_str():
    assert isinstance(task2.state, str)


def test_task2_zip_code_is_str():
    assert isinstance(task2.zip_code, str)
