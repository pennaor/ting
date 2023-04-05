from ting_file_management.file_management import txt_importer


def is_file_unique(path_file, instance):
    path_file_unique = True
    for index in range(len(instance)):
        try:
            file_metadata = instance.search(index)
            if file_metadata["nome_do_arquivo"] == path_file:
                path_file_unique = False
        except (IndexError):
            break
    return path_file_unique


def process(path_file, instance):
    if not is_file_unique(path_file, instance):
        return
    rows = txt_importer(path_file)
    file_metadata = dict({
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(rows),
        "linhas_do_arquivo": rows,
    })
    instance.enqueue(file_metadata)
    print(file_metadata)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
