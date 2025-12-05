# 🎯 Objetivo do Projeto

Repositório de estudos, destinado a entender e comparar diferentes **estruturas de filas em Python**.

A ideia é criar um espaço organizado onde cada estrutura — FIFO, filas circulares, de prioridade, deques — possa ser explorada de forma clara, prática e com foco tanto no aprendizado quanto na observação de desempenho.

Para cada estrutura implementada, o projeto oferece:

- **Implementação ingênua (naive)**
    
    Uma versão simples, ideal para enxergar o funcionamento interno sem camadas de abstração.
    
- **Implementação otimizada**
    
    Uma variante eficiente, aproveitando estruturas internas do Python quando fizer sentido.
    
- **Explicação detalhada**
    
    Como funciona, quando usar, limitações e visualizações que ajudam a entender o fluxo da estrutura.
    
- **Análise Big-O**
    
    Complexidade das operações explicada e documentada.
    
- **Comparação de performance**
    
    Benchmarks que mostram, de forma prática, como cada implementação se comporta.
    
- **Testes unitários completos**
    
    Garantem que a estrutura funciona corretamente e lida bem com cenários extremos.
    
- **Demonstrações executáveis (demos)**
    
    Pequenos exemplos para ver a fila operando com logs claros.
    

O projeto serve como base sólida para dominar filas, experimentar melhorias e construir conhecimento que será útil quando a transição para sistemas de filas distribuídas (como Redis, Celery ou RabbitMQ) acontecer naturalmente.

---
# Requisitos
Python 3.10

---

# Variáveis de Ambiente

## Variáveis

| Variável             | Tipo | Valores aceitos                                   | Padrão | Descrição |
| ---                  | ---  | ---                                               | ---    | --- |
| `QUEUELAB_LOG_LEVEL` | str  | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`   | `INFO` | Controla o nível de detalhamento dos logs durante demos e benchmarks. |



## Comandos utéis

Caso pretenda configurar o comportamento do projeto por variáveis de ambiente, utilize o arquivo `env.example` como ponto de partida. Ele contém todas as variáveis reconhecidas pelo sistema e seus valores padrão (quando aplicável).

```bash
cp .env.example .env
```

---

## Como validar comportamento das estruturas

### 1) Testes unitários

Os testes estão em dentro de cada implementação específica, exemplo: `fifo/tests/`.

Execute:

```
python -m unittest discover -v
```

ou, para rodar os testes de uma determinada estrutura:

```
python -m unittest discover -v fifo/tests
```

### 2) Benchmarks

Para comparar na prática o desempenho das implementações, utilize o módulo benchmark.

Cada estrutura de dados possui seu próprio arquivo de benchmark, seguindo o padrão:

```
<estrutura>_benchmark.py
```

Por exemplo, para FIFO:

```
benchmark/fifo_benchmark.py
```

O benchmark base — responsável pela lógica comum de medição — está em:

```
benchmark/base_benchmarks.py
```