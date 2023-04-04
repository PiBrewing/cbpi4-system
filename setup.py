from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-system',
      version='0.0.9.a4',
      description='CraftBeerPi4 Plugin for system fucntions',
      author='Alexander Vollkopf',
      author_email='avollkopf@web.de',
      url='https://github.com/avollkopf/cbpi4-system',
      include_package_data=True,
      keywords='globalsettings',
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-system': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-system'],

      install_requires=[
            'psutil>=5.9.0',
            'gpiozero',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
