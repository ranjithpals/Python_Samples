import findspark
findspark.init()
from pyspark.sql import SparkSession
from pathlib import Path
import xml.etree.ElementTree as ET

# Current Directory
p_path = Path.cwd().parent
# xml location
d_path = p_path /'data_files/dataset.xml'

# Create Spark Session
spark = SparkSession.builder.master("local[*]").appName("read_xml_SparkDF").getOrCreate()

# Read XML file
xml_rdd = spark.read.text(d_path.as_posix(), wholetext=True).rdd
'''
xml_df = spark.read \
        .format("xml") \
        .option("path", d_path.as_posix()) \
        .load()
'''
root = ET.fromstring(xml_rdd.take(1)[0][0])
# Count of df
for child in root:
    print(child.tag, child[1].text)

# Parse XML to convert to Spark DataFrame
# https://www.linkedin.com/pulse/parsing-xml-file-using-pyspark-part-1-author-deepika-sharma-/?trk=public_profile_article_view