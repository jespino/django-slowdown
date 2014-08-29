Django-Slowdown
---------------

Ultra simple slowdown middleware for django (Add a time.sleep(settings.SLOWDOWN / 1000) in a middleware).

Install
=======

.. code-block::

  pip install django-slowdown

Usage
=====

Add your settings file the Slowdown middleware and the SLOWDOWN setting
variable (the default value is 1000 miliseconds).

.. code-block::

  MIDDLEWARE_CLASSES += ["slowdown.middleware.SlowDownMiddleware"]
  SLOWDOWN = 3000
