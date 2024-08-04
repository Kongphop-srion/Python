def main():
   
    emp_files = open('employees.txt', 'r') 
    for line in emp_files:
        f1 = line.split(';')
     
        print('Name : ', f1[0])
        print('ID : ',f1[1])
        print('Dept : ',f1[2])

    emp_files.close()

main()