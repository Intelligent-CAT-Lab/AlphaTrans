import os
import json
import requests
from bs4 import BeautifulSoup
import tqdm
import argparse
import re


def main(args):

    os.makedirs(f'data/type_resolution/assert_api', exist_ok=True)

    assert_descriptions = {}

    if args.language == 'java':
        link = 'https://junit.org/junit4/javadoc/4.13/org/junit/Assert.html'

        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')

        method_details = soup.find_all('table')
        for method_detail in tqdm.tqdm(method_details):
            if 'Method Summary' not in method_detail.text:
                continue

            # print all rows
            rows = method_detail.find_all('tr')
            for row in rows[1:]:
                regex = r"^(static\s+void)\s*(\w+\([^)]*\))\s*(.*)$"
                matches = re.search(regex, row.text, re.MULTILINE)

                if matches:
                    static_void = matches.group(1).replace('\u00a0', ' ')
                    method_signature = ' '.join([x.strip().replace('\u00a0', ' ') for x in matches.group(2).split('\n')])
                    deprecation_notice = matches.group(3).replace('\u00a0', ' ')

                    assert_descriptions[method_signature] = {
                        'return_type': static_void.strip(),
                        'method_signature': method_signature.strip(),
                        'description': deprecation_notice.strip()
                    }
                else:
                    print(row.text)
                    print("No match found.")
                
    with open(f'data/type_resolution/assert_api/{args.language}.json', 'w', encoding='utf-8') as f:
        json.dump(assert_descriptions, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crawl type descriptions')
    parser.add_argument('--language', required=True, type=str, help='Name of the programming language')
    args = parser.parse_args()
    main(args)
