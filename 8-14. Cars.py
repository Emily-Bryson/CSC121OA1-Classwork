def make_car(manufaturer, model, **car_info):
    """Build a dictionary containing everything we know about a car"""
    car_info['manufacturer']= manufaturer
    car_info['model']= model
    return car_info
car= make_car('ford', 'mach 1 mustang', color='dark purple', heatedseats=True)

print(car) 
