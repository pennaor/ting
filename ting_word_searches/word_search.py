from typing import Callable, Any
from ting_file_management.queue import Queue


Formatter_fn = Callable[[int, Any], dict[str, str]]
Match_result = dict[str, dict[str, str]]


class WordMatcher:
    """
    Implementa método para verificar ocorrência
    de palavra em determinada linha.

    É inicializada com uma função de formatação
    que recebe os dados relativos ao número e conteúdo da linha
    em que há ocorrência e que retorna estrutura para visualização do usuário

    Cada linha em que há ocorrência
    é formatada e adicionada a lista de ocorrências
    """

    def __init__(self, formatter_fn: Formatter_fn) -> None:
        self._data: list[dict[str, str]] = []
        self._current_position = 0
        self._formatter = formatter_fn

    def _matcher(self, lane: str, word: str) -> bool:
        return lane.lower().find(word.lower()) >= 0

    def _append(self, position: int, lane: str) -> None:
        self._data.append(self._formatter(position, lane))

    def parse(self, lane: str, word: str) -> None:
        if self._matcher(lane, word):
            self._current_position += 1
            self._append(self._current_position, lane)

    @property
    def data(self):
        return self._data


def get_matched_metadata(
    word: str,
    queue: Queue,
    formatter_fn: Formatter_fn
) -> list[Match_result]:
    """
    Desenfileira arquivos em Queue, inicializando
    classe WordMatcher com formatter_fn e armazenando
    resultados de cada arquivo verificado
    em uma lista que é retornada
    """

    results = []
    for _ in range(len(queue)):
        metadata = queue.dequeue()
        matcher = WordMatcher(formatter_fn)
        for lane in metadata["linhas_do_arquivo"]:
            matcher.parse(lane, word)
        ocurrencies = matcher.data if len(matcher.data) else "Sem ocorrência"
        results.append({
            "metadata": metadata,
            "search_result": {
                "palavra": word,
                "arquivo": metadata["nome_do_arquivo"],
                "ocorrencias": ocurrencies,
            },
        })
    return results


def exists_word(word: str, instance: Queue):
    """
    Busca numeração das linhas em que a palavra
    ocorre nos arquivos processados
    """

    def new_lane(position: int, _dummy: None):
        return {"linha": position}
    return get_matched_metadata(word, instance, new_lane)


def search_by_word(word: str, instance: Queue):
    """
    Busca numeração e conteúdo das linhas em que a palavra
    ocorre nos arquivos processados
    """

    def new_content_lane(position: int, content: str):
        return {"conteudo": content, "linha": position}
    return get_matched_metadata(word, instance, new_content_lane)
