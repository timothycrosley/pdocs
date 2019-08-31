import pdocs.doc
import pdocs.extract
import tutils


def test_simple():
    with tutils.tdir():
        m = pdocs.extract.extract_module("./modules/one.py")
        assert m


class Dummy:
    def method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass


class DummyChild(Dummy):
    def class_method(self):
        pass


def test_is_static():
    assert pdocs.doc._is_method(Dummy, "method")
    assert not pdocs.doc._is_method(Dummy, "class_method")
    assert not pdocs.doc._is_method(Dummy, "static_method")

    assert pdocs.doc._is_method(DummyChild, "method")
    assert pdocs.doc._is_method(DummyChild, "class_method")
    assert not pdocs.doc._is_method(Dummy, "static_method")
