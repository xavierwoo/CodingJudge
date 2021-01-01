import os
import lzma
BASE_dir = os.path.dirname(os.path.realpath(__file__))
for dir in os.listdir(BASE_dir):
    if dir.startswith(".") or os.path.isfile(dir): continue
    with open(dir + '/.core/data_bk.py', 'rb') as data_bk_file:
        with lzma.open(dir + '/.core/data.dat', 'wb') as data_file:
            data_file.write(data_bk_file.read())