
# coding: utf-8

# # Git Tutorial
# 
# 2/3/2018

# This notebook contains a very brief introduction to Git.
# 
# Git is a very useful and powerful version control system
# 
# Git is **NOT** very user-friendly
# 
# There are a number of websites and programs that attempt to make git more user friendly

# ## Resources

# - https://try.github.io/ - cool site to introduce you to git
# - https://git-scm.com/doc - Official documentation
# - https://git-scm.com/book/en/v2 - Free Git Book

# ## Installing git

# Go to https://git-scm.com/ and install Git for your particular operating system

# ## Setting up git

# Open up a terminal window - this will depend on your operating system.
#  - Windows: start GitBash
#  - Linux: open a terminal
#  - OS X: open a terminal???
#  - ChromsOS : In developer mode, type CLT-ALT-T

# In[2]:


get_ipython().getoutput('git config --list')


# You want to store your username and email address:
# ```
# git config --global user.name "John Doe"
# git config --global user.email johndoe@example.com
# ```

# ## Github

# [Github](https://github.com) is a website that allows you to easily create public git repositories. Students are also able to create private git repositories.
# 
# You should sign up to github when you have the chance, however you do not need to for the next step.
# 
# Clone the repository containing this document:
# 
# ```
# git clone https://github.com/b-trav/GitTutorial.git
# ```

# ## Repository

# - A repository is a store of all the versions of all the files in a git project (directory).
# - A repository can either be a _working_ repository, or a _bare_ repository.
# - Working repositories have all your files in them, but they also have a sub-directory called `.git` which contains all the versions of your work.
# - A bare repository is simply the .git folder on its own - normally called `ProjectName.git`

# ## Cloning a repository

# ```
# git clone https://github.com/b-trav/GitTutorial.git
# ```

# ## Creating a repository

# Rather than cloning a repository, you can make your current directory into a git project by simply typing:
# ```
# git init
# ```

# ## Checking the status of a repository

# In[8]:


get_ipython().system('git status')


# ## Adding files

# In[4]:


get_ipython().system('git add Git*')


# ## Committing files

# In[5]:


get_ipython().system('git commit -m "Initial commit of this repository. Committing the Jupyter notebook containing a tutorial about git."')


# ## Ignoring files

# There are often files in git that you do not want versioned. These might include binary files from a compiler, unnecessary backup files, or sensitive files containing usernames or passwords.
# 
# Jupyter creates a directory call `.ipynb_checkpoints/` which stores info about your current notebook. We do not need to version this file, so let's ignore it.
# 
# We ignore files by simply listing them in a special file called `.gitignore`.
# 

# In[6]:


get_ipython().system('echo ".ipynb_checkpoints/" >> .gitignore')


# In[7]:


get_ipython().system('cat .gitignore')


# In[9]:


get_ipython().system('git add .gitignore')


# In[10]:


get_ipython().system('git commit -m "Adding .gitignore file, and ignoring ipynb_checkpoints."')


# In[11]:


get_ipython().system('git status')


# ## Pushing files

# In[13]:


get_ipython().system('git push origin master')


# ## Pulling files

# In[14]:


get_ipython().system('git pull origin master')


# ## Branches, merging and much more

# In[ ]:




