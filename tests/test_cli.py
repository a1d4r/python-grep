from pathlib import Path

from myapp import run


class TestCLI:
    """Test command line application (myapp.run)."""

    def test_one_file(self, dir_with_one_file, runner):
        path, file = dir_with_one_file
        result = runner.invoke(run, [str(path), 'Hello'])
        expected = f'{file} line=1: Hello, world!\n'
        assert result.output == expected

    def test_multiple_files(self, dir_with_two_files, runner):
        path, file1, file2 = dir_with_two_files
        expected = {
            f'{file1} line=1: print("Hello, world!")',
            f'{file2} line=2: world',
            '',
        }
        result = runner.invoke(run, [str(path), 'world'])
        assert set(result.output.split('\n')) == expected

    def test_multiline_file(self, dir_with_one_multiline_file, runner):
        path, file = dir_with_one_multiline_file
        expected = {f'{file} line=3: abc1', f'{file} line=7: qwertyabc', ''}
        result = runner.invoke(run, [str(path), 'abc'])
        assert set(result.output.split('\n')) == expected

    def test_file_in_nested_dirs(self, nested_dir_with_one_file, runner):
        path, file = nested_dir_with_one_file
        expected = {f'{file} line=1: text', ''}
        result = runner.invoke(run, [str(path), 'text'])
        assert set(result.output.split('\n')) == expected

    def test_no_matches(self, dir_with_three_files, runner):
        path, *_ = dir_with_three_files
        result = runner.invoke(run, [str(path), 'abc'])
        assert not result.output

    def test_path_does_not_exist(self, tmp_path: Path, runner):
        path = tmp_path / 'notexist'
        result = runner.invoke(run, [str(path), 'abc'])
        assert 'Error: Invalid' in result.output
