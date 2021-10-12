from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='tracardi',
    version='0.6.17',
    description='Tracardi Customer Data Platform backend',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Risto Kowaczewski',
    author_email='risto.kowaczewski@gmail.com',
    packages=['tracardi'],
    install_requires=[
        'pip>=21.2.4',
        'pydantic',
        'aiohttp',
        'aiohttp[speedups]',
        'redis',
        'aioredis',
        'elasticsearch==7.13.4',
        'prodict>=0.8.18',
        'tzlocal',
        'python-multipart>=0.0.5',
        'lark>=0.11.3',
        'dateparser',
        'dotty-dict==1.3.0',
        'pytz',
        'device_detector==0.10',
        'deepdiff>=5.5.0',
        'tracardi-plugin-sdk>=0.6.18',
        'tracardi_graph_runner>=0.6.5',
        'tracardi-dot-notation>=0.6.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['tracardi'],
    include_package_data=True,
    python_requires=">=3.8",
)