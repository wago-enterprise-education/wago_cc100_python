#Author Bjarne Zaremba <bjarne.zaremba@wago.com>

from distutils.core import setup
setup(
  name = 'CC100IO',         
  packages = ['CC100IO'],   
  version = '1.0',     
  license='MIT',        
  description = 'Basic python module to control the input and output ports of a WAGO CC100 controller',   
  author = 'Bjarne Zaremba',                   
  author_email = 'bjarne.zaremba@wago.com',      
  url = 'https://github.com/wago-enterprise-education/wago_cc100',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
  keywords = ['CC100IO'],   
  install_requires=[
      "pyfakefs >= 6.1.0"
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
