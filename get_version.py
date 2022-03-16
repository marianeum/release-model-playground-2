import re
import sys

def main():
    file_path = "version.json"

    version_regex = re.compile(r"(\"version\":\s*['\"])((([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?)(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?)")
    with open(file_path, "r+") as f:
        content = f.read()
        version = re.findall(version_regex, content)[0]
        return version[1]

if __name__ == "__main__":
    main()
