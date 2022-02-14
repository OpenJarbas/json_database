from setuptools import setup

setup(
    name='json_database',
    version='0.7.0',
    packages=['json_database'],
    url='https://github.com/OpenJarbas/json_database',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    install_requires=["combo_lock~=0.2.1"],
    description='searchable json database with persistence'
)
