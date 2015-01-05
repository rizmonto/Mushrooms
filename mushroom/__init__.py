#from simple_ml import clean_instances_of_errant, load_attribute_names_and_values, load_instances, load_attribute_values, load_attributes, attribute_value_counts
from simple_ml import*
from _collections import*
from sqlite3 import collections

all_instances2 = [] #initialize list
data_filename = 'agaricus-lepiota.data'
attribute_filename = 'agaricus-lepiota.attributes'
clean_instances = []

all_instances2 = load_instances(data_filename)

#print '|'.join(all_instances2[0])

attribute_values = []
attribute_values = load_attribute_values(attribute_filename)

'''
attribute_filename = 'agaricus-lepiota.attributes'
attribute_names_and_values = load_attribute_names_and_values(attribute_filename)
print 'Read', len(attribute_names_and_values), 'attribute values from', attribute_filename
print 'First attribute name:', attribute_names_and_values[0]['name'], '; values:', attribute_names_and_values[0]['values']
'''
clean_instances = clean_instances_of_errant(data_filename)
#print len(clean_instances), 'clean instances'
#print attribute_values[0]
#print clean_instances
attribute_names = load_attributes(attribute_filename)

#index = attribute_value_counts(clean_instances, 'bruises', attribute_names)

#print index

#index2 = attribute_value_proportion(clean_instances, 'bruises', attribute_names)
#print index2

#index = attribute_value_proportion(clean_instances, 'cap-shape', attribute_names)
#print index


parent_entropy = entropy(clean_instances, attribute_names)
#print parent_entropy

#generic_entropy = entropy_generic(clean_instances, attribute_names, 'cap-shape')
#print generic_entropy

info_gain = {} 

#info_gain = information_gain(parent_entropy, clean_instances, attribute_names, 'cap-shape')
#print info_gain

#for name in attribute_names:
    #info_gain[name] = information_gain(parent_entropy, clean_instances, attribute_names, name)

#for key,value in info_gain.iteritems():
    #print key, ' - ', value

#print attribute_value_relative_edible_counts(clean_instances, 'cap-shape', attribute_names)

partitions = split_instances(clean_instances, 5)
#print [(partition, len(partitions[partition])) for partition in partitions]

print majority_value(clean_instances)

info_gain = choose_best_attribute_index(clean_instances, attribute_names[1:])
print info_gain

tree = {5:{}}
tree[5]['a'] = 'sexy'
print tree

