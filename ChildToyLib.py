import maya.cmds as cmds

class ChildToy():
    def __init__(self):
        self.size = 5
        self.hole = 4
        self.holes_per_col = 2
        self.holes_per_row = 3

    def mkCube(self):
        """ Makes Cube """
        # creates cube based on selected size
        self.ShapeSortingCube = cmds.polyCube(depth=self.size, height=self.size, 
                                         width=self.size)
        # renames cube to toy name
        cmds.rename('ShapeSortingCube')
        # move Y axis to origin
        cmds.move(0, self.size/2, 0)

    def mkShapes(self):
        """ Makes Block Shapes """
        pass

    def mkHoles(self):
        """ Makes Hole Shapes in Cube """
        # create subdivision based on hole number
        # different procedures if holes isnt even per side
        number_of_holes = self.is_odd(self.hole)
        if number_of_holes == True:
            pass
            # TODO: implement odd numbers
        if number_of_holes == False:
            # for 2, 4, 6
            # max 6
            # ex 6: 3x2
            self.holes_per_col = 2
            self.holes_per_row = self.hole/2
        cmds.setAttr("polyCube1.subdivisionsWidth", self.holes_per_col)
        cmds.setAttr("polyCube1.subdivisionsHeight", self.holes_per_row)
        cmds.setAttr("polyCube1.subdivisionsDepth", self.holes_per_col)

    def mkLid(self):
        """ Makes Lid of Cube """
        # create lid
        pass
    
    def is_odd(self, num):
        if num//2 != 0:
            # num is odd
            return True
        else:
            # num is even
            return False
        
    def build(self):
        self.mkCube()
        self.mkHolePlacements()
        self.mkHoles()



# Prototype
    # Child's blocks toy
# change name
# width, length, height
# number of holes
# hole size
# hole shape
# block colors, toy color
# lid location

# make cube
# make blocks
# make lid


if __name__ == "__main__":
    toy1 = ChildToy()
    toy1.build()
    
