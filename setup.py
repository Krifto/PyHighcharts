from distutils.core import setup

setup(
    name='PyHighcharts',
    version='0.0.1',
    author='Dieter Vandenbussche',
    author_email='',
    packages=['PyHighcharts', 'PyHighcharts.highcharts'],
    package_data={'PyHighcharts': ['templates/*.tmp']},
    url='',
    description='',
    long_description=open('README.md').read(),
)
