'''
Created on Dec 16, 2014

@author: rangeles
'''

def print_attribute_names_and_values(instance, attribute_names):
    '''Prints the attribute names and values of an instance'''
    for i in range(len(instance)):
        print attribute_names[i], '=', instance[i]
    return