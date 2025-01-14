from pro_filer.actions.main_actions import show_preview  # NOQA
from .test_data import (
    context_with_values,
    empty_context,
    context_with_six_files,
    context_with_six_dirs,
)


def test_show_preview_with_context_with_values(capsys):
    show_preview(context_with_values)
    captured = capsys.readouterr()
    expected_out = "Found 3 files and 2 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\nFirst 5 directories: ['src', 'src/utils']\n"
    assert captured.out == expected_out


def test_show_preview_with_empty_context(capsys):
    show_preview(empty_context)
    captured = capsys.readouterr()
    expected_out = "Found 0 files and 0 directories\n"
    assert captured.out == expected_out


def test_show_preview_with_more_than_five_files(capsys):
    show_preview(context_with_six_files)
    captured = capsys.readouterr()
    expected_out = f"Found 6 files and 2 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/utils/one.py', 'src/utils/two.py']\nFirst 5 directories: ['src', 'src/utils']\n"
    assert captured.out == expected_out


def test_show_preview_with_more_than_five_directories(capsys):
    show_preview(context_with_six_dirs)
    expected_out = f"Found 3 files and 6 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\nFirst 5 directories: ['src', 'src/utils', 'src/utils/one', 'src/utils/two', 'src/utils/three']\n"
    captured = capsys.readouterr()
    assert captured.out == expected_out
