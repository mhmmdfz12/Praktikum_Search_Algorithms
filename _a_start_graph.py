# -*- coding: utf-8 -*-
"""*A Start Graph

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nk6M4kJ-cAaj27uM2bq8cjEmH5pPn0xi
"""

from queue import PriorityQueue

def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))  # (f(n), node)

    came_from = {}  # Menyimpan jalur terpendek
    cost_so_far = {start: 0}  # Menyimpan biaya g(n)
    explored = set()  # Simpan simpul yang sudah dieksplorasi

    while not frontier.empty():
        current_cost, current_node = frontier.get()  # Ambil simpul dengan f(n) terendah

        if current_node in explored:
            continue  # Lewati jika sudah dieksplorasi

        explored.add(current_node)  # Tandai sebagai dieksplorasi

        if current_node == goal:
            # Rekonstruksi jalur dari goal ke start
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from.get(current_node, None)
            path.reverse()

            print("Simpul tujuan ditemukan!")
            print("Jalur yang ditemukan:", " → ".join(path))
            print("Total biaya jalur:", cost_so_far[goal])
            return True

        for neighbor, step_cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + step_cost  # g(n) + biaya langkah

            if neighbor not in explored and (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current_node  # Simpan jalur

    print("Simpul tujuan tidak ditemukan!")
    return False

# Heuristik (h(n))
heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0
}

# Graph dengan biaya antar simpul (g(n))
graph = {
    'S': {'A': 3, 'E': 2},
    'A': {'B': 3, 'C': 4},
    'B': {'D': 5},
    'C': {'G': 3},
    'D': {'G': 3},
    'E': {'D': 6}
}

start_node = 'S'
goal_node = 'G'

a_star_graph_search(graph, start_node, goal_node, heuristic)