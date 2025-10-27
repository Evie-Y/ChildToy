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
        self.shape_area = self.shape_size*self.shape_size

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
        cmds.select('ShapeSortingCube.f[1]')
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
        x_pos = self.applyChanceLocationToGrid()
        z_pos = self.applyChanceLocationToGrid()
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
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        return rectangle_plane
    
    def mkStarPlane(self):
        """ Makes Star Shapes """
        # edit name & subdivisions
        star_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        
    def mkCirclePlane(self):
        """ Makes Circle Shapes """
        # edit name & subdivisions
        circle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        
    def mkHeartPlane(self):
        """ Makes Heart Shapes """
        # edit name & subdivisions
        heart_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        # scale x,y,z
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        
    def mkTriangleplane(self):
        """ Makes Triangle Shapes """
        # edit name & subdivisions
        triangle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        
    def mkSemiOvalplane(self):
        """ Makes Semi-Oval Shapes """
        # semi-oval so it doesn't fit in circle hole
        # might delete b/c repetitive
        # edit name & subdivisions
        semi_oval_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        
    def mkTrapazoidPlane(self):
        """ Makes Trapazoid Shapes """
        # edit name & subdivisions
        trapazoid_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        
    def getChanceLocation(self):
        """ Picks Random Location"""
        # pick random int
        # from floor, except area in self.size around origin
        # variables
        # TODO: edit step, stop, start
        # self.shape_area
        stop = int((self.size*3))
        # +1 since randrange only takes integer
        step = int((self.size/2)+1)
        # int((self.size/2)+shapeXscale)
        random_space = random.randrange(0, stop, step)
        return random_space
    
    def applyChanceLocationToGrid(self):
        # apply random_space to entire grid 
        # variables
        random_space = self.getChanceLocation()
        chance = random.random()
        if chance <= .5:
            # neg grid
            random_space = random_space*-1
            return random_space
        else:
            # positve grid
            return random_space

    def mkGroup(self):
        ''' Makes Groups '''
        # select all blocks
        all_blocks = cmds.ls('block*', type='transform')
        # make block grp
        cmds.group(all_blocks, name="blocks_GRP")
        
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

    def editShapePivotCenter(self, shape_block):
        ''' Edits Object Pivot for Translation'''
        # select pivot
        cmds.select(shape_block)
        # centers pivot for translation
        cmds.xform(centerPivots=True)

        # TODO: implement feature
        # TODO: decide how pivot works
            # center pivot?
            # pivot on bottom -> snap into hole

    def editShapePivotRigSnap(self, shape_name):
        ''' Edits Object Pivot for Rig'''
        # TODO: implement feature
        # TODO: decide how pivot works
            # center pivot?
            # pivot on bottom -> snap into hole

    def editLidPivot(self):
        ''' Edits Lid Pivot'''
        # variables
        z_pos = self.size/2
        y_pos = -1*(self.size/20)
        # select Lid
        cmds.select('ShapeSortingCubeLid')
        # move pivot
        cmds.move(0, y_pos, z_pos, 'ShapeSortingCubeLid.scalePivot',
                  'ShapeSortingCubeLid.rotatePivot', relative=True)
        # TODO: implement pivot align when on side
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
        ''' Makes Shape's Rig '''
        # TODO: implement
        # make control simple circle

    def mkNonShapes(self):
        ''' Make Everything But Shapes'''
        self.mkCube()
        self.mkLid()
        self.editLidPivot()
        self.mkFloor()

    # TODO: move planes to align w/ box
    # TODO: turn planes into holes on box
    # TODO: rename holes

            
    def build(self):
        # TODO: edit code to allow multiple instances of build() to work
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
            print(shape_block)
            shape_height = self.getShapeHeight(shape_name)
            self.editShapePivotCenter(shape_block)
            self.moveBlock(shape_block, shape_height)
                # center pivot b4 moveBlock
            # TODO make planes into holes on toy function
            # TOD0: dreeze shape transformations at end
        # TODO: how to put planes into list to randomize
        self.mkGroup()





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
    
