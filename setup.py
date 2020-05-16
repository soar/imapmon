import os
from pathlib import Path
from setuptools import setup, find_namespace_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='imapmon',
    version=Path('version.txt').read_text().strip(),
    packages=find_namespace_packages(include=['imapmon.*']),
    include_package_data=True,
    url='https://soar.name',
    license='MIT',
    author='soar',
    author_email='i@soar.name',
    description='Tool for monitoring IMAP mailboxes and retransmitting received emails via alternative channels',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords=['imap', 'telegram'],
    entry_points={
        'console_scripts': [
            'imapmon = imapmon.scripts:run'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
