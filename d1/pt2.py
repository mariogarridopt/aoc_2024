from reader import read_file

def getLists():
    lines = read_file("input.txt")
    bucket_a = []
    bucket_b = []
    
    for line in lines:
        values = line.split("   ")
        if len(values) == 2:
            bucket_a.append(int(values[0]))
            bucket_b.append(int(values[1]))
        
    return bucket_a, bucket_b

def countNumbers(list: list, number: int):
    count = 0
    for item in list:
        if item == number:
            count += 1
    return count


def main():
    left_list, right_list = getLists();
    similarity_score = 0;

    for i in range(len(left_list)):
        left_value = left_list[i];
        right_value_count = countNumbers(right_list, left_value);

        similarity_score = similarity_score + (left_value * right_value_count)
    
    print(similarity_score)

if __name__ == "__main__":
    main()
