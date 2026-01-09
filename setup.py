from setuptools import setup, find_packages

setup(
    name="lyricalabs",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.8",
    description="Lyrica Labs API Python, Nexa LLM",
    url="https://lyricalabs.vercel.app",
    author="Lyrica Labs",
    author_email="lyricalabs@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
