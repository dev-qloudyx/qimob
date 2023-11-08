=====
Docs
=====

Docs is a Django application designed for managing files and documents in a generic manner.

Quick start
-----------

1. Add "docs" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "docs",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("docs/", include("docs.urls")),

3. Run ``python manage.py migrate`` to create the docs models.



