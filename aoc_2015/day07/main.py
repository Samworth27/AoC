from aoc_util.inputs import parse_input, fields
from components.gates import BitwiseANDGate, BitwiseORGate, BitwiseShiftLeftGate, BitwiseShiftRightGate
from components.wire import Wire
from components.constant import Constant
from circuit import Circuit

def build_circuit(data):
    new_circuit = Circuit()
    for instruction in data:
        new_circuit.add_connection(instruction)
    return new_circuit

def test():
    test_circuit = build_circuit(parse_input(example=True, function=lambda data:[x for x in fields(data) if x != '->']))
    results1 = test_circuit.wires
    for (key, expected) in parse_input(example=True, test_case='expected', function=fields):
        print(f"Wire {key} = {results1[key].value}, expected: {expected}. Correct = {results1[key].value == int(expected)}")
    
def main():
    data = parse_input(function=lambda data:[x for x in fields(data) if x != '->'])
    part1_circuit = build_circuit(data)
    a_value = part1_circuit.get_value('a')
    print(f"Part 1 result: {a_value}")
    part1_circuit.add_connection((a_value,'b'))
    part1_circuit.reset()
    new_a_value = part1_circuit.get_value('a')
    print(f"Part 1 result: {new_a_value}")

    
if __name__ == '__main__':
    # test()
    main()