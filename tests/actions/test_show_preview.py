from pro_filer.actions.main_actions import show_preview  # NOQA
from .test_data import context_with_values, empty_context


def test_show_preview_with_context_with_values(capsys):
    show_preview(context_with_values)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Found 3 files and 2 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\nFirst 5 directories: ['src', 'src/utils']\n"
    )


def test_show_preview_with_empty_context(capsys):
    show_preview(empty_context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
