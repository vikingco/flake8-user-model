from __future__ import with_statement
from setuptools import setup


def get_version(fname='flake8_user_model.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)

install_requires = ['flake8']

setup(
    name='flake8-user-model',
    version=get_version(),
    description="user model import checker plugin for flake8",
    long_description=get_long_description(),
    keywords='flake8 user-level imports',
    author='Unleashed NV',
    author_email='development@unleashed.be',
    url='https://github.com/unleashed/flake8-user-model',
    license='MIT',
    py_modules=['flake8_user_model'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'flake8_user_model = flake8_user_model:UserModelImportsChecker',
        ],
    },
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
