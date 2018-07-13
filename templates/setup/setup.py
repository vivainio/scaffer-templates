from distutils.core import setup

setup(name='scflibname',
      version='1.0.0',
      description='Desciption for scflibname here',
      author='scf-gitusername',
      author_email='scf-gitemail',
      url='scf-gitrepo',
      packages=['scflibname'],
      install_requires=[],
      entry_points = {
        'console_scripts': [
            'scflibname = scflibname.scflibname:main'
        ]
      }
     )
