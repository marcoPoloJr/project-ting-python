"""linter"""
import pytest

from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    def mock(number):
        return {
            'nome_do_arquivo': 'file_name',
            'qtd_linhas': number,
            'linhas_do_arquivo': 'file_lines'
        }
    test_queue = PriorityQueue()

    test_queue.enqueue(mock(12))
    test_queue.enqueue(mock(1))
    test_queue.enqueue(mock(2))
    test_queue.enqueue(mock(3))

    assert test_queue.dequeue() == mock(1)

    assert test_queue.search(0) == mock(2)

    with pytest.raises(IndexError):
        test_queue.search(4)
