from pathlib import Path

def count_words(path):
    """Counting approx. amount of words in certain file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"File {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"File {path} contains {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)