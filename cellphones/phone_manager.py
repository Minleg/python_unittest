# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        # TODO raise exception if two employees with same ID are added
        if employee in self.employees: # if employee already in the employee list
            raise PhoneError # raises an Exception
        else:
            self.employees.append(employee)


    def add_phone(self, phone):
        # TODO raise exception if two phones with same ID are added
        if phone in self.phones:
            raise PhoneError
        else:
            self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list
        # TODO if phone is already assigned to an employee, do not change list, raise exception
        # TODO if employee already has a phone, do not change list, and raise exception
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.
        for phone in self.phones:
            employee_with_phone = [] # list to store id of all employees with phone
            if phone.employee_id != None:
                employee_with_phone.append(phone.employee_id)
            if phone.id == phone_id: # if phone with phone_id is found in the phone list
                employee_id_assigned_to_phone = phone.employee_id # gets the employee id assigned to the phone id
                if employee.id == employee_id_assigned_to_phone: # if employee id and employee id assigned to phone number is same
                    return
                elif employee.id in employee_with_phone: # if employee has been assigned another phone
                    raise PhoneError
                elif employee_id_assigned_to_phone != None: # if phone is assigned to other employee
                    raise PhoneError
                else:
                    phone.assign(employee.id)
                    return
                
            


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        # TODO should return None if the employee does not have a phone
        # TODO the method should raise an exception if the employee does not exist

        for phone in self.phones:
            employee_with_phone = [] # list to store id of all employees with phone
            if phone.employee_id != None:
                employee_with_phone.append(phone.employee_id)
            if employee.id not in employee_with_phone: # if employee doesn't have phone assigned
                return None
            if employee not in self.employees: # if employee not in employee list
                raise PhoneError
            if phone.employee_id == employee.id:
                return phone

        return None


class PhoneError(Exception):
    pass
