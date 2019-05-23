# Otter the Job Application Tracker
Otter is a tool for job applicants to track the progress of their applications.

<a href="https://otterwerks-application-tracker.herokuapp.com">View live site!</a> 

Demo account: otterwerks/otterwerks

## Summary
I wanted to build a project that would allow me to practice my development skills and also provide value once complete. This is a tool built with Django that gives users the ability to keep track of job applications and the status of those applications. Otter will render a visual Recruitment Funnel based on the stages of each application for the user as well as a chart showing the % stages of all applications across all users. I have created a public demo account to explore the project without having to register, use the link and credentials above.

## Technical
Otter was built with the Django framework and Postgres. There are three main database models: User, Application, and Event. They are organized simply through foreign keys in that Events belong to Applications which belong to Users - where User is from the built in Django Auth. The UI was adapted from a free boostrap template I found called <a href="https://bootstrapmade.com/plato-responsive-bootstrap-website-template/">Plato</a>.

#### Django Structure
- Application Tracker (Main Project: this is the site root
  - Accounts (app): this app handles the user registration and authenitication, based off Django's Auth
  - Applications (app): most of the functionality resides here, interacting with applications is what this site is about
  - Events (app): this is where event services are located
  - Pages (app): static pages are handled here
  
#### Charting
The recruitment funnel charting is performed with PyGal. The Django view will instantiate the funnel chart and either collect data for all applications in the database or, if a user is specified, will collect data on applictions for only that user.

## Resources
- <a href="https://docs.djangoproject.com/en/2.2/intro/tutorial01/#">Writing your first Django app</a>
- <a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website">Mozilla MDN Django Tutorial: The Local Library website</a>
- <a href="https://www.udemy.com/python-django-dev-to-deployment/">Python Django Dev to Development</a>
- <a href="https://hackernoon.com/server-rendered-charts-in-django-2604f903389d">Server-rendered charts in Django</a>
