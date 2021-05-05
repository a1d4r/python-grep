from pathlib import Path
from typing import Tuple

import pytest
from click.testing import CliRunner


@pytest.fixture()
def runner():
    """Create runner for command line application."""
    return CliRunner()


@pytest.fixture()
def dir_with_one_file(tmp_path: Path) -> Tuple[Path, Path]:
    """Create one file and return paths to directory and file."""
    file = tmp_path / 'f1.txt'
    file.write_text('Hello, world!')
    return tmp_path, file


@pytest.fixture()
def dir_with_two_files(tmp_path: Path) -> Tuple[Path, Path, Path]:
    """Create two files and return paths to directory and these files."""
    file1 = tmp_path / 'f1.py'
    file1.write_text('print("Hello, world!")')
    file2 = tmp_path / 'f2.txt'
    file2.write_text('hello\nworld')
    return tmp_path, file1, file2


@pytest.fixture()
def dir_with_one_multiline_file(tmp_path: Path) -> Tuple[Path, Path]:
    """Create one file with multiple lines and return paths to directory and file."""
    file = tmp_path / 'file.txt'
    file.write_text('\n\nabc1\nABC\naabbcc\na b c\nqwertyabc')
    return tmp_path, file


@pytest.fixture()
def nested_dir_with_one_file(tmp_path: Path) -> Tuple[Path, Path]:
    """Create one file inside nested directories and return paths to directory and file."""
    dir_ = tmp_path / 'dir1' / 'dir2' / 'dir3'
    dir_.mkdir(parents=True)
    file = dir_ / 'FILENAME'
    file.write_text('text')
    return tmp_path, file


@pytest.fixture()
def dir_with_three_files(tmp_path: Path) -> Tuple[Path, Path, Path, Path]:
    """Create three files and return paths to directory and these files."""
    file1 = tmp_path / 'file1.txt'
    file1.write_text('content of file1')
    file2 = tmp_path / 'file2.txt'
    file2.write_text('content of file2')
    file3 = tmp_path / 'file3.txt'
    file3.write_text('content of file3')
    return tmp_path, file1, file2, file3
