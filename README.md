# Garden-Connect

As beginner gardeners, it can often be difficult to find a place on how to begin gardening. With the vast amounts of information available, it can be overwhelming and even demoralizing to garden with the chance of failure. What if there were an application that would help you garden along the way. Garden connect is an application which helps beginner gardeners through their gardening adventures. With features such as messaging between other beginner gardeners; posting gardener photos; accessing helpful information pages; and receiving notifications on when to garden, Garden Connect is an application that has the backs of many beginner gardeners.

## Required Software
To run the software, you will need the following:
* Django
* celery
* Django-celery-beat
* pillow
* asgiref
* pytz
* sqlparse

### Library installation
To install the all of the necessary libraries, we recommend doing the following:
* Ensure that you're running a version of Python that is 3.9 or above
* Open a terminal for a version of Linux installed on your machine
* Once it loads, we recommend creating a new Anaconda environment. This can be done by doing the following
```
conda create --name <Environment Name> python=3.9
```
Where you may name your environment whatever you would like
* Be patient and make sure that you type y to create your environment after a dialog box appears
* After the environment has been created, run the following command
```
conda activate <Environment Name>
```
To activate your Anaconda environment
* You're now ready to install the libraries to use this repository. Ensure that your file directory is at the root of this repository. By typing `ls` in the repository directory, you should see a file called `requirements.txt`. Finally, you can run the following

```
pip install -r requirements.txt
```
* Be patient and wait for the libraries to finish installing

### Running Garden Connect Locally
If you would like to test out the Garden Connect application locally, please do the following:
* Ensure that you are at the root repository directory
* By typing `ls` in the repository directory, you should see a file called `manage.py`
* In the terminal, type in the following which will set up the dependencies to run the app:
```
python manage.py migrate
```
* Please be patient while you wait for all of the dependencies to load
* After the dependencies have finished loading, type the command
```
python manage.py runserver
```
* A local IP address should load where you may copy it and paste it into your web browser
* You are now free to use Garden Connect in whatever way you may feel like it!

If you would like to learn more about the mission and drive of Garden Connect, feel free to check out our website explaining the puporse of our project [https://kla-pie.github.io/garden-connect/](https://kla-pie.github.io/garden-connect/). Happy Gardening!

If you have any questions, please feel free to reach out to Solomiia Kachur (skachur@olin.edu) or Kevin Lie-Atjam (klieatjam@olin.edu)