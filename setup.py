# Copyright 2015 D-red inc.
# Author: Koichi Yoshigoe <yoshigoe@d-red.jp>

from setuptools import setup

setup(
    name = 'eksperimentoj',
    package = ['eksperimentoj']
    author = 'Koichi Yoshigoe',
    author = 'Koichi Yoshigoe',
    author_email = 'yoshigoe@d-red.jp',
    install_requires = ['tornado'],
    entry_points = {
        '': [
            'tornado = eksperimentoj:app'
        }
    }
)
