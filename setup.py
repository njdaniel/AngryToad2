from setuptools import setup

setup(name='angrytoad',
      version='1.0.1',
      packages=['angrytoad'],
      entry_points={
          'console_scripts': [
              'angrytoad = angrytoad.__main__:main'
          ]
      },
      )