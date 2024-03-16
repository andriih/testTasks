import pytest
from loggers import Loggers
from pathlib import Path


@pytest.fixture(scope="function")
def log_file_path(request):
    root_folder = Path.cwd() 
    log_file = root_folder / f"application.log"
    yield log_file
    if log_file.exists():
        log_file.unlink()


def test_log_file(log_file_path):
    """Test if log_message method creates the log file."""
    Loggers.log_message(str(log_file_path), "Test message", "INFO")
    assert log_file_path.exists()

def test_info_log(log_file_path):
    """Test if log_message method writes INFO log correctly."""
    Loggers.log_message(str(log_file_path), "Test info message", "INFO")
    with open(log_file_path, "r") as f:
        log_content = f.read()
    assert "[INFO] Test info message" in log_content

def test_log_warning_log(log_file_path):
    """Test if log_message method writes WARNING log correctly."""
    Loggers.log_message(str(log_file_path), "Test warning message", "WARNING")
    with open(log_file_path, "r") as f:
        log_content = f.read()
    assert "[WARNING] Test warning message" in log_content

def test_error_log(log_file_path):
    """Test if log_message method writes ERROR log correctly."""
    Loggers.log_message(str(log_file_path), "Test error message", "ERROR")
    with open(log_file_path, "r") as f:
        log_content = f.read()
    assert "[ERROR] Test error message" in log_content

def test_invalid_level(log_file_path):
    """Test if log_message method raises ValueError for invalid log level."""
    with pytest.raises(ValueError):
        Loggers.log_message(str(log_file_path), "Test message", "INVALID")