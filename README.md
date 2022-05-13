# Milestone Project 5 - Milestone Fitness Website

Milestone Fitness is a django based application to help you achieve your fitness goals. For a monthly subscription you will be given access to the tools you need to lose weight or to pack on some muscle. 

The app will take your details and calculate the amount of calories you should consume for what you want to achieve. A range of recipes will be offered which will be tailored to you and your goals, you will also be given a training routine which will go hand in hand with your nutrition plan and boost your progress!

# UX

## Strategy

Target audience:

  * 18 - 55 year olds
  * People who want to lose weight
  * People who want to improve their fitness

What do users want from the site:

  * Easy to use website which is easy to navigate
  * Ability to subscribe to reap the benefits of the website
  * Account functionality to track progress of weight loss
  * Simple meal plans
  * Workouts that can be done at home

The website will offer all of these features once subscribed, the subscription process will be quick and painless.

I will assume that the site will be visited by people on mobile, tablets and laptops. The website will have to be responsive 
to allow for a pleasant user experience on all devices.

# User Stories

## Core Functionality:

  * As a user I can easily navigate throughout the site so that I can get to where I want quickly
  * As a user I can see the sites key information on the homepage so that I know what the site is offering immediately
  * As a user I can visit the site on any device so that I can visit on the go 
  * As a user I can create an account so that use the sites features

## Subscribing

  * As a user I can easily subscribe so that I can benefit from the premium features without hassle
  * As a user I can see all of the subscription so that make an informed decision on wether to subscribe
  * As a subscriber I can cancel my membership at any time if I change my mind
  * As an admin I can manually update a members subscription status in case the need arises to

## Profile

  * As a subscriber I can view my details on the profile page
  * As a subscriber I can compare my starting weight with my current weight so that I can track my progress
  * As a subscriber I can leave a testimonial so that share my progress with other users
  * As a subscriber I can edit or delete my testimonial so that I can change it if needed
  * As an admin I can edit or delete testimonials so that I can change them if needed

## Nutrition and Fitness

  * As a subscriber I can get a personalised meal plan so that I can lose weight
  * As a subscriber I can see a list of ingredients and instructions for each meal so that I can prepare them easily
  * As a Subscriber I can get workouts I can do at home so that I can improve my fitness

## Marketing

  * As a User I can sign up for a newsletter so that I can receive health and fitness tips
  * As a user I can visit a facebook page so that keep up to date with the site

# Features

* All pages will include a navigation bar at the top, with links to register, log in, log out, the membership page, profile page and account settings.
* Depending on if the user is subscribed / registered or not, they will see different links in the nav bar.
* On smaller screens, the nav bar links will collapse down into a burger icon, clicking on this will open up a menu of the links above.
* Clicking on these links will direct the user to the appropriate page on the site

## Homepage

* The homepage will feature a responsive hero image, this will zoom out more as the resolution gets smaller.
* The next section of the homepage lists the sites features that are included with the subscription.
* The above features are listed across the screen on large screens, this collapses down to 1 column on smaller screens
* The following section shows 3 randomly selected testimonials from the database, the same responsive styling as above is applied.

## Registration

* The registration for the site is handled by allauth to allow for a quick and painless registration process.

## Membership

* The membership page is where you can subscribe, it will feature the monthly price and all of the features you will get as a subscriber. Once you have purchased your subscription you will be redirected back to this page to fill in a form with your details to calculate your total daily energy expediture.
* Unregistered users will be prompted to register before they are able to subscribe. In this situation the subscribe button will be replaced 
with a link to register
* The subscribe button will direct to a confirmation page, allowing the user to confirm the details of the subscription before proceeding.
* The confirmation page will show confirmation of the price, features and a reminder that members are able to cancel at any time, a subscribe button will
proceed to the checkout.
* The checkout is handled by Stripe.
* Once the checkout is complete the user will be directed to one of the screens below.
* If the subscription was successful, the user will be redirected to a simple success screen with a link to return to the membership page
* If the subscription was unsuccessful, the user will be redirected to a simple error screen with a link to return to the membership page
* Once subscribed, the membership page will feature a form which the user must fill in.
* The form requires data such as height and weight, this will calculate the caloric intake for that user so that the meal plans can be created.
* Once the form has been filled in with valid data, the user can click calculate to log their data. They will then be redirected to the Profile page.

## Profile

* The profile page is the hub for subscribed members.
* The top of the page features all of the data logged using the form on the previous screen.
* The above section also includes the "Current Weight", this defaults as the weight entered in the form previously, but can be updated by the user
to track the progress of their weight loss.
* Also at the top of this page are a set of radio buttons which set the users goal.
* The user can select either Weight Loss, Maintenance or Weight Gain. This will update the users target calories in the database and update their meal
plan accordingly.
* The remainder of this page contains all of the information about the workouts and nutrition plan.
* The nutrition section contains 2 links, one for the low carb meals and one for high carb meals.
* The progression section contains links to both the testimonial page and the weight log page.
* The testimonial page contains a simple form for writing a review of the site, once published this could feature on the homepage.
* Users are able to edit or delete published testimonials.
* The weight log page contains a simple form to log your current weight, this will update the current weight part at the top of the page.
Users are recommended to do this once per week.

## Nutrition

* The nutrition page contains all of the ingredients and instructions needed to prepare the meals included with the site.
* Depending on the users target calories in the database, the amount of ingredients will change so that they take in the perfect amount of calories for their goals.
* The page will either show low carb or high carb meals, depending on which link the user clicked on.

## Settings

* This page will allow you to cancel your membership if needed.
* If the membership has been cancelled, the page will display a notice that their membership has been cancelled and will run to the end of their billing cycle.

# Future Features

  * A feature currently out of scope that I'd like to add is a shop for merchandise and nutritional supplements.

# Colour Scheme 

  * The sites colour scheme is blue (#0d6efd) and white throughout. Giving the site a clean and modern look.

# Wireframes

### Homepage

* [Desktop](docs/wireframes/homepage.png) 
* [Tablet](docs/wireframes/homepage-tablet.png)
* [Mobile](docs/wireframes/homepage-mobile.png)

### Subscription

* [Desktop](docs/wireframes/subscription.png) 
* [Tablet](docs/wireframes/subscription-tablet.png)
* [Mobile](docs/wireframes/subscription-mobile.png)

### Profile

* [Desktop](docs/wireframes/profile.png) 
* [Tablet](docs/wireframes/profile-tablet.png)
* [Mobile](docs/wireframes/profile-mobile.png)

### Nutrition

* [Desktop](docs/wireframes/nutrition.png) 
* [Tablet](docs/wireframes/nutrition-tablet.png)
* [Mobile](docs/wireframes/nutrition-mobile.png)

# Entity Relationship Diagram

* [ERD](docs/ERD/erd.png)

# Marketing

### Facebook

* The site has a facebook page to help drive engagement from their huge userbase and attempt to increase traffic to the site.
* The page will keep followers updated with the site and offer health and fitness tips.

* [Facebook](docs/screenshots/fb-screenshot.png)
* [Facebook2](docs/screenshots/fb-screenshot-2.png)

### Newsletter

* Site users will also be able to sign up to a newsletter which will provide site news, health tips and potentially discount offers
if the shop is set up.
* The newsletter is created using mailchimp.

### Search Engine Optimization

The topics I started were as follows:

* Fitness
* Nutrition
* Lose Weight
* Exercise

I built upon these with the following:

#### Fitness

* I want to improve my fitness
* How can I improve my fitness
* Health and Fitness

#### Nutrition

* Nutrition plan
* Meal plan
* Personalised nutrtition plan
* Personalised meal plan for weight loss
* Clean eating

#### Lose Weight

* I want to lose weight
* I want to lose fat
* How can I lose weight
* Weight loss plan

#### Exercise

* Training
* Exercise plan
* Workout plan for beginners
* High intensity interval training
* Exercise for weight loss

After doing some research and testing all of these keywords using Googles search engine, I refined the list above into the keywords below.

The list below was formed by checking the "Related search" and "People also ask" sections of the google search. The refined list will now 
hopefully contain keywords which have a high search volume, yet unique enough to boost the sites SEO.

* Health and Fitness
* How to improve fitness fast
* How to keep fit at home
* Best way to improve fitness
* Lose weight fast
* Personalised weight loss plan for my body
* Meal plan generator based on macros
* Exercise for weight loss at home
* No equipment workout plan

I noticed there was a big demand for home workouts, "fast" results and no equipment workouts. Since the pandemic working out at home 
has become a lot more popular. As the workouts on my site can all be done without equipment and at home, I've updated the info on the 
site to focus more on this, utilising semantics such as headers and strong tags.

* [SEO](docs/screenshots/sde-homepage.png)

# Technologies Used

### Integrated Development Environment

* Github
  * Used to host my codes repository

* Git
  * Used to manage and store revisions of the project

* Gitpod
  * The development environment

### Languages Used

* HTML
  * The front end coding language used 
* CSS
  * Another front end coding language, handling the presentation of the site
* Python
  * The core back end coding language used
* JavaScript
  * Secondary back end language used for things like the checkout

### Database

* PostreSQL
  * Used to store the relational databases utilised by the site
* SQLite
  * Used to run the sites databases locally

### Storage

* Cloudinary

### Frameworks & Libraries

* Django
  * The core framework used to create the site and each of it's apps
* Bootstrap
  * Used to help with the styling of the site and to make it responsive on all devices
* jQuery
  * Used on the profile page to allow the radio button to update the database.

### Packages and other tools

* gunicorn
  * Used to run the python application instance
* psycopg2
  * PostgreSQL database adapter
* django allauth
  * Package to handle all of the registration and authentication for the site
* django crispy forms
  * Used to add bootstrap styling to django forms

# Testing

## Core Functionality:

  * As a user I can easily navigate throughout the site so that I can get to where I want quickly
  * As a user I can see the sites key information on the homepage so that I know what the site is offering immediately
  * As a user I can visit the site on any device so that I can visit on the go 
  * As a user I can create an account so that use the sites features

## Subscribing

  * As a user I can easily subscribe so that I can benefit from the premium features without hassle
  * As a user I can see all of the subscription so that make an informed decision on wether to subscribe
  * As a subscriber I can cancel my membership at any time if I change my mind
  * As an admin I can manually update a members subscription status in case the need arises to

## Profile

  * As a subscriber I can view my details on the profile page
  * As a subscriber I can compare my starting weight with my current weight so that I can track my progress
  * As a subscriber I can leave a testimonial so that share my progress with other users
  * As a subscriber I can edit or delete my testimonial so that I can change it if needed
  * As an admin I can edit or delete testimonials so that I can change them if needed

## Nutrition and Fitness

  * As a subscriber I can get a personalised meal plan so that I can lose weight
  * As a subscriber I can see a list of ingredients and instructions for each meal so that I can prepare them easily
  * As a Subscriber I can get workouts I can do at home so that I can improve my fitness

## Marketing

  * As a User I can sign up for a newsletter so that I can receive health and fitness tips
  * As a user I can visit a facebook page so that keep up to date with the site

### Code Validation

[W3C Markup Validation](https://validator.w3.org/)

* For the html code I pasted in the urls for the pages that didn't require authorisation.
* For pages that did require authorisation, I copied the code from google dev tools to paste directly into the validator.

[W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

* For the css code, I pasted the base.css file directly into the validator

[PEP8 Validation](http://pep8online.com/)

* For the Python code I used both Pep8 above, as well as the flake8 validator in the gitpod terminal.
* Pep8 had no errors
* Flake8 returned some negligible pylint errors

[Beautify Tools](https://beautifytools.com/javascript-validator.php)

* For the small amount of JS I validated with Beautify
* The code returned 3 defined errors as they were defined in the view.


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