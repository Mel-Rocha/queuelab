"""
Demonstrações básicas para estruturas de filas.

Este módulo contém uma função utilitária usada para executar uma
demonstração genérica de qualquer implementação de fila compatível
(com métodos como enqueue, dequeue, peek, size e is_empty).
A demo exibe operações comuns e registra o comportamento via logging.
"""

import logging

from domain.exceptions import QueueEmptyError
from instrumentation.logging_config import configure_logging


def run_queue_demo(queue, enqueue_strategy):
    """
    Executa uma demonstração simples utilizando uma instância de fila.

    A função realiza operações básicas como enfileirar, desenfileirar,
    espiar o próximo elemento e testar o comportamento ao tentar remover
    itens de uma fila vazia. Todas as ações são registradas via logging.

    :param queue: Instância de uma fila que implementa os métodos padrão
                  (enqueue, dequeue, peek, size, is_empty).
    :param enqueue_strategy: Estratégia de enfileiramento.

    :return: None
    """
    configure_logging()
    logger = logging.getLogger(__name__)

    logger.info("Enfileirando itens...")
    enqueue_strategy(queue)

    logger.info("Espiando próximo elemento: %s", queue.peek())
    logger.info("Tamanho da fila: %d", queue.size())

    logger.info("Desenfileirando itens...")
    while not queue.is_empty():
        item = queue.dequeue()
        logger.info("Item removido: %s", item)

    logger.info("Testando remoção em fila vazia...")
    try:
        queue.dequeue()
    except QueueEmptyError as e:
        logger.error("Erro esperado: %s", e)