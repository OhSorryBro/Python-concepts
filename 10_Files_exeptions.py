from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)
path_example = Path('text_files/name_of_the_file.txt')

contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)