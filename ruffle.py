
'''
creating list and checking elements of it
'''
#import mymodule

while True:
    
    len_list = int(input(' Enter your list size: '))
    if not len_list %2 == 0:
        print(' your list size must be even')
        continue
    else:
    #list_size was successfully parsed!
    #we're ready to exit the loop.
        break
                
element_list = []

#checking if the lenght of list is zero or not
if len_list == 0:
    print('True')
    
#append the elements into list               
for i in range(len_list):
    element = input(' Enter your element: ')
    element_list.append(element)
    
print(element_list)

def Rshk(element_list):
    result = []
    middle_index = len_list // 2

    for i in range(len(element_list)):
        result.append(element_list[i // 2 + (i % 2) * middle_index])
    return result

print(Rshk(element_list))











    
    
    



       












    
