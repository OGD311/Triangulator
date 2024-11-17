from cx_Freeze import setup, Executable

setup(
    name="AmIInSheffield?",
    version="69",
    description="Checks if you are in Sheffield",
    options={
        'build_exe': {
            'packages': ['joblib', 'numpy', 'sklearn', 'time', 'pythonping', 'haversine', 'json', 'random', 'webbrowser', 'scipy'],  # Added scikit-learn package
            'include_files': ['disTime.joblib'],
        }
    },
    executables=[Executable("distancifier.py", icon="path/to/your/icon.ico")],
)