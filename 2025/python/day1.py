# AdventOfCode 2025 Day 1
import sys

input_test = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

class Dial():
    @staticmethod
    def left(num, distance):
        return (num + distance) % 100
    
    @staticmethod
    def right(num, distance):
        return (num - distance) % 100

    def __init__(self, start=50):
        self.number = start
        
        print(f"\t- The dial starts by pointing at {start}")

    def rotate(self, rotation):
        assert isinstance(rotation, str)
        assert len(rotation) >= 2         # min rotaion is direction + distance 
        
        direction = rotation[0]
        try: 
            distance = int(rotation[1:])
        except ValueError:
            print(f"{rotation[1:]} is not integer")
            return None

        match direction:
            case 'L':
               number =  (self.number - distance) % 100
            case 'R':
               number =  (self.number + distance) % 100
            case '_':
                print(f"{direction} is invalid direction")
                return None

        print(f"\t- The dial is rotated {rotation[:-1]} to point at {number}.")
        return number

    def get_passward(self, document_path):
        num_of_zero = 0
        
        with open(document_path, 'r') as f:
            for rotation in f.readlines():
                if len(rotation) == 0: continue

                number = self.rotate(rotation)
                if number is None:
                    print("Error.")
                    return
                
                if number == 0:
                    num_of_zero += 1
                self.number = number

        print(f"The password is: {num_of_zero}")
        return


if __name__ == "__main__":
    document_path = sys.argv[1]

    dial = Dial()
    dial.get_passward(document_path)


