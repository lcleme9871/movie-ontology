import logging
import rdflib
from _pyio import open

# configuring logging
logging.basicConfig()

# creating the graph
g=rdflib.Graph()
result=g.parse("full_example.owl", "xml")
print("graph has %s statements.\n" % len(g))


# FILTER (str(?name) = str(?name1)) line is a neat trick to combine individuals that are created
# from two sources.For example individual 1236 is actually the data from linkedmdb for the movie 
# Harry Potter and the Philosopher's Stone. 1236 includes raiting information for the movie 
# which is not available from DBpedia.
query="""
PREFIX ma: <http://www.semanticweb.org/ontologies/ECS735/movie.owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
SELECT DISTINCT ?name ?budget ?rating
WHERE { ?film ma:title ?name .
        ?film ma:budget ?budget . 
        ?film1 ma:title ?name1 .
        ?film1 ma:rating ?rating .
        FILTER (str(?name) = str(?name1))
        FILTER regex(str(?name),"Harry Potter")        
        } ORDER BY DESC(?budget)
        """

# querying and displaying the results
print ('{0:45s} {1:10s} {2:10s}'.format("Title","Budget","Rating"))
for x,y,z in g.query(query):
    print ('{0:45s} {1:10s} {2:10s}'.format(x,y,z))
    