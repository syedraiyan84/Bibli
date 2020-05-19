# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='bibexcel',
      version='1.0.0',
      description='A python executable to get JSON and Excel data from a bibexcel text file',
      url='http://github.com/storopoli/bibexcel',
      author='Jose Eduardo Storopoli',
      author_email='thestoropoli@gmail.com',
      license='MIT',
      packages=['seletivo-lattes'],
      install_requires=[
          'pandas',
          'json'
      ],
      zip_safe=False)