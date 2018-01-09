import pypandoc
from setuptools import setup

if __name__ == '__main__':
    readme = open('README.md').read()
    long_description = pypandoc.convert_text(
        readme, 'rst', format='markdown_github')

    console_scripts = ["pystart = pystart.cmd:entry_point"]
    setup(
        entry_points=dict(console_scripts=console_scripts),
        long_description=long_description)
