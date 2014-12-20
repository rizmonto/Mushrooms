'''
Created on Dec 16, 2014

@author: rangeles
'''

def print_attribute_names_and_values(instance, attribute_names):
    '''Prints the attribute names and values of an instance'''
    for i in range(len(instance)):
        print attribute_names[i], '=', instance[i]
    return

def load_instances(filename):
    instances = []

    with open(filename, 'r') as f:
        for line in f:
            instances.append(line.strip().split(','))

    return instances

def load_attribute_values(filename):
    '''Returns a list of attribute values in a file.
    
    The attribute values are represented as dictionaries, wherein the keys are abbreviations and the values are descriptions.
    filename is expected to have one attribute name and set of values per line, with the following format:
        name: value_description=value_abbreviation[,value_description=value_abbreviation]*
    for example
        cap-shape: bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
    The attribute value description dictionary created from this line would be the following:
        {'c': 'conical', 'b': 'bell', 'f': 'flat', 'k': 'knobbed', 's': 'sunken', 'x': 'convex'}'''
    
    attribute_values = []
    
    with open(filename, 'r') as f:
        for line in f:
            
    