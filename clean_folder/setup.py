from setuptools import setup, find_namespace_packages

setup(name='cleanfolder',
      version='1',
      description='Organize folder based on extensions',
      url='https://github.com/AnastasiaFa/',
      author='Anstasiia',
      author_email='annfatyeyeva@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points ={
            'console_scripts': [
                'cleanfolder = clean:clean'
            ]})