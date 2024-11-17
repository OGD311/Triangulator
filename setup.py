from cx_Freeze import setup, Executable

setup(
    name="AmIInSheffield?",
    version="69",
    description="Checks if you are in Sheffield",
    options={
        'build_exe': {
            'include_files': ['disTime.joblib'],
        }
    },
    executables=[Executable("distancifier.py")],
)
