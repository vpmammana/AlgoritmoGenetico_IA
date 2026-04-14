Esse código implementa uma versão do problema clássico **“Robby the Robot”** usando **algoritmo genético**.

Em termos simples: ele está tentando **evoluir automaticamente uma estratégia** para um robô andar num tabuleiro 10x10, encontrar latas e coletá-las, evitando ações ruins como bater na parede ou tentar pegar lata onde não existe.

## O que ele faz, no geral

Cada **indivíduo da população** representa uma “mente” possível para o robô.

Essa “mente” é um vetor com **243 genes**. Cada gene diz qual ação o robô deve tomar quando estiver em um certo **estado do ambiente**.

O robô pode fazer 7 ações:

* andar para cima
* baixo
* esquerda
* direita
* pegar lata
* ficar parado
* movimento aleatório

O algoritmo cria **300 indivíduos**, testa todos, dá nota para cada um, seleciona os melhores, cruza esses indivíduos, aplica mutações e repete isso por **5000 gerações**.

---

## Que tipo de simulação é essa

Não é uma simulação física, nem de animação realista.

É uma **simulação evolutiva/estocástica de comportamento**:

* **evolutiva**, porque usa seleção, cruzamento e mutação;
* **estocástica**, porque várias partes são aleatórias:

  * genes iniciais,
  * posição das latas,
  * posição inicial do robô,
  * escolha de pais,
  * ponto de corte do crossover,
  * mutações,
  * ação aleatória quando o gene vale 6.

Ou seja, o programa não ensina o robô passo a passo. Ele **gera muitas estratégias, testa, mantém as melhores e vai refinando ao longo das gerações**.

---

## Ideia central dos 243 genes

Esse é o coração do código.

O robô “enxerga” 5 posições:

* célula atual
* cima
* baixo
* esquerda
* direita

Cada uma dessas posições pode estar em 3 estados:

* 0 = vazio
* 1 = lata
* 2 = parede

Então o número total de combinações é:

**3 × 3 × 3 × 3 × 3 = 3^5 = 243**

Por isso cada indivíduo tem **243 genes**.

Na prática, o gene funciona como uma **tabela de decisão**:

> “Se o ambiente ao meu redor estiver nesse estado, então faço esta ação.”

A função `get_state()` transforma a vizinhança do robô em um número de 0 a 242 usando **base 3**, e esse número é usado como índice do gene.

---

## Blocos principais do programa

### 1. Inicialização da população

A função `init_population()` cria os 300 indivíduos e preenche os 243 genes de cada um com valores aleatórios de 0 a 6.

Isso gera estratégias totalmente aleatórias no começo.

---

### 2. Geração do tabuleiro

A função `generate_board()` cria um tabuleiro 10x10 vazio e espalha **50 latas** em posições aleatórias.

Então, a cada teste, o ambiente muda.

Isso evita que o robô “decore” um único cenário.

---

### 3. Leitura do ambiente e construção do estado

As funções `get_cell()` e `get_state()` servem para o robô “perceber” o que tem em volta.

* `get_cell()` devolve vazio, lata ou parede
* `get_state()` combina essas informações em um número entre 0 e 242

Esse cálculo é repetido o tempo todo, porque a cada movimento o robô precisa decidir o que fazer.

---

### 4. Avaliação dos indivíduos

Esse é o bloco mais pesado do programa.

Para cada indivíduo:

* ele é testado em **10 tabuleiros diferentes**
* em cada tabuleiro ele pode fazer até **300 movimentos**

A pontuação funciona assim:

* **+10** ao pegar uma lata corretamente
* **-1** ao tentar pegar onde não há lata
* **-5** ao bater na parede

No final, a nota do indivíduo é a **média** dos 10 tabuleiros.

Isso serve para medir o quão boa é a estratégia dele de forma mais justa, reduzindo a sorte.

---

### 5. Ordenação por desempenho

Depois que todos recebem nota, a população é ordenada do melhor para o pior com `qsort()`.

Aí o programa sabe quem sobrevive e quem vai servir de base para a próxima geração.

---

### 6. Elitismo, seleção, cruzamento e mutação

Depois da avaliação, entra a parte genética.

* **Elitismo**: os 29 melhores passam direto
* **Repescagem**: 1 indivíduo ruim entra no pool para manter diversidade
* **Crossover**: dois pais geram filhos trocando partes dos genes
* **Mutação**: alguns genes mudam aleatoriamente com taxa de 1%

Isso é o mecanismo que tenta melhorar a população ao longo do tempo.

---

### 7. Visualização

Há duas partes visuais:

* `print_board()` mostra o robô andando no tabuleiro de vez em quando
* `update_graph()` atualiza um gráfico no Gnuplot com o melhor resultado por geração

Elas servem mais para acompanhar a evolução do que para a lógica do algoritmo em si.

---

## Quais cálculos são mais repetidos e quantas vezes

Aqui está a parte mais importante da carga de processamento.

### Por geração

Para cada geração, o programa testa:

* **300 indivíduos**
* cada um em **10 tabuleiros**
* cada tabuleiro com até **300 movimentos**

Então o máximo por geração é:

**300 × 10 × 300 = 900.000 decisões do robô por geração**

Cada decisão inclui:

* calcular o estado do ambiente
* consultar o gene correspondente
* executar a ação
* atualizar pontuação e posição

---

### No total da execução

Como são **5000 gerações**, o limite máximo é:

**900.000 × 5000 = 4,5 bilhões de passos de decisão**

Na prática, costuma ser menos porque existe **early stop**:

* se o robô ficar parado demais
* ou bater na parede repetidamente

o teste termina antes dos 300 movimentos.

---

### Quantas vezes o estado é calculado

A função `get_state()` é chamada uma vez por movimento.

Logo:

* até **900.000 chamadas por geração**
* até **4,5 bilhões no total**

E cada `get_state()` chama `get_cell()` **5 vezes**.

Então `get_cell()` pode ser chamado até:

* **4,5 milhões de vezes por geração**
* **22,5 bilhões no total**

Esse é um dos trechos mais repetidos do programa.

---

### Quantas simulações de tabuleiro são feitas

Cada indivíduo é avaliado em 10 tabuleiros.

Então:

* **300 × 10 = 3000 tabuleiros por geração**
* **3000 × 5000 = 15 milhões de tabuleiros no total**

---

### Cruzamento e mutação

Depois da avaliação:

* 29 indivíduos passam direto
* faltam 271 posições para completar a nova população

Como os filhos são criados em pares, o laço de cruzamento roda **136 vezes por geração**.

Em cada cruzamento, os **243 genes** são percorridos.

A mutação também percorre praticamente todos os genes dos não elitistas:

**271 × 243 = 65.853 verificações de mutação por geração**

Com taxa de 1%, isso dá em média cerca de:

**658 mutações por geração**

---

## Para que serve repetir tanto

Essas repetições têm funções bem claras:

* **10 tabuleiros por indivíduo**: reduzir o efeito da sorte
* **300 movimentos por tabuleiro**: dar chance de a estratégia agir bastante
* **300 indivíduos por geração**: manter variedade de estratégias
* **5000 gerações**: permitir evolução gradual
* **mutação**: evitar que a população fique presa numa solução ruim
* **repescagem**: preservar diversidade genética

---

## Em uma frase: o que está sendo evoluído?

O que o algoritmo está evoluindo é uma **política de decisão**:

> dado o que há na célula atual, acima, abaixo, à esquerda e à direita, qual ação o robô deve tomar?

---

## Observações importantes sobre o código

Tem alguns detalhes interessantes:

1. **Os comentários não batem totalmente com os valores**

   * `ELITISM 29`, mas o comentário fala “Top 20”
   * `REPESCAGEM 1`, mas o comentário fala “10 ruins”

2. **O gráfico diz “Média da Nota”, mas está guardando o melhor indivíduo**

   * `history_best[gen] = population[0].score;`
   * então o gráfico é do **melhor score**, não da média da população

3. **O pool de pais não é exatamente “os 29 melhores com peso 3”**

   * o código coloca os índices `0` até `86`
   * então, na prática, ele usa os **87 melhores** no pool, mais 1 pior
   * isso é diferente do que o comentário sugere

4. **No fim, ele cria a nova geração e encerra sem avaliá-la de novo**

   * então o resultado final mostrado vem do que foi copiado para a próxima geração
   * normalmente isso ainda preserva o melhor elite, mas é um detalhe importante

5. **O contador de estagnação não é zerado**

   * então “ficar parado 3 vezes” ao longo do episódio já pode encerrar o teste, mesmo que não sejam 3 vezes seguidas

---

## Resumo final

Esse código serve para **treinar por evolução** um robô coletor de latas.

Ele simula repetidamente:

* um ambiente aleatório,
* um robô com uma estratégia codificada por genes,
* uma pontuação de desempenho,
* e uma evolução genética da população.

O objetivo final é encontrar uma **boa estratégia automática** para maximizar a coleta de latas e minimizar erros.


