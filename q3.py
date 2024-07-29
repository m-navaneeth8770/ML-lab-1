def q3(list1, list2):
   
    common_count = 0
    checked_elements = []
    
    for element in list1:

        found = False
        for checked in checked_elements:
            if checked == element:
                found = True
                break
        
        if not found:
            
            length = len(checked_elements)
            checked_elements += [0] * (length + 1 - len(checked_elements))  
            checked_elements[length] = element
            
           
            for item in list2:
                if item == element:
                    common_count += 1
                    break

    return common_count

def main():
    
    list1 = []
    n1 = int(input("Enter the number of elements in the first list: "))
    print("Enter the elements of the first list:")
    for _ in range(n1):
        list1 += [int(input())] 

    list2 = []
    n2 = int(input("Enter the number of elements in the second list: "))
    print("Enter the elements of the second list:")
    for _ in range(n2):
        list2 += [int(input())]  
    
    common_count = q3(list1, list2)
    print("Number of common elements:", common_count)


main()

