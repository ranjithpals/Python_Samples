import xml.etree.ElementTree as eT
from pathlib import Path

# Find the path of the xml file
dir_path = Path.cwd()
parent = dir_path.parent
file_path = parent / 'data_files/tag_attrib_value.xml'

xml = eT.parse(file_path)
# Get root node
root = xml.getroot()

for node in root:
    print(node.tag, node.attrib)

# Find all nodes which have child node 'country'
for node in root.findall('country'):
    print(node.find('rank').text, node.get('name'))

# Find all attributes and values for the sub-node neighbor
for attrib in root.iter('neighbor'):
    print(attrib.attrib)


