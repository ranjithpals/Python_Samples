import os.path
from pathlib import Path
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime

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

# Sample XML with tag, attribute
'''
<?xml version="1.0" encoding="utf-8"?>
<Event status="happened">
    <Song title="Erase and rewind">
        <Artist name="The Cardigans" ID="340900"></Artist>
        <Info StartTime="22:22:13" JazlerID="8310" PlayListerID="" />
    </Song>
</Event>
'''

# Get the xml tree
tree = ET.parse('C:/Users/Owner/Documents/Python/Python_Samples/data_files/tag_attribute.xml')
# Get the root of the xml
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    for x in child:
        print(x.tag, x.attrib)
        for key in x.attrib:
            value = x.attrib.get(key)
            if value:
                print(key, "= ", value)

# Get the xml tree
tree = ET.parse(required_path_strFormat)

# Get the root of the xml
root = tree.getroot()

# Create a Dictionary holding the XML data
xml_dict = defaultdict(tuple)

for child in root:
    # print(child.tag, child.attrib)
    date = datetime.strptime(child[4].text, "%d/%M/%Y")
    xml_dict[int(child[0].text)] = (int(child[1].text), int(child[2].text), int(child[3].text), date)

# print(root[0][1].text)

for key, value in dict(xml_dict).items():
    print(key, " = ", value)







