from setuptools import setup, find_packages
setup(
    name="mownfish",
    description="A Tornado Productional Skeleton",
    author="Ethan-Zhang",
    author_email = 'unpeeled_onion@outlook.com',
    license="http://www.apache.org/licenses/LICENSE-2.0",
    url = 'https://github.com/ethan-zhang/mownfish',
    download_url = 'https://github.com/Ethan-Zhang/mownfish/tree/v2.4',
    keywords = ['tornado'],
    packages=find_packages(),
    package_data={'':['*.ico']},
    include_package_data=True,
    version='2.4.2',
    entry_points = {
        'console_scripts': [
            'mownfishd = mownfish.cmd.mownfishd:main',
            ],
        },
    py_modules=['mownfish'],
    )
