
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers seperated by commas(eg. 5,67,32)")


def get_user_input():
    user_input = input()
    str_list = user_input.split(",")
    num_list = [float(n) for n in str_list]
    return num_list
    


def calc_average_temp(num_list):
    calc_average = sum(num_list)/len(num_list)
    return f"average is {calc_average}"
    

def find_min_max(num_list):
    min_value =min(num_list)
    max_value = max(num_list)
    return f"min value is {min_value} and max value {max_value}"



def sort_temperatur(num_list):
    num_list = sorted(num_list)
    return num_list

def calc_median_temperature(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    
    # 2. If odd, return the middle element
    if n % 2 != 0:
        return sorted_lst[mid]
    
    # 3. If even, return the average of the two middle elements
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    average = calc_average_temp(temp_list)
    median = calc_median_temperature(temp_list)
    min_max = find_min_max(temp_list)

    print(str(average))
    print(str(min_max))
    print(str(median))
    

    
   

main()