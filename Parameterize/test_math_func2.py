import math_func2
import pytest



#                                       -same function test with different types value
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


@pytest.mark.parametrize('num1,num2,result',
                                [
                                    (7,3,10),
                                    ('hello ','world','hello world'),
                                    (10.5,25.5,36)
                                ])
def test_add(num1,num2,result):
    assert math_func2.add(num1,num2)==result
