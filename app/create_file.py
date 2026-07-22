import sys
import os
from datetime import datetime


dirs = []
filename = None
i = 1
while i < len(sys.argv):
    if sys.argv[i] == '-d':
        i += 1
        while i < len(sys.argv) and not sys.argv[i].startswith('-'):
            dirs.append(sys.argv[i])
            i += 1
    elif sys.argv[i] == '-f':
        i += 1
        if i < len(sys.argv):
            filename = sys.argv[i]
            i += 1
    else:
        i += 1

# Створення директорій — ПЕРЕД перевіркою filename
if dirs:
    os.makedirs(os.path.join(*dirs), exist_ok=True)

if filename is not None:
    if dirs:
        file_path = os.path.join(*dirs, filename)
    else:
        file_path = filename

    # Збір рядків від користувача
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    # Формуємо контент
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n"
    for i, line in enumerate(lines, 1):
        content += f"{i} {line}\n"

    # Записуємо у файл
    if os.path.exists(file_path):
        content = "\n" + content
    with open(file_path, "a") as file:
        file.write(content)
