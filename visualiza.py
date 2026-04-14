import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import random
import time

# Os 5 melhores genes extraídos da sua simulação
gene_1 = [6, 4, 4, 0, 4, 6, 1, 4, 0, 1, 4, 3, 1, 4, 5, 3, 4, 1, 0, 4, 5, 2, 4, 2, 3, 1, 6, 2, 4, 5, 0, 4, 1, 1, 4, 3, 2, 4, 5, 6, 6, 6, 5, 1, 2, 0, 4, 6, 0, 2, 2, 1, 1, 2, 3, 4, 1, 3, 4, 0, 6, 2, 1, 3, 4, 0, 6, 0, 1, 3, 2, 2, 1, 6, 5, 5, 1, 1, 2, 6, 2, 3, 4, 4, 0, 4, 6, 1, 4, 3, 1, 4, 6, 0, 4, 3, 6, 1, 0, 0, 4, 3, 6, 0, 5, 4, 0, 0, 6, 4, 0, 2, 6, 4, 1, 4, 4, 1, 2, 4, 1, 1, 1, 3, 4, 3, 0, 4, 0, 6, 5, 0, 5, 2, 5, 3, 4, 5, 3, 4, 2, 2, 6, 3, 1, 5, 3, 5, 2, 0, 3, 2, 2, 3, 3, 1, 3, 6, 5, 5, 6, 0, 2, 4, 0, 2, 4, 5, 2, 4, 6, 1, 4, 5, 1, 4, 1, 3, 0, 3, 2, 2, 3, 1, 5, 0, 5, 5, 3, 1, 4, 3, 6, 4, 1, 2, 0, 1, 6, 3, 3, 2, 2, 3, 4, 2, 1, 5, 2, 2, 2, 4, 6, 4, 2, 6, 1, 6, 1, 1, 6, 4, 3, 0, 4, 6, 2, 6, 3, 6, 4, 2, 3, 1, 1, 4, 3, 2, 5, 0, 0, 1, 0]
gene_2 = [6, 4, 1, 0, 4, 5, 1, 4, 5, 1, 4, 4, 0, 4, 2, 4, 4, 3, 0, 3, 1, 0, 4, 4, 4, 5, 4, 2, 4, 2, 6, 4, 3, 1, 4, 5, 1, 4, 3, 3, 0, 4, 3, 1, 1, 0, 4, 4, 5, 0, 6, 1, 2, 3, 3, 4, 1, 3, 4, 4, 3, 3, 1, 3, 4, 4, 3, 4, 6, 4, 5, 6, 2, 0, 2, 5, 0, 0, 6, 1, 1, 6, 4, 5, 6, 4, 4, 1, 4, 0, 3, 4, 6, 1, 4, 4, 5, 1, 3, 0, 4, 5, 3, 3, 3, 2, 3, 4, 2, 4, 3, 0, 6, 3, 3, 4, 3, 3, 4, 4, 1, 4, 2, 4, 3, 2, 0, 4, 2, 1, 4, 4, 0, 2, 5, 0, 3, 1, 3, 0, 0, 1, 3, 1, 0, 3, 1, 1, 3, 0, 5, 3, 1, 4, 4, 6, 4, 2, 3, 1, 4, 3, 2, 4, 4, 2, 4, 2, 4, 2, 0, 2, 4, 6, 2, 6, 0, 2, 2, 6, 0, 4, 4, 0, 1, 1, 2, 5, 0, 0, 1, 3, 3, 0, 5, 0, 5, 5, 1, 2, 2, 1, 6, 2, 6, 1, 3, 6, 4, 0, 6, 0, 2, 4, 6, 0, 3, 0, 4, 2, 4, 0, 5, 4, 0, 5, 3, 2, 1, 6, 1, 3, 5, 0, 6, 2, 1, 3, 2, 6, 3, 4, 6]
gene_3 = [6, 4, 3, 0, 4, 1, 1, 4, 3, 1, 4, 2, 1, 4, 4, 6, 6, 6, 0, 4, 4, 4, 6, 4, 5, 5, 1, 2, 4, 4, 2, 4, 1, 3, 4, 6, 2, 4, 6, 6, 4, 3, 6, 6, 4, 0, 4, 0, 2, 2, 5, 6, 4, 6, 3, 4, 5, 3, 4, 1, 0, 5, 4, 3, 4, 5, 3, 4, 2, 3, 3, 3, 1, 6, 5, 2, 2, 0, 0, 0, 5, 3, 4, 4, 0, 4, 1, 1, 4, 1, 1, 4, 1, 6, 4, 6, 1, 2, 3, 0, 4, 4, 0, 2, 5, 4, 1, 5, 6, 4, 4, 6, 4, 1, 1, 4, 1, 3, 4, 3, 3, 3, 5, 6, 5, 1, 0, 4, 5, 2, 4, 1, 2, 1, 1, 2, 5, 0, 6, 3, 0, 3, 3, 5, 6, 2, 3, 1, 2, 5, 0, 4, 5, 0, 0, 4, 5, 1, 6, 0, 6, 3, 2, 4, 0, 2, 4, 6, 0, 5, 2, 2, 4, 1, 2, 4, 4, 1, 4, 3, 0, 6, 3, 2, 1, 3, 6, 5, 6, 3, 2, 6, 5, 0, 6, 2, 4, 6, 2, 4, 4, 2, 0, 4, 6, 1, 2, 3, 6, 0, 5, 4, 2, 4, 0, 6, 4, 0, 3, 5, 2, 6, 3, 2, 6, 0, 5, 1, 6, 3, 6, 3, 0, 5, 3, 1, 2, 3, 3, 5, 2, 2, 3]
gene_4 = [6, 4, 0, 0, 4, 2, 1, 4, 1, 1, 4, 6, 0, 4, 3, 1, 1, 5, 0, 4, 4, 0, 4, 5, 5, 0, 0, 2, 4, 3, 0, 4, 6, 2, 4, 3, 1, 4, 4, 0, 6, 4, 2, 4, 3, 2, 4, 4, 2, 4, 2, 6, 2, 0, 3, 4, 6, 0, 4, 6, 1, 4, 0, 1, 4, 6, 1, 1, 6, 1, 4, 6, 3, 4, 0, 3, 4, 5, 5, 5, 0, 3, 4, 2, 0, 4, 5, 1, 3, 6, 3, 4, 3, 0, 4, 0, 6, 6, 1, 3, 4, 3, 0, 4, 1, 5, 2, 0, 3, 4, 6, 3, 3, 0, 2, 4, 5, 2, 3, 6, 1, 3, 4, 1, 3, 3, 3, 4, 4, 0, 0, 1, 6, 2, 2, 1, 4, 4, 3, 4, 2, 1, 3, 3, 3, 4, 3, 3, 3, 1, 1, 1, 0, 3, 4, 1, 6, 3, 5, 6, 4, 2, 2, 4, 5, 1, 0, 0, 1, 6, 0, 1, 4, 6, 1, 0, 2, 1, 4, 2, 2, 4, 2, 2, 4, 0, 3, 5, 1, 2, 4, 6, 2, 4, 0, 6, 1, 6, 2, 4, 3, 1, 4, 1, 2, 4, 6, 2, 2, 6, 6, 0, 2, 6, 4, 5, 6, 0, 1, 4, 6, 6, 3, 3, 6, 2, 4, 0, 0, 4, 0, 2, 0, 0, 4, 4, 3, 0, 5, 1, 6, 2, 3]
gene_5 = [6, 4, 6, 0, 4, 1, 1, 4, 1, 1, 4, 5, 6, 0, 2, 3, 4, 2, 0, 4, 0, 0, 4, 3, 5, 6, 6, 2, 4, 4, 0, 4, 4, 2, 4, 5, 2, 4, 1, 6, 0, 3, 3, 4, 4, 2, 4, 2, 3, 4, 2, 4, 2, 6, 3, 4, 5, 0, 4, 1, 3, 4, 1, 1, 4, 6, 1, 4, 0, 1, 4, 1, 0, 4, 0, 0, 0, 4, 1, 1, 6, 3, 4, 3, 3, 0, 0, 3, 4, 6, 1, 4, 1, 0, 0, 3, 3, 4, 0, 3, 4, 3, 3, 0, 6, 3, 4, 0, 2, 4, 2, 0, 0, 3, 2, 4, 0, 2, 3, 0, 0, 0, 1, 1, 4, 5, 2, 2, 1, 3, 2, 6, 3, 0, 0, 3, 3, 2, 6, 0, 6, 3, 4, 6, 1, 3, 6, 1, 3, 1, 0, 3, 2, 3, 4, 4, 6, 0, 4, 5, 6, 3, 2, 4, 4, 0, 4, 1, 1, 4, 5, 1, 4, 3, 2, 0, 2, 1, 4, 4, 0, 4, 1, 0, 0, 1, 2, 5, 1, 2, 4, 5, 2, 0, 5, 3, 2, 6, 1, 4, 1, 6, 0, 4, 1, 2, 1, 0, 4, 5, 0, 1, 4, 1, 0, 4, 4, 5, 5, 3, 6, 2, 0, 4, 4, 2, 5, 0, 6, 4, 3, 2, 4, 3, 0, 2, 1, 0, 6, 0, 1, 2, 2]

# Cria o pool de 8 genes repetindo os 3 primeiros
genes_pool = [gene_1, gene_2, gene_3, gene_4, gene_5, gene_1, gene_2, gene_3]

# Função para obter o estado do robô no tabuleiro
def get_state(board, x, y):
    def get_cell(cx, cy):
        if cx < 0 or cx >= 10 or cy < 0 or cy >= 10:
            return 2 # Parede
        return board[cy][cx]

    current = get_cell(x, y)
    up = get_cell(x, y - 1)
    down = get_cell(x, y + 1)
    left = get_cell(x - 1, y)
    right = get_cell(x + 1, y)

    return current * 1 + up * 3 + down * 9 + left * 27 + right * 81

# Lógica de movimento
def simulate_step(board, rx, ry, gene):
    state = get_state(board, rx, ry)
    action = gene[state]
    if action == 6:
        action = random.randint(0, 3) # Aleatório entre as 4 direções

    if action == 0 and ry > 0: ry -= 1 # Cima
    elif action == 1 and ry < 9: ry += 1 # Baixo
    elif action == 2 and rx > 0: rx -= 1 # Esquerda
    elif action == 3 and rx < 9: rx += 1 # Direita
    elif action == 4 and board[ry][rx] == 1: board[ry][rx] = 0 # Pega lata

    return board, rx, ry

# Ativa o modo interativo do matplotlib
plt.ion()

# Configuração da Janela 1: Tabuleiros
fig_boards, axes = plt.subplots(2, 4, figsize=(12, 6))
fig_boards.canvas.manager.set_window_title('Robby the Robot - 8 Tabuleiros')
fig_boards.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_boards.suptitle("Animação Simultânea - 500 movimentos (~6 segundos)")

# Mapa de cores: 0=Branco(Vazio), 1=Verde(Lata)
cmap = mcolors.ListedColormap(['white', 'limegreen'])

im_list = []
rob_scat = []

# Configuração da Janela 2: Gráfico de Latinhas
fig_graph, ax_graph = plt.subplots(figsize=(8, 5))
fig_graph.canvas.manager.set_window_title('Evolução - Latinhas Restantes')

history = {i: [] for i in range(8)}
epoch = 0

while True:
    # Inicializa tabuleiros e robôs
    boards = []
    robots = []
    for i in range(8):
        b = np.zeros((10, 10), dtype=int)
        cans = random.sample(range(100), 50)
        for c in cans: b[c // 10][c % 10] = 1
        boards.append(b)
        robots.append([random.randint(0, 9), random.randint(0, 9)])

        # Desenho Inicial
        if epoch == 0:
            ax = axes.flatten()[i]
            im = ax.imshow(boards[i], cmap=cmap, vmin=0, vmax=1)
            im_list.append(im)

            # Formato do robô na tela (quadradinho vermelho)
            scat = ax.scatter(robots[i][0], robots[i][1], c='red', s=80, marker='s', edgecolors='black')
            rob_scat.append(scat)

            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_title(f'Solução {i+1}')

            # Adiciona grid para enxergar as casas
            ax.set_xticks(np.arange(-0.5, 10, 1), minor=True)
            ax.set_yticks(np.arange(-0.5, 10, 1), minor=True)
            ax.grid(which='minor', color='lightgray', linestyle='-', linewidth=1)

    start_time = time.time()

    # Simula 500 movimentos (Loop de 6 segundos)
    for m in range(500):
        for i in range(8):
            boards[i], robots[i][0], robots[i][1] = simulate_step(boards[i], robots[i][0], robots[i][1], genes_pool[i])

        # Atualiza a tela a cada 10 movimentos para ter performance no Python
        if m % 10 == 0:
            for i in range(8):
                im_list[i].set_data(boards[i])
                rob_scat[i].set_offsets([[robots[i][0], robots[i][1]]])

            fig_boards.canvas.draw_idle()
            fig_boards.canvas.flush_events()

            # Controle rígido de tempo para cravar em 6 segundos
            elapsed = time.time() - start_time
            expected_time = (m / 500) * 6.0
            if elapsed < expected_time:
                time.sleep(expected_time - elapsed)

    # Finalizou os 500 movimentos, plota o gráfico na Janela 2
    epoch += 1
    ax_graph.clear()
    for i in range(8):
        remaining = np.sum(boards[i] == 1)
        history[i].append(remaining)
        ax_graph.plot(range(1, epoch + 1), history[i], marker='o', label=f'Solução {i+1}')

    ax_graph.set_title(f'Latinhas que NÃO foram pegas ao final de 500 movimentos (Rodada: {epoch})')
    ax_graph.set_xlabel('Rodada Sorteada (Epoch)')
    ax_graph.set_ylabel('Quantidade de Latinhas (de 50)')
    ax_graph.grid(True, linestyle='--')

    # Posiciona a legenda do lado de fora do gráfico
    ax_graph.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig_graph.tight_layout()

    fig_graph.canvas.draw_idle()
    fig_graph.canvas.flush_events()
