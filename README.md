# Store Server

The project for study Django.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [BOOTSTRAP](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [PostgreSQL](https://www.postgresql.org/)
- [Stripe](https://docs.stripe.com/)
  

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py runserver 
   ```
   
