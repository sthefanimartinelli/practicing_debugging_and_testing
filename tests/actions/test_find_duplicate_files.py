from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
from unittest.mock import patch
import pytest
import os


def test_find_duplicate_with_existing_files(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file3 = tmp_path / "file3.json"
    file1.touch()
    file2.touch()
    file3.touch()

    with patch(
        "pro_filer.actions.main_actions.filecmp.cmp",
        side_effect=[True, False, False],
    ):
        context = {"all_files": [str(file1), str(file2), str(file3)]}
        result = find_duplicate_files(context)

    assert result == [(str(file1), str(file2))]
    assert os.path.isfile(file1)
    assert os.path.isfile(file2)
    assert os.path.isfile(file3)


def test_find_duplicate_with_non_existing_file():
    context = {"all_files": ["file1.json", "file2.json"]}

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
