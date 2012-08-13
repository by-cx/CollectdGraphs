import os
from glob import glob
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "collectd_graphs",
    version = "0.1",
    author = "Adam Strauch",
    author_email = "cx@initd.cz",
    description = ("Collectd frontend"),
    license = "GPLv2",
    keywords = "collectd,graphs,statistics",
    url = "https://github.com/creckx/CollectdGraphs",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    long_description="Make iptables rules more easier to maintain.",#read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    #data_files=["views", glob("views/*")],
    install_requires=[
        #"termcolor",
    ],
    entry_points="""
    [console_scripts]
    collectd_graphs = collectd_graphs.web:main
    """
)