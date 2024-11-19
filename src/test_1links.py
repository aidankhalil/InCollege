import pytest
from importantLinks import importantLinks
from usefulLinks import usefulLinks
from unittest.mock import patch

#only passes with "pytest -s test_links.py" and not "pytest -s"
def test_important_links(capsys, monkeypatch):
    # assert find person has working functionality
    with patch('builtins.input', return_value='Exit'):
        result = importantLinks()
        captured = capsys.readouterr()
        assert "-=-=-=-=Important Links Page=-=-=-=-" in captured.out, "Failed to display links"

def test_useful_links(capsys, monkeypatch):
    # assert find person has working functionality
    with patch('builtins.input', return_value='Exit'):
        result = usefulLinks()
        captured = capsys.readouterr()
        assert "\n-=-=-=-=Useful Links Page=-=-=-=-\n" in captured.out, "Failed to display links"