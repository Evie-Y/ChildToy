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
        box = cmds.polyCube(depth=self.size, height=self.size, 
                                         width=self.size)
        print(box)
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
        return box

    def convertsPlaneToBlock(self, shape_name):
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
        # select corresponding plane shape
        # TODO: implement select random plane
            # for now, select rectangle for testing
        cmds.select(f"{shape_name[0]}.f[0:]", replace=True)
        shape_block = cmds.duplicate(shape_name, name='block1')
        cmds.select(f"{shape_block[0]}.f[0:]", replace=True)
        # extrude
        cmds.polyExtrudeFacet(thickness=self.size/2)
        # rotate block 90 degrees
        cmds.select({shape_block[0]})
        cmds.rotate(90, 0, 0)
        # freeze transformations
        cmds.makeIdentity(apply=True)
        return shape_block

    def moveBlock(shape_block):
        # move block to random place from end of grid to toy
        # TODO: implement random 12, self.size
        
        
    def mkRectanglePlane(self):
        """ Makes Rectangle Shapes """
        '''DONE'''
        # edit name & subdivisions
        rectangle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale it
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
        return rectangle_plane

    def mkLid(self):
        """ Makes Lid of Cube """
        '''DONE'''
        # make lid w/ modified height
        lid =cmds.polyCube(depth=self.size, height=self.size/10, 
                                         width=self.size)
        # renames lid
        cmds.rename('ShapeSortingCubeLid')
        # move Y axis to origin
        cmds.move(0, self.size+(self.size/20), 0)
        # edit pivot?
        # freeze transformations
        cmds.makeIdentity(apply=True)
        return lid
    
    def isOdd(self, num):
        '''DONE'''
        if num % 2 == 0:
            return False
        else:
            return True
        
    def rename(self):
        # eventually rename blocks to have _block suffix
        # rename plane to hole suffix
        pass
            
    def build(self):
        # list
        # TODO: make shape randomizer w/ lists
        shapes = []
        # might delete later if unused vvv
        blocks = []
        self.mkCube()
        self.mkLid()
        # example loop
        for idx in range(self.hole*4):
            # make random plane shape for hole
            shape_name = self.mkRectanglePlane()
            # adds to list
            shapes.append(shape_name)
            # make corresponding block for hole
            shape_block = self.convertsPlaneToBlock(shape_name)
            # adds to list
            blocks.append(shape_block)
            self.moveBlock(shape_block)
            # TODO make planes into holes on toy function
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

# is there a thing as too much squedocode, probably


if __name__ == "__main__":
    toy1 = ChildToy()
    toy1.build()
    
