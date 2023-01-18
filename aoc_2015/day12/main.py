from util.inputs import parse_input
import re
import json

def part1():
    data = parse_input()[0]
    numbers = re.findall(r'-?\d+',data)
    return sum(int(i) for i in numbers)

def part2():
    data = json.loads(parse_input()[0])
    cleaned_data = clean_data(data)
    print(cleaned_data)
    json_string = json.dumps(cleaned_data)
    numbers = re.findall(r'-?\d+',json_string)
    return sum(int(i) for i in numbers)
      
def clean_dict(data:dict):
    for key,value in data.items():
        if value == 'red':
            return {}
        if type(value) == dict:
            data[key] = clean_dict(value)        
        if type(value) == list:
            data[key] = clean_list(value)
    return data

def clean_list(data:list):
    for i,element in enumerate(data):
                if type(element) == dict:
                    data[i] = clean_dict(element)
                if type(element) == list:
                    data[i] = clean_list(element)
                    
    return data

def clean_data(data:dict):
    if 'red' in data.values():
        return {}
    data = clean_dict(data)
                    
    return data
    
    
def test():
    for data, expected in zip(parse_input(True,'example'),parse_input(True,'expected')):
        print(data)
        result = None
        print(f"Result: {result}, expected: {expected}, match = {result == expected}")
    
def main():
    result1 = part1()
    result2 = part2()
    print(f"Part 1 result: {result1}, Part 2 result: {result2}")
    
if __name__ == '__main__':
    # test()
    main()