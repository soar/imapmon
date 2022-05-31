from pathlib import Path
from setuptools import setup, find_namespace_packages


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
    long_description=Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    keywords=['imap', 'telegram'],
    entry_points={
        'console_scripts': [
            'imapmon = imapmon.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
