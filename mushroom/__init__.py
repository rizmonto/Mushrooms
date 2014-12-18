import simple_ml

#mushroom = ['a', ' b ', '\nc', 'd']

#print mushroom.index('a', )

#print range(len(mushroom)), 'omg'

#simple_ml.print_attribute_names_and_values(['p', 'a', 'f'], ['awesome', 'badass', 'hamster'])

all_instances = []; #initialize list
data_filename = 'agaricus-lepiota.data'

with open(data_filename, 'r') as f:
    for line in f:
        #clean each line and add into an array
        all_instances.append(line.strip().split(','))

print 'Read:', len(all_instances), 'instances from ', data_filename

print 'First Instance', all_instances[0][0]