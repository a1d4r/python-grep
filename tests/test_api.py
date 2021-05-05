import pytest

from myapp import Match, grep


class TestAPI:
    def test_one_file(self, dir_with_one_file):
        path, file = dir_with_one_file
        match = Match(file, 1, 'Hello, world!')
        gen = grep(path, 'Hello')
        assert next(gen) == match
        with pytest.raises(StopIteration):
            next(gen)

    def test_multiple_files(self, dir_with_two_files):
        path, file1, file2 = dir_with_two_files
        expected = {Match(file1, 1, 'print("Hello, world!")'), Match(file2, 2, 'world')}
        gen = grep(path, 'world')
        actual = set(gen)
        assert actual == expected

    def test_multiline_file(self, dir_with_one_multiline_file):
        path, file = dir_with_one_multiline_file
        expected = {Match(file, 3, 'abc1'), Match(file, 7, 'qwertyabc')}
        gen = grep(path, 'abc')
        actual = set(gen)
        assert actual == expected

    def test_file_in_nested_dirs(self, nested_dir_with_one_file):
        path, file = nested_dir_with_one_file
        expected = {Match(file, 1, 'text')}
        gen = grep(path, 'text')
        actual = set(gen)
        assert actual == expected

    def test_no_matches(self, dir_with_three_files):
        path, *_ = dir_with_three_files
        gen = grep(path, 'abc')
        with pytest.raises(StopIteration):
            next(gen)
