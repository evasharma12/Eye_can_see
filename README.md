# Eye Can See

A web application built on the first theme of Microsoft Engage 2022, i.e. Face Recognition.


![Image](https://res.cloudinary.com/dtqeozivt/image/upload/v1653460727/Screenshot_from_2022-05-24_14-30-17_hsugls.png)


## Description
It is a face detection application which is used to strengthen security systems at entrances.
Whenever someone knocks at your door, this application will recognize if the person is known to you. 

## [Video Demo](https://drive.google.com/file/d/15eKbkzAKjnTQ4lCSArzMdtIg8ZH6ScFE/view?usp=sharing)

### Technologies Used
-   Open CV - for detecting faces
-   Face recognition - for recognizing faces from the database
-   Django - Framework
-   SQL - database for storing the names and images of people
-   Python - programming language
-   HTML, CSS - frontend

## Installation and Setup

#### Requirements
You should have the following things installed in your device:

 - pip
 - python3

 #### Setup

 - Clone project

     git clone https://github.com/evasharma12/Eye_can_see.git

 - Go to the project directory
 

    cd Eye_can_see/

 - Install dependencies

    pip install -r requirements.txt


 - Start server
 python3 manage.py runserver

![https://res.cloudinary.com/dtqeozivt/image/upload/v1653460906/Screenshot_from_2022-05-25_12-11-34_odejiq.png](https://res.cloudinary.com/dtqeozivt/image/upload/v1653460906/Screenshot_from_2022-05-25_12-11-34_odejiq.png)

## How to get Started
For a video tutorial, refer to this link.

In the Home page:

Enter your name as the user and submit.

Second Page:

#### Adding a person to database

 - Enter your name as user
 - Enter the person's name or relation
 - Choose a photo of the person from your device
 - Click Submit
 
 ![https://res.cloudinary.com/dtqeozivt/image/upload/v1653484440/Screenshot_from_2022-05-25_18-38-11_sq2ynu.png](https://res.cloudinary.com/dtqeozivt/image/upload/v1653484440/Screenshot_from_2022-05-25_18-38-11_sq2ynu.png)

You will be rediected to the home page after the person has been added.

#### Recognizing a Person

 - Click on 'Recognize' on the navbar
 *(Make sure your camera is not being used by any other application)*
 - Press Q after 3-5 seconds after the web camera opens
![https://res.cloudinary.com/dtqeozivt/image/upload/v1653484439/Screenshot_from_2022-05-25_18-38-26_ttlxyl.png](https://res.cloudinary.com/dtqeozivt/image/upload/v1653484439/Screenshot_from_2022-05-25_18-38-26_ttlxyl.png)
 
 The person will be recognized by his name or unkonwn. The voice API will speak aloud the name of the person and it will also be displayed on the screen.

 
![https://res.cloudinary.com/dtqeozivt/image/upload/v1653460741/Screenshot_from_2022-05-24_14-30-58_nnvshv.png](https://res.cloudinary.com/dtqeozivt/image/upload/v1653460741/Screenshot_from_2022-05-24_14-30-58_nnvshv.png)
