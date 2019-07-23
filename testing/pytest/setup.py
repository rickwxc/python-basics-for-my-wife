from setuptools import setup, find_packages
# find_namespace_packages


setup(
    name='test1',
    version='0.1',
    # //py_modules=['pkg1'],
    package_dir={'': 'src'},
    packages=find_packages('src')  # , exclude=('tests', 'pkg1'))
    # packages=find_namespace_packages(include=['rickw.*'])
)
