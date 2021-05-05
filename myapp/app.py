from pathlib import Path
from typing import Generator, NamedTuple

import click
import click_pathlib


class Match(NamedTuple):
    file: Path
    line_number: int
    line: str


def grep(path: Path, substring: str) -> Generator[Match, None, None]:
    """
    Generator which search for the substring in all the files in the directory.
    Yields matches with lines containing the substring.
    """
    for file in path.rglob('*'):
        if file.is_file():
            try:
                with open(file) as f:
                    for line_number, line in enumerate(f, 1):
                        if substring in line:
                            yield Match(file, line_number, line.rstrip('\n'))
            except (UnicodeDecodeError, OSError):  # pragma: no cover
                pass


@click.command()
@click.argument('path', type=click_pathlib.Path(exists=True))
@click.argument('substring', type=str)
def run(path: Path, substring: str) -> None:
    """
    Search files in the specified directory for lines containing a specified substring.
    """
    for match in grep(path, substring):
        print(f'{match.file} line={match.line_number}: {match.line}')
