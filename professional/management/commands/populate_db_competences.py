import re
import requests
from django.core.management.base import BaseCommand
from professional.models import Competencia


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_competences(self):
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
                competenceName = result.get('competenceLabel', {}).get('value', "")

                try:
                    if not competenceDescription or not competenceName:  # Se não houver nome ou descrição, pule
                        print(f"Empty label or description. Skipping {result['competence']['value']}...")
                        continue
                    if re.match(r"Q\d+", competenceName):  # Se não houver nome (label) além do QID, pule
                        print(f"Empty entity. Skipping {result['competence']['value']}...")
                        continue
                except:
                    print(f"Failed to process {result}")
                    continue

                # Nome e descrição prontos para registrar sob nova competência no DB
                # print(f"Competence: {competenceName}.\n\tDescription: {competenceDescription}\n")
                competences[competenceName] = competenceDescription

            # Create and save competences on DB
            for competenceLabel, competenceDescription in competences.items():
                print(competences.items())
                createCompetence = Competencia(nome=competenceLabel, descricao=competenceDescription)
                createCompetence.save()
        else:
            print("Failed GET request to SPARQL endpoint.")

    def handle(self, *args, **options):
        self._create_competences()
