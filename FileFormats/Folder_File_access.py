import os.path
from pathlib import Path


# Convert string path to Path Object to access Folders/Files
print("Find File Path using Path object using Pathlib library")
current_path = Path.cwd()
print("Path Object: ", current_path)
parent_path = current_path.parent
print("Path Object: ", parent_path)
required_path = parent_path / "data_files/dataset.xml"
print("Path Object: ", required_path)
required_path_strFormat = required_path.as_posix()
print("Path Object as string: ", required_path_strFormat)

# Use string path to access Folders/Files
current_path = os.path.dirname(__file__)
print("String Object: ", current_path)
parent_path = os.path.split(current_path)[0]
print("String Object: ", parent_path)
# When joining paths, the directory holding the file should be represented by / in the end of the string
required_path = os.path.join(parent_path, "data_files/", "dataset.xml")
print("String Object: ", required_path)