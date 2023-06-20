

def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = list()

    for i in range(0, len(instance)):
        file = instance.search(i)
        ocurrs = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': list()
        }

        for line, text in enumerate(file['linhas_do_arquivo']):
            if word.casefold() in text.casefold():
                ocurrs['ocorrencias'].append({'linha': line + 1})

        if len(ocurrs['ocorrencias']) > 0:
            result.append(ocurrs)
            
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
