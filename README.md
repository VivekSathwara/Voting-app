# Voting-app
1)Voting App:
    
    This is a Django-based web application for creating and managing polls. Users can vote on various questions, and the results are displayed in real-time using charts.

2)Features:-

  ->Create Polls: Admin users can create new polls with multiple choices.
  ->Vote on Polls: Users can vote on any available poll.
  ->View Results: Results are displayed using dynamic charts (Matplotlib and Chart.js).
  ->User Management: Admin users can manage other users and their permissions.
  
3)Prerequisites:-

  ->Python 3.x
  ->Django 3.x or higher
  ->Matplotlib
  ->Chart.js
  ->Installation

  
4)Clone the repository:-

  bash
  Copy code
  git clone https://github.com/YourUsername/Voting-app.git
  cd Voting-app
  
5)Create and activate a virtual environment:-
  bash
  Copy code
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  
6)Install the required dependencies:-
  bash
  Copy code
  pip install -r requirements.txt
  Apply migrations:
  
  bash
  Copy code
  python manage.py migrate
  Create a superuser for accessing the admin panel:
  
  bash
  Copy code
  python manage.py createsuperuser
  Run the development server:
  
  bash
  Copy code
  python manage.py runserver
Access the application:


7)Open your browser and navigate to http://127.0.0.1:8000/ to access the app:-

  Access the admin panel at http://127.0.0.1:8000/admin/ to manage polls, questions, and users.
  Usage
  Create Polls:
  
  Log in as an admin and navigate to the admin panel.
  Create questions and corresponding choices.
  Vote on Polls:
  Users can select a poll and vote on one of the available choices.
  View Poll Results:
  
  Poll results can be viewed immediately after voting, displayed as charts using Matplotlib and Chart.js.
