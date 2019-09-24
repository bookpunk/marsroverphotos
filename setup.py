from setuptools import setup

with open('README.md', 'r') as infile:
    long_description = infile.read()

with open('requirements.txt', 'r') as infile:
    install_requirements = list(infile.read().splitlines())

setup(name='marsroverapp',
      version='0.1',
      description='Retrieve Mars Rover Photos using the NASA API',
      url='https://github.com/bookpunk/marsroverphotos.git',
      author='Matt Adams',
      author_email='bookpunk@gmail.com',
      license='MIT',
      long_description=long_description,
      install_requires=install_requirements,
      python_requires='>=3.5',
      packages=['marsroverapp'],
      zip_safe=False)

