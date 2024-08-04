import pickle



def main():
    member = {'Min':'0969936296','Wave':'0957083561','Bunnapon':'0638011033','Jane':'0929907061','Mic':'0809031245','Palm':'0963916108',
        'Mac':'0820759182','Deaw':'0956123020','Dan':'0613298526','Chalongrath':'0999165470','Gust':'0946192332','Fern':'0623289157','Bell':'0927845184'}

    Display_mem = 1
    Search_mem = 2
    Edit_mem = 3
    Del_mem = 4
    Clear_mem = 5
    Quit_program = 6
    opfile = open('pkl.dat','wb')
    pickle.dump(member,opfile)
    while True:
        display_menu()
        pb = int(input('Which function do you want ? : '))
        if pb == Display_mem:
            print(member)
        elif pb == Search_mem: 
            teln = input('Which one do you want to know telephone number ? : ')
            opfile = open('pkl.dat','rb')
            search =pickle.load(opfile)
            print('TEL : ',search[teln])
        elif pb == Edit_mem:
            key = input('Which one do you want to edit telephone number ? : ')
            values = input('Enter the telephone number :') 
            opfile = open('pkl.dat','wb')
            pickle.dump(member,opfile)
            member[key]=values 
            print(member)
        elif pb == Del_mem: 
            delmember = input('Which one do you want to delete telephone number ? : ')
            opfile =open('pkl.dat','wb')
            pickle.dump(member,opfile)
            del member[delmember] 
            print(member)
        elif pb == Clear_mem: 
            opfile = open('pkl.dat','wb')
            member = member.clear()
            print('PHONE BOOK DATA HAS BEEN CLEARED')
            print(member) 
        elif pb == Quit_program:
            print('Quiting program . . . ') 
            break
        else: 
            print('Error invaild selection.')
            
       


def display_menu():
    print('-'*29)   
    print(' \tHEROES ')
    print('-'*29)   
    print('1) DISPLAY TELEPHONE NUMBER')
    print('2) SEARCH TELEPHONE NUMBER')   
    print('3) EDIT TELEPHONE NUMBER')
    print('4) DELETE TELEPHONE NUMBER')
    print('5) DELETE PHONEBOOK DATA')
    print('6) QUIT PROGRAM')
    print('-'*29)   
main()
          
