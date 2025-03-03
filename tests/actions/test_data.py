context_with_values = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"],
}

empty_context = {"all_files": [], "all_dirs": []}

context_with_six_files = {
    "all_files": [
        "src/__init__.py",
        "src/app.py",
        "src/utils/__init__.py",
        "src/utils/one.py",
        "src/utils/two.py",
        "src/utils/three.py",
    ],
    "all_dirs": ["src", "src/utils"],
}

context_with_six_dirs = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": [
        "src",
        "src/utils",
        "src/utils/one",
        "src/utils/two",
        "src/utils/three",
        "src/utils/four",
    ],
}
