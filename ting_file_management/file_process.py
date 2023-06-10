import sys
from ting_file_management.file_management import txt_importer


def is_file_unique(path_file, instance):
    try:
        for index in range(len(instance)):
            file_metadata = instance.search(index)
            if file_metadata["nome_do_arquivo"] == path_file:
                return False
    except (IndexError):
        pass
    return True


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


def remove(instance):
    file_metadata = instance.dequeue()
    if file_metadata is None:
        print("Não há elementos")
    else:
        name = file_metadata["nome_do_arquivo"]
        print(f"Arquivo {name} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except (IndexError):
        print("Posição inválida", file=sys.stderr)
