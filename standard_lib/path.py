from pathlib import Path
from zipfile import ZipFile
from time import ctime

# path and directories

path = Path("ecommerce")
path.exists()
path.is_file()
path.rename("ecommerce2")
path.mkdir()
path.rmdir()
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.absolute())
for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]  # only return dir
py_files = [p for p in path.glob("**/*.py")]  # only py file
py_files = [p for p in path.rglob("*.py")]  # only py file
#  files

path = Path("ecommerce/__init__.py")
print(path.stat())
path.read_text()
path.unlink()
path.rename("fext.txt")
ctime(path.stat().st_atime)

with open("__init__.py", "r") as file:
    ...
path.write_bytes("sadf")
path.write_text("asdfasdf")


# working with zip file
with ZipFile("files", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo(("ecommerce"))
    info.file_size()
    info.compress_size()
    zip.extractall()
