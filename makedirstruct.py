from pprint import pprint as pp
import re
import os


def clean(dirty):
    return dirty.replace('-&gt', '').replace('+', '-').replace('?', '').replace(
        ':', '').replace('&#39;', '').replace('&amp', '').replace('Ã¨', 'e').replace(
        'è', 'e').replace(';', '-').replace('/', '-').replace('!', '').replace('(', '_'
        ).replace(')', '_').replace('Ã©', 'e').replace(',', '').replace('Ã§', 'c').replace(
        '#', '').replace('\n', '').replace('~', '_').replace('Ã¶', 'o').replace('%', '_').replace(
        'Ã¤', 'a').replace('Ã¼', 'u')

with open('photopaths.csv') as f:
    for line in f:
        category, album, path = line.split(';;')
        category = clean(category)
        catpath = f'./galleries/{category}'
        if not os.path.exists(catpath):
            os.mkdir(catpath)

        album = clean(album)
        albpath = f'{catpath}/{album}'
        if not os.path.exists(albpath):
            os.mkdir(albpath)
        
        path = path.strip()
        path_in = f'./albums/{path}'
        filename = clean(path.split('/')[-1])
        path_out = f'./galleries/{category}/{album}/{filename}'
        if os.path.exists(path_in):
            if not os.path.exists(path_out):
                print(f'{path_in} => {path_out}')
                os.rename(path_in, path_out)
