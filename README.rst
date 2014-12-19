django-simpleapi: API's for everyone
====================================

.. image:: https://api.travis-ci.org/voidfiles/django-simpleapi.svg
    :target: https://travis-ci.org/voidfiles/django-simpleapi

.. image:: https://badge.fury.io/py/django-simpleapi.png
    :target: http://badge.fury.io/py/django-simpleapi

.. image:: https://pypip.in/d/django-simpleapi/badge.png
        :target: https://crate.io/packages/django-simpleapi/


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
- Easy execption handling, creation
- Easy addition to meta

Installation
------------

To install Requests, simply:

.. code-block:: bash

    $ pip install django-simpleapi


Documentation
-------------

This easyiest way to get started is to use the `api_handler` decorator.

.. code-block:: python

    from simpleapi import api_handler

    @api_handler
    def get_some_yak(request):
        return {
            'yak': 'yummm'
        }

Any view function that returns a dict object will work with this interface.

Next, often in APIs you need to fail for some reason. Validation, missing params, you name it. There is an easy way to make that happen `SimpleHttpException`

.. code-block:: python

    from simpleapi import api_handler, SimpleHttpException

    @api_handler
    def get_some_yak(request):
        required_param = request.GET.get('required_param')

        if required_param is None:
            raise SimpleHttpException("Missing required_param", 'missing-required-param', 400)

        return {
            'yak': 'yummm'
        }


Now when you request this view and forget to pass required_param you would see something like this.


.. code-block:: shell

    curl http://localhost:8000/get/some/yak

    {
        "meta": {
            "code": 400,
            "error_message": "Missing required_param",
            "error_slug": "missing-required-param"
        }
    }

Not only will the HTTP Status code be in the meta response, it will also be the HTTP Code sent back. Error slug is helpfull in resolving exceptions progrmattically. It's mucher easier then relying on string grepping to figure out what went wrong.

Finally, you might want to add you own information to the meta part of the envelope. This would helpfull for passing information like pagination information.

.. code-block:: python

    from simpleapi import api_handler

    @api_handler
    def get_some_yak(request):
        request.META['_simple_api_meta']['yak_count'] = 1

        return {
            'yak': 'yummm'
        }

The response would now look something like this.

.. code-block:: shell

    curl http://localhost:8000/get/some/yak

    {
        "data": {
            "yak": "yummm"
        },
        "meta": {
            "code": 200,
            "yak_counter": 1
        }
    }

