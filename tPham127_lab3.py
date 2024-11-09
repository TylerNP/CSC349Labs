import sys

#word_1 = sys.argv[1]
#word_2 = sys.argv[2]

def edit_distance(word_1 : str, word_2 : str) -> None:
    matrix = [[0 for _ in range(len(word_1)+1)] for _ in range(len(word_2)+1)]
    for index in range(len(word_2)+1):
        matrix[index][0] = index
    for index in range(len(word_1)+1):
        matrix[0][index] = index
    for m in range(len(word_2)+1):
        for n in range(len(word_1)+1):
            print()
    print(matrix)
    print(word_1 + " " + word_2)

#edit_distance(word_1, word_2)

if __name__ == "__main__":
    str_1 = "SNOWY"
    str_2 = "SUNNY"
    edit_distance(str_1, str_2)