Django-Slowdown
---------------

Ultra simple slowdown middleware for django (Add a time.sleep(settings.SLOWDOWN / 1000) in a middleware).

Install
=======

  pip install django-slowdown

Usage
=====

Add your settings file the Slowdown middleware and the SLOWDOWN setting
variable (the default value is 1000 miliseconds).

  MIDDLEWARE_CLASSES += ["taiga.middleware.SlowDownMiddleware"]
  SLOWDOWN = 3000
