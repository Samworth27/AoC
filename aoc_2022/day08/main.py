from util.inputs import parse_input
from visibility_grid import VisGrid
from visualisation import create_visualisation

    

def record():
    grid = VisGrid(parse_input(example=True),(100,5,20))
    grid.start_recording(record_video=False)
    grid.record_state()
    grid.count_visible()
    grid.stop_recording()
    

def main():
    grid = VisGrid(parse_input())
    print(f"Part 1: result = {grid.count_visible()}, expected value: 1840")
    print(f"Part 2: result = {grid.highest_vis_score()}, expected value: 405769")
    
if __name__ == '__main__':
    # main()
    record()