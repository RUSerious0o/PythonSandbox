from pprint import pprint


def introspection_info(obj: object):
    info = {
        'Class': obj.__class__,
        'Attributes': [attr_ for attr_ in dir(obj) if not callable(getattr(obj, attr_))],
        'Public Methods': [method_ for method_ in dir(obj)
                           if callable(getattr(obj, method_))
                           and not method_.startswith('_')
                           and type(getattr(obj, method_)) != type(object)],
        'Private Methods': [method_ for method_ in dir(obj)
                            if callable(getattr(obj, method_))
                            and method_.startswith('__')
                            and type(getattr(obj, method_)) != type(object)],
        'Protected Methods': [method_ for method_ in dir(obj)
                                if callable(getattr(obj, method_))
                                and not method_.startswith('__')
                                and method_.startswith('_')
                                and type(getattr(obj, method_)) != type(object)],
        'Classes': [subclass_ for subclass_ in dir(obj)
                       if type(getattr(obj, subclass_)) == type(object)]
    }
    try:
        info['Module'] = obj.__module__
    except:
        info['Module'] = 'Module detection error'

    return info


class TestObject:
    class SubClass:
        def __init__(self):
            pass

    def __init__(self):
        self._custom_attr = -1

    def test_method(self):
        return 1

    def _protected_m(self):
        pass

    def __str__(self):
        return 'Not in the mood!'


pprint(introspection_info(TestObject()))
pprint(introspection_info(74))
