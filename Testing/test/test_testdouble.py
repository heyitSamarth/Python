from LineReader import readFromFile
from unittest.mock import MagicMock

def test_returnCorrectString(monkeypatch):
    mock_file=MagicMock()
    mock_file.readline=MagicMock(return_value="test line")
    mock_open=MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open",mock_open)
    result=readFromFile("blah")
    mock_open.assert_called_once_with("blah","r")
    assert result=="test line"