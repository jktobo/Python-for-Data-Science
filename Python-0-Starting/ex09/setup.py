from setuptools import setup

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    author="dkaratae",
    author_email="dkaratae@student.42abudhabi.ae",
    license="MIT",
    classifiers=[],
    entry_points={
        "console_scripts": [
            "ft_package=ft_package:main",  # Пример, если у вас есть точка входа в пакет
        ],
    },
    packages=["ft_package"],
    python_requires=">=3.6",
    metadata_version="2.1",
    installer="pip",
)
