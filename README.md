
###### The code constructs a graph of all word senses using a horde of relations like attributes, causes, derivationally related forms, topic domains, hypernyms and hyponyms etc. The measure of similarity between two senses is a function of the shortest path distance between them in the wordnet graph.

###### This is a revamp of the codebase: https://github.com/sharmi/metonym

* Instructions:

	- Building the codebase:

			pip install requiremnts.txt
		
	- Creating the graph:

			python3 scripts/create_wordnet_graph /path/to/wordnet_graph.adj
			
	- Similarity comparison test:
	
			python test/test.py <graph_name>.adj <w1> <w2>
		
