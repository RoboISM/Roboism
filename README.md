[![Build Status](https://travis-ci.org/markroxor/Roboism.svg?branch=master)](https://travis-ci.org/markroxor/Roboism)
[![Dependency status](https://gemnasium.com/markroxor/Roboism.svg)](https://gemnasium.com/markroxor/Roboism)

## RoboISM - Running at [roboism.markroxor.in](roboism.markroxor.in)

RoboISM is the official site of Robotics Club ISM Dhanbad. Well right now it is ![alt tag](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQpNgHwfZ40zcRFx2AJ-17aoqeQF9xR53Ho-dPXPh7mku_uaETCjg)



####Who can Contribute ?

* Strictly Homo Sapiens Sapines, Extraterristrials like Martians, Reptillians, Grey Aliens etc, Spongbob, Octopus or any creature who aims to improve our website. 

####How to Contribute?

#####What to do? 
* Keep your code clean and use meaningful variables.
* Use occasional commenting if code is large
* Try using CamelCase for naming functions or classes. 
* Test your code locally before pushing
* Give proper indentaion, use Tab instead of spacing, especially in html code.
* Store all static files(.css, .js, images etc) in [mainsite/static/](https://github.com/markroxor/Roboism/blob/master/mainsite/static/)
* All arrangement related stying(position, padding, margin), of html elements are to be in [mainsite/static/arrangements.css](https://github.com/markroxor/Roboism/blob/master/mainsite/static/arrangements.css) and all styles(like border, font) are to be in  [mainsite/static/style.css](https://github.com/markroxor/Roboism/blob/master/mainsite/static/style.css)

#####What <b>not</b> to do?
* No spagetti code
* Don't complicate the code
* Don't give lot of css/javascript code inside html, use seperate css/js files. One or two line is acceptable. 


Follow the rules, bad code will be rejected, or modified and credit denied. Yes, we are evil :trollface:

####For Newbies: How to run code locally ?
* Clone your code into your PC. Let the folder name be Roboism. 
* Install python 3 in your PC. Preferably in default directory (C:/)
* delete Roboism/myvenv folder
* Open Command Prompt/Terminal and cd into the directory (Roboism). <br>
  For Window Users:-
  ```C:\Python34\python -m venv myvenv```<br>
  For Linux Users and OS X Users:-
  ```python 3 -m venv myvenv```<br>

* Then do <br>
  For Window Users:- ```myvenv\Scripts\activate```<br>
  For Linux Users and OS X Users:-
  ```source myvenv/bin/activate``` <br>
  Now, you should see a (myvenv) script before cmd commands. <br>

* Next, check updates (if any) for pip module by
  ```pip install --upgrade pip```

* After that, do
  ```pip install django```
  
* Next, do 
  ```pip install django_extensions```
  
* After that, do
  ```pip install Pillow```

* After installation is complete, do
  ```python manage.py makemigrations mainsite```
  And 
  ```python manage.py migrate mainsite```
  And
  ```python manage.py collectstatic```

* Finally, to run a virtual server, do
  ```python manage.py runserver```
  Go to any browser, type this url '127.0.0.1:8000' without quotes. If everything went as planned, you will see the site       locally. <br>
  
* For accessing/modifying users and other data, do 
  ```python manage.py createsuperuser``` and input onscreen details to create a superuser account followed by opening           '127.0.0.1:8000/admin/' in a browser window without quotes and logging in with the newly made superuser.
  
* Make any changes to the code and see the change reflected on the locally hosted site. 
