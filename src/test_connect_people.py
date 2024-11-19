import pytest
from findSomeone import findPerson
from unittest.mock import patch

def test_find_person(capsys, monkeypatch):
    # assert find person has working functionality
    with patch('builtins.input', return_value='Exit'):
        result = findPerson()
        captured = capsys.readouterr()
        assert "-=-=-=-=Welcome to the connection page=-=-=-=-" in captured.out, "Failed to display options"
