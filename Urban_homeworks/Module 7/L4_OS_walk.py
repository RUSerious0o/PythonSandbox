import os
import time

directory = os.path.normpath('../')
for dirpath, dirnames, filenames in os.walk(directory):
    if '.idea' in dirpath or '.venv' in dirpath or '__pyc' in dirpath:
        continue

    print(dirpath, dirnames, filenames)
    if len(filenames) > 0:
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            filetime = os.path.getmtime(filepath)
            print(f'\t{os.path.abspath(filepath):150}'
                  f'size: {os.path.getsize(filepath):12}'
                  f'\t{time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))}')

