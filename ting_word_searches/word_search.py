from ting_file_management.queue import Queue


class WordMatcher:
    def __init__(self, formatter_fn):
        self._data = []
        self._current_position = 1
        self._formatter = formatter_fn

    def _matcher(self, lane, word):
        return lane.lower().find(word.lower()) >= 0

    def _append(self, position, lane):
        self._data.append(self._formatter(position, lane))

    def parse(self, lane, word):
        if self._matcher(lane, word):
            self._append(self._current_position, lane)
        self._current_position += 1

    @property
    def data(self):
        return self._data


def get_matched_metadata(word, queue: Queue, matcher):
    result = []
    for index in range(len(queue)):
        metadata = queue.search(index)
        for lane in metadata["linhas_do_arquivo"]:
            matcher.parse(lane, word)
        if matcher.data:
            result.append({
                "metadata": metadata,
                "search_result": {
                    "palavra": word,
                    "arquivo": metadata["nome_do_arquivo"],
                    "ocorrencias": matcher.data
                }})
    return result


def exists_word(word, instance: Queue):
    def new_lane(position, _dummy):
        return {"linha": position}
    return get_matched_metadata(word, instance, WordMatcher(new_lane))


def search_by_word(word, instance):
    def new_content_lane(position, content):
        return {"conteudo": content, "linha": position}
    return get_matched_metadata(word, instance, WordMatcher(new_content_lane))
