django-simpleapi: API's for everyone
====================================

.. image:: https://badge.fury.io/py/requests.png
    :target: http://badge.fury.io/py/requests

.. image:: https://pypip.in/d/requests/badge.png
        :target: https://crate.io/packages/requests/


django-simpleapi is an MIT Licensed django app, written in Python, for developers.

How many times have you wanted to create a simple JSON api in Django.
I mean simple. There are great tools out their like * and * but sometimes
you just want to send back some JSON.

This app makes it super simple to do that.

.. code-block:: python

    from simpleapi import api_handler

    @api_handler
    def get_some_yak(request):
        return {
            'yak': 'yummm'
        }

    urlpatterns = patterns(
        '',
        url(r'^get/some/yak$', get_some_yak),
    )

.. code-block:: shell

    curl http://localhost:8000/get/some/yak

    {
        "data": {
            "yak": "yummm"
        },
        "meta": {
            "code": 200
        }
    }



Features
--------

- A Simple API for Django

Installation
------------

To install Requests, simply:

.. code-block:: bash

    $ pip install django-simpleapi


Documentation
-------------

