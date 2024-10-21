import os
import json
import requests
from bs4 import BeautifulSoup
import tqdm
import argparse


def main(args):

    os.makedirs('data/crawl', exist_ok=True)

    java_module_documentation = {}
    java_module_documentation.setdefault(args.module_name, {})

    base_url = 'https://docs.oracle.com/en/java/javase/21/docs/api/'
    index_url = base_url + 'index.html'

    req = requests.get(index_url)
    if req.status_code != 200 or req.url != index_url:
        print(f'Error: Failed to get index url {index_url}')
        return
    
    print(f'Processing index page: {index_url}')

    soup = BeautifulSoup(req.text, 'html.parser')
    modules_block = soup.find('div', {'id': 'all-modules-table'})
    module_block = modules_block.find('div', string=args.module_name)
    if module_block is None:
        print(f'Error: Failed to find package {args.module_name}')
        return

    module_url = base_url + module_block.find('a')['href']

    req = requests.get(module_url)
    if req.status_code != 200 or req.url != module_url:
        print(f'Error: Failed to get module url {module_url}')
        return
    
    print(f'Processing module page: {module_url}')
    
    soup = BeautifulSoup(req.text, 'html.parser')
    packages_block = soup.find('section', {'id': 'packages-summary'})
    available_packages = [package for package in packages_block.find_all('div') if package.text.startswith('java.')]
    for package in tqdm.tqdm(available_packages):
        package_url = module_url.replace('module-summary.html', '') + package.find('a')['href']

        java_module_documentation[args.module_name].setdefault(package.text, {})

        print(f'Processing package {package_url}')

        req = requests.get(package_url)
        if req.status_code != 200 or req.url != package_url:
            print(f'Error: Failed to get package url {package_url}')
            return
        
        soup = BeautifulSoup(req.text, 'html.parser')

        summary_block = soup.find('section', {'class': 'summary'})

        buttons = {button.text: button['id'] for button in summary_block.find_all('button')}

        for button_name, button_id in buttons.items():

            if button_name == 'All Classes and Interfaces':
                continue

            java_module_documentation[args.module_name][package.text].setdefault(button_name, {})

            divs = summary_block.find_all('div', {'class': button_id})
            for div in divs:

                if 'col-first' not in div['class']:
                    continue

                assert div.find('a') is not None, f'Error: Failed to find link in {button_name} {div}'

                java_module_documentation[args.module_name][package.text][button_name].setdefault(div.find('a').text, {})

                interface_class_url = package_url.replace('package-summary.html', '') + div.find('a')['href']

                print(f'Processing {button_name} {interface_class_url}')

                req = requests.get(interface_class_url)
                if req.status_code != 200 or req.url != interface_class_url:
                    print(f'Error: Failed to get {button_name} url {interface_class_url}')
                    break

                soup = BeautifulSoup(req.text, 'html.parser')

                div_block = soup.find('section', {'class': 'details'})

                if div_block is None:
                    print(f'Warning: No details block in {button_name} {interface_class_url}')
                    continue
                
                java_module_documentation[args.module_name][package.text][button_name][div.find('a').text].setdefault('fields', {})
                java_module_documentation[args.module_name][package.text][button_name][div.find('a').text].setdefault('constructors', {})
                java_module_documentation[args.module_name][package.text][button_name][div.find('a').text].setdefault('methods', {})

                for element in ['field', 'constructor', 'method']:

                    details_block = div_block.find('section', {'class': f'{element}-details'})
                    if details_block is not None:
                        for element_section in details_block.find_all('section', {'class': 'detail'}):

                            if element_section.find('div', {'class': 'deprecation-block'}) is not None: # Skip deprecated elements
                                continue

                            name = element_section['id']
                            signature = element_section.find("div", {"class": "member-signature"}).text
                            description = element_section.find("div", {"class": "block"}).text
                            notes = element_section.find("dl", {"class": "notes"}).text if element_section.find("dl", {"class": "notes"}) is not None else ''

                            java_module_documentation[args.module_name][package.text][button_name][div.find('a').text][f'{element}s'].setdefault(name, {})
                            java_module_documentation[args.module_name][package.text][button_name][div.find('a').text][f'{element}s'][name]['signature'] = signature.replace('\u00a0', ' ')
                            java_module_documentation[args.module_name][package.text][button_name][div.find('a').text][f'{element}s'][name]['description'] = description.replace('\u00a0', ' ')
                            java_module_documentation[args.module_name][package.text][button_name][div.find('a').text][f'{element}s'][name]['notes'] = notes.replace('\u00a0', ' ')
                    else:
                        print(f'Warning: No field details found in {button_name} {interface_class_url}')
    
    with open(f'data/crawl/{args.module_name}_module_doc.json', 'w') as f:
        json.dump(java_module_documentation, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crawl java module and packages')
    parser.add_argument('--module_name', type=str, default='java.base', help='Java module name. Default: java.base')
    args = parser.parse_args()
    main(args)
