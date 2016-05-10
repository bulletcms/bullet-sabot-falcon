from setuptools import setup

setup(
    name='bulletsabot',
    version='0.1.0',
    description='part of the bulletcms',
    url='http://github.com/bulletcms/bullet-sabot',
    author='xorkevin',
    license='MPL-2.0',
    packages=['bulletsabot'],
    install_requires=[
        'falcon',
        'ujson',
        'gcloud',
        'meinheld',
        'gunicorn'
    ]
)
