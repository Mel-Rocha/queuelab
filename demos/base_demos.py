import logging

from instrumentation.logging_config import configure_logging
from fifo.exceptions import QueueEmptyError


def run_queue_demo(queue):
    configure_logging()
    logger = logging.getLogger(__name__)

    logger.info("Iniciando demo genérica de Queue")
    logger.info("Fila criada: %s", type(queue).__name__)

    logger.info("Enfileirando itens...")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    logger.info("Estado atual da fila: %s", queue)

    logger.info("Desenfileirando um elemento...")
    item = queue.dequeue()
    logger.info("Item removido: %s", item)

    logger.info("Espiando próximo elemento: %s", queue.peek())
    logger.info("Tamanho atual da fila: %d", queue.size())

    logger.info("Testando remoção de fila vazia intencionalmente...")

    try:
        empty_queue = type(queue)()
        empty_queue.dequeue()
    except QueueEmptyError as e:
        logger.error("Erro esperado: %s", e)
