import simple_ml

attribute_names = ['class', 
                   'cap-shape', 'cap-surface', 'cap-color', 
                   'bruises?', 
                   'odor', 
                   'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 
                   'stalk-shape', 'stalk-root', 
                   'stalk-surface-above-ring', 'stalk-surface-below-ring', 
                   'stalk-color-above-ring', 'stalk-color-below-ring',
                   'veil-type', 'veil-color', 
                   'ring-number', 'ring-type', 
                   'spore-print-color', 
                   'population', 
                   'habitat']

all_instances2 = [] #initialize list
data_filename = 'agaricus-lepiota.data'
clean_instances = []

all_instances2 = simple_ml.load_instances(data_filename)


#print '|'.join(all_instances2[0])

for instance in all_instances2:
    if '?' not in instance:
        clean_instances.append(instance)

#print len(clean_instances)

kaboom = {'a' : 'apple', 'b' : 'banana'}

test = 'bam : sexy : awesome : omg'
test2 = []
test2 = test.strip().split(':')
print test2