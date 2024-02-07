import os
import json
import requests
from bs4 import BeautifulSoup
import tqdm
import argparse


def main(args):

    project = args.project_name

    if not os.path.exists(f'data/type_resolution/{project}/type_description.json'):

        types = {}
        with open(f'data/type_resolution/{project}/s1_input.json') as f:
            types = json.load(f)
        
        type_descriptions = {}
        for type_ in types:

            if types[type_] != '':
                continue

            type_descriptions[type_] = {
                'link': '',
                'text': '',
                'summarized_text': ''
            }
        
        with open(f'data/type_resolution/{project}/type_description.json', 'w') as f:
            json.dump(type_descriptions, f, indent=4)


    type_descriptions = {}
    with open(f'data/type_resolution/{project}/type_description.json') as f:
        type_descriptions = json.load(f)

    for type_ in tqdm.tqdm(type_descriptions):

        assert type_descriptions[type_]['text'] == ''

        formatted_type = ''
        if '<' in type_:
            formatted_type = type_[:type_.find('<')]
        elif '[' in type_:
            formatted_type = type_[:type_.find('[')]
        else:
            formatted_type = type_

        if type_descriptions[type_]['link'] != '':
            description_link = type_descriptions[type_]['link']
        else:
            description_link = 'https://docs.oracle.com/javase/8/docs/api/' + formatted_type.replace('.', '/') + '.html'

        req = requests.get(description_link)
        if req.status_code != 200 or req.url != description_link:
            continue

        soup = BeautifulSoup(req.text, 'html.parser')
        text = soup.find('div', {'class': 'block'}).text

        sentences = text.split('.')
        type_descriptions[type_]['link'] = description_link
        type_descriptions[type_]['text'] = text
        type_descriptions[type_]['summarized_text'] = sentences[0]

    with open(f'data/type_resolution/{project}/type_description.json', 'w') as f:
        json.dump(type_descriptions, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crawl type descriptions')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    args = parser.parse_args()
    main(args)
