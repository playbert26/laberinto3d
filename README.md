# Laberinto 3D - Estructura de Datos

Prototipo de videojuego interactivo en entorno tridimensional basado en la exploración de laberintos, desarrollado en Python. Este proyecto implementa un **Grafo No Dirigido** y el algoritmo de búsqueda **BFS (Breadth-First Search)** mediante una Cola para optimizar la navegación de los bots y la gestión dinámica del mapa.

## 🌐 Juega en línea

Enlace público del despliegue: [https://albertfl.pythonanywhere.com/](https://albertfl.pythonanywhere.com/)

---

## 🎮 Controles e Instrucciones

* **Movimiento:** Utiliza las teclas de dirección (Flechas) o W, A, S, D para recorrer los corredores del laberinto en perspectiva 3D.
* **Cámara / Interacción:** Rota la vista con el cursor del ratón para evaluar las rutas libres de obstáculos.
* **Objetivo:** Encontrar la salida del laberinto antes de que el tiempo se agote o los bots controlados por la inteligencia artificial alcancen tu posición.

---

## ⚙️ Mecánicas Implementadas

* **Modelado por Grafos (`GrafoLaberinto`):** El mapa completo se estructura mediante nodos interconectados (aristas) que representan cada intersección y pasillo transitable.
* **Inteligencia Artificial con BFS (`ruta_bfs`):** Los bots utilizan una Cola (`deque`) para calcular la ruta más corta posible hacia la posición actual del jugador Albert en tiempo real.
* **Servidor Web con Flask:** Arquitectura ligera en Python para procesar las peticiones del cliente y renderizar la interfaz web interactiva.

---

## 🛠️ Tecnologías y Entorno

* **Lenguaje:** Python 3.13
* **Framework Web:** Flask
* **Estructuras de Datos:** Grafos No Dirigidos, Nodos y Colas (BFS)
* **Hosting / Despliegue:** PythonAnywhere (Servidor WSGI)
* **Control de Versiones:** Git / GitHub (`albert-hub/laberinto3d`)


* **Albert** — Escuela Profesional de Ingeniería de Sistemas, Universidad Andina del Cusco.
* **Asignatura:** Estructura de Datos
* **Docente:** Giomar
