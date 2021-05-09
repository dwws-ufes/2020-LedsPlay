import re
from pprint import pprint
import requests

BASE_URL = "https://query.wikidata.org/sparql"

# Buscando instâncias de 'professional skill', 'capability', 'skill' e 'programming language'
competenceQuery = """
SELECT ?competence ?competenceLabel ?competenceDescription
WHERE
{  {  ?competence wdt:P31 wd:Q7535186  }  UNION { ?competence wdt:P31 wd:Q1347367 } UNION {  ?competence wdt:P31 wd:Q205961 } UNION { ?competence wdt:P31 wd:Q9143 }.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,pt". }
}
"""

headers = {
    "Accept": "application/sparql-results+json"
}

# GET request para endpoint SPARQL com retorno em json
response = requests.get(
    BASE_URL,
    params={'query': competenceQuery},
    headers=headers,
)
results = response.json()

if response.status_code == 200:
    print("Successful GET request to SPARQL endpoint!")

    # Dicionário com competências
    competences = {}
    for result in results["results"]["bindings"]:
        # Se não existir descrição, deixe-a vazia
        competenceDescription = result.get('competenceDescription', {}).get('value', "")

        try:
            competenceName = result['competenceLabel']['value']
            if re.match(r"Q\d+", competenceName):  # Se não houver nome (label), pule
                print("\nEmpty entity. Skipping...\n")
                continue
            if not competenceDescription:  # Se não houver descrição, pule
                print("\nEmpty description. Skipping...\n")
                continue
        except:
            print(f"\nFailed to get competenceLabel ({result})\n")
            continue

        # Nome e descrição prontos para registrar sob nova competência no DB
        # print(f"Competence: {competenceName}.\n\tDescription: {competenceDescription}\n")
        competences[competenceName] = competenceDescription

    # pprint(competences)
else:
    print("Failed GET request to SPARQL endpoint.")
