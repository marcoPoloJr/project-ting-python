from operator import index
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        file = instance.search(i)
        # print('FILE', file)
        if file["nome_do_arquivo"] == path_file:
            return

    txtFile = txt_importer(path_file)
    
    dictionary = {
        "nome_do_arquivo": path_file,
        "qtq_linhas": len(txtFile),
        "linhas_do_arquivo": txtFile
    }

    instance.enqueue(dictionary)
    print(dictionary)
    # print('Intance', instance.enqueue(dictionary))
    # print('TXTFILE', txtFile)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
