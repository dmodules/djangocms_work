=====
DJANGOCMS WORK (PORTFOLIO app)
=====

DJANGO_CMS WORK is a simple DjangoCMS app to add your best works from your customers.

Quick start
-----------

1. Add "djangocms_work" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'djangocms_work',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('djangocms_work/', include('djangocms_work.urls')),

3. Run `python manage.py migrate` to create the djangocms_work models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a works (you'll need the Admin app enabled).
   
   Use templates tags to get data in your django project templates
