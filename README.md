# Otter the Job Application Tracker
Otter is a tool for job applicants to track the progress of their applications.

<a href="https://otterwerks-application-tracker.herokuapp.com">View live site!</a> 

Demo account: otterwerks/otterwerks

## Summary
I wanted to build a project that would allow me to practice my development skills and also provide value once complete. This is a tool built with Django that gives users the ability to keep track of job applications and the status of those applications. I have created a public demo account to explore the project without having to register, use the link and credentials above.

## Technical
Otter was built with the Django framework and Postgres. There are three main database models: User, Application, and Event. They are organized simply through foreign keys in that Events belong to Applications which belong to Users - where User is from the built in Django Auth. The UI was adapted from a free boostrap template I found called <a href="https://bootstrapmade.com/plato-responsive-bootstrap-website-template/">Plato</a>.

#### Django Structure
- Application Tracker (Main Project: this is the site root
  - Accounts (app): this app handles the user registration and authenitication, based off Django's Auth
  - Applications (app): most of the functionality resides here, interacting with applications is what this site is about
  - Events (app): this is where event services are located
  - Pages (app): static pages are handled here

## Resources
_coming soon_
