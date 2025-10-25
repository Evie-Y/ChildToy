import maya.cmds as cmds
from maya import cmds
import random

class ChildToy():
    def __init__(self):
        # add more variables for shapes?
        # remeber to delete '''DONE''' when finished
        self.size = 5
        self.hole = 4
        self.shape_size = self.size/self.hole

    def mkFloor(self):
        """ Makes Floor"""
        '''DONE'''
        # edit name & subdivisions
        floor = cmds.polyPlane(name='Floor',
                            subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.size * 6, 0, self.size * 6)
        return floor

    def mkCube(self):
        """ Makes Cube """
        '''DONE'''
        # creates cube based on selected size
        box = cmds.polyCube(depth=self.size, height=self.size, 
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
        return box
    
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

    def convertsPlaneToBlock(self, shape_name):
        """ Make Plane Into Block"""
            # pentagon?
            # clover?
            # diamond?
        # TODO: implement select random plane
            # for now, select rectangle for testing
        # select corresponding plane shape
        cmds.select(f"{shape_name[0]}.f[0:]", replace=True)
        shape_block = cmds.duplicate(shape_name[0], name='block1')
        cmds.select(f"{shape_block[0]}.f[0:]", replace=True)
        # extrude
        cmds.polyExtrudeFacet(thickness=self.size/2)
        # rotate block 90 degrees
        cmds.select({shape_block[0]})
        cmds.rotate(90, 0, 0)
        return shape_block

    def moveBlock(self, shape_block, shape_height):
        """ Move Block Around Grid """
        # variables
        x_pos = self.getXChanceLocation()
        z_pos = self.getZChanceLocation()
        # select block
        cmds.select(shape_block)
        # move block random xy
        # TODO: chance y per shape type
        cmds.move(x_pos, shape_height/2, z_pos)
        # freeze transformations
        # cmds.makeIdentity(apply=True)
        return shape_block
        
    def mkRectanglePlane(self):
        """ Makes Rectangle Shapes """
        '''DONE'''
        # edit name & subdivisions
        rectangle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
        return rectangle_plane
    
    def mkStarPlane(self):
        """ Makes Star Shapes """
        # edit name & subdivisions
        star_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
        
    def mkCirclePlane(self):
        """ Makes Circle Shapes """
        # edit name & subdivisions
        circle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
        
    def mkHeartPlane(self):
        """ Makes Heart Shapes """
        # edit name & subdivisions
        heart_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
        
    def mkTriangleplane(self):
        """ Makes Triangle Shapes """
        # edit name & subdivisions
        triangle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
        
    def mkSemiOvalplane(self):
        """ Makes Semi-Oval Shapes """
        # semi-oval so it doesn't fit in circle hole
        # might delete b/c repetitive
        # edit name & subdivisions
        semi_oval_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
        
    def mkTrapazoidPlane(self):
        """ Makes Trapazoid Shapes """
        # edit name & subdivisions
        trapazoid_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_size*self.shape_size, 0, (self.shape_size *
                                                        self.shape_size)/3)
    
    def getXChanceLocation(self):
        """ Picks Random Location"""
        # pick random int
        # from (floor end- shape thickness) to cube perimeter
        shape_length = int(self.size/2)
        if random.random() > .5:
            random_x_space = random.randrange(self.size,
                            (self.size * 3)-shape_length, shape_length)
            return random_x_space
        else:
            random_x_space = random.randrange((-1*((self.size * 3)
                            - shape_length)),(-1*self.size), shape_length)
            return random_x_space
        
    def getZChanceLocation(self):
        """ Picks Random Location"""
        # pick random int
        # from (floor end- shape thickness) to cube perimeter
        #
        shape_width = int(self.shape_size*self.shape_size)
        if random.random() > .5:
            random_z_space = random.randrange(self.size,
                                            (self.size * 3)-shape_width, 3)
            return random_z_space
        else:
            random_z_space = random.randrange((-1*((self.size * 3)-shape_width)),
                                            (-1*self.size), 3)
            return random_z_space
        
    def mkGroup(self):
        ''' Makes Group '''
        # TODO: make group
        
    def getRandomShape(self):
        ''' Picks Random Shape'''
        # TODO: implement random shape pick

    def getShapeHeight(self, shape):
        ''' Get Shape Height'''
        shape_height = cmds.getAttr(f"{shape[0]}.scaleZ")
        return shape_height
    
    def isOdd(self, num):
        # might delete funct late if not useful
        '''DONE'''
        if num % 2 == 0:
            return False
        else:
            return True
        
    def addSuffix(self):
        ''' Adds Suffix/Correct Name Conventions'''
        # eventually rename blocks to have _block suffix
        # rename plane to _hole suffix
        # rename grps w/ _GRP
        pass

    def mkNewName(self):
        ''' Makes New Name '''
        # TODO: make names
        # name for master group
        # name for shapes group
        # name for blocks group
        # name for non-shapes group

    def editShapePivot(self):
        ''' Edits Object Pivot'''
        # TODO: implement feature
        # TODO: decide how pivot works
            # center pivot?
            # pivot on bottom -> snap into hole

    def editLidPivot(self):
        ''' Edits Lid Pivot'''
        # TODO: implement
        # put pivot on bottom-back-center,
        # so rig works correctly
            
    def mkLidRig(self):
        ''' Makes Lid Rig '''
        # TODO: make curve, edit curv, parent/constraint
        # make control an arrow?

    def mkCubeRig(self):
        ''' Makes Cube Rig '''
        # TODO: implement
        # make control circle/square
        # different collor?

    def mkShapeRig(self):
        ''' Makes SHape's Rig '''
        # TODO: implement
        # make control simple circle

    def mkNonShapes(self):
        ''' Make Everything But Shapes'''
        self.mkCube()
        self.mkLid()
        self.mkFloor()

    # TODO: move planes to align w/ box
    # TODO: turn planes into holes on box
    # TODO: rename holes

            
    def build(self):
        # list
        # TODO: make shape randomizer w/ lists
        # TODO: group lists
        shapes = []
        blocks = []
        # makes non-shapes
        self.mkNonShapes()
        # example loop
        for idx in range(self.hole*4):
            # make random plane shape for hole
            # TODO: implement random
            shape_name = self.mkRectanglePlane()
            # adds to list
            shapes.append(shape_name)
            # make corresponding block for hole
            shape_block = self.convertsPlaneToBlock(shape_name)
            # adds to list
            blocks.append(shape_block)
            shape_height = self.getShapeHeight(shape_name)
            self.moveBlock(shape_block, shape_height)
                # center pivot b4 moveBlock
            # TODO make planes into holes on toy function
            # TOD0: dreeze shape transformations at end
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
    
