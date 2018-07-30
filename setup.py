from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='deep_plots',
      version='0.1.1',
      description='Visualize Your Deep Learning Training in Static Graphics',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/jfilter/deep-plots',
      author='Johannes Filter',
      author_email='hi@jfilter.de',
      license='MIT',
      packages=['deep_plots'],
      install_requires=['plotnine==0.3.*', 'pandas==0.23.*'],
      classifiers=['Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 2.7',
                   'License :: OSI Approved :: MIT License',
                   'Development Status :: 3 - Alpha'
                   ],
      zip_safe=False)
