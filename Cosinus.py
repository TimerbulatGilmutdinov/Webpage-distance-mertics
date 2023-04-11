import math


def calculate_cosinus(vector_1, vector_2):
    intersection = set(vector_1.keys()) & set(vector_2.keys())
    numerator = sum([vector_1[x] * vector_2[x] for x in intersection])
    sum1 = sum([vector_1[x] ** 2 for x in list(vector_1.keys())])
    sum2 = sum([vector_2[x] ** 2 for x in list(vector_2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    return float(numerator) / denominator
