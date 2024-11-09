import sys

def edit_distance(word_1 : str, word_2 : str) -> None:
    matrix = [[y + x if y == 0 or x == 0 else 0 for x in range(len(word_1)+1)] for y in range(len(word_2)+1)]
    for m in range(len(word_2)):
        for n in range(len(word_1)):
            add = 0 if word_1[n] == word_2[m] else 1
            matrix[m+1][n+1] = max(min(matrix[m][n], matrix[m][n+1], matrix[m+1][n]) + add, m-n)
    return matrix[len(word_2)][len(word_1)]

if __name__ == "__main__":
    word_1 = sys.argv[1]
    word_2 = sys.argv[2]
    print(edit_distance(word_1, word_2))