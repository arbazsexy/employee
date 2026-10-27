import sys
def employee_details(name,employee_id,department,salary):
    return f"name:{name}\nEmployee ID: {employee_id}\nDepartment:{department}\nSalary: {salary}"

if __name__ == "__main__":
    name = sys.argu[1]
    employee_id = sys.argu[2]
    department = sys.argu[3]
    salary = sys.argu[4]

    print("\nEmployee Details")
    print("-------------------")
    print(employee_details(name,employee_id,department,salary))