from math import acos, cos, sqrt

def compute_word_frequencies(words) -> dict:
    """
    Input:  list of words
    Output: dictionary of word count
    """
    word_dict = {}
    for word in words:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict

def compute_dot_product(doc1, doc2) -> float:
    """
    Input:  dictionary of word frequencies
    Output: dot product
    """
    sum = 0
    for key in doc1.keys():
        if key in doc2.keys():                                              # compute dot product only if the word is same
                sum += doc1[key] * doc2[key]

    return sum 


def document_distance(doc1, doc2) -> float:
    """
    Input:  2 lists of words
    Output: Distance between them
    """
    # Compute word frequencies
    doc1_words = compute_word_frequencies(doc1)
    doc2_words = compute_word_frequencies(doc2)

    # compute dot product
    dot_product = compute_dot_product(doc1_words, doc2_words)

    return dot_product


if __name__ == '__main__':

    # converting the document to words
    doc1 = [ word for line in open("examples/dog-cat/document1.txt").readlines() for word in line.split() ]
    doc2 = [ word for line in open("examples/dog-cat/document2.txt").readlines() for word in line.split() ]

    numerator = document_distance(doc1, doc2)
    denominator = sqrt(document_distance(doc1, doc1) * document_distance(doc2, doc2))
    print("Distance:", acos(numerator/denominator) )

    # converting the document to words
    doc1 = [ word for line in open("examples/lecture2_data/t1.verne.txt").readlines() for word in line.split() ]
    doc2 = [ word for line in open("examples/lecture2_data/t6.onemillion.txt").readlines() for word in line.split() ]

    numerator = document_distance(doc1, doc2)
    denominator = sqrt(document_distance(doc1, doc1) * document_distance(doc2, doc2))
    print("Distance:", acos(numerator/denominator) )
