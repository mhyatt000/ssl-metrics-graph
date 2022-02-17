from setuptools import setup

# TODO: Change import
from ssl_metrics_MODULE_NAME import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # TODO: Change name
    # TODO: Change packages
    # TODO: Change description
    name="ssl-metrics-MODULE-NAME",
    packages=["ssl_metrics_MODULE_NAME"],
    version=version.version(),
    description="SSL Metrics - SHORT DESCRIPTION",
    author="Software and Systems Laboratory - Loyola University Chicago",
    author_email="ssl-metrics@ssl.luc.edu",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ssl.cs.luc.edu/projects/metricsDashboard",
    project_urls={
        # TODO: Change Bug Tracker URL
        # TODO: Change GitHub Repository URL
        "Bug Tracker": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-REPOSITORY-NAME/issues",
        "GitHub Repository": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-REPOSITORY-NAME",
    },
    keywords=[
        "bus factor",
        "commits",
        "engineering",
        "git",
        "github",
        "issue density",
        "issues",
        "kloc",
        "loyola",
        "loyola university chicago",
        "luc",
        "mining",
        "metrics",
        "repository",
        "repository mining",
        "simple",
        "software",
        "software engineering",
        "software metrics",
        "software systems laboratory",
        "ssl",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.9",
    install_requires=[
        # TODO: Add requirements
    ],
    entry_points={
        # TODO: Change module name
        # TODO: Change module function to execute
        "console_scripts": [
            "ssl-metrics-MODULE-NAME-compute = ssl_metrics_MODULE_NAME.FILENAME:main",
            "ssl-metrics-MODULE-NAME-graph = ssl_metrics_MODULE_NAME.create_graph:main",
        ]
    },
)
