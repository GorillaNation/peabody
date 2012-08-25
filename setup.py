from distutils.core import setup

setup(
    name='peabody',
    version='0.2.0',
    author='Jeremy Kitchen',
    author_email='jeremy.kitchen@gorillanation.com',
    packages=['peabody'],
    scripts=['bin/peabody'],
    url='https://bitbucket.org/kitchen/peabody',
    license='LICENSE.txt',
    description='wrapper for cronjobs to provide timeouts, locking, and some other fun features',
    long_description=open('README.txt').read(),
    install_requires=[
        "lockfile",
    ],
)
