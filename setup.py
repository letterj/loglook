

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple web interface to search logs',
    'author': 'Jay Payne (letterj)',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'letterj@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['loglook'],
    'scripts': [],
    'name': 'loglook'
}

setup(**config)
