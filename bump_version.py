import re
import sys

file_path = "version.json"
new_version = sys.argv[1]

version_regex = re.compile(r"(\"version\":\s*['\"])((([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?)(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?)")
with open(file_path, "r+") as f:
    content = f.read()
    f.seek(0)
    f.write(
        re.sub(
            version_regex,
            lambda match: '{}{}'.format(match.group(1), new_version),
            content,
        )
    )
    f.truncate()
