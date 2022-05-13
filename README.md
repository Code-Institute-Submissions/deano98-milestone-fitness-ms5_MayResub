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

# Design

### Colour Scheme 

* The sites colour scheme is blue (#0d6efd) and white throughout. Giving the site a clean and modern look.

### Typography

* The two fonts used on the website are Lato and Raleway, a pairing recommended by Google. The fonts have a clean and modern look and will complement the theme of the Gym perfectly. Sans Serif will be a substitute if the chosen fonts don't work.

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

I have opted to use manual testing for the project. Each of my user stories will be tested throughly to ensure all of the features work as intended.
All testing was done using Google chrome.

## Core Functionality:

1. As a user I can easily navigate throughout the site so that I can get to where I want quickly
  * The nav bar at the top of the page allows for quick navigation around the site.
  * As per the screenshots below, the nav bar correctly changes depending on wether the user is logged in or not.

  * [Logged in](docs/screenshots/nav-bar.png)
  * [Logged out](docs/screenshots/nav-bar-logged-out.png)

  * The bar also correctly collapses down into a burger icon on smaller screens.
  * When the burger is clicked, this opens up all of the sites links as per the screenshot below

  * [Collapsed nav bar](docs/screenshots/nav-bar-small.png)
  * [Opened nav bar](docs/screenshots/nav-bar-open.png)


2. As a user I can see the sites key information on the homepage so that I know what the site is offering immediately
  * All of the key info about the site is displayed in the first section of the homepage.
  * As per the screenshots below, the homepage is resposive to smaller screens

  * [Key info](docs/screenshots/site-info.png)
  * [Key info tablet](docs/screenshots/key-info-tablet.png)
  * [key info mobile](docs/screenshots/key-info-mobile.png)

3. As a user I can visit the site on any device so that I can visit on the go 
  * Following on from the above, each page on the site is fully responsive on all devices as per the below screenshots

  * [Homepage](docs/screenshots/homepage-responsive.png)

  * [Membership](docs/screenshots/membership-no-reg.png)

  * [Profile](docs/screenshots/profile-screen.png)
  * [Profile tablet](docs/screenshots/profile-tablet.png)
  * [Profile mobile](docs/screenshots/profile-mobile.png)

  * [Nutrition](docs/screenshots/nutrition-page.png)
  * [Nutrition tablet](docs/screenshots/nutrition-tablet.png)
  * [Nutrition mobile](docs/screenshots/profile-mobile.png)

4. As a user I can create an account so that use the sites features
  * Users are able to create an account very easily thanks to allauth.
  * I have tested the sign up process thoroughly to make sure there are no issues:

  * As per the screenshot below, the form will give a validation error if you attempt to sign up with an invalid email
  * [Invalid email](docs/screenshots/register-invalid-email.png)

  * Validation errors will also be given if you enter a duplicate username
  * The same is true if you enter a password that is too short
  * [Invalid username or password](docs/screenshots/register-invalid-username-password.png)

  * The password will also be invalid if it is too similar to the username.
  * [Invalid username or password](docs/screenshots/register-pass-too-similar.png)

  * If the above fields are entered correctly, the user is registered and ready to go.

## Subscribing

1. As a user I can easily subscribe so that I can benefit from the premium features without hassle
  * Once the user is registered, the site correctly displays the subscribe button. Otherwise the user is prompted to register:

  * [Subscribe](docs/screenshots/subscribe-button.png)
  * [Register](docs/screenshots/please-register.png)

  * Clicking on the subscribe button will take you to the confirm page, so the user can make sure they are happy before proceeding to checkout.

  * [Confirm](docs/screenshots/sub-confirm.png)

  * Once confirmed this will take you through the stripe checkout, when the user has entered their billing details they are returned to the site:

  * [Success](docs/screenshots/congrats.png)


2. As a user I can see all of the subscription features so that I can make an informed decision on wether to subscribe.
  * All of the features you get with a membership are on both the homepage and membership page:

  * [Sub details](docs/screenshots/membership-reg.png)

3. As a subscriber I can cancel my membership at any time if I change my mind
  * Members can visit the settings page on the nav bar to cancel their subscription if needed:

  * [Cancel](docs/screenshots/cancel-membership.png)

  * Once cancelled, the settings page will let the user know that their subscription will run to the end of their final billing cycle:

  * [Cancelled](docs/screenshots/membership-cancelled.png)

4. As an admin I can manually update a members subscription status in case the need arises to
  * Membership status can be amended in the admin panel:

  * [Membership Admin](docs/screenshots/membership-admin.png)


## Profile

1. As a subscriber I can view my details on the profile page
  * Once a user has subscribed, they will be asked to enter their details into the TDEE form to generate their profile
  * The form requires all fields to be valid as per the screenshots below:

  * [TDEE form validation](docs/screenshots/tdee-form-validation.png)
  * [TDEE form validation 2](docs/screenshots/tdee-validation-2.png)
  * [TDEE form validation 3](docs/screenshots/tdee-missing-field.png)

2. As a subscriber I can compare my starting weight with my current weight so that I can track my progress
  * Once the user has entered valid details into the form, they can go to the profile page
  * Clicking on the log weight button will allow users to update the current weight part of the profile
  * See screenshots below for weight log validation:

  * [Weight log validation](docs/screenshots/log-weight-validation.png)
  * [Weight log validationn 2](docs/screenshots/log-weight-validation-2.png)

  * Once a valid weight is logged, the current weight is successfully updated:

  * [Weight log](docs/screenshots/weight-log.png)

3. As a subscriber I can leave a testimonial so that share my progress with other users
  * Users can leave testimonials by clicking the write testimonial button on the profile page.
  * As per the previous forms users must submit a valid form for the testimonial to be published.
  * The testimonial then has a random chance to displayed on the homepage.

  * [Testimonial](docs/screenshots/testimonial.png)
  * [Testimonial validation](docs/screenshots/testimonial-validation.png)
  * [Testimonial homepage](docs/screenshots/testimonial-homepage.png)
  * [Testimonial random](docs/screenshots/testimonial-random.png)

4. As a subscriber I can edit or delete my testimonial so that I can change it if needed
  * Once published the user is able to edit or delete it as they see fit.

  * [Testimonial edit](docs/screenshots/testimonial-edit.png)

5. As an admin I can edit or delete testimonials so that I can change them if needed
  * Testimonials are fully editable withing the sites admin panel:

  * [Testimonial admin](docs/screenshots/testimonial-delete-admin.png)

## Nutrition and Fitness

1. As a subscriber I can get a personalised meal plan so that I can lose weight
  * Members have access to the sites meal plan from the profile page
  * As per the screenshots below, the ingredients correctly change dependant on the users caloric intake saved in the database:

  * [High carb meals](docs/screenshots/high-carb.png)
  * [Ingredients change](docs/screenshots/ingredients-change.png)

2. As a subscriber I can see a list of ingredients and instructions for each meal so that I can prepare them easily
  * Full ingredients list and instructions are present for meals as shown above.
  * Please note - as this website is for the project's purposes only, there is only 2 meals for each category.

3. As a Subscriber I can get workouts I can do at home so that I can improve my fitness
  * Subscribers get full instructions for doing their own home workouts:

  * [Workouts](docs/screenshots/workout-guide.png)

## Marketing

1. As a User I can sign up for a newsletter so that I can receive health and fitness tips
  * Newsletter functionality is provided by MailChimp, fully tested and working as shown in the screenshots below:

  * [Newsletter](docs/screenshots/high-carb.png)
  * [Newsletter clicked](docs/screenshots/newsletter-thanks.png)
  * [MailChimp](docs/screenshots/mailchimp-sub.png)


2. As a user I can visit a facebook page so that keep up to date with the site.
  * Users can visit the sites facebook page by clicking on the link at the bottom of the homepage.

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