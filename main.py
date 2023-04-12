from graphdisp import *
import sys


if __name__ == "__main__":
    if sys.argv[1] == 'scores':
        if len(sys.argv) >= 3:
            if sys.argv[2] == 'reload':
                save_json()
            else:
                if len(sys.argv[2]) != 9:
                    raise Exception('Enter a correct Student ID !')
                compute(sys.argv[2])
        else:
            get_tab()
    elif sys.argv[1] == 'display':
        print('eded')
        if len(sys.argv) < 4:
            raise Exception('Choose an integer between 0 and 100 and a type of graph! (Student ID is optionnal)')
    
        gr_type = sys.argv[2]
        res_bool = True
        try: 
            float(sys.argv[3])
        except: 
            res_bool = False
        if not res_bool:
            raise Exception('Choose an float between 0 and 100 !')

        prc = float(sys.argv[3])
        if prc > 100 or prc < 0:
            raise Exception('Choose an float between 0 and 100 !')
        elif not operator.xor((gr_type != 'bar'),(gr_type != 'line')):
            raise Exception('Choose a correct type of graph!')

        if len(sys.argv) == 5:
            st_id = sys.argv[4]
            if len(st_id) == 9:
                print("Generating a " + gr_type + " graph of precision of "+str(prc) +" with student ID : "+ st_id +"...")
                sc_id = load_json()
                vline = get_rank(sc_id,st_id)[1]
                create_line_plot(prc,gr_type,vline)
            else:
                raise Exception('Enter a correct Student ID !')
        else:
            print("Generating a " + gr_type + " graph of precision of "+str(prc) +"...")
            create_line_plot(prc,gr_type)
   
