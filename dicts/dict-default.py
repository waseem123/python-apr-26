employee = {
            
        }
print(employee)
employee.setdefault('empId',0)
employee.setdefault('empName','NA')
employee.setdefault('empSalary',0)
employee.setdefault('empDesignation','NA')
employee.setdefault('empExperience',0)
print(f'Experience- {employee['empExperience']} YEARS')
print(employee)