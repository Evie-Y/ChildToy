import maya.cmds as cmds
from maya import cmds

class ChildToy():
    def __init__(self):
        self.size = 5
        self.hole = 8

    def mkCube(self):
        """ Makes Cube """
        # creates cube based on selected size
        cmds.polyCube(depth=self.size, height=self.size, 
                                         width=self.size)
        # renames cube to toy name
        cmds.rename('ShapeSortingCube')
        # move Y axis to origin
        cmds.move(0, self.size/2, 0)
        # delete wanted face
        cmds.delete('ShapeSortingCube.f[1]')
        # reselect cube
        cmds.select('ShapeSortingCube')

    def mkShapes(self):
        """ Makes Block Shapes """
        # TODO: make cube shapes for holes
        # create plane for number of holes
        cmds.polyPlane(name='shape')
        # edit subdivisions
        # make different shapes
        # each shape own function
            # star
            # rectangle
            # circle
            # star
            # heart
            # wide half circle
            # triangle
            # pentagon?
            # clover?
            # diamond?
        pass
        
    def mkRectanglePlane(self):
        """ Makes Rectangle Shapes """
        # create plane for number of holes
        cmds.polyPlane(name='shape')
        # edit subdivisions
        # make different shapes
        # each shape own function
            # star
            # rectangle
            # circle
            # star
            # heart
            # wide half circle
            # triangle
            # pentagon?
            # clover?
            # diamond?
            
    def mkHoles(self):
        """ Makes Hole Shapes in Cube """
        # create subdivision based on hole number
        # different procedures if holes isnt even per side
        # TODO: implement different solution than current one
        number_of_holes = self.is_odd(self.hole)
        if number_of_holes == True:
            pass
            # TODO: implement odd numbers
        if number_of_holes == False:
            # for 2, 4, 6
            # max 6
            # ex 6: 3x2
            holes_per_col = 2
            holes_per_row = self.hole/2
        cmds.setAttr("polyCube1.subdivisionsHeight", holes_per_col)
        cmds.setAttr("polyCube1.subdivisionsWidth", holes_per_row)
        cmds.setAttr("polyCube1.subdivisionsDepth", holes_per_row)

    def mkLid(self):
        """ Makes Lid of Cube """
        # make lid w/ modified height
        cmds.polyCube(depth=self.size, height=self.size/10, 
                                         width=self.size)
        # renames lid
        cmds.rename('ShapeSortingCubeLid')
        # move Y axis to origin
        cmds.move(0, self.size+(self.size/20), 0)
        # edit pivot?
    
    def is_odd(self, num):
        if num % 2 == 0:
            return False
        else:
            return True
            
    def build(self):
        self.mkCube()
        self.mkLid()
        self.mkShapes()




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
    
