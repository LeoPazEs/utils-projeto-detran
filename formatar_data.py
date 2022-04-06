def achar_index_barras(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def converter_data_numero_db(pesquisa): 
    if pesquisa:
        if '/' in pesquisa: 
            indexes = achar_index_barras(pesquisa, '/') 
            dia = pesquisa[indexes[0] - 2: indexes[0]] 
            mes = pesquisa[indexes[0] + 1: indexes[0] + 3] 
            if len(indexes) > 1: 
                ano = pesquisa[indexes[1] + 1 : indexes[1] + 5]
                data_db = f'{ano}-{mes}-{dia}' 
            else:
                if mes == '': 
                    data_db = f'-{dia}' 
                else:
                    data_db = f'-{mes}-{dia}'
            return data_db 
    return pesquisa