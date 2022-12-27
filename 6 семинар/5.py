import random

numbers = [random.randint(1,100) for _ in range(200)]
print(f'список без совпадений: {list(filter(lambda x:[0] != x[1],enumerate(numbers)))}')