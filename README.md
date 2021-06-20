# home_project_dke_2021

I used the hydrated texts of tweets mentioning left- or rightleaning plds to train a multinomial naive bayes classifier.

## generation of training data
I generated the training data in 4 steps:
* For each pld I queried the TweetsCOV19 SPARQL endpoint (https://data.gesis.org/tweetscov19/sparql) for all the tweet ids in which the pld is mentioned.
This is my SPARQL query:
```

PREFIX schema: <http://schema.org/>
PREFIX sioc: <http://rdfs.org/sioc/ns#>

SELECT ?tweetId 
WHERE
{?tweet schema:citation ?url.
  FILTER REGEX( STR(?url), """ + pld + """, "i" )    
  ?tweet sioc:id ?tweetId      
}
	 
```

* For each pld I used the generated tweet ids to hydrate the full texts of the tweets. I used 'twarc'(https://pypi.org/project/twarc/) for this. 
* With help of 'NLTK' (https://www.nltk.org/) I generated a feature set with the 6000 most used words in those texts.
* I then generated the training dataset by counting the occurences of those words in all of the tweets related to one pld.

## classification
I used 'scikit-learn'(https://scikit-learn.org/stable/index.html) to train a multionomial naive bayes classifier on the generated feature set.
The classifier can be used for the test data after preparing it the same way as mentioned above (without generating a new feature set of course).

## Reproduce the output
The output can be reproduced by running the 'full_script_to_reproduce_outputs.py' file. It might take a while and you also need twitter API keys to hydrate the tweets with twarc.

## Process

At first I wanted to generate a feature set with metadata like mentioned entities, mentioned users, sentiment scores and hashtags.
I figured out that it takes a really long time to retrieve enough data via SPARQL queries, so I tried to download the TweetsCOV19 dataset and browse it.
Even after I collected some data with the mentioned features and trained it with different classifiers my results were not very good.
I decided to go another way and analyzed the tweets language.
Later I thought that maybe I could have made better use of the SPARQL endpoint by specifying my queries more (e.g. not just count tweets mentioning a specific person, then count tweets having a specific sentiment scores, but counting tweets mentioning a specific person and having a specific sentiment score),
but maybe those combinations are also covered by some classification algorithms and I shoud just have gathered more data.





