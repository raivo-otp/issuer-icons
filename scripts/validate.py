import os
import re
import sys
import glob
import json
import validators

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

def is_valid_domain(domain):
    """Check if the given domain name is valid.
        
    Args:
        domain (str): The domain name to check for.

    Returns:
        bool: Positive if valid.

    """

    return validators.domain(domain) == True

def root_did_not_change():
    """Check if any of the file names in the root changed

    Returns:
        bool: Positive if not changed.

    """

    files = os.listdir('.')
    allowed_files = [
        '.gitignore',
        '.github',
        '.git',
        '.htaccess',
        '.semver',
        '.DS_Store',
        'README.md',
        'LICENSE.md',
        'SECURITY.md',
        'PRIVACY.md',
        'requirements.txt',
        'scripts',
        'vectors',
        'dist'
    ]

    for file in files:
        if file not in allowed_files:
            return False

    return True


def main():
    """Run the validation on all vector issuer icons."""

    try:
        vectors = glob.glob('./vectors/*/*.svg')
    except:
        vectors = []

    print('Running validation on {} icons.'.format(len(vectors)))

    # Generic validations
    guard(len(vectors) >= 680, 'It looks like many vectors were deleted. There are only {} left while there should be more than 450. Did you delete any per accident?'.format(len(vectors)))
    guard(root_did_not_change(), 'It looks like the root of the repository changed. Are you sure you added your icon to the \'vectors/\' subdirectory?')

    # Icon specific validations
    for vector in vectors:
        domain = vector[10:].split('/')[0]
        filename = vector[10:].split('/')[1]

        output_directory = './dist/{}'.format(domain)
        output_file = '{}/{}.png'.format(output_directory, domain)

        safe_output_directory = re.sub(r'[^a-z0-9-\./]+', '', output_directory)
        safe_output_file = re.sub(r'[^a-z0-9-\./]+', '', output_file)
        safe_input_file = re.sub(r'[^a-z0-9-\./]+', '', vector)

        try:
            svg_handle = open(vector, 'r', encoding='utf-8')
            svg_body = svg_handle.read().strip().lower()
        except Exception as e:
            guard(False, str(e), vector)

        # Meta
        guard(vector.islower(), 'The directory (domain name) and the filename must both be lowercase.', vector)
        guard(len(domain.split('.')) >= 1, 'The directory name of the vector must be the primary domain name of the issuer, and must contain at least one dot.', vector)
        guard(len(domain.split('.')) <= 3, 'The directory name of the vector must be the primary domain name of the issuer, and must contain at maximum three dots.', vector)
        guard(is_valid_domain(domain), 'The directory name must be a valid domain name', vector)
        guard(safe_output_directory == output_directory, 'Folder and file must be lowercase, consisting of only the characters "a-z", "0-9" and "\'"', output_directory)
        guard(safe_output_file == output_file, 'Folder and file must be lowercase, consisting of only the characters "a-z", "0-9" and "\'"', output_file)
        guard(safe_input_file == vector, 'Folder and file must be lowercase, consisting of only the characters "a-z", "0-9" and "\'"', vector)
        guard(len(safe_output_directory.split("..")) == 1, 'Directory may not contain two dots in a row.', safe_output_directory)
        guard(len(safe_output_directory.split("/")) > 2, 'Directory may not contain more than 2 slashes.', safe_output_directory)
        guard(len(safe_output_file.split("..")) == 1, 'File may not contain two dots in a row.', safe_output_file)
        guard(len(safe_output_file.split("/")) > 2, 'Directory may not contain more than 2 slashes.', safe_output_file)
        guard(len(safe_input_file.split("..")) == 1, 'File may not contain two dots in a row.', safe_input_file)
        guard(len(safe_input_file.split("/")) > 2, 'Directory may not contain more than 2 slashes.', safe_input_file)

        # Body
        guard('data:' not in svg_body, 'Vector may not contain embedded non-vector images (JPG/PNG/etc)', vector)
        guard('base64' not in svg_body, 'Vector may not contain embedded non-vector images (JPG/PNG/etc)', vector)
        guard(svg_body[0:4] == '<svg', "Vector must start with `<svg`", vector)
        guard(svg_body[-6:] == '</svg>', "Vector must end with `</svg>`", vector)

        pattern = re.compile(r'<svg[^>]*(width|height) ?=[^>]*?>', re.MULTILINE|re.IGNORECASE)
        is_static_size = pattern.match(svg_body)
        guard(not is_static_size, 'Vector must not have static width and/or height attributes. Use a viewBox instead.', vector)

        pattern = re.compile(r'<svg[^>]*(viewBox) ?=[^>]*?>', re.MULTILINE|re.IGNORECASE)
        has_viewbox = pattern.match(svg_body)
        guard(has_viewbox, 'Vector must have a viewBox attribute', vector)

    print('Validation finished, everything looks good!')

if __name__ == '__main__':
    """If this file is ran, run the main() function."""

    main()
