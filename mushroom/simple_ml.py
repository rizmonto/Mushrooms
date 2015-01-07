'''
Created on Dec 16, 2014

@author: rangeles
'''
from _collections import defaultdict
import operator
from decimal import Decimal
import math
import collections
from operator import contains

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
                clean_instances_list.append(line.strip().split(','))
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

def attribute_value_relative_edible_counts(instances, attribute, attribute_names):
    '''Returns a dictionary with count of edibility based on attribute entered, used for entropy and information gain'''
    attribute_value_counts = defaultdict(int)
    instance_value_counts = {}
    #find position of attribute in attribute_name
    position_index = attribute_names.index(attribute)

    #count occurrences of values in that position in the index list
    for instance in instances:
        #save the value of the attribute
        instance_value = instance[position_index]
        #check if it's edible and not in the list
        #if instance_value not in instance_value_counts and instance[0] == 'e': deprecated
        if instance_value not in instance_value_counts: #takes into account zero occurence attributes
            #add to dictionary, but strip beforehand
            instance_value_counts[instance_value.strip()] = 0
        #increment at dictionary key, make sure you strip beforehand, and only do this if it's edible
        if instance[0] == 'e':
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
    entropy_calculation = - side_a - side_b
    return entropy_calculation

def entropy_generic(instances, attribute_names, entropy_attribute):
    '''Returns dictionary of entropy of a data set of attributes values'''
    attribute_value_count = {}
    attribute_edible_count = {}
    attribute_entropies = {}

    attribute_value_count = attribute_value_counts(instances, entropy_attribute, attribute_names)
    #get relative edible count    
    attribute_edible_count = attribute_value_relative_edible_counts(instances, entropy_attribute, attribute_names)
    #print attribute_edible_count
    for key,value in attribute_edible_count.iteritems():
        #calculate the proportion of edible
        attribute_and_edible = float(value)/attribute_value_count[key]

        #save the inedible count
        inedible_count = attribute_value_count[key] - value

        #calculate the proportion of inedible
        attribute_and_inedible = float(inedible_count)/attribute_value_count[key]

        if attribute_and_edible != 0: #can't take the log of 0
            calc1 = math.log(attribute_and_edible, 2) #log base 2
        else:
            calc1 = 0
        
        if attribute_and_inedible != 0:
            calc2 = math.log(attribute_and_inedible, 2)
        else:
            calc2 = 0

        attribute_entropies[key] = - ((attribute_and_edible * calc1) + (attribute_and_inedible * calc2))

    #TODO - Take into account proper edible count proportions
    return attribute_entropies

def information_gain(parent_entropy, instances, attribute_names, entropy_attribute):
    '''Prints information gain of a set of instances'''
    class_proportion_count = attribute_value_proportion(instances, entropy_attribute, attribute_names)
    attribute_entropies = entropy_generic(instances, attribute_names, entropy_attribute)
    aggregate_entropy = 0

    for key in class_proportion_count.keys():
        #print class_proportion_count[key]
        aggregate_entropy =  aggregate_entropy + class_proportion_count[key] * attribute_entropies[key]
    info_gain = parent_entropy - aggregate_entropy
    return info_gain

def split_instances(instances, attribute_index):
    '''Returns a list of dictionaries, splitting a list of instances according to their values of a specified attribute''
    The key of each dictionary is a distinct value of attribute_index,
    and the value of each dictionary is a list representing the subset of instances that have that value for the attribute'''
    partitions = defaultdict(list)
    for instance in instances:
        #every time an attribute value occurs, add the entire instance to that attribute value occurrence
        partitions[instance[attribute_index]].append(instance)
    return partitions

def choose_best_attribute_index(instances, attribute_names):
    '''Returns the index in the list of candidate_attribute_indexes that provides the highest information gain if instances 
    are split based on that attribute index.'''
    info_gain = {}
    full_attribute_names = load_attributes('agaricus-lepiota.attributes')
    parent_entropy = entropy(instances, full_attribute_names)
    #skip over the first class, edible/poisonous
    for name in attribute_names:
        info_gain[name] = information_gain(parent_entropy, instances, full_attribute_names, name)
    #sort the list and returns a tuple
    sorted_info_gain = sorted(info_gain.items(), key = operator.itemgetter(1), reverse = True)

    #return the attribute index with the highest info gain, the top attribute
    if sorted_info_gain[0][0] in full_attribute_names:
        return full_attribute_names.index(sorted_info_gain[0][0], )

def majority_value(instances, class_index = 0):
    '''returns the most frequently occurring value of class_index in instances'''
    class_values = []
    for instance in instances:
        class_values.append(instance[class_index])

    class_counts = collections.Counter(class_values)
    #return class_counts.most_common(1)
    #access index key of most common occurring key
    return class_counts.most_common(1)[0][0]

def create_decision_tree(instances, candidate_attribute_indexes = None, class_index = 0, default_class = None, trace = 0):
    '''Returns a new decision tree trained on a list of instances.

    The tree is constructed by recursively selecting and splitting instances based on 
    the highest information_gain of the candidate_attribute_indexes.

    The class label is found in position class_index.

    The default_class is the majority value for the current node's parent in the tree.
    A positive (int) trace value will generate trace information with increasing levels of indentation.

    class_index is the target attribute to classify by, in this case it is poisonous or edible

    candidate_attribute_indexes is the attributes the tree will create against

    Derived from the simplified ID3 algorithm presented in Building Decision Trees in Python by Christopher Roach,
    http://www.onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html?page=3'''

    attribute_list = load_attributes('agaricus-lepiota.attributes')

    #if no candidate_attribute_indexes are provided, assume that we will use all but the target_attribute_index
    if candidate_attribute_indexes is None:
        #candidate_attribute_indexes = range(len(instances[0]))
        candidate_attribute_indexes = load_attributes('agaricus-lepiota.attributes')
        #delete classes attribute at index 0
        del candidate_attribute_indexes[0]

    #add occurences of edible or poisonous into a dict Counter
    class_labels_and_counts = collections.Counter([instance[class_index] for instance in instances])

    #if the dataset is empty or the candidate attributes list is empty, return the default value
    if not instances or not candidate_attribute_indexes:
        if trace:
            print '{}Using default class {}'.format('< ' * trace, default_class)
        return default_class

    #if all the instances have the same class label, return that class label
    elif len(class_labels_and_counts) == 1:
        class_label = class_labels_and_counts.most_common(1)[0][0]
        if trace:
            print '{}All {} instances have label {}'.format('< ' * trace, len(instances), class_label)
        return class_label
    else:
        default_class = majority_value(instances, class_index)

        # Choose the next best attribute index to best classify the instances
        #best_index = choose_best_attribute_index(instances, candidate_attribute_indexes, class_index)
        best_index = choose_best_attribute_index(instances, candidate_attribute_indexes)
        if trace:
            print '{}Creating tree node for attribute index {}'.format('> ' * trace, best_index)

        # Create a new decision tree node with the best attribute index and an empty dictionary object (for now)
        tree = {best_index:{}}

        # Create a new decision tree sub-node (branch) for each of the values in the best attribute field
        partitions = split_instances(instances, best_index)

        # Remove that attribute from the set of candidates for further splits
        #remaining_candidate_attribute_indexes = [i for i in candidate_attribute_indexes if i != best_index] DEPRECATED
        #remove the next best index
        print best_index
        #find the attribute to remove from the master list of attributes
        attribute_to_remove = attribute_list[best_index]
        #find the index of the attribute to remove
        index_to_remove = candidate_attribute_indexes.index(attribute_to_remove, )
        #finally, remove the attribute at that candidate index level
        del candidate_attribute_indexes[index_to_remove]
        remaining_candidate_attribute_indexes = candidate_attribute_indexes

        for attribute_value in partitions:
            if trace:
                print '{}Creating subtree for value {} ({}, {}, {}, {})'.format(
                    '> ' * trace,
                    attribute_value,
                    len(partitions[attribute_value]),
                    len(remaining_candidate_attribute_indexes),
                    class_index,
                    default_class)

            # Create a subtree for each value of the the best attribute
            subtree = create_decision_tree(partitions[attribute_value], remaining_candidate_attribute_indexes,
                class_index,
                default_class,
                trace + 1 if trace else 0)

            # Add the new subtree to the empty dictionary object in the new tree/node we just created
            tree[best_index][attribute_value] = subtree

    return tree

def classify(tree, instance, default_class=None):
    '''Returns a classification label for instance, given a decision tree
    default_class is the default classification, in this case, whether edible or poisonous'''
    #if tree is empty
    if not tree:
        return default_class
    #if tree is NOT a dict then we've got a problem
    if not isinstance(tree, dict): 
        return tree
    #return the first key of the dict
    attribute_index = tree.keys()[0]
    #return the first value of the dict
    attribute_values = tree.values()[0]
    #save the attribute value of the instance of hte highest entropy attribute
    instance_attribute_value = instance[attribute_index]
    #if that attribute value was not found in the value set
    if instance_attribute_value not in attribute_values:
        return default_class
    return classify(attribute_values[instance_attribute_value], instance, default_class)
    