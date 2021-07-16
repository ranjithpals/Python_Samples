import findspark
findspark.init()
import json
from pathlib import Path
from collections import defaultdict
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import IntegerType, StringType
from pyspark.sql import SparkSession

p_path = Path.cwd().parent
f_path = p_path /'data_files/mock_data.json'
# Create File Object in Read Mode
file = open(f_path, 'r')
# load the json data
json_data = json.load(file)
# Default dict to store values
json_dict = defaultdict(tuple)

# Convert JSON to dictionary with tuple values
for node in json_data:
    json_dict[node['id']] = (node['id'], node['first_name'], node['last_name'], node['email'], node['gender'], node['ip_address'])

print(json_dict.get(1))

spark = SparkSession.builder.master("local[*]").appName('json_parse').getOrCreate()
json_schema = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address']
df = spark.createDataFrame(json_dict.values(), schema=json_schema)

df.show()

