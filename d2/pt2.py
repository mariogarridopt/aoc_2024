from reader import read_file

def get_levels() -> list:
    lines = read_file("input.txt")
    levels = []
    
    for line in lines:
        level = []

        values = line.split(" ")
        for value in values:
            level.append(int(value))
        
        levels.append(level)
        
    return levels

def get_failing_index(level_list: list) -> int:
    is_increasing = True
    is_decreasing = True

    for i in range(len(level_list) - 1):
        change = abs(level_list[i] - level_list[i + 1]);
        if change < 1 or change > 3:
            return i

        if level_list[i] < level_list[i + 1]:
            if i != 0 and is_decreasing == True:
                return i
            is_decreasing = False  # If it's increasing, it's not decreasing
        elif level_list[i] > level_list[i + 1]:
            if i != 0 and is_increasing == True:
                return i
            is_increasing = False  # If it's decreasing, it's not increasing
    return -1


def is_level_safe(level_list: list) -> bool:
    first_result = get_failing_index(level_list);
    if(first_result == -1):
        print(f"{level_list} - NoN")
        return True;

    #check sides
    remove_left_result = 0;
    remove_center_result = 0;
    remove_right_result = 0;

    if(first_result != 0): # left
        level_list_clone = level_list[:]; # cloning to not affect parent
        level_list_clone.pop(first_result - 1);
        remove_left_result = get_failing_index(level_list_clone);
    
    # center
    level_list_clone = level_list[:]; # cloning to not affect parent
    level_list_clone.pop(first_result);
    remove_center_result = get_failing_index(level_list_clone);

    if(first_result < len(level_list) - 1): # right
        level_list_clone = level_list[:]; # cloning to not affect parent
        level_list_clone.pop(first_result + 1);
        remove_right_result = get_failing_index(level_list_clone);
    
    # Result 
    return (remove_left_result == -1 or remove_center_result == -1 or remove_right_result == -1)

def main():
    levels = get_levels()
    safe_levels = 0

    for level in levels:
        if is_level_safe(level):
            safe_levels += 1
            #print(level)
    
    print(safe_levels)

if __name__ == "__main__":
    main()
