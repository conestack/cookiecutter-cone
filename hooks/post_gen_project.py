import shutil
import os

options = {{dict(**cookiecutter)}}

# declaration of files to delete
# delete files that are bound to an option
# if the option is a list, then one of the options is sufficient for the files to be kept
optional_files = [
    ("vscode_support", [".vscode"]),
    ("tests", ["src/{{cookiecutter.project_path}}/tests"]),
    ("buildout", ["buildout.cfg", "dev.cfg"]),
    (("buildout", "runnable"), ["dev.ini"]),
    ("makefile", ["sources.ini", "Makefile", "requirements_barebone.txt", "constraints.txt"])
]


def purge_files():
    """
    delete files that for which the option is "n" or False
    """
    for keys, files in optional_files:
        if not isinstance(keys, (list, tuple)):
            keys = (keys,)

        # if none of the keys is positive we delete the file
        if all([options.get(k) in ("n", False) for k in keys]):
            for fname in files:
                if os.path.exists(fname):
                    print(f"removing file {fname}")
                    if os.path.isdir(fname):
                        os.rmdir(fname)
                    else:
                        os.remove(fname)



purge_files()