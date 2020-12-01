import math_func
import pytest
import sys
@pytest.mark.skipif(sys.version_info <(3,3),reason="do not add number add test")
# @pytest.mark.number


# def test_functionname():                      -here test is a keyword
# pytest test_math_func.py                       -normal test(Good way to do test)
# py.test                                        -another representation
# py.test -v                                    -v=verbose representation
# pytest test_math_func.py -v

# we can use =,<=,>=,is,in,not in, etc..... anything 


#  pytest test_math_func.py::test_add               -only will run  text_add test not all test


# pytest -v -k "add"                               - Its goin to run test which contains "add"  keyword

# pytest -v -k "add or string"                      - will perform all test that have add or string keyword
# pytest -v -k "add or string"                           --add and string keyword

# pytest -v -m number                                 - all test that have mark number

# pytest -v -m string                                     -    - all test that have mark string

#  pytest -v -x                                             -as soon as first test fail occurs it exits and dont go for next tests
# pytest -v -x --tb=no                                                             -will not print stack trace
# pytest -v -maxfail=2    -will exit if 2 fails are founded
#   @pytest.mark.skip(reason="do notadd number add test")        -Skip first test     
#  pytest -v -s    , pytest -v --capture=no                           -to execute all print statement
# pytest -v -q                                                                      -Quite view will not display al the details,will tell 
# 
# 
# 
# 




# @pytest.mark.number
def test_add():
    assert math_func.add(7,3)==10
    assert math_func.add(7)==9
    assert math_func.add(5)==7
    print(math_func.add(7,3),'------------------------------------')

# @pytest.mark.number
def test_product():
    assert math_func.product(5,5)==25
    assert math_func.product(5)==10
    assert math_func.product(7)==14

# @pytest.mark.string
def test_add_string():
    result=math_func.add('hello',' world')
    assert result=='hello world'
    assert type(result) is str
    assert 'hello' in result


# @pytest.mark.string 
def test_product_string():
    assert math_func.product('hello',3)=='hellohellohello'
    result=math_func.product('hello')
    assert result=='hellohello'

    assert type(result) is str
    assert 'hello' in result




    