import argparse
import requests
from whois import whois
from urllib.parse import urlparse
from datetime import datetime


def parse_args():
    parse = argparse.ArgumentParser(description='URL health checker')
    parse.add_argument('path', type=str, help='path to open file with url')
    return parse.parse_args()


def load_urls4check(path):
    with open(path, encoding='utf-8') as urls_file:
        for url_string in urls_file:
            yield url_string.rstrip('\n')


def is_server_respond_with_200(verifiable_url):
    try:
        response = requests.get(verifiable_url)
        if response.status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        return False


def get_domain_expiration_date(domain_name):
    domain_info = whois(domain_name)
    return domain_info.expiration_date


if __name__ == '__main__':
    arg = parse_args()
    for url in load_urls4check(arg.path):
        response_200 = is_server_respond_with_200(url)
        if response_200:
            domain_expiration_date = get_domain_expiration_date(
                urlparse(url)[1]
            )
            current_date = datetime.now()
            delta = domain_expiration_date - current_date
            if delta.days > 30:
                print(url)
                print('Response '
                      'from URL: {}'.format(response_200))
                print('Expiration date: {}'.format(domain_expiration_date))
                print('Days before expiration: {}'.format(delta.days))
                print('------------------------------------------------------')
