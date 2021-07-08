# heroku-django-api-template

## Local deployment:
1. Migrate with ``python3 manage.py makemigrations`` and ``python3 manage.py migrate``.
2. Create super user for admin-page access with ``python3 manage.py createsuperuser``.
3. Start development server with ``python3 manage.py runserver --settings=apiserver.local_settings``.
4. ``ExampleEntity`` has been added as an example for a fast start. Edit it to fit your needs.

## Heroku deployment with GitHub:
1. Create app in heroku dashboard (https://dashboard.heroku.com/apps).
2. In "Resources" tab of the created application find add-on "Heroku Postgres" and choose free version. Database information should be automatically added. It can be checked in "Settings" tab in section "Config vars". Click "Reveal config vars", `DATABASE_URL` should be visible there.
3. In "Deploy" tab you can choose a way of deploying your app.
   To achieve this, chose "Github" in "Deployment method" and choose repository in section "App connected to GitHub".
   You can setup automatic deployments after push to `main` branch in section "Automatic deploys" or deploy manually from Heroku interface in "Manual deploy" section.
4. Finally, to setup the database created in step 2, click on "More" button on the top right (next to the "Open app" button). 
   Select "Run console", start bash and when connected to the console type:
   ``python3 manage.py makemigrations`` and then ``python3 manage.py migrate``. 
   You can also create superuser for your django-admin website by typing ``python3 manage.py createsuperuser``.