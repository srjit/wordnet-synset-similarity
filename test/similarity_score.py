from nltk.corpus import wordnet as wn
#from metonym import WordNetGraph


import sys
sys.path.insert(0, '../syn_sim')

from syn_sim import WordNetGraph
from argparse import ArgumentParser

graph = "wordnet_syn_graph.adj"

def similarity_score(w1, w2):

	wngraph = WordNetGraph(graph)
	syns1 = wn.synsets(w1)
	syns2 = wn.synsets(w2)

	sim = 0.0

	for syn1 in syns1:
		for syn2 in syns2:
			path_similarity = wngraph.path_similarity(syn1, syn2)
			if path_similarity > sim:
				sim = path_similarity
				print("%s\t%s\t%s" %(syn1.name(), syn2.name(), path_similarity))

	return sim


print(similarity_score("mathematics", "computer_science"))




