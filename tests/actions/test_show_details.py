from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import patch
from datetime import datetime


def test_show_file_details(capsys):
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}

    with patch("os.path.exists", return_value=True), patch(
        "os.path.getsize", return_value=1024
    ), patch("os.path.isdir", return_value=False), patch(
        "os.path.splitext", return_value=("/home/trybe/Downloads", ".png")
    ), patch(
        "os.path.getmtime", return_value=datetime(2023, 1, 1).timestamp()
    ):

        show_details(context)

    captured = capsys.readouterr()
    assert "File name: Trybe_logo.png" in captured.out
    assert "File size in bytes: 1024" in captured.out
    assert "File type: file" in captured.out
    assert "File extension: .png" in captured.out
    assert "Last modified date: 2023-01-01" in captured.out


def test_show_details_without_directory(capsys):
    context = {"base_path": "/home/trybe/Downloads"}

    with patch("os.path.exists", return_value=True), patch(
        "os.path.getsize", return_value=22438
    ), patch("os.path.isdir", return_value=True), patch(
        "os.path.splitext", return_value=("/home/trybe/Downloads", "")
    ), patch(
        "os.path.getmtime", return_value=datetime(2023, 1, 1).timestamp()
    ):

        show_details(context)

    captured = capsys.readouterr()
    assert (
        captured.out
        == "File name: Downloads\nFile size in bytes: 22438\nFile type: directory\nFile extension: [no extension]\nLast modified date: 2023-01-01\n"
    )


def test_show_details_without_file(capsys):
    context = {"base_path": "/home/trybe/????"}

    with patch("os.path.exists", return_value=False):
        show_details(context)

    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"
