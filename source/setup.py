#setup.py
from cx_Freeze import setup, Executable
setup(
    name = "IOTA-SeedGenerator",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["os","sys"],
        'include_msvcr': True,
    }},
    executables = [Executable("seed-generator.py",base="Win32GUI")]
    )
