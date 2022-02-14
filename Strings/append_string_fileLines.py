from pathlib import Path

# Get the Parent directory
parent_dir = Path.cwd().parent

# Display the Parent directory
print(parent_dir)

# Access the text file need to process
data_file = parent_dir / "data_files/tables.txt"
# Display the data file path
print(data_file)

file = open(data_file, "r")


def read_file():
    for line in open(data_file, "r"):
        yield line


# Open the file
with open(parent_dir / "data_files/data_file_mod.txt", "w") as f_out:
    mod_line = []
    ch = "'"
    for l in read_file():
        new_line = 'drop table '+'`'+l.rstrip()+'`'+';'+"\n"
        print(new_line)
        mod_line.append(new_line)

    f_out.writelines(mod_line)

print("Finished file processing")

# Close the modified file
f_out.close()