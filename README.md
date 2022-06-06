# TP1

Este é o código implementado para o Trabalho Prático 1 da disciplina Introdução à Inteligência Artificial do Departamento de Ciência da Computação da Universidade Federal de Minas Gerais.

### Execução

Para executar o programa, execute:

```bash
python3 src/main.py <Algoritmo> <Configuração do Jogo> [PRINT]
```

Os algoritmos disponíveis são:
- A (A*)
- B (Breadth-First Search)
- G (Greedy)
- H (Hill Climbing)
- I (Iterative Deepening Search)
- U (Uniform Cost Search)

A configuração do jogo pode tem 9 números inteiros únicos de 0 a 8. Um jogo resolvido tem formato `1 2 3 4 5 6 7 8 0`.

Se deseja-se executar o algoritmo A* para a configuração `1 5 2 4 0 3 7 8 6` imprimindo o passo a passo da solução basta executar

```bash
python3 src/main.py A 1 5 2 4 0 3 7 8 6 PRINT
```

Para os algoritmos A* e Greedy existe uma heurística alternativa. Para utilizá-la, use a variável de ambiente `ALTERNATE_HEURISTIC` com valor `True`:

```bash
ALTERNATE_HEURISTIC=True python3 src/main.py G 1 5 2 4 0 3 7 8 6 PRINT
```
