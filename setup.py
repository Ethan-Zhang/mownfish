from setuptools import setup, find_packages
setup(
    name="mownfish",
    description="A Tornado Productional Skeleton",
    author="Ethan-Zhang",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    packages=find_packages(),
    package_data={'':['*.ico']},
    include_package_data=True,
    version='2.0.0',
    entry_points = {
        'console_scripts': [
            'mownfishd = mownfish.cmd.mownfishd:main',
            ],
        },
    py_modules=['mownfish'],
    )
