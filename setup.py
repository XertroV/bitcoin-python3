from setuptools import setup, find_packages
setup(
    name='bitcoin-python3',
    version='0.3',
    description='Friendly Bitcoin JSON-RPC API binding for Python 3',
    long_description='This package allows performing commands such as listing the current balance'
    ' and sending coins to the Satoshi (original) client from Python 3. The communication with the'
    ' client happens over JSON-RPC.',
    maintainer='Ashot Seropian',
    maintainer_email='ondaemon@gmail.com',
    url='http://laanwj.github.com/bitcoin-python/doc/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial'
    ],
    packages=find_packages("src"),
    package_dir={'': 'src'}
)
