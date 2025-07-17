from setuptools import setup, find_packages

setup(
    name="crypto_tools",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'ccxt',
        'python-telegram-bot',
        'python-dotenv'
    ],
)