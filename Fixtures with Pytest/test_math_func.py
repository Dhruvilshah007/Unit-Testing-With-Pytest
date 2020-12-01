from math_func import StudentDB
import pytest
db=None

# scope=module to call setup only once at beginning
# yield is added when we add teardown in fixture

@pytest.fixture(scope='module')
def db():
    print('--------setup method------')
    db=StudentDB()
    db.connect('data.json')
    yield db
    print('--------Teardown Module ------')
    db.close()

# python fixtures alternative of setup_module and teardown module
# called before all test are executed
# def setup_module(module):
#     print('--------setup method------')
#     global db
#     db=StudentDB()
#     db.connect('data.json')

# called after all test are executed  to free any resources or to cloes the connection with database
# def teardown_module(module):
#     print('--------Teardown Module ------')
#     db.close()


def test_scott_data(db): 
    scott_data=db.get_data('Scott')

    assert scott_data['id']==1
    assert scott_data['name']=='Scott'
    assert scott_data['result']=='pass'


def test_mark_data(db):
    mark_data=db.get_data('Mark')

    assert mark_data['id']==2
    assert mark_data['name']=='Mark'
    assert mark_data['result']=='fail'