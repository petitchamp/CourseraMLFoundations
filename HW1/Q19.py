#Random loop
import random
import itertools


def evaluate_hypothesis_performance( w, data_set):
    errors = 0
    for data in data_set:
        result = sum(itertools.imap(lambda x, y: x * y, w, data[:-1]))
        hx = -1
        if result > 0:
            hx = 1
        if hx != data[-1]:
            errors += 1
    return errors


def load_data(file_path):
    training_data = open(file_path)
    text_datum = training_data.readlines()
    training_data.close()
    data_set = []
    for line in text_datum:
        data_set.append([1.] + [float(elem) for elem in line.split()])
    return data_set

if __name__ == '__main__':
    coefficient = 1
    #0.5 for Q17
    coefficient = 0.5
    training_data_set = load_data("hw1_18_train.dat")
    test_data_set = load_data("hw1_18_test.dat")
    line_count = 0
    iteration_count = 0
    total_error_rate_count = 0
    PLA_iteration_count = 1000
    input_count = len(training_data_set)

    for ii in range(PLA_iteration_count):
        if ii % 100 == 0:
            print('Round %d' % ii)
        error_count = 1
        w = [0., 0., 0., 0., 0.]
        pocket_w = w
        current_error_count = evaluate_hypothesis_performance(w,training_data_set)
        random.seed(random.random())
        random_sequence = []
        while len(random_sequence) != input_count:
            random_index = int(random.random() * input_count)
            if random_index not in random_sequence:
                random_sequence.append(random_index)
        update_count = 0

        while error_count != 0 and update_count < 50:
            iteration_count += 1
            #print('iteration %d, line count %d' % (iteration_count, line_count))
            error_count = 0

            for line_count, random_index in enumerate(random_sequence):
                data = training_data_set[random_index]
                summation = sum(itertools.imap(lambda x, y: x * y, w, data[:-1]))
                hx = -1
                if summation > 0:
                    hx = 1
                if hx != data[-1]:
                    #print('iteration %d, line count %d' % (iteration_count, line_count))

                    error_count += 1
                    update_count += 1
                    #Update w
                    correction_vector = [coefficient * xi * data[-1] for xi in data[:-1]]
            #        print (correction_vector,data[:-1])
                    w = list(itertools.imap(lambda x, y: x + y, w, correction_vector))
            new_w_error_count = evaluate_hypothesis_performance(w, training_data_set)

            if new_w_error_count < current_error_count:
                pocket_w = w
                current_error_count = new_w_error_count
                #print(data, summation, w ,line_count)
                #break
         #print(error_count)
        total_error_rate_count += evaluate_hypothesis_performance(pocket_w, test_data_set)/float(len(test_data_set))
        #print(total_error_rate_count)

    print(total_error_rate_count)
    print('average update count %f' % (float(total_error_rate_count)/PLA_iteration_count))
    #print("PLA stop after %d iterations" % iteration_count)






