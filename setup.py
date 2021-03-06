from distutils.core import setup

long_description = """
Documentation: https://github.com/ziberna/i3-py/blob/master/README.md

Examples: https://github.com/ziberna/i3-py/tree/master/examples

"""

setup(
    name='i3-py',
    description='tools for i3 users and developers',
    long_description=long_description,
    author='Jure Ziberna',
    author_email='jure@ziberna.org',
    url='https://github.com/ziberna/i3-py',
    version='0.6.5',
    license='GNU GPL 3',
    py_modules=['i3']
)
