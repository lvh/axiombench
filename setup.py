from distutils.core import setup

setup(name='axiombench',
      version='0',
      description='Silly benchmarks for Axiom',
      url='https://github.com/lvh/axiombench',

      author='Laurens Van Houtven',
      author_email='_@lvh.cc',

      packages=["axiombench", "axiombench.test"],

      license='ISC',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Twisted",
        "License :: OSI Approved :: ISC License (ISCL)",
        ]
)
