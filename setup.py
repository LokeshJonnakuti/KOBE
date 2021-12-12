from setuptools import find_packages, setup

setup(
    name="kobe",
    version="2.0",
    author="Qibin Chen",
    author_email="qibinc@andrew.cmu.edu",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(exclude=[]),
    install_requires=[
        "black>=21.10b0",
        "cached_property>=1.5.2",
        "gdown>=4.2.0",
        "isort>=5.8.0",
        "joblib>=1.0.1",
        "pandas>=1.3.4",
        "pre-commit>=2.15.0",
        "pytest>=6.2.4",
        "pytorch-lightning>=1.5.4",
        "sacrebleu>=2.0.0",
        "sentencepiece>=0.1.96",
        "scipy>=1.7.3",
        "torch>=1.10",
        "tqdm>=4.62.3",
        "wandb>=0.12.7",
        "webdataset>=0.1.103",
    ],
)
