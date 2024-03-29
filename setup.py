from setuptools import setup
REQUIRES = [
    'allure',
    'requests'
]

setup(
    name='dm_account_api',
    version='0.0.1',
    packages=['dm_account_api', 'dm_account_api.apis', 'dm_account_api.models'],
    url='https://github.com/widowblack11/dm_account_api.git',
    license='MIT',
    author='oksanaprokopenko',
    author_email='-',
    istall_requires=REQUIRES,
    description='client for dm_account_api service'
)
