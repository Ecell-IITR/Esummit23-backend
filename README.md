
# E-summit Backend

### Description
The E-Summit Event Management System is a Django-based project designed to streamline and enhance the management of an E-Summit event, which is a flagship entrepreneurial event organized by educational institutions or organizations. This project provides a comprehensive platform for planning, organizing, and conducting an E-Summit, enabling participants, speakers, and organizers to collaborate effectively.

### Key Features:

Event Registration: The system allows participants to register for the E-Summit event through a user-friendly registration form. Participants can provide their personal details, select the sessions they wish to attend, and make payments securely.

Speaker Management: Organizers can manage the profiles of speakers and panelists participating in the E-Summit. They can add speaker details, assign them to specific sessions or workshops, and provide information about their expertise and accomplishments.

Schedule and Agenda: The project provides a centralized platform for creating and managing the event's schedule and agenda. Organizers can define session timings, allocate rooms or virtual links, and update the agenda in real-time. Participants can view the agenda, select sessions of interest, and receive notifications or reminders.

Workshop and Session Management: The system enables organizers to create and manage workshops and sessions conducted during the E-Summit. They can specify the topic, duration, location. Participants can view available sessions, register, and receive confirmations.

Networking and Collaboration: The platform offers features to facilitate networking and collaboration among participants, speakers, and organizers. Participants can create profiles, and communicate info to the particepents.

Sponsorship Management: The project includes features for managing event sponsorships. Organizers can display sponsor logos and information on the event website.

Feedback and Surveys: Participants can provide feedback and ratings for sessions, workshops, and overall event experience. Organizers can collect valuable insights and suggestions through surveys, enabling them to improve future E-Summit events.

Analytics and Reporting: The system offers reporting and analytics capabilities to organizers. They can generate reports on registration statistics, session attendance, participant demographics, and other relevant metrics. These insights can assist in evaluating the success of the event and making data-driven decisions for future iterations.

The E-Summit Event Management System built with Django provides a comprehensive and efficient platform for organizing and managing E-Summit events. Its user-friendly interface, collaborative features, and robust functionality make it an indispensable tool for event organizers, participants, and speakers, ensuring a successful and engaging entrepreneurial event.


## Installation

Install and run Backend with python 3.8

```bash
  pip install -r requirements.txt
```
Start Redis Server
```bash
  redis-server start
```
Migrate SQL Databse
```bash
  python manage.py runserver
```
Create Superuser
```bash
  python manage.py createsuperuser
```
Start Server
```bash
  python manage.py runserver
```
Start Celery Server
```bash
  celery -A esummit worker -l info -P gevent
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file


`SECRET_KEY`

`SECRET_KEY_2`

`RAZORPAY_KEY_ID`

`RAZORPAY_SECRET_KEY`


## Authors

- [@I-shika](https://www.github.com/I-shika)
- [@Novice-expert](https://www.github.com/Novice-expert)
- [@vinayIITian](https://www.github.com/vinayIITian)
- [@pranav-iitr](https://www.github.com/pranav-iitr)


## Tech Stack

**Server:** Django, Python, DRF

**Frontend:** DTL, CSS, JS

**Message Brocker:** Redis,Redis-queue

**DataBase:** MySql ,Redis-DB

**Asycrounus Programming:** Celery
