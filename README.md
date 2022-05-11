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

  * As a user I wish to be able to easily navigate througout the site 
  * As a user I want to see all of the websites key information on the homepage
  * As a user I can visit the website on any kind of device with a similar experience 
  * As a user I wish to be able to easily create an account on the website

## Subscribing

  * As a user I'd like to be able easily subscribe to the website
  * As a user I want to be able to easily see all of the features that come with a subscription
  * As a user I would like to easily be able to cancel my subscription at any time.
  * As an admin I can manually update a users membership status

## Profile

  * As a subscriber I want to be able to see all of my details on a profile page.
  * As a subscriber I would like to be able to track my weight loss progress.
  * As a subscriber I'd like to be able to leavee testimonials to share my progress with others.
  * As a subscriber I need to be able to edit and delete my testimonial after it has been posted.
  * As an admin I can edit or delete testimonials.

## Nutrition and Fitness

  * As a subscriber I want to get a meal plan personalised to me
  * As a subscriber I'd like to see a list of ingredients and clear instructions on how to prepare each meal
  * As a subscriber I would like to be given workouts I can do at home

## Marketing

  * As a user I can sign up for a newsletter to receive health and fitness tips
  * As a user I would like to be able to visit a facebook page to keep up with the site.



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