
### Understanding Python Modules  
Can you imagine building a webserver from scratch? Or making a port to a database driver? Or, maybe, comming up with an image manipulation tool? I'm not saying that this is impossible, all I'm saying is that it would be a whole new project by itself.  

Third party libraries are welcome in a way that they prevent you from reinventing the wheel. They save you time to focus on what really matters: to finish and deliver your application.  


#### Meet pip  

pip has become the official Python package manager and it is used basically to install and uninstall packages from the Python Package Index.  


#####However...  
As much as it's a really awesome idea to use modules, you should however not install modules in the main python path! You should also not uninstall python itself and any packages related to the main python path. It is highly recommended to use a virtual environment

#### The Virtual Environment  

By now, you should have understood why it is important (and sane) to separate the dependencies of your projects and that no Python package should be installed under the main Python installation.  

The virtual environment does the following:  
1. Creates a new instance of your main Python installation in a particular directory.  
2. It provides tools for you to activate and deactivate these instances in a way that whenever 	they are activated, they have precedence on your system's PATH. In other words, it means that if you activated your virtualenv and attempted to run any Python binary, it is going to look for it in the new instance's directory first.  

In order to use Python modules, installation is done through pip as below:  
```
sudo pip install virtualenv
```
NOTE: This step is only done once!  

When you're starting a new project you will definitely need an environment. Starting a new environment is as below:  

First ensure you're in a fresh or new folder for your project.  
Second, create a new instance of a virtual environment with a name of your choice
```
virtualenv myenvname

```

Your directory should have the following;  
1. a folder with the name myenvname  
2. Inside the folder, four more directories namely: bin, include, lib and local

Now the only thing remaining to do is to activate the environment done as below:  

```
source myenvname/bin/activate

```

REMEMBER: This is where you are going to install all your third party modules.  
Different projects have different environments thus it's good practice to have environments for each.  

Finally, to deactivate an environment, call the below command:

```
deactivate

```
