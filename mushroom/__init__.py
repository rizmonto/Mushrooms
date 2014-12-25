#from simple_ml import clean_instances_of_errant, load_attribute_names_and_values, load_instances, load_attribute_values, load_attributes, attribute_value_counts
from simple_ml import*

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


#index = attribute_value_counts(clean_instances, 'habitat', attribute_names)
#print index

#index = attribute_value_proportion(clean_instances, 'cap-shape', attribute_names)
#print index

print_all_attribute_value_counts(clean_instances, attribute_names)