#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name="example-pkg-shaurya",
    version="1.0.1",
    author="shaurya sinha",
    author_email="shaurya.r.sinha2000@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shauryabit2k18/samplepackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
 )

