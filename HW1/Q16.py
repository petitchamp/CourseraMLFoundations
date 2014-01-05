
training_data = open("w1_15_train.dat")
w = [0., 0., 0., 0., 0.]
datum = training_data.readlines()
training_data.close()
line_count = 0
iteration_count = 0
error_count = 1
while error_count != 0:
    iteration_count += 1
    print('iteration %d, line count %d' % (iteration_count, line_count))
    error_count = 0
    for line_count, line in enumerate(datum):
        data = [1.] + [float(elem) for elem in line.split()]
        summation = 0
        for index, xi in enumerate(data[:-1]):
            summation += w[index] * xi
        hx = -1
        if summation > 0:
            hx = 1
        if hx != data[-1]:
            error_count += 1
            #Update w
            correction_vector = [ xi*data[-1] for xi in data[:-1] ]
    #        print (correction_vector,data[:-1])
            for index, elem in enumerate(correction_vector):
                w[index] += elem
     #       print(data, summation, w ,line_count)
            #break
    print(error_count)

print("PLA stop after %d iterations" % iteration_count)
