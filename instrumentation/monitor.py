"""
Monitor de performance simples baseado em tempo de execução.

Este módulo fornece utilitários para medir o tempo que funções individuais
levam para serem executadas. É especialmente útil em cenários de benchmarking
e comparação entre diferentes implementações de estruturas de dados.
"""

import time

class PerformanceMonitor:
    @staticmethod
    def measure(func, *args, **kwargs):
        """
        Executa uma função arbitrária e retorna seu resultado junto ao tempo gasto.

        :param func: Função que será executada.
        :param args: Argumentos posicionais repassados para a função.
        :param kwargs: Argumentos nomeados repassados para a função.

        :return: dict com:
            - "result": valor retornado pela função.
            - "time": tempo de execução em segundos.
        """
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        return {
            "result": result,
            "time": end - start,
        }
