import os
import re
import sys
import glob
import json
import validate
import cairosvg
import subprocess

def guard(result, message, metadata = None):
    """Make sure the result is a positive result. Exit otherwise.
        
    Args:
        result (bool): A boolean indicating a positive or negative result.
        message (str): The message to show if the result is negative.
        metadata (obj): Optional metadata to show if the result is negative.

    """

    if result:
        return

    print('Guard failed! {}'.format(message))

    if metadata:
        print(metadata)

    sys.exit(1)

def main():
    """Run the validation & generation for all vector issuer icons."""

    validate.main()

    search_data = {}
    manifest_data = {}
    output_count = 0

    search_denylist = [
        'text', 'monochrome', 'filled', 'circle', 'rounded', 'square', 'icon', 'symbol', 'alt', 'alternative', 'main', 'second', 'secondary', 'light', 'dark', 'white', 'black'
    ]

    try:
        vectors = glob.glob('./vectors/*/*.svg')
    except:
        vectors = []

    # Generate a PNG for every SVG
    for vector in vectors:
        print('Processing {}...'.format(vector))

        domain = vector[10:].split('/')[0]
        filename = vector[10:].split('/')[1][0:-4]

        output_directory = './dist/{}'.format(domain)
        output_file = '{}/{}.png'.format(output_directory, filename)

        safe_output_directory = re.sub(r'[^a-z0-9-\./]+', '', output_directory)
        safe_output_file = re.sub(r'[^a-z0-9-\./]+', '', output_file)
        safe_input_file = re.sub(r'[^a-z0-9-\./]+', '', vector)

        subprocess.check_call(['mkdir', '-p', safe_output_directory])
        subprocess.check_call(['cairosvg', safe_input_file, '-f', 'png', '-W', '200', '-H', '200', '-o', safe_output_file])
        output_count = output_count + 1

        # MANIFEST
        if domain not in manifest_data.keys():
            manifest_data[domain] = {
                'domain': domain,
                'additional_search_terms': [],
                'icons': []
            }

        manifest_data[domain]['icons'].append('{}/{}.png'.format(domain, filename))
        
        # SEARCH
        for issuer_part in filename.split('-'):
            if issuer_part in search_denylist:
                continue

            if len(issuer_part) <= 1:
                continue

            if issuer_part not in search_data.keys():
                search_data[issuer_part] = ['{}/{}.png'.format(domain, filename)]
            elif '{}/{}.png'.format(domain, filename) not in search_data[issuer_part]:
                search_data[issuer_part].append('{}/{}.png'.format(domain, filename))

    with open('dist/manifest.json', 'w') as manifest_file:
        json.dump(manifest_data, manifest_file)

    print('Manifest JSON generation done!')

    with open('dist/search.json', 'w') as search_file:
        json.dump(search_data, search_file)

    print('Generation finished, everything looks good! Generated {} icons.'.format(output_count))

if __name__ == '__main__':
    """If this file is ran, run the main() function."""

    main()
