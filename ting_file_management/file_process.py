import sys
from ting_file_management.file_management import txt_importer


def is_file_unique(path_file, instance):
    """
    Assegura que arquivos com o mesmo nome e caminho
    não devem ser readicionados a Queue.
    """

    try:
        for index in range(len(instance)):
            file_metadata = instance.search(index)
            if file_metadata["nome_do_arquivo"] == path_file:
                return False
    except (IndexError):
        pass
    return True


def process(path_file, instance):
    """
    Transforma o conteúdo da lista gerada
    pela função txt_importer em um dicionário
    que será armazenado dentro da Queue.
    """

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
    """Remove o primeiro arquivo processado da Queue."""

    file_metadata = instance.dequeue()
    if file_metadata is None:
        print("Não há elementos")
    else:
        name = file_metadata["nome_do_arquivo"]
        print(f"Arquivo {name} removido com sucesso")


def file_metadata(instance, position):
    """Imprime as informações superficiais de um arquivo processado."""

    try:
        print(instance.search(position))
    except (IndexError):
        print("Posição inválida", file=sys.stderr)
