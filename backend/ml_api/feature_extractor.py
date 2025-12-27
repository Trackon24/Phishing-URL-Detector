import re
from urllib.parse import urlparse

suspicious_words = [
    'login', 'verify', 'update', 'bank',
    'secure', 'account', 'signin', 'confirm'
]

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    features = {}

    features['url_length'] = len(url)
    features['domain_length'] = len(domain)

    features['count_digits'] = sum(c.isdigit() for c in url)
    features['digit_ratio'] = features['count_digits'] / max(len(url), 1)

    features['count_special_chars'] = len(
        re.findall(r'[@\-_=?.&]', url)
    )

    features['num_subdomains'] = domain.count('.')

    features['has_https'] = int(parsed.scheme == 'https')

    features['has_ip'] = int(
        bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))
    )

    features['suspicious_word_count'] = sum(
        word in url.lower() for word in suspicious_words
    )

    return features
