def main():
    # Get the num of emps for create
    num_emps = int(input('How many employee records ' + \
                        'do you want to create? : '))
    # Open files for writing 
    emp_files = open('employees.txt', 'w')

    # Get each employee's data and write it to the file.
    for count in range(1, num_emps + 1):
        print('Enter data for employee # ', count, sep='')
        name = input('Name : ')
        id_num = input('ID number : ')
        dept = input('Department : ')

        # Write the data as a record 
        emp_files.write( name +';'+id_num+';'+dept + '\n')

        # Display a blank line 
        print()

    emp_files.close()
    

main()