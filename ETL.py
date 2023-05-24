import requests
import pandas as pd

def get_human_characters():
    response = requests.get('https://rickandmortyapi.com/api/character')
    data = response.json()
    characters = data['results']

    human_characters = [character for character in characters if character['species'] == 'Human']
    df = pd.DataFrame(human_characters)
    html_table = df.to_html()
    return html_table


def generate_html_table(results):
    df = pd.DataFrame(results)
    html_table = df.to_html()
    return html_table