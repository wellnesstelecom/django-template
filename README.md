
Wellness telecom django template
================================

Project template for django projects based on django1.3

install
-------

Clone repository and execute:

    pip install -E myenv -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver
    firefox http://localhost:8000/test/

Support to SASS
-------

    Ruby > 1.8: sudo apt-get install ruby
    Ruby gems : sudo apt-get install rubygems
    Sass      : sudo gem install sass

    Link sass binary: sudo ln -s /var/lib/gems/1.8/bin/sass /usr/local/bin/sass
    or edit COMPRESS_PRECOMPILERS and replace sass with absolute rute

 
