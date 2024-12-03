from reader import read_file

def getLists():
    lines = read_file("input.txt")
    bucket_a = []
    bucket_b = []
    
    for line in lines:
        values = line.split("   ")
        if len(values) == 2:
            bucket_a.append(values[0])
            bucket_b.append(values[1])
        
    return bucket_a, bucket_b

def popSmaller(numbers):
    smallest = min(numbers)  # Find the smallest value
    numbers.remove(smallest)  # Remove the smallest value
    return smallest, numbers


def main():
    left_list, right_list = getLists();
    total = 0;

    for i in range(len(left_list)):
        min_left, left_list = popSmaller(left_list);
        min_right, right_list = popSmaller(right_list);
        total = total + abs(int(min_left) - int(min_right))
    
    print(total)

if __name__ == "__main__":
    main()
