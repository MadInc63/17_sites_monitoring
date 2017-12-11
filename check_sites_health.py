import argparse
import requests
from whois import whois
from urllib.parse import urlparse
from datetime import datetime


def arg_parser():
    parse = argparse.ArgumentParser(description='URL health checker')
    parse.add_argument('path', type=str, help='path to open file with url')
    return parse.parse_args()


def load_urls4check(path):
    with open(path, encoding='utf-8') as urls_file:
        for url_string in urls_file:
            yield url_string.strip()


def is_server_respond_with_200(verifiable_url):
    responce = requests.get(verifiable_url)
    return responce


def get_domain_expiration_date(domain_name):
    domain_info = whois(domain_name)
    return domain_info.expiration_date


if __name__ == '__main__':
    arg = arg_parser()
    for url in load_urls4check(arg.path):
        domain_expiration_date = get_domain_expiration_date(urlparse(url)[1])
        current_date = datetime.now()
        delta = domain_expiration_date - current_date
        if delta.days > 30:
            print(url)
            print('Responce '
                  'from URL: {}'.format(is_server_respond_with_200(url)))
            print('Expiration date: {}'.format(domain_expiration_date))
            print('Days before expiration: {}'.format(delta.days))
            print('----------------------------------------------------------')
