"""
Configurações de logging do projeto.

Este módulo **não configura logging automaticamente ao ser importado**.
Em vez disso, fornece a função configure_logging(), que deve ser chamada somente
em entrypoints da aplicação, como scripts de demo, CLIs ou blocos
`if __name__ == "__main__":`.

Motivo: chamar configurações de logging dentro de módulos importados
pode interferir no logging global do processo e causar comportamento
indesejado caso este pacote seja utilizado como biblioteca em outros
projetos.

Em código de produção dentro do pacote, use apenas:

    logger = logging.getLogger(__name__)

e deixe a decisão de como o logging será configurado para o programa
que estiver importando este pacote.
"""


import logging
import logging.config
import os
from typing import Optional

DEFAULT_LOG_LEVEL = os.getenv("QUEUELAB_LOG_LEVEL", "INFO").upper()


def _build_dict_config(level: str = DEFAULT_LOG_LEVEL):
    """
    Retorna um dict compatível com logging.config.dictConfig,
    configurando apenas saída para o console (stdout).

    """
    return {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "standard": {
                "format": "%(asctime)s %(levelname)s %(name)s: %(message)s"
            },
            "short": {
                "format": "%(levelname)s %(name)s: %(message)s"
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": level,
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            }
        },

        "root": {
            "level": level,
            "handlers": ["console"]
        },

        "loggers": {
            "urllib3": {"level": "WARNING"},
            "asyncio": {"level": "WARNING"},
        }
    }

def configure_logging(level: Optional[str] = None):
    """
    Configura logging global do projeto.
    Apenas console (stdout).

    Deve ser chamada apenas por entrypoints (scripts, demos, CLI).
    Nunca chame em módulos importados para não reconfigurar logging
    quando o pacote for utilizado como biblioteca.
    """
    lvl = (level or DEFAULT_LOG_LEVEL).upper()

    config = _build_dict_config(level=lvl)
    logging.config.dictConfig(config)

    logging.getLogger(__name__).debug("Logging configurado (level=%s)", lvl)

def get_logger(name: str):
    """
    Conveniência — devolve logger com o nome indicado.
    (Mas preferível usar logging.getLogger(__name__) diretamente nos módulos.)
    """
    return logging.getLogger(name)
