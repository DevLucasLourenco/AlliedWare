import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter", 'customtkinter','pathlib','pandas', 'sys', 'subprocess', 'json', 'datetime', 'enum', 'typing', 'PIL', 'logging']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Allied",
    version="0.1",
    description="AlliedWare by Lucas Lourenço",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)