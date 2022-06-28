def elementwise_multiplication(vec_a, vec_b):
    op = []
    for i,j in zip(vec_a, vec_b):
        op.append(i*j)
    return op
    
inputs = [8.3,9.4, 2.4, 9.2, 9, 12]
weights = [0.2, 0.5, 0.1, 0.56, 0.63]

print(elementwise_multiplication(inputs, weights))

