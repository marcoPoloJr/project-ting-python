"""Linter"""
import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    file = '.txt'
    if file not in path_file:
        print('Formato inválido', file=sys.stderr)
        return None
    try:
        with open(path_file, mode='r', encoding="utf-8") as file_text:
            line = file_text.read().split('\n')
            return line
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
        return None

