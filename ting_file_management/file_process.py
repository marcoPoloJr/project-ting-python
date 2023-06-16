"""Linter"""
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        file = instance.search(i)
        # print('FILE', file)
        if file["nome_do_arquivo"] == path_file:
            return

    txt_file = txt_importer(path_file)

    dictionary = {
        'nome_do_arquivo': path_file,
        'qtq_linhas': len(txt_file),
        'linhas_do_arquivo': txt_file
    }

    instance.enqueue(dictionary)
    print(dictionary, file=sys.stdout)
    # print('Intance', instance.enqueue(dictionary))
    # print('TXTFILE', txtFile)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return print('Não há elementos', file=sys.stdout)
    file = instance.dequeue()
    file_removed = file['nome_do_arquivo']
    print(f'Arquivo {file_removed} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
