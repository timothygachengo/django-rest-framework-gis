Changelog
=========

Version 0.9 [unreleased]
------------------------

- `#55 <https://github.com/djangonauts/django-rest-framework-gis/pull/55>`_: Fixed exception in ``DistanceToPointFilter`` in case of invalid point
- `#58 <https://github.com/djangonauts/django-rest-framework-gis/pull/58>`_: Fixed handling of ``None`` values in ``GeoFeatureModelSerializer`` to avoid problems with ``FileField`` and ``ImageField``
- `#57 <https://github.com/djangonauts/django-rest-framework-gis/pull/57>`_: Added support for GeoJSON Bounding Boxes in ``GeoFeatureModelSerializer``

Version 0.8.2 [2015-04-29]
--------------------------

- `#53 <https://github.com/djangonauts/django-rest-framework-gis/pull/53>`_: Added support for PATCH requests in ``GeoFeatureModelSerializer``

Version 0.8.1 [2015-03-25]
--------------------------

- Added compatibility with django-rest-framework 3.1.x
- Added compatibility with django 1.8 (RC1)

Version 0.8 [2015-03-03]
------------------------

- Added compatibility with django-rest-framework 3.x

Version 0.7 [2014-10-03]
------------------------

- upgraded development status classifer to Beta
- avoid empty string in textarea widget if value is None
- allow field definition in GeoFeatureModelSerializer to be list

Version 0.6 [2014-09-24]
------------------------

- Added compatibility to django-rest-framework 2.4.3

Version 0.5 [2014-09-07]
------------------------

- added TMSTileFilter
- added DistanceToPointFilter
- renamed InBBOXFilter to InBBoxFilter
- added compatibility with DRF 2.4.0

Version 0.4 [2014-08-25]
------------------------

- python3 compatibility
- improved DRF browsable API HTML widget (textarea instead of text input)

Version 0.3 [2014-07-07]
------------------------

- added compatibility with DRF 2.3.14

Version 0.2 [2014-03-18]
------------------------

- geofilter support
- README in restructured text for pypi
- updated python package info

Version 0.1 [2013-12-30]
------------------------

- first release