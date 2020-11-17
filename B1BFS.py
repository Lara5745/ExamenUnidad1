#Busqueda bidireccional Mejor el primero 

# Definir la clase del nodo

class AdjacentNode:
	
	def __init__(self, vertex):
		
		self.vertex = vertex
		self.next = None

# Clase de implementación del logaritmo
class BidirectionalSearch:
	
	def __init__(self, vertices):
		
		# Inicializar vertices y gráficos con vertices

		self.vertices = vertices
		self.graph = [None] * self.vertices
		
		# Inicializar la cola la busqueda de ida y de vuelta

		self.src_queue = list()
		self.dest_queue = list()
		
		# Inicializar busqueda y orientación al visitar nodos falsos

		self.src_visited = [False] * self.vertices
		self.dest_visited = [False] * self.vertices
		
		# Inicializar busqueda y orientación para los nodos padres  

		self.src_parent = [None] * self.vertices
		self.dest_parent = [None] * self.vertices
		
	# Función para agregar vortices unidireccionales  
	def add_edge(self, src, dest):
		
		# Agregar vortices al grafo
		
		# Agregar destinacion
		node = AdjacentNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		node = AdjacentNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
		
	# Funcion BEST - FIRST
	def bfs(self, direction = 'forward'):
		
		if direction == 'forward':
			
			# BFS direccion de ida
			current = self.src_queue.pop(0)
			connected_node = self.graph[current]
			
			while connected_node:
				vertex = connected_node.vertex
				
				if not self.src_visited[vertex]:
					self.src_queue.append(vertex)
					self.src_visited[vertex] = True
					self.src_parent[vertex] = current
					
				connected_node = connected_node.next
		else:
			
			# BFS direccion de regreso
			current = self.dest_queue.pop(0)
			connected_node = self.graph[current]
			
			while connected_node:
				vertex = connected_node.vertex
				
				if not self.dest_visited[vertex]:
					self.dest_queue.append(vertex)
					self.dest_visited[vertex] = True
					self.dest_parent[vertex] = current
					
				connected_node = connected_node.next
				
	# Checar vertice de intersección
	def is_intersecting(self):
		
		# Regresar el nodo de intersección
		
		for i in range(self.vertices):
			if (self.src_visited[i] and
				self.dest_visited[i]):
				return i
				
		return -1

	# Imprimir en pantalla el camino 
	def print_path(self, intersecting_node, 
				src, dest):
						
		
		path = list()
		path.append(intersecting_node)
		i = intersecting_node
		
		while i != src:
			path.append(self.src_parent[i])
			i = self.src_parent[i]
			
		path = path[::-1]
		i = intersecting_node
		
		while i != dest:
			path.append(self.dest_parent[i])
			i = self.dest_parent[i]
			
		print("*****CAMINO*****")
		path = list(map(str, path))
		
		print(' '.join(path))
	
	# funcion de Busqueda bidireccional
	def bidirectional_search(self, src, dest):
		
		# Agregar fuenete a la cola para distinguir los nodos visitados
		self.src_queue.append(src)
		self.src_visited[src] = True
		self.src_parent[src] = -1
		
		self.dest_queue.append(dest)
		self.dest_visited[dest] = True
		self.dest_parent[dest] = -1

		while self.src_queue and self.dest_queue:
			
			# BFS dirección de ida
			self.bfs(direction = 'forward')
			
			# BFS dirección de vuelta
			self.bfs(direction = 'backward')
			
			# Checar vertice de intersección
			intersecting_node = self.is_intersecting()
			
			
			if intersecting_node != -1:
				print(f"Si exitse un camino entre el nodo : {src} y el nodo: {dest}")
				print(f"El nodo intersección es : {intersecting_node}")
				self.print_path(intersecting_node, 
								src, dest)
				exit(0)
		return -1

# Driver code
if __name__ == '__main__':
	
	# NNumero de vertices en el grafo
	n = 15
	
	# vertice fuente
	src = 0
	
	# vertice destino
	dest = 14
	
	# Grafo
	graph = BidirectionalSearch(n)
	graph.add_edge(0, 4)
	graph.add_edge(1, 4)
	graph.add_edge(2, 5)
	graph.add_edge(3, 5)
	graph.add_edge(4, 6)
	graph.add_edge(5, 6)
	graph.add_edge(6, 7)
	graph.add_edge(7, 8)
	graph.add_edge(8, 9)
	graph.add_edge(8, 10)
	graph.add_edge(9, 11)
	graph.add_edge(9, 12)
	graph.add_edge(10, 13)
	graph.add_edge(10, 14)
	
	out = graph.bidirectional_search(src, dest)
	
	if out == -1:
		print(f"No existe un camino entre el nodo : {src} y el nodo : {dest}")

