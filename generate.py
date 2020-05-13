import os
import re
import sys
import glob
import json
import cairosvg
import subprocess

manifest_data = {}
search_data = {}
input_files = glob.glob("./vectors/*/*.svg")


def guard(result, message='Unknown error', data=None):
    if not result:
        print('--------------------------------------------------------------')
        raise Exception("Guard failed! " + str(message) + "\nFailed vector/image: " + str(data))


for input_file in input_files:
    print("Parsing " + input_file + "...")

    filename = "".join(input_file.split("/")[-1:])[:-4]
    directory = "/".join(input_file.split("/")[:-1]) + "/"
    issuer = directory[10:-1]

    output_directory = "./dist/" + issuer
    output_file = output_directory + "/" + filename + ".png"

    safe_output_directory = re.sub(r"[^a-z0-9-\./]+", "", output_directory)
    safe_output_file = re.sub(r"[^a-z0-9-\./]+", "", output_file)
    safe_input_file = re.sub(r"[^a-z0-9-\./]+", "", input_file)

    try:
        guard(safe_output_directory == output_directory, 'Folder and file must be lowercase, concisting of only the characters "a-z", "0-9" and "\'"', output_directory)
        guard(safe_output_file == output_file, 'Folder and file must be lowercase, concisting of only the characters "a-z", "0-9" and "\'"', output_file)
        guard(safe_input_file == input_file, 'Folder and file must be lowercase, concisting of only the characters "a-z", "0-9" and "\'"', input_file)
        guard(len(safe_output_directory.split("..")) == 1, 'Directory may not contain 2 dots.', safe_output_directory)
        guard(len(safe_output_directory.split("/")) == 3, 'Directory may not contain more than 2 slashes.', safe_output_directory)
        guard(len(safe_output_file.split("..")) == 1, 'File may not contain 2 dots.', safe_output_file)
        guard(len(safe_output_file.split("/")) == 4, 'Directory may not contain more than 2 slashes.', safe_output_file)
        guard(len(safe_input_file.split("..")) == 1, 'File may not contain 2 dots.', safe_output_file)
        guard(len(safe_input_file.split("/")) == 4, 'Directory may not contain more than 2 slashes.', safe_output_file)

        with open(directory + "information.json", "r") as information_handle:
            information = json.loads(information_handle.read())

            subprocess.check_call(['mkdir', '-p', safe_output_directory])
            subprocess.check_call(['cairosvg', safe_input_file, '-f', 'png', '-W', '200', '-H', '200', '-o', safe_output_file])

            # MANIFEST
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

            # SEARCH
            for issuer_part in issuer.split("-"):
                if issuer_part not in search_data.keys():
                    search_data[issuer_part] = [issuer + "/" + filename + ".png"]
                elif issuer + "/" + filename + ".png" not in search_data[issuer_part]:
                    search_data[issuer_part].append(issuer + "/" + filename + ".png")

            if "additional_search_terms" in information.keys():
                for term in information["additional_search_terms"]:
                    if term not in search_data.keys():
                        search_data[term] = [issuer + "/" + filename + ".png"]
                    elif issuer + "/" + filename + ".png" not in search_data[term]:
                        search_data[term].append(issuer + "/" + filename + ".png")

    except Exception as e:
        sys.exit(str(e))


with open("dist/manifest.json", "w") as manifest_file:
    json.dump(manifest_data, manifest_file)

print("Manifest JSON generation done!")

with open("dist/search.json", "w") as search_file:
    json.dump(search_data, search_file)

print("Search JSON generation done!")

print("Finished!")
