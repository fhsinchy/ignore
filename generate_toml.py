import os.path
import configparser

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# Create a ConfigParser object
config = configparser.ConfigParser()

# Set the values in the configuration
config['package'] = {
    'name': 'ignore',
    'version': '1.0.0',
    'description': 'generates a .gitignore file using a given template name',
    'long_description': README,
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/fhsinchy/ignore',
    'author': 'Farhan Hasin Chowdhury',
    'author_email': 'shovik.is.here@gmail.com',
    'license': 'GPL-3.0',
    'classifiers': [
        'License :: OSI Approved :: GPL-3.0 License',
        'Programming Language :: Python :: 3',
    ],
    'py_modules': 'ignore',
    'entry_points': {
        'console_scripts': 'ignore=ignore:main'
    },
    'install_requires': 'requests'
}

# Write the configuration to a file
with open('config.ini', 'w') as file:
    config.write(file)
