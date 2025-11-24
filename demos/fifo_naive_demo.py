import logging

from instrumentation.logging_config import configure_logging
from fifo.naive import FIFOQueueNaive
from fifo.exceptions import QueueEmptyError


def main():
    configure_logging()
    logger = logging.getLogger(__name__)

    logger.info("Iniciando demo da FIFOQueueNaive")

    queue = FIFOQueueNaive()
    logger.info("Fila criada.")

    logger.info("Enfileirando itens...")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    logger.info("Estado atual: %s", queue)

    logger.info("Desenfileirando um elemento...")
    item = queue.dequeue()
    logger.info("Removido: %s", item)

    logger.info("Espiando próximo elemento: %s", queue.peek())
    logger.info("Tamanho atual da fila: %d", queue.size())

    logger.info("Testando remoção de fila vazia intencionalmente...")
    try:
        queue = FIFOQueueNaive()
        queue.dequeue()
    except QueueEmptyError as e:
        logger.error("Erro esperado: %s", e)


if __name__ == "__main__":
    main()
