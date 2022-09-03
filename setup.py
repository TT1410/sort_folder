from setuptools import setup


setup(name='sort_folder',
      version='1',
      description='Сортування файлів у папці',
      url='http://github.com/dummy_user/useful',
      author='TT1410',
      author_email='tarplax@gmail.com',
      license='MIT',
      packages=['sort_folder'],
      include_package_data=True,
      entry_points={'console_scripts': ['sort-folder = sort_folder:main']}
)
