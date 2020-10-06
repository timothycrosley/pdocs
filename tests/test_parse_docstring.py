from pdocs import doc
from tests import tutils
import pdocs


def simple_function(arg1, arg2=1):
    """
    Just a simple function.

    Args:
      arg1 (str): first argument
      arg2 (int): second argument

    Returns:
      List[str]: first argument repeated second argument types.
    """
    return [arg1] * arg2


def test_parse_docstring():
    fun_doc = doc.Function("simple_function", __name__, simple_function)
    assert fun_doc.parsed_docstring is not None
    parsed = fun_doc.parsed_docstring
    assert len(parsed.params) == 2
    first_param, second_param = parsed.params
    assert first_param.arg_name == "arg1"
    assert first_param.type_name == "str"
    assert first_param.description == "first argument"
    assert first_param.is_optional == False
    assert second_param.arg_name == "arg2"
    assert second_param.type_name == "int"
    assert second_param.description == "second argument"
    # assert second_param.is_optional == True
    # assert second_param.default == 1


def token_to_alias(raw_text, vocab):
    """
    Replaces known tokens with their "tag" form.
    
    i.e. the alias' in some known vocabulary list.

    Parameters
    ----------
    raw_text: pd.Series
        contains text with known jargon, slang, etc
    vocab: pd.DataFrame
        contains alias' keyed on known slang, jargon, etc.

    Returns
    -------
    pd.Series
        new text, with all slang/jargon replaced with unified representations
    """
    pass


def test_numpydocs():
    fun_doc = doc.Function("token_to_alias", __name__, token_to_alias)
    assert fun_doc.parsed_docstring is not None
    parsed = fun_doc.parsed_docstring
    assert parsed.short_description == 'Replaces known tokens with their "tag" form.'
    assert len(parsed.params) == 2
    assert len(parsed.raises) == 0
    first_param, second_param = parsed.params
    assert first_param.arg_name == "raw_text"
    assert first_param.type_name == "pd.Series"
    assert first_param.description == "contains text with known jargon, slang, etc"
    assert first_param.is_optional == False
    assert second_param.arg_name == "vocab"
    assert second_param.type_name == "pd.DataFrame"
    assert second_param.description == "contains alias' keyed on known slang, jargon, etc."
    assert second_param.is_optional == False
    returns = parsed.returns
    assert returns.description == "new text, with all slang/jargon replaced with unified representations"
    assert returns.return_name is None
    assert returns.type_name == "pd.Series"
    assert not returns.is_generator


def test_parse_numpy_example():
    with tutils.tdir():
        m = pdocs.extract.extract_module(f"./docstring_parser/example_numpy.py")
    
    assert m.parsed_docstring
    pd = m.parsed_docstring
    assert pd.short_description == "Module level docstring."
    assert not pd.long_description

    assert "add" in m.doc
    add_pd = m.doc["add"].parsed_docstring
    assert add_pd.short_description == "Return $x + y$."
    assert len(add_pd.params) == 2
    x, y = add_pd.params
    assert x.description == "The first parameter."
    assert y.description == "The second parameter. Default={default}."
    assert add_pd.returns.type_name == "int"
    assert add_pd.returns.description == """Added value.

!!! note
    The return type must be duplicated in the docstring to comply with the NumPy
    docstring style."""

    assert "gen" in m.doc
    gen_pd = m.doc["gen"].parsed_docstring
    assert gen_pd.short_description == "Yield a numbered string."
    n, = gen_pd.params
    assert n.description == "The length of iteration."
    assert n.type_name == "int"
    assert n.arg_name == "n"
    assert gen_pd.returns.type_name == "str"
    assert gen_pd.returns.is_generator
    assert gen_pd.returns.description == "A numbered string."

    assert "ExampleClass" in m.doc
    ex_class = m.doc["ExampleClass"]
    ec_pd = ex_class.parsed_docstring
    assert ec_pd.short_description == "A normal class."
    x, y = ec_pd.params
    assert x.description == "The first parameter."
    assert y.description == "The second parameter."
    assert len(ec_pd.raises) == 1
    raises = ec_pd.raises[0]
    assert raises.type_name == "ValueError"
    assert raises.description == "If the length of `x` is equal to 0."
    msg_pd = ex_class.doc["message"].parsed_docstring
    assert msg_pd.short_description == "Return a message list."
    n = msg_pd.params[0]
    assert n.arg_name == "n"
    assert n.description == "Repetition."
    assert "readonly_property" in ex_class.doc_init
    ro_prop_pd = ex_class.doc_init["readonly_property"].parsed_docstring
    assert ro_prop_pd.short_description == "str: Read-only property documentation."
    assert "readwrite_property" in ex_class.doc_init
    rw_prop_pd = ex_class.doc_init["readwrite_property"].parsed_docstring
    assert rw_prop_pd.short_description == "Read-write property documentation."


def test_parse_google_example():
    with tutils.tdir():
        m = pdocs.extract.extract_module(f"./docstring_parser/example_google.py")
    
    assert m.parsed_docstring
    pd = m.parsed_docstring
    assert pd.short_description == "Module level docstring."
    assert not pd.long_description

    assert "add" in m.doc
    add_pd = m.doc["add"].parsed_docstring
    assert add_pd.short_description == "Return $x + y$."
    assert len(add_pd.params) == 2
    x, y = add_pd.params
    assert x.description == "The first parameter."
    assert y.description == "The second parameter. Default={default}."
    assert add_pd.returns.type_name == "int"
    assert add_pd.returns.description == "Added value."

    assert "gen" in m.doc
    gen_pd = m.doc["gen"].parsed_docstring
    assert gen_pd.short_description == "Yield a numbered string."
    n, = gen_pd.params
    assert n.description == "The length of iteration."
    assert n.type_name == "int"
    assert n.arg_name == "n"
    assert gen_pd.returns.type_name == "str"
    assert gen_pd.returns.is_generator
    assert gen_pd.returns.description == "A numbered string."

    assert "ExampleClass" in m.doc
    ex_class = m.doc["ExampleClass"]
    ec_pd = ex_class.parsed_docstring
    assert ec_pd.short_description == "A normal class."
    x, y = ec_pd.params
    assert x.description == "The first parameter."
    assert y.description == "The second parameter."
    assert len(ec_pd.raises) == 1
    raises = ec_pd.raises[0]
    assert raises.type_name == "ValueError"
    assert raises.description == "If the length of `x` is equal to 0."
    msg_pd = ex_class.doc["message"].parsed_docstring
    assert msg_pd.short_description == "Return a message list."
    n = msg_pd.params[0]
    assert n.arg_name == "n"
    assert n.description == "Repetition."
    assert "readonly_property" in ex_class.doc_init
    ro_prop_pd = ex_class.doc_init["readonly_property"].parsed_docstring
    assert ro_prop_pd.short_description == "str: Read-only property documentation."
    assert "readwrite_property" in ex_class.doc_init
    rw_prop_pd = ex_class.doc_init["readwrite_property"].parsed_docstring
    assert rw_prop_pd.short_description == "Read-write property documentation."
