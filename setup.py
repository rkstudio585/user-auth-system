from setuptools import setup, find_packages

setup(
    name="user-auth-system", 
    version="6.1.0",  # Version
    description="A Python-based User Authentication System using SQLite3 and SHA-256",
    author="RK", 
    author_email="mdriyadkhan585@gmail.com",  
    url="https://github.com/rkstudio585/user-auth-system", 
    packages=find_packages(),  # Automatically find packages
    install_requires=[  # Dependencies, if any
        # Add any dependencies here, example:
        # 'requests',
    ],
    classifiers=[  # Classifiers to describe your project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
)
