from pathlib import Path
contents = "I love programming. "
contents += "I love making games. "
contents += "I love working with data. "
path = Path('programming.txt')
path.write_text(contents)