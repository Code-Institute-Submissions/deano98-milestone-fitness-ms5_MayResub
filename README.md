# Milestone Project 5 - Milestone Fitness Website

Milestone Fitness is a django based application to help you achieve your fitness goals. For a monthly subscription you will be given access to the tools you need to lose weight or to pack on some muscle. 

The app will take your details and calculate the amount of calories you should consume for what you want to achieve. A range of recipes will be offered which will be tailored to you and your goals, you will also be given a training routine which will go hand in hand with your nutrition plan and boost your progress!

# User Stories

* As a site user I want to be able to easily register so that I can have my own profile 
* As a site user I want to be able to easily log in or log out to access my profile
* As a site user I want to be able to easily subscribe to use all of the tools the site offers

* As a subscriber I'd like to get nutrition and exercise plans tailored to me so that I can achieve my fitness goals more efficiently 
* As a subscriber I want to be able to write a testimonial share my progress with fellow subscibers to help motivate others and myself
* As a subscriber I'd like to be able to edit / delete my testimonial if I ever need to
* As a subscriber I want to be able to track my progress from when I first joined the site

# Features

* All pages will include a navigation bar at the top, with links to register, log in, log out, the membership page, profile page and account settings.

## Homepage

* The homepage will feature a hero image at the top, followed by a quick intro to the sites features and subscriber testimonials.

## Membership

* The membership page is where you can subscribe, it will feature the monthly price and all of the features you will get as a subscriber. Once you have purchased your subscription you will be redirected back to this page to fill in a form with your details to calculate your total daily energy expediture.

## Profile

* The profile page is the hub for a subscribed member. You will be able to see your details and set your goal. All of the information about how the plan works is displayed here as well as links to your tailored meals and the option to write a testimonial.

## Settings

* This page will allow you to cancel your membership if needed.

# Technologies Used

### Integrated Development Environment

* Github

### Languages Used

* HTML
* CSS
* Python
* JavaScript

### Database

* PostreSQL

### Storage

* Cloudinary

### Frameworks

* Django
* Bootstrap
* jQuery

### Packages and other Tools

* gunicorn
* psycopg2
* django allauth
* django crispy forms

# Testing

### Code Validation

[W3C Markup Validation](https://validator.w3.org/) 

[W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

* For the Python code I used the problems tab in GitPod

### Testing User Stories

1. As a site user I want to be able to easily register so that I can have my own profile 
 * If a user isn't registered, they will be able to make an account using the Register link on the navigation bar.

2. As a site user I want to be able to easily log in or log out to access my profile
 * Users can click on the links on the nav bar to log in or out

3. As a site user I want to be able to easily subscribe to use all of the tools the site offers
 * Registered site members are able to subscribe using the membership link in the navbar

4. As a subscriber I'd like to get nutrition and exercise plans tailored to me so that I can achieve my fitness goals more efficiently 
 * subscribers are given a range of meals and workouts tailored to the details they have given during the set up process.

5. As a subscriber I want to be able to write a testimonial share my progress with fellow subscibers to help motivate others and myself
 * Subscribers are able to write a testimonial via the profile page

6. As a subscriber I'd like to be able to edit / delete my testimonial if I ever need to
 * Subscribers are able to edit and delete their testimonials

7. As a subscriber I want to be able to track my progress from when I first joined the site
 * Subscribers can update their weight whenever they want and compare it to their starting weight.

## Supported Devices

* The site has been tested on and supports the following devices:
  * Moto G4
  * Galaxy S5
  * Pixel 2
  * Pixel 2 XL
  * iPhone 5/SE
  * iPhone 6/7/8
  * iPhone 6/7/8 Plus
  * iPhone X
  * iPhone 11
  * iPad
  * iPad Pro
  * Surface Duo

## Supported Browsers

* The site has been tested on and supports the following browsers:
  * Google Chrome
  * Mozilla Firefox
  * Microsoft Edge
  * Safari

# Deployment

1. GitPod
  * Migrate changes to database.
  * Change Debug in settings.py to False

2. Heroku
  * Navigate to the apps page on Heroku
  * Click new > Create app
  * Enter a unique name for your app and choose your region
  * Click create app
  * Navigate to the Settings tab and click Reveal Config Vars
  * Add CLOUDINARY_URL and input the Cloudinary URL
  * Add DATABASE_URL and input the postgres URL
  * Add SECRET_KEY and input your secret key
  * Navigate to the Deploy tab
  * Click on Connect to GitHub in the deployment method section
  * Enter your projects repository name in the Connect to GitHub section, then click search.
  * When your repository is displayed, click connect
  * If you wish for your deployed app to be rebuilt each time you push a new change, click Enable Automatic Deploys
  * If you wish to deply manually, click Deploy Branch
  * Once your app has finished building, it is then deployed on Heroku.

# External Resources

* [w3schools](https://www.w3schools.com/) For help with code issues
* [Stack Overflow](https://stackoverflow.com/) For help with code issues
* [Youtube](https://youtube.com/) Code Tutorials
* Django 3 by Example ebook

# Credits

 * Thanks to my mentor Rohit Sharma, for the support with my project.
 * Thanks to everyone on Slack for just being a great source of help and information.