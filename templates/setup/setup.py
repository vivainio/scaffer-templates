from distutils.core import setup

setup(name='bah',
      version='0.0.0',
      description='Blah',
      author='Bah',
      author_email='bah@gmail.com',
      url='https://github.com/',
      packages=['wpathr'],
      install_requires=['dep'],
      entry_points = {
        'console_scripts': [
            'bahher = bahher.bahher:main'
        ]
      }
     )
