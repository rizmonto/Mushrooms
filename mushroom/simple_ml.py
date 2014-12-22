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
            attribute_name_and_value_string_list = line.strip().split(':')

            #save attribute name
            attribute_name = attribute_name_and_value_string_list[0]
            if len(attribute_name_and_value_string_list) < 2:
                attribute_values.append({}) # no values for this attribute, only the  attribute name exists
            else:
                value_abbreviation_description_dict = {}
                #strip and separate the attribute values in index 1 into a list next
                description_and_abbreviation_string_list = attribute_name_and_value_string_list[1].strip().split(',')

                #then strip and split the individual values
                for description_and_abbreviation_string in description_and_abbreviation_string_list:
                    description_and_abbreviation = description_and_abbreviation_string.strip.split('=')
                    description = description_and_abbreviation[0]
                    if len(description_and_abbreviation) < 2: #assumption: no more than 1 value is missing an abbreviation
                        value_abbreviation_description_dict[None] = description
                    else:
                        abbreviation = description_and_abbreviation[1]

                        #assign the value description to the abbreviation key
                        value_abbreviation_description_dict[abbreviation] = description
                attribute_values.append(description_and_abbreviation)

    return attribute_values
    