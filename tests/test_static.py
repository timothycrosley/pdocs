import pathlib

import pytest

import pdocs.extract
import pdocs.static
import tutils


@pytest.mark.parametrize(
    "modspec,ident,path",
    [
        ("./modules/one", "one", "one.html"),
        ("./modules/dirmod", "dirmod", "dirmod.html"),
        ("./modules/submods", "submods", "submods/index.html"),
        ("./modules/submods", "submods.two", "submods/two.html"),
        ("./modules/submods", "submods.three", "submods/three.html"),
        ("./modules/index", "index", "index/index.html"),
        ("./modules/index", "index.index", "index/index.m.html"),
    ],
)
def test_module_path(modspec, ident, path):
    with tutils.tdir():
        root = pdocs.extract.extract_module(modspec)
        submod = root.find_ident(ident)

        mp = pdocs.static.module_to_path(submod)
        assert mp == pathlib.Path(path)

        retmod = pdocs.static.path_to_module([root], mp)
        assert retmod.name == submod.name

        retmod = pdocs.static.path_to_module([root], mp.with_suffix(""))
        assert retmod.name == submod.name


def test_path_to_module():
    with tutils.tdir():
        root = pdocs.extract.extract_module("./modules/submods")
        with pytest.raises(pdocs.static.StaticError):
            pdocs.static.path_to_module([root], pathlib.Path("nonexistent"))


def test_static(tmpdir):
    dst = pathlib.Path(str(tmpdir))
    with tutils.tdir():
        one = pdocs.extract.extract_module("./modules/one")
        two = pdocs.extract.extract_module("./modules/submods")
        assert not pdocs.static.would_overwrite(dst, [one])
        assert not pdocs.static.would_overwrite(dst, [one, two])
        pdocs.static.html_out(dst, [one])
        assert pdocs.static.would_overwrite(dst, [one])
        assert pdocs.static.would_overwrite(dst, [one, two])
        pdocs.static.html_out(dst, [one, two])
        assert pdocs.static.would_overwrite(dst, [one])
        assert pdocs.static.would_overwrite(dst, [one, two])
