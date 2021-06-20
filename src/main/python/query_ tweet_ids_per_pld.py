from SPARQLWrapper import SPARQLWrapper, JSON


def query_tweet_ids_per_pld(pld):
    sparql = SPARQLWrapper("https://data.gesis.org/tweetscov19/sparql")
    sparql.setQuery("""

    PREFIX schema: <http://schema.org/>
    PREFIX sioc: <http://rdfs.org/sioc/ns#>


    SELECT ?tweetId WHERE {
    ?tweet schema:citation ?url.
      FILTER REGEX( STR(?url), """ + pld + """, "i" )    
      ?tweet sioc:id ?tweetId      
     }

    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    result_json = results['results']
    bindings = result_json['bindings']
    ids = []
    for tweetId in bindings:
        ids.append(tweetId['tweetId']['value'])
    return ids
