import pytest
from ting_file_management.priority_queue import PriorityQueue


expected_high_metadata = [
    {"qtd_linhas": 3},
    {"qtd_linhas": 2},
    {"qtd_linhas": 4},
]

expected_regular_metadata = [
    {"qtd_linhas": 11},
    {"qtd_linhas": 7},
    {"qtd_linhas": 5},
]

unordered_metadata = [
    {"qtd_linhas": 11},
    {"qtd_linhas": 3},
    {"qtd_linhas": 2},
    {"qtd_linhas": 7},
    {"qtd_linhas": 5},
    {"qtd_linhas": 4},
]


def test_basic_priority_queueing():
    queue = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(0)

    regular, high, *_ = unordered_metadata

    queue.enqueue(regular)
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 0

    queue.enqueue(high)
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 1

    assert queue.dequeue() is not None
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 0

    assert queue.dequeue() is not None
    assert len(queue.regular_priority) == 0
    assert len(queue.high_priority) == 0

    assert queue.dequeue() is None

    for priority in unordered_metadata:
        queue.enqueue(priority)

    files_metadata = expected_high_metadata + expected_regular_metadata

    for index in range(len(files_metadata)):
        process = queue.search(index)
        assert files_metadata[index] == process
