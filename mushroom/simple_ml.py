'''
Created on Dec 16, 2014

@author: rangeles
'''
from _collections import defaultdict
import operator
from decimal import Decimal
import math

def print_attribute_names_and_values(instance, attribute_names):
    '''Prints the attribute names and values of an instance'''
    for i in range(len(instance)):
        print attribute_names[i], '=', instance[i]
    return

def load_instances(filename):
    '''Returns a 2D list of instances and their values'''
    instances = []

    with open(filename, 'r') as f:
        for line in f:
            instances.append(line.strip().split(','))

    return instances

def load_attributes(filename):
    '''Returns list of attributes names'''
    temp_list = []
    attribute_names = []
    with open(filename) as f:
        for line in f:
            temp_list = line.strip().split(':')
            attribute_names.append(temp_list[0])
    return attribute_names

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
    with open(filename) as f:
        for line in f:
            attribute_name_and_value_string_list = line.strip().split(':')
            attribute_name = attribute_name_and_value_string_list[0]
            if len(attribute_name_and_value_string_list) < 2:
                attribute_values.append({}) # no values for this attribute
            else:
                value_abbreviation_description_dict = {}
                description_and_abbreviation_string_list = attribute_name_and_value_string_list[1].strip().split(',')
                for description_and_abbreviation_string in description_and_abbreviation_string_list:
                    description_and_abbreviation = description_and_abbreviation_string.strip().split('=')
                    description = description_and_abbreviation[0]
                    if len(description_and_abbreviation) < 2: # assumption: no more than 1 value is missing an abbreviation
                        value_abbreviation_description_dict[None] = description
                    else:
                        abbreviation = description_and_abbreviation[1]
                        value_abbreviation_description_dict[abbreviation] = description
                attribute_values.append(value_abbreviation_description_dict)
    return attribute_values

def load_attribute_names_and_values(filename):
    '''Returns a list of dictionaries of dictionaries (lol) of the attributes, values, and name'''
    attribute_values = []
    attribute_names_and_values = []
    #take care of the values first
    with open(filename) as f:
        for line in f:
            attribute_name_and_value_string_list = line.strip().split(':')
            attribute_name = attribute_name_and_value_string_list[0];
            if len(attribute_name_and_value_string_list) < 2:
                attribute_values.append({}) # no values for this attribute
            else:
                value_abbreviation_description_dict = {}
                description_and_abbreviation_string_list = attribute_name_and_value_string_list[1].strip().split(',')
                for description_and_abbreviation_string in description_and_abbreviation_string_list:
                    description_and_abbreviation = description_and_abbreviation_string.strip().split('=')
                    description = description_and_abbreviation[0]
                    if len(description_and_abbreviation) < 2: # assumption: no more than 1 value is missing an abbreviation
                        value_abbreviation_description_dict[None] = description
                    else:
                        abbreviation = description_and_abbreviation[1]
                        value_abbreviation_description_dict[abbreviation] = description
                #attribute_values.append(value_abbreviation_description_dict)
                attribute_names_and_values_dict = {}
                attribute_names_and_values_dict['name'] = attribute_name
                attribute_names_and_values_dict['values'] = value_abbreviation_description_dict
                attribute_names_and_values.append(attribute_names_and_values_dict)
    return attribute_names_and_values

def clean_instances_of_errant(filename):
    '''Returns a list of lists of strings of cleaned instances'''
    clean_instances_list = []
    with open(filename) as f:
        for line in f:
            if '?' not in line:
                clean_instances_list.append(line.split(','))
    return clean_instances_list


def attribute_value_counts(instances, attribute, attribute_names):
    '''Returns a defaultdict containing the counts of occurrences of each value of attribute in the list of
    instances.attribute_names is the list we created above, where each element is the name of an attribute.'''
    attribute_value_counts = defaultdict(int)
    instance_value_counts = {}
    #find position of attribute in attribute_name
    position_index = attribute_names.index(attribute)

    #count occurrences of values in that position in the index list
    for instance in instances:
        #save the value of the attribute
        instance_value = instance[position_index]
        if instance_value not in instance_value_counts:
            #add to dictionary, but strip beforehand
            instance_value_counts[instance_value.strip()] = 0
        #increment at dictionary key, make sure you strip beforehand
        instance_value_counts[instance_value.strip()] += 1
    return instance_value_counts

def attribute_value_proportion(instances, attribute, attribute_names):
    '''Returns a defaultdict containing the counts of occurrences and proportion of each value of attribute in the list of
    instances.attribute_names is the list we created above, where each element is the name of an attribute.'''
    attribute_value_counts = defaultdict(int)
    instance_value_counts = {}
    instance_proportions = {}
    #find position of attribute in attribute_name
    position_index = attribute_names.index(attribute)

    #count occurrences of values in that position in the index list
    for instance in instances:
        #save the value of the attribute
        instance_value = instance[position_index].strip()
        if instance_value not in instance_value_counts:
            #add to dictionary, but strip beforehand
            instance_value_counts[instance_value] = 0
            instance_proportions[instance_value] = 0
        #increment at dictionary key, make sure you strip beforehand
        instance_value_counts[instance_value] += 1
        instance_proportions[instance_value] = float(instance_value_counts[instance_value]) / len(instances)
    return instance_proportions

def print_all_attribute_value_counts(instances, attribute_names):
    '''Returns printing of all each attribute name, value abbreviation, count of occurences, then proporation'''
    instance_attribute_value_counts = {}
    instance_attribute_value_counts_proportions = {}
    for attribute in attribute_names:
        #add counts to dictionary with attribute
        instance_attribute_value_counts[attribute] = attribute_value_counts(instances, attribute, attribute_names)
    #for
    print instance_attribute_value_counts

def entropy(instances, attribute_names):
    '''Returns entropy of a data set of mushrooms'''
    class_value_count = {}
    class_value_count = attribute_value_counts(instances, 'classes', attribute_names)
    number_of_instances = len(instances)
    #calculate edible first
    e = float(class_value_count['e'])
    p = float(class_value_count['p'])
    side_a = (e / number_of_instances) * math.log((e / number_of_instances), 2)
    #then calculate poisonous next
    side_b = (p / number_of_instances) * math.log((p / number_of_instances), 2)
    entropy_calculation = -side_a - side_b
    print entropy_calculation

def entropy_generic(instances, attribute_names, entropy_attribute):
    '''Returns entropy of a data set of mushrooms'''
    class_value_count = {}
    class_value_count = attribute_value_counts(instances, entropy_attribute, attribute_names)
    number_of_instances = len(instances)

    e = float(class_value_count['e'])
    p = float(class_value_count['p'])
    side_a = (e / number_of_instances) * math.log((e / number_of_instances), 2)
    #then calculate poisonous next
    side_b = (p / number_of_instances) * math.log((p / number_of_instances), 2)
    entropy_calculation = -side_a - side_b
    print entropy_calculation

def information_gain(clean_instances, index):
    '''Prints information gain of a set of instances'''
    for instance in clean_instances:
        print instance[index]
    
    
        
