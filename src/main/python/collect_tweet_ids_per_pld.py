import csv
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
    entities = []
    for tweetId in bindings:
        entities.append(tweetId['tweetId']['value'])
    return entities


def tweet_ids_per_pld(pld, output_directory_tweet_ids):
    pld_prepared = "\"" + pld[0] + "\""
    tweet_ids_list = query_tweet_ids_per_pld(pld_prepared)
    tweet_ids_list = map(lambda x: x + '\n', tweet_ids_list)
    tweet_ids_file = open(output_directory_tweet_ids+'tweet_ids_'+pld[0]+'.txt', 'w')
    tweet_ids_file.writelines(tweet_ids_list)
    tweet_ids_file.close()


def collect_tweet_ids_per_pld(input_file_name_left, input_file_name_right, output_directory_tweet_ids):
    with open(input_file_name_left, newline='') as left_train:
        left_plds = csv.reader(left_train, delimiter=' ', quotechar='|')
        for pld in left_plds:
            tweet_ids_per_pld(pld, output_directory_tweet_ids)
    with open(input_file_name_right, newline='') as right_train:
        right_plds = csv.reader(right_train, delimiter=' ', quotechar='|')
        for pld in right_plds:
            tweet_ids_per_pld(pld, output_directory_tweet_ids)


def collect_tweet_ids_per_pld(input_file_name, output_directory_tweet_ids):
    with open(input_file_name, newline='') as train:
        plds = csv.reader(train, delimiter=' ', quotechar='|')
        for pld in plds:
            tweet_ids_per_pld(pld, output_directory_tweet_ids)

