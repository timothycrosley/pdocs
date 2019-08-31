import pdocs.doc
import pdocs.extract
import pdocs.render
import tutils


def test_html_module():
    with tutils.tdir():
        m = pdocs.extract.extract_module("./modules/one")
        assert pdocs.render.html_module(m)


def test_html_module_index():
    with tutils.tdir():
        roots = [
            pdocs.extract.extract_module("./modules/one"),
            pdocs.extract.extract_module("./modules/submods"),
        ]
        assert pdocs.render.html_index(roots)
