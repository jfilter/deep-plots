from setuptools import setup

setup(name='deep_plots',
      version='0.1.0',
      description='Plotting Loss and Accuracy for your Deep Learning Training',
      url='https://github.com/jfilter/deep-plots',
      author='Johannes Filter',
      author_email='hi@jfilter.de',
      license='MIT',
      packages=['deep_plots'],
      install_requires=['plotnine==0.3.0', 'pandas==0.23.3'],
      zip_safe=False)
