from formatar_data import converter_data_numero_db
from django.db.models import Q 

def montador_de_filtro(cls, campos_desejados, pesquisa):
    campos_pesquisa = []
    campos_do_modelo = cls._meta.get_fields()
    for desejado in campos_desejados : 
        for campo in campos_do_modelo: 
            if campo.name == desejado: 
                campos_pesquisa.append(campo)  
    filtro = None
    for campo in campos_pesquisa:
        if not campo.is_relation : 
            if filtro == None:
                filtro = (Q(('%s__icontains' % campo.name, pesquisa)))
                if 'data_' in campo.name: 
                    filtro = (Q(('%s__icontains' % campo.name, converter_data_numero_db(pesquisa))))
            else:
                if 'data_' in campo.name:
                    filtro.add(Q(('%s__icontains' % campo.name, converter_data_numero_db(pesquisa))), Q.OR)
                else: 
                    filtro.add(Q(('%s__icontains' % campo.name, pesquisa)), Q.OR)             
    return filtro 