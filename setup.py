from setuptools import setup, find_packages
setup(
    name='pyas',
    version='1.0.2',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description="Run machine code directly in Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/pyas',
    project_urls={
        'Documentation': 'https://github.com/donno2048/pyas#readme',
        'Bug Reports': 'https://github.com/donno2048/pyas/issues',
        'Source Code': 'https://github.com/donno2048/pyas',
    },
    packages=find_packages()
)
