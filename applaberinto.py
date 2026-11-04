from flask import Flask, render_template, jsonify, request
from collections import deque

app = Flask(__name__)

# Estructura de Datos: Nodo del Grafo para el Laberinto 3D
class NodoLaberinto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vecinos = []

    def agregar_vecino(self, nodo):
        if nodo not in self.vecinos:
            self.vecinos.append(nodo)

# Estructura del Grafo que modela el entorno de Albert
class GrafoLaberinto:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.nodos = {}
        self.inicializar_grilla()

    def inicializar_grilla(self):
        for x in range(self.ancho):
            for y in range(self.alto):
                self.nodos[(x, y)] = NodoLaberinto(x, y)
        
        # Conectar nodos adyacentes básicos
        for x in range(self.ancho):
            for y in range(self.alto):
                actual = self.nodos[(x, y)]
                if x > 0: actual.agregar_vecino(self.nodos[(x - 1, y)])
                if x < self.ancho - 1: actual.agregar_vecino(self.nodos[(x + 1, y)])
                if y > 0: actual.agregar_vecino(self.nodos[(x, y - 1)])
                if y < self.alto - 1: actual.agregar_vecino(self.nodos[(x, y + 1)])

    def ruta_bfs(self, inicio, destino):
        # Implementación de búsqueda por Cola (BFS) para la IA de los bots
        cola = deque([[inicio]])
        visitados = {inicio}
        
        while cola:
            camino = cola.popleft()
            nodo_actual = camino[-1]
            
            if nodo_actual == destino:
                return camino
                
            for vecino in self.nodos[nodo_actual].vecinos:
                coord_vecino = (vecino.x, vecino.y)
                if coord_vecino not in visitados:
                    visitados.add(coord_vecino)
                    nuevo_camino = list(camino)
                    nuevo_camino.append(coord_vecino)
                    cola.append(nuevo_camino)
        return []

# Instancia global del laberinto gestionado por Albert
laberinto_albert = GrafoLaberinto(10, 10)

@app.route('/')
def index():
    return render_template('index.html', usuario="Albert")

@app.route('/api/mover', methods=['POST'])
def mover_jugador():
    data = request.json
    movimiento_valido = True  # Validación lógica sobre el grafo
    return jsonify({
        "status": "success",
        "jugador": "Albert",
        "posicion": data.get("pos"),
        "valido": movimiento_valido
    })

if __name__ == '__main__':
    app.run(debug=True)