import ting_word_searches.word_search as engine
from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def enqueue_files(paths):
    queue = Queue()
    for path in paths:
        process(path, queue)
    return queue


def result_printer(result):
    if not len(result):
        print("Nenhum ocorrência encontrada")
        return
    for index, data in enumerate(result):
        print(
            f"{index + 1}. INFORMAÇÕES DO ARQUIVO PROCESSADO:",
            data["metadata"],
            sep="\n",
            end="\n")
        print(
            "-- RESULTADO DA BUSCA:",
            data["search_result"],
            sep="\n",
            end="\n\n")


def exists_word(word: str, *files_paths: str):
    queue = enqueue_files(files_paths)
    result_printer(result=engine.exists_word(word, queue))


def search_by_word(word: str, *files_paths: str):
    queue = enqueue_files(files_paths)
    result_printer(result=engine.search_by_word(word, queue))
