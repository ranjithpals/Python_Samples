import findspark
findspark.init()
from pyspark.sql import SparkSession
# from pyspark.sql.functions import List
import xml.etree.ElementTree as eT
# import xmlschema
from collections import defaultdict
from pathlib import Path
from datetime import datetime

# Build a Spark Session
spark = SparkSession.builder.master("local[*]").appName("imo_solution").getOrCreate()

# Get the current directory
curr_dir = Path.cwd()
parent_dir = curr_dir.parent
# Construct the path to access the xml dataset.xml
file_path = parent_dir /'data_files/dataset.xml'
# Open the xml file for parsing
xml_data = eT.parse(file_path)
# Get the root of xml
root = xml_data.getroot()

# Check if the xml follows the xsd

# DefaultDict for storing the tags of the xml
records = defaultdict(tuple)

# Extract the xml data and convert it to dictionary
for node in root:
    date = datetime.strptime(node[4].text, "%d/%M/%Y")
    records[int(node[0].text)] = (int(node[0].text), int(node[1].text), int(node[2].text), int(node[3].text), node[4].text)

# Display the records from the dictionary
'''
for record in records.items():
    print(record)
'''
# xml schema
xml_schema = ['id', 'cust_id', 'quantity', 'price', 'date']
# create dataframe
df = spark.createDataFrame(records.values(), schema=xml_schema)

print(df.count())
df.show()

