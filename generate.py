import os
import re
import sys
import glob
import json
import cairosvg
import subprocess

manifest_data = {}
input_files = glob.glob("./vectors/*/*.svg")

def guard(result):
    if not result:
        raise Exception("Guard failed!")

for input_file in input_files:
    print("Parsing " + input_file + "...")
    
    filename = "".join(input_file.split("/")[-1:])[:-4]
    directory = "/".join(input_file.split("/")[:-1]) + "/"
    issuer = directory[10:-1]

    output_directory = "./dist/" + issuer
    output_file = output_directory + "/" + filename + ".png"

    safe_output_directory = re.sub(r"[^A-z0-9-\./]+", "", output_directory)
    safe_output_file = re.sub(r"[^A-z0-9-\./]+", "", output_file)
    safe_input_file = re.sub(r"[^A-z0-9-\./]+", "", input_file)

    try:
        guard(len(safe_output_directory.split(".")) == 2)
        guard(len(safe_output_directory.split("/")) == 3)
        guard(len(safe_output_file.split(".")) == 3)
        guard(len(safe_output_file.split("/")) == 4)
        guard(len(safe_input_file.split(".")) == 3)
        guard(len(safe_input_file.split("/")) == 4)

        with open(directory + "information.json", "r") as information_handle:
            information = json.loads(information_handle.read())

            subprocess.check_call("mkdir -p " + safe_output_directory, shell=True)
            subprocess.check_call("cairosvg " + safe_input_file + " -f png -W 200 -H 200 -o " + safe_output_file, shell=True)

            if issuer not in manifest_data.keys():
                additional_search_terms = []
                
                if "additional_search_terms" in information.keys():
                    additional_search_terms = information["additional_search_terms"]

                manifest_data[issuer] = {
                    "domain": information["domain"],
                    "additional_search_terms": additional_search_terms,
                    "icons": []
                }

            manifest_data[issuer]["icons"].append(issuer + "/" + filename + ".png")
    except:
        continue

with open("dist/manifest.json", "w") as manifest_file:
    json.dump(manifest_data, manifest_file)

print("Generation done!")