from urllib.parse import urlparse


def domain_name(url):
    items = urlparse(url).hostname if str(url).startswith("http") else url
    items = items.split('.')
    return items[1] if items[0] == 'www' else items[0]
