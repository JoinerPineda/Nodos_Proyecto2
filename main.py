import tkinter as tk
from tkinter import messagebox
import math

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruta Más Corta")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Botones
        self.btn_add_node = tk.Button(root, text="Agregar Nodo", command=self.add_node_mode)
        self.btn_add_node.pack(side=tk.LEFT)

        self.btn_add_edge = tk.Button(root, text="Agregar Arista", command=self.add_edge_mode)
        self.btn_add_edge.pack(side=tk.LEFT)

        self.btn_shortest_path = tk.Button(root, text="Camino Más Corto", command=self.find_shortest_path_mode)
        self.btn_shortest_path.pack(side=tk.LEFT)

        # Variables
        self.nodes = []  # Lista de nodos
        self.edges = {}  # Diccionario de aristas dirigidas
        self.node_count = 0
        self.mode = None  # Modo actual
        self.selected_nodes = []  # Nodos seleccionados para aristas o caminos

        # Eventos del canvas
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def add_node_mode(self):
        self.mode = "add_node"

    def add_edge_mode(self):
        self.mode = "add_edge"
        self.selected_nodes = []

    def find_shortest_path_mode(self):
        self.mode = "shortest_path"
        self.selected_nodes = []

    def on_canvas_click(self, event):
        if self.mode == "add_node":
            self.add_node(event.x, event.y)
        elif self.mode == "add_edge":
            self.select_node_for_edge(event.x, event.y)
        elif self.mode == "shortest_path":
            self.select_node_for_path(event.x, event.y)

    def add_node(self, x, y):
        self.node_count += 1
        node_id = self.node_count
        self.nodes.append((node_id, x, y))
        self.edges[node_id] = {}
        self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="lightblue")
        self.canvas.create_text(x, y, text=str(node_id), fill="black")

    def select_node_for_edge(self, x, y):
        node = self.get_node_at_position(x, y)
        if node:
            self.selected_nodes.append(node)
            if len(self.selected_nodes) == 2:
                self.add_edge(self.selected_nodes[0], self.selected_nodes[1])
                self.selected_nodes = []

    def add_edge(self, node1, node2):
        x1, y1 = self.get_node_coordinates(node1)
        x2, y2 = self.get_node_coordinates(node2)
        weight = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
        self.edges[node1][node2] = weight
        self.draw_arrow(x1, y1, x2, y2)

    def draw_arrow(self, x1, y1, x2, y2):

        radius = 15

        dx = x2 - x1
        dy = y2 - y1
        distance = math.sqrt(dx**2 + dy**2)

        # Ajustar los puntos para que terminen en el borde del círculo
        if distance != 0:  
            x1_adjusted = x1 + (dx / distance) * radius
            y1_adjusted = y1 + (dy / distance) * radius
            x2_adjusted = x2 - (dx / distance) * radius
            y2_adjusted = y2 - (dy / distance) * radius
        else:  # Si los nodos están superpuestos, no ajustar
            x1_adjusted, y1_adjusted = x1, y1
            x2_adjusted, y2_adjusted = x2, y2

        # Dibujar la flecha ajustada
        self.canvas.create_line(
            x1_adjusted, y1_adjusted, x2_adjusted, y2_adjusted, fill="black", arrow=tk.LAST
        )

    def select_node_for_path(self, x, y):
        node = self.get_node_at_position(x, y)
        if node:
            self.selected_nodes.append(node)
            if len(self.selected_nodes) == 2:
                path, distance = self.find_shortest_path(self.selected_nodes[0], self.selected_nodes[1])
                if path:
                    messagebox.showinfo("Camino Más Corto", f"Ruta: {'-'.join(map(str, path))} (Distancia: {distance})")
                else:
                    messagebox.showwarning("Camino No Encontrado", "No hay camino entre los nodos seleccionados.")
                self.selected_nodes = []

    def find_shortest_path(self, start, end):
        unvisited = {node: float('inf') for node in self.edges}
        unvisited[start] = 0
        visited = {}
        parents = {}

        while unvisited:
            current_node = min(unvisited, key=unvisited.get)
            current_distance = unvisited[current_node]

            if current_node == end:
                path = []
                while current_node in parents:
                    path.insert(0, current_node)
                    current_node = parents[current_node]
                path.insert(0, start)
                return path, current_distance

            for neighbor, weight in self.edges[current_node].items():
                if neighbor not in visited:
                    new_distance = current_distance + weight
                    if new_distance < unvisited[neighbor]:
                        unvisited[neighbor] = new_distance
                        parents[neighbor] = current_node

            visited[current_node] = current_distance
            unvisited.pop(current_node)

        return None, None

    def get_node_at_position(self, x, y):
        for node_id, nx, ny in self.nodes:
            if (nx - 15 <= x <= nx + 15) and (ny - 15 <= y <= ny + 15):
                return node_id
        return None

    def get_node_coordinates(self, node_id):
        for node in self.nodes:
            if node[0] == node_id:
                return node[1], node[2]
        return None, None

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
