from ecommerce.shopping import sales
from pathlib import Path
from zipfile import ZipFile
sales.calc_tax()

# path and directories
# path = Path("ecommerce")
# path.exists()
# path.is_file()
# path.rename("ecommerce2")
# path.mkdir()
# path.rmdir()
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# print(path.absolute())

# for p in path.iterdir():
#     print(p)

#  files
# path = Path("ecommerce/__init__.py")
# print(path.stat())
# path.read_text()
# path.unlink()
# path.rename("fext.txt")

# with open("__init__.py", "r") as file:
#     ...

# path.write_bytes("sadf")
# path.write_text("asdfasdf")


# working with zip file
with ZipFile("files", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)
