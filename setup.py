from setuptools import setup, find_packages


SETUP = {
    'name': 'mypy_type_alias',
    'python_requires': '~= 3.8',
    'install_requires': [
        'typing_extensions ~= 4.4.0; python_version < "3.10"',
    ],
    'extras_require': {
        'development': [
            'mypy ~= 0.991',
        ],
    },
}

if __name__ == '__main__':
    setup(**SETUP)
