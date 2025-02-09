from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import patch


def test_show_disk_usage_with_files(capsys, tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file1.touch()
    file2.touch()

    file_sizes = {str(file1): 3000, str(file2): 1000}
    with patch("os.path.getsize", side_effect=lambda path: file_sizes[path]):
        context = {"all_files": [str(file1), str(file2)]}
        show_disk_usage(context)

    captured = capsys.readouterr().out.splitlines()

    assert "file1.json" in captured[0] and "3000 (75%)" in captured[0]
    assert "file2.json" in captured[1] and "1000 (25%)" in captured[1]
