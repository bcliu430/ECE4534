coordinatex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
coordinatey = [0, 1, 2, 3, 4, 5]
 
class Coor:
    def conversion(self, coor):
        return [coordinatex.index(coor[0]), coordinatey.index(coor[1])]

    def getNewCoor(self, coor, d):
##        coor = self.conversion(coor)
        if (d == 'N'):
            coor[1] = coor[1] - 1;
        elif (d == 'S'):
            coor[1] = coor[1] + 1;
        elif (d == 'W'):
            coor[0] = coor[0] - 1;
        elif (d == 'E'):
            coor[0] = coor[0] + 1;
        else:
            pass
        return [coordinatex[coor[0]], coordinatey[coor[1]]]    

    def get_new_dir(self, direction, user_in):
        if direction == 'N':
            if user_in == 'F': ## forward
                return 'N'
            elif user_in == 'L': ## left 
                return 'W'
            elif user_in == 'R': ## right 
                return 'E'

        elif direction == 'S':
            if user_in == 'F': ## forward
                return 'S'
            elif user_in == 'L': ## left 
                return 'E'
            elif user_in == 'R': ## right 
                return 'W'

        elif direction == 'W':
            if user_in == 'F': ## forward
                return 'W'
            elif user_in == 'L': ## left 
                return 'S'
            elif user_in == 'R': ## right 
                return 'N'

        elif direction == 'E':
            if user_in == 'F': ## forward
                return 'E'
            elif user_in == 'L': ## left 
                return 'N'
            elif user_in == 'R': ## right 
                return 'S'





