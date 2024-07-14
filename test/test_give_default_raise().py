from employee import Employee
one=Employee('Li','Bai',10000)
def test_give_default_raise():
    first_name=one.first_name
    last_name=one.last_name
    yearly_salary=one.give_raise()
    assert first_name=='Li',last_name=='Bai'
    assert yearly_salary==15000