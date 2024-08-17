# stats101
Basic classical statistics in Python

# Content

* [Chapter 1: Git and Github](#Chapter1)
* [Chapter 2: Python virtual environment](#Chapter2)
* [Chapter 3: Normal Distribution,mean, median, mode and standard deviation](#Chapter3)
* [Chapter 4: Central Limits Theorem, sample size, statistical power](#Chapter4)

<div id="Chapter1"></div>

Git and Github
-----------------

**Git**

A software tool for code version control

You can save snapshots of your code. Typically when you have a bug free and working version of your code, you "commit" (take a snap shot) of the code to your repository. You then continue to edit your code to add more functionality. But at times, your code may no longer work because of errors in your logic and you may want to revert back to the older version of your code. With git version control it is possible for you to retrieve older versions of your code.

**Github**

It is an online platform for creating code repositories that can be shared by many people. Software projects usually have many people collaborating on code development. Github code repositories make it possible to share and edit code in a systematic manner with git version control.

**How to install Git**

On windows we can install Git by installing Github.
But first create an account on Github. It is free.

# stats101
Basic classical Statistics in Python

# Content

* [Chapter 1: Git and Github](#Chapter1)
* [Chapter 2: Python virtual environment](#Chapter2)
* [Chapter 3: Normal Distribution,mean, median, mode and standard deviation](#Chapter3)
* [Chapter 4: Central Limits Theorm, sample size, statistical power](#Chapter4)

<div id="Chapter1"></div>

Git and Github
-----------------

**Git**

A software tool for code version control

You can save snapshots of your code. Typically when you have a bug free and working version of your code, you "commit" (take a snap shot) of the code to your repository. You then continue to edit your code to add more functionality. But at times, your code may no longer work because of errors in your logic and you may want to revert back to the older version of your code. With git version control it is possible for you to retrieve older versions of your code.

**Github**

It is an online platform for creating code repositories that can be shared by many people. Software projects usually have many people collaborating on code development. Github code repositories make it possible to share and edit code in a systematic manner with git version control.

**How to install Git**

On windows we can install Git by installing Github.
But first create an account on Github. It is free.

https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github


<div id="Chapter2"></div>

 Python Virtual Environment
 -----------------------------------------------------------------


A Virtual Environment is an isolated working copy of Python for each project you create. In thi manner you can customize the python environment for a project without affecting other projects. 

For now just learn how to set up python "virtual environment" for developing code.
Once you start writing some code, installing python "libraries" or "packages", you will begin to understand why we create "virtual environments" for developing code.


**How to create python vnenv**

On the terminal

1. pip install virtualenv
2. python -m venv .venv
3. source .venv/bin/activate


<div id="Chapter3"></div>

# Normal Distribution, mean, median, mode, variance and standard deviation

**Population and Sample**

What is a population?

The entire group on which you would like to collect information on.

A hypothetical example of a population could be all the 10000 students of Jadavpur university and the information you may want to collect may be the average weights of the students. You may also want to examine the average weight of the students by gender.

* average weight = sum of all the students' weight / total number of students

* average female weight = sum of all the female students' weight / total number of female students

* average male weight = sum of all the female students' weight / total number of female students

So how will you find out this information?

Will you measure the weights of all the students?

It will cost time and money to measure all the students.

Is it possible to arrive at the answers you seek by measuring the weights of a subset of the students instead? That would be nice as you can save time and money.

But before we go about sampling a subset of data, let us investigate the properties of the data of the "population".

It so happens that some of the phenomena in nature have values that are distributed more or less symmetrically about the mid point of their data range.

Most values in the data are near the center of the range of the data. For example the weight of adult humans in kilograms in Asia. The range is 45 to 85 kilos and most people weight around 65 kilos 

The center of the range is the mean or the average of the data. 

As you go further and further away from the center or the mean the frequency of data points decreases. Extreme values on either side are very very very rare. 

This kind of behaviour produces a frequencey distribution curve that looks like a bell. 

Data with such a bell shape are said to be "normally distributed" about the mean.

**Normal distribution (The Bell Shaped Curve) is also know as Gaussian distribution**

![The Bell Curve](./images/bell-curve.jpg "The Bell Curve")

[Source: https://www.simplypsychology.org/normal-distribution.html]

**Mean, median, mode and standard deviation**

![The Bell Curve](./images/normal-distribution.webp "The Bell Curve")

[Source: https://www.simplypsychology.org/normal-distribution.html]

<div id="Chapter4"></div>

The Central limits theorm, sample size and statistical power
-------------------------------------------------------------
