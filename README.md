# Blog app (with Django)

You can find example of running application on [pythonanywhere.com](https://aplatkouski.pythonanywhere.com/)

On that website you can find last version app from master-branch.

If you want to deploy this app on [pythonanywhere.com](https://pythonanywhere.com) use this instruction:

 1. Sign up for a PythonAnywhere account
 2. Creating a PythonAnywhere API token (see help on the website)
 3. Configuring your site on PythonAnywhere command-line
    ```bash
    # PythonAnywhere command-line
    $ pip3 install --user pythonanywhere
    $ pa_autoconfigure_django.py --python=3 https://github.com/aplatkouski/blog-app.git
    $ python manage.py createsuperuser
    ```
 4. On the future if you want to deploy new version you should use these commands:
    ```bash
    # PythonAnywhere command-line
    $ cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
    $ workon <your-pythonanywhere-domain>.pythonanywhere.com
    $ git pull
    $ ./manage.py migrate
    $ ./manage.py collectstatic
    ```
 5. Reload your application on the tab "Web" with Reload button.
