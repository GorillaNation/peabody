from distutils.core import setup

setup(
    name='peabody',
    version='0.2.1',
    author='Jeremy Kitchen',
    author_email='jeremy.kitchen@gorillanation.com',
    packages=['peabody'],
    scripts=['bin/peabody'],
    url='https://github.com/gorillanation/peabody',
    license='LICENSE.txt',
    description='wrapper for cronjobs to provide timeouts, locking, and some other fun features',
    long_description=open('README.rst').read(),
    install_requires=[
        "lockfile",
        "redis",
    ],
)
