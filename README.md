# TASKBOX

## What is Taskbox?

### Keep Your Tasks Organized and Get Things Done with Ease

Say goodbye to sticky notes and messy to-do lists. Our to-do app offers
a clean and user-friendly interface to help you stay on top of your
tasks. With our app, you can easily add, edit, and prioritize tasks, set
due dates and reminders, and track your progress. Whether you need to
manage work projects, household chores, or personal goals, our app has
got you covered. Sign up now and start achieving your goals with ease.

### Boost Your Productivity and Focus on What Matters Most

Are you tired of feeling overwhelmed by your to-do list? Our to-do app
is designed to help you stay focused and productive. With features like
task categorization, priority levels, and deadline reminders, you can
prioritize your tasks and focus on what's important. Our app also offers
a calendar view to help you plan your schedule and avoid overbooking.
Whether you're a student, a professional, or a busy parent, our app can
help you stay organized and achieve your goals. Try it now and take
control of your day.

## Features

1. User can create an account and will redirect to a private To-Do-List.
2. User can Login with E-Mail and Passwort
3. User cann create To-Do-Tasks for a specific date and time
4. User can edit tasks and rename
5. User can delete tasks

## Tech-Stack

- Html
- CSS
- Python
- Flask
- SQLite
- SQLAlchemy
- PostgreSql

## Tasks

### Part 1: HTML & CSS

- Have at least 3 HTML pages - done
- Use a variety of CSS styles and make sure the website is responsive - done

### Part 2: Backend

- Use a backend framework (Flask) - done
- Have at least 3 routes through that framework - at least one should be dynamic - done
- render content dynamically using a templating language (jinja2) - done

### Part 3: Database Setup

- Use a database and ORM - done
- Your application should have at least 2 models - done
- At least 1 page renders content from the database dynamically - done

### Part 4: CRUD & Deployment

- Users can Create, update, and delete records through forms. - done
- The application is deployed online and works - done

### Part 5: Client-Side JavaScript

- Include JavaScript on the client-side - done
- Let users do anything on the page that uses JavaScript to manipulate the DOM. - done

## How to clone this repository and install requirements

`$ mkdir Folder`
`$ cd Folder`
`$ git clone https://github.com/danieltrier/Foundations-Daniel-Trier.git`
`$ python3 -m venv venv`
`On macOS and Linux run: $source venv/bin/activate`
`On Windows run: $venv\Scripts\activate.bat`
`pip install -r requirements.txt`

## Add into the project enviroment variables in the .env file

`FLASK_DEBUG=True`
`DATABASE_URL=sqlite:///database.db`
`FLASK_APP=run.py`
`SECRET_KEY=`

## How to run it locally

`$ python run.py`

Open (http://127.0.0.1:5000/) to test locally.

## How to test the code

There are already easy to use tests implemented into project. Just use insert the command below into the terminal.

`$ pytest -v`

## Contributing and ideas

For any suggestions and ideas how to upgrade project please contact me.
