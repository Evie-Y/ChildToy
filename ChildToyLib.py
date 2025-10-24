import maya.cmds as cmds
from maya import cmds
import random

class ChildToy():
    def __init__(self):
        self.size = 5
        self.hole = 4
        self.shape_size = self.size/self.hole

    def mkCube(self):
        """ Makes Cube """
        '''DONE'''
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
        # freeze transformations
        cmds.makeIdentity(apply=True)

    def convertsPlaneToBlock(self):
        """ Make Plane Into Block"""
        # turns planes into 3D blocks
        # make different shapes
        # each shape/hole/block own function
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
        # create plane for rectangle
        # edit scale & name
        cmds.polyPlane(name='rectanglePlane1', height=self.shape_size*self.
                       shape_size, width=(self.shape_size*self.shape_size)/3)
        # subdivisions for rectangle
        cmds.setAttr('polyPlane1.subdivisionsHeight', 1)
        cmds.setAttr('polyPlane1.subdivisionsWidth', 1)

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
        '''DONE'''
        # make lid w/ modified height
        cmds.polyCube(depth=self.size, height=self.size/10, 
                                         width=self.size)
        # renames lid
        cmds.rename('ShapeSortingCubeLid')
        # move Y axis to origin
        cmds.move(0, self.size+(self.size/20), 0)
        # edit pivot?
        # freeze transformations
        cmds.makeIdentity(apply=True)
    
    def isOdd(self, num):
        '''DONE'''
        if num % 2 == 0:
            return False
        else:
            return True
        
            
    def build(self):
        # list
        shapes = []
        blocks = []
        self.mkCube()
        self.mkLid()
        self.mkRectanglePlane()
        # example loop
        # for block_num in range(self.hole*4):
            # make random plane shape for hole
            # make corresponding block for hole
        # TODO: how to put planes into list to randomize





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
    
