from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue


def is_file_unique(path_file, instance):
    path_file_unique = True
    for index in range(len(instance)):
        try:
            process_dict = instance.search(index)
            if process_dict["nome_do_arquivo"] == path_file:
                path_file_unique = False
        except(IndexError):
            break
    return path_file_unique


def process(path_file, instance):
    if is_file_unique(path_file, instance):
        rows = txt_importer(path_file)
        process_dict = dict({
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(rows),
            "linhas_do_arquivo": rows,
        })
        instance.enqueue(process_dict)
        print(process_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
