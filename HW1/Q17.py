#Random loop
import random

training_data = open("w1_15_train.dat")
datum = training_data.readlines()
training_data.close()
line_count = 0
iteration_count = 0
total_error_count = 0
input_count = len(datum)
for ii in range(2000):
    
    print('Round %d' % ii)
    error_count = 1
    w = [0., 0., 0., 0., 0.]
    while error_count != 0:
        iteration_count += 1
        #print('iteration %d, line count %d' % (iteration_count, line_count))
        error_count = 0
        random.seed(ii)
        random_sequence = {}
        while len(random_sequence) != input_count:
            random_index = int(random.random()*input_count)
            try:
                test = random_sequence[random_index]
            except:
                random_sequence[random_index] = random_index
        for line_count, random_index in enumerate(random_sequence.keys()):
            data = [1.] + [float(elem) for elem in datum[random_index].split()]
            summation = 0
            for index, xi in enumerate(data[:-1]):
                summation += w[index] * xi
            hx = -1
            if summation > 0:
                hx = 1
            if hx != data[-1]:
                error_count += 1
                total_error_count += 1
                #Update w
                correction_vector = [ xi*data[-1] for xi in data[:-1] ]
        #        print (correction_vector,data[:-1])
                for index, elem in enumerate(correction_vector):
                    w[index] += elem
         #       print(data, summation, w ,line_count)
                #break
        #print(error_count)
print total_error_count
print('average update count %d' % (total_error_count/2000))
#print("PLA stop after %d iterations" % iteration_count)
