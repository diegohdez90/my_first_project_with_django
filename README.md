# Website with Django
 
1. Install Python 3.5 or later from Python [website](https://www.python.org/downloads/) or using [Anaconda](https://www.anaconda.com/download/).

- Install Python with Anaconda:

  -Open Anaconda prompt.

  - Create an environment with specific versions of python and django:
 
  `$ conda create --name <env-name> django=1.10 & python=3.6`

  - List conda envs with: 
  
  `$ conda info --envs`

  - Activate a conda env: 
  
  `$ activate <env-name>`

  - Review if python is correct (3.x.y)

2. Install Django (v1.10).
  - With pip: 
  
  `$ pip install django==1.10`
  - With Anaconda, after create and activate an environment with Anaconda: 
  
  `$ conda install django=1.10`

3. Clone project