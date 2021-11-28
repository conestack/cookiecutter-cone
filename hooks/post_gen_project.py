import shutil
import os

options = {{dict(**cookiecutter)}}

optional_files = {
    "vscode_support": [".vscode"]
}

def purge_files():
    for k in optional_files:
        if options.get(k) in ("n", False, None):
            files = optional_files[k]
            for fname in files:
                print(f"removing file {fname}")
                shutil.rmtree(fname)


purge_files()