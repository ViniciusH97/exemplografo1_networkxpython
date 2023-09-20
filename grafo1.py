import networkx as nx
import matplotlib.pyplot as plt

# Verifique a versão, no teminal digite: python --version
# Use o gerenciador de pacote pip e instale networkx e matplotlib: 
# pip install networkx
# pip install matplotlib

G = nx.Graph()

# Adicionando as vértices

G.add_node('v1')
G.add_node('v2')
G.add_node('v3')
G.add_node('v4')
G.add_node('v5')
G.add_node('v6')
G.add_node('v7')
G.add_node('v8')

# Adicionando as arestas ao grafo

G.add_edge('v1', 'v2')
G.add_edge('v1', 'v3')
G.add_edge('v2', 'v1')
G.add_edge('v2', 'v3')
G.add_edge('v3', 'v6')
G.add_edge('v3', 'v1')
G.add_edge('v3', 'v2')
G.add_edge('v6', 'v7')
G.add_edge('v7', 'v8')
G.add_edge('v1', 'v5')
G.add_edge('v2', 'v4')
G.add_edge('v4', 'v9')

# Mostrar todos os vértices do grafo

print('Os vértices do grafo G são:')
for i in G.nodes():
  print(i)
  
# Mostrar as arestas

print('As arestas presentes no grafo G são:')
for c in G.edges():
  print(c)
  
# Graus dos grafos
print('Graus dos vértices:')
print(G.degree())

# Representação do grafico com imagem

print('Grafo G')
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()