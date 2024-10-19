# A template for lab 2 - strong connectivity in graphs - for CSC 349 at Cal Poly
# Reads a file with a list of edges, then creates one component for each node and outputs it to the screen
# Credit: Rodrigo Canaan 

import sys
import math

class node:

	def __init__(self,name,out_edges,in_edges,previsit, postvisit,component):
		self.name = name
		self.out_edges = out_edges
		self.in_edges = in_edges
		self.previsit = previsit
		self.postvisit = postvisit
		self.component = component

def strong_connectivity(G):
	indexes = order(G)
	components = assign(G, indexes)
	sort_component_list(components)
	return components

def sort_component_list(components):
	for c in components:
		c.sort()
	components.sort(key = lambda x: x[0])

def order(G : list[node]) -> list[node]:
	counter = 1
	sorted_list = []
	for index in range(len(G)):
		if G[index].previsit == -1:
			counter = explore_out(G, index, counter, sorted_list)
	return sorted_list

def explore_out(G : list[node], vertex : int, accumulator : int, sorted_list : list[int]) -> int:
	G[vertex].previsit = accumulator
	accumulator = accumulator + 1
	for neighbor in G[vertex].out_edges:
		if G[neighbor].previsit == -1:
			accumulator = explore_out(G, neighbor, accumulator, sorted_list)
	G[vertex].postvisit = accumulator
	sorted_list.append(vertex)
	accumulator = accumulator + 1
	return accumulator

def assign(G : list[node], indexes : list[int]) -> list[list[int]]:
	component_count = 0
	component_list = []
	for index in range(len(indexes)-1, -1, -1):
		if G[indexes[index]].component == None:
			component_count = component_count + 1
			subgroup = []
			explore_in(G, indexes[index], component_count, subgroup)
			component_list.append(subgroup)
	return component_list

def explore_in(G : list[node], vertex : int, group : int, vertices : list[int]) -> None:
	G[vertex].component = group
	vertices.append(G[vertex].name)
	for neighbor in G[vertex].in_edges:
		if G[neighbor].component == None:
			explore_in(G, neighbor, group, vertices)

def read_file(filename):

	with open(filename) as f:
		lines = f.readlines()
		v = int(lines[0])
		if  v == 0:
			raise ValueError("Graph must have one or more vertices")
		G = list(node(name = i, out_edges=[],in_edges=[],previsit= -1, postvisit=-1, component=None) for i in range(v))
		for l in lines[1:]:
			tokens = l.split(",")
			fromVertex,toVertex = (int(tokens[0]),int(tokens[1]))
			G[fromVertex].out_edges.append(toVertex)
			G[toVertex].in_edges.append(fromVertex)
		return G


def main():
	filename = sys.argv[1]
	G = read_file(filename)
	components = strong_connectivity(G)
	print(components)
		
		
if __name__ == '__main__':
	main()
