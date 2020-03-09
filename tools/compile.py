from cx_Freeze import setup, Executable

setup(
        name = "MyProgName",
        version = "1.0",
        description = "My program description",
        executables = [Executable("main.py")]
)



