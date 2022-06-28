def elementwise_multiplication(vec_a, vec_b):
    op = []
    for i,j in zip(vec_a, vec_b):
        op.append(i*j)
   


def elementwise_addition(vec_a, vec_b):
    op = []
    for i,j in zip(vec_a, vec_b):
        op.append(i+j)
   

def vector_sum(vec_a):
    sum = 0
    for i in vec_a:
        sum+=i
    return sum

def vector_avg(vec):
    sum=0
    for i in vec_a:
        sum+=i
    return sum/len(vec_a)

inputs = [8.3,9.4, 2.4, 9.2, 9, 12]
weights = [0.2, 0.5, 0.1, 0.56, 0.63]

print(elementwise_multiplication(inputs, weights))

