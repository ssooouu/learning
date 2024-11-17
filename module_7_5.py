import os
from datetime import datetime

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(file)
        filetime = datetime.fromtimestamp(os.path.getmtime(file))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}, Родительская директория: {parent_dir}')
