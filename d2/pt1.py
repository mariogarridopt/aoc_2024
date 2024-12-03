from reader import read_file

def get_levels():
    lines = read_file("input.txt")
    levels = []
    
    for line in lines:
        level = []

        values = line.split(" ")
        for value in values:
            level.append(int(value))
        
        levels.append(level)
        
    return levels

def is_level_safe(level_list: list):
    is_increasing = True
    is_decreasing = True

    for i in range(len(level_list) - 1):
        change = abs(level_list[i] - level_list[i + 1]);
        if change < 1 or change > 3:
            return False

        if level_list[i] < level_list[i + 1]:
            is_decreasing = False  # If it's increasing, it's not decreasing
        elif level_list[i] > level_list[i + 1]:
            is_increasing = False  # If it's decreasing, it's not increasing

    return is_increasing or is_decreasing


def main():
    levels = get_levels()
    safe_levels = 0

    for level in levels:
        if is_level_safe(level):
            safe_levels += 1
    
    print(safe_levels)

if __name__ == "__main__":
    main()
