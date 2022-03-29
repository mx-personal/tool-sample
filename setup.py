from setuptools import setup, find_packages

setup(
  name='tool-sample',
  packages=find_packages(),
  version='0.1',
  license='MIT',
  description='Dummy app to test apps deployment possibilities',
  author='mx',
  url='https://github.com/mx-personal/tool-sample',
  keywords=['tool', 'test', ],
  install_requires=[],
  include_package_data=True,
  package_data={'': ['*.txt']},
  entry_points={
    'console_scripts': [
      'tool_test=tool.main:script_foo',
    ]
  }
)