import os
import sys
import json
import generate
from PIL import Image


def guard(result, message, data):
    if not result:
        sys.exit("Guard failed! " + str(message) + "\nGot data: " + str(data))


with open("./dist/manifest.json", "r") as manifest_handle:
    manifest = json.loads(manifest_handle.read())

    for issuer, information in manifest.items():
        print("Evaulating issuer " + issuer + "...")

        guard("domain" in information.keys(), "Domain is required.", issuer)
        guard(len(information["domain"].split(".")) == 2, "Domain must have a maximum of one [dot] (e.g. 'twitter.com').", issuer)
        guard(len(information["domain"].split(".")[0]) > 1, "Domain must have characters before the [dot].", issuer)
        guard(len(information["domain"].split(".")[1]) > 1, "Domain must have characters behind the [dot].", issuer)

        if "additional_search_terms" in information.keys():
            guard(len(information["additional_search_terms"]) <= 10, "A maximum of 10 additional search terms are allowed.", issuer)

        guard("icons" in information.keys(), "At least one icon is required.", issuer)

        for icon in information["icons"]:
            print("Evaluating icon " + icon + "...")

            guard(icon.islower(), "Folder and file must be lowercase.", icon)

            guard(os.path.isfile("./dist/" + icon), "PNG distribution file does not exist.", icon)

            dist_size = os.path.getsize("./dist/" + icon)
            guard(dist_size <= 30000, "PNG distribution icon must be smaller than 30KB.", icon)

            try:
                dist_image = Image.open("./dist/" + icon)
                dist_image.verify()
            except:
                guard(False, "PNG distribution icon is not a valid image.", icon)

            guard(dist_image.format == "PNG", "PNG distribution icon is not a PNG file.", icon)

print("Validation done, everything looks good!")
