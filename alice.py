from pathlib import Path
path = Path('alice.txt')
try:
    contents = path.read_text(encoding ='utf-8')
except FileNotFoundError:
    print(f"Sorry, but file {path} does not exist.")
else:
    #Cout of words
    words = contents.split()
    num_words = len(words)
    print(f"File {path} zawiera {num_words} words.")