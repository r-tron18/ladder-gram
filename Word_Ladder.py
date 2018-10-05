
from collections import defaultdict as dd
import re,sys,os

## dictionary defaults
def default():
    return False
def li_default():
    return []            

in_dic = dd(default)
all_words= dd(li_default)

class Linked:
    def __init__(self,wrd):
        self.value=wrd
        self.parent=None
        self.child=[]

def build(start,pattern,words,seen,LIST,ignore_list):
    li =[word for word in words if re.search(pattern,word) and word not in seen and word not in LIST and word != start and word not in ignore_list]
    return li
        
def answer(li):
    answer_string= str(len(li)-1)+'  '
    for it in li[:-1]:
        answer_string+=it+'-->'
    answer_string += li[-1]

    return answer_string


def make_linked(start,target,NOT_LIST):

    ln =len(start)
    root=Linked(start)
    
    seen=[start]
    our_words = all_words[ln]
    list_of_nodes =[root]
    
    while True:
        new_node_li=[]
        status = 0
        for node in list_of_nodes:
            val = node.value
            patterns = [val[:i]+'.'+val[i+1:] for  i in range(ln) ]
            pattern_li = []
            for pattern in patterns:
                pattern_li+=build(val,pattern,our_words,seen,pattern_li,NOT_LIST)
            
            seen += pattern_li
            for wrd in pattern_li:
                tmp_node =Linked(wrd)
                tmp_node.parent=node
                new_node_li.append(tmp_node)
            
                if wrd==target:
                    answer_li=[wrd]
                    while tmp_node.parent!=None:
                        tmp_node=tmp_node.parent
                        answer_li.append(tmp_node.value)
                    answer_li.reverse()
                    return answer(answer_li)

            if pattern_li != []:
                status = 1

        if not status:
            ## answer not possible since no such path
            string='No path found'
            return string
        else:
            list_of_nodes = new_node_li
            

    li=[]
    for pattern in patterns:
        li=build(start,pattern,our_words,seen,li)
    

def solution(start,target,NOT_LIST):
    if not(in_dic[start] and in_dic[target]):
        return 'Start or target not found in given dictionary'
    elif len(start) != len(target):
        return 'Start and Target are of different length'
    elif start==target:
        return '0  '+source+'-->'+target
    else:
        return make_linked(start,target,NOT_LIST)

def initialise(dictionary_name):
   
    try:
        with open(dictionary_name) as fp:
            data=fp.read()
            tmp_list=data.split()

            for word in tmp_list:
                all_words[len(word)].append(word)
                in_dic[word]=True

    except:
        return 0

if __name__=="__main__":
    dictionary_name=input('Enter dictionary name ')  ## change to user input
    if initialise(dictionary_name)==0:
        print('Dictionary',dictionary_name,'is not present in the present directory')
        sys.exit()

    start=input('Enter start: ')
    target=input('Enter Target: ')
    print('Do u want to enter the list of words that is not supposed to be in the path')

    choice=input('Y or N: ')
    if choice=='Y' or choice=='y':
        print('Enter your word list as space separated input')
        unacceptable = input().split()
        print('Your solution is')
        print(solution(start,target,unacceptable))
    else:
        print('Your solution is')

        print(solution(start,target,[]))
        
