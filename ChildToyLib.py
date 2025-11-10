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
        # TODO:
        # make holes
        # make con
        # make UI
        # figure out color
        # fix random generation

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
        box = cmds.polyCube(depth=self.size, height=self.size, 
                                         width=self.size)
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
        cmds.rename('ShapeSortingCubeLid')
        # move Y axis to origin
        cmds.move(0, self.size+(self.size/20), 0)
        # freeze transformations
        cmds.makeIdentity(apply=True)
        return lid
    
    def movePlanesToOneSide(self, shape_name, idx):
        ''' Move Planes '''
        # how to determine where to place plane based on # of holes
        x_pos = self.getHoleNumX(idx)
        y_pos = self.getHoleNumY(idx)
        cmds.move(x_pos, y_pos, self.size/2, shape_name[0])
        cmds.rotate(90, 0, 0, shape_name[0], relative=True)
        return shape_name

    def getholeXpos(self, idx):
        # determines x_pos based on odd/even
        hole_num = self.isOdd(idx)
        if hole_num == True:
            x_pos = self.size/4
        else:
            x_pos = (self.size/4)*-1
        return x_pos

    def getHoleNumX(self, idx):
        # hole in center if only one
        if self.hole == 1:
            x_pos = 0
        else:
            x_pos = self.getholeXpos(idx)
        return x_pos        
    
    def getHoleNumY(self, idx):
        if self.hole == 1:
            y_pos = self.size/2
        else:
            y_pos = self.getHoleYPos(idx)
        return y_pos
    
    def getHoleYPos(self, idx):
        y_pos = self.size/4
        for i in range(1, (self.hole*4)+1, self.hole):
            if i == idx:
                y_pos = (self.size/2)+(self.size/4)
        for i in range(2, (self.hole*4)+1, self.hole):
            if i == idx:
                y_pos = (self.size/2)+(self.size/4)
        return y_pos
        
    def rotatePlanestoWholeBox(self, shape_name, idx):
        if idx > self.hole:
            cmds.move(0, 0, 0, f'{shape_name[0]}.scalePivot')
            cmds.move(0, 0, 0, f'{shape_name[0]}.rotatePivot')
            cmds.select(shape_name[0])
            cmds.makeIdentity(apply=True)
            if idx <= self.hole*2:
                cmds.rotate(90, rotateY=True, relative=True)
            elif idx <= self.hole*3:
                cmds.rotate(180, rotateY=True, relative=True)
            else:
                cmds.rotate(270, rotateY=True, relative=True)
        return shape_name

    def convertsPlaneToBlock(self, shape_name):
        """ Make Plane Into Block"""
        '''DONE'''
        cmds.select(f"{shape_name[0]}.f[0:]", replace=True)
        shape_block = cmds.duplicate(shape_name[0], name='block1')
        cmds.select(f"{shape_block[0]}.f[0:]", replace=True)
        cmds.polyExtrudeFacet(thickness=self.size/2)
        cmds.select({shape_block[0]})
        cmds.rotate(90, 0, 0)
        return shape_block
    
    def mergePlanesToBox(self):
        all_objects = cmds.ls(dag=True, long=False, type='transform')
        objects = []
        for obj in all_objects:
            if 'plane' in obj.lower():
                objects.append(obj)
        for obj in objects:
            box = cmds.polyUnite(obj, 'ShapeSortingCube', name='box')
            cmds.delete(box, ch=True)
        cmds.select(box[0], replace=True)
        cmds.rename('ShapeSortingCube')

    def mkHoles(self):
        # faces = 4 + self.hole*4
        pass
    
    def moveBlock(self, shape_block, shape_height):
        """ Move Block Around Grid """
        '''DONE'''
        # variables
        # TODO: fix repeat locations
        x_pos = self.getXChanceLocation()
        z_pos = self.getZChanceLocation(x_pos)
        x_pos = self.applyChanceLocationToGrid(x_pos)
        z_pos = self.applyChanceLocationToGrid(z_pos)
        cmds.select(shape_block)
        # move block random xy
        cmds.move(x_pos, shape_height/2, z_pos, rotatePivotRelative=True)
        # freeze transforms
        cmds.makeIdentity(apply=True)
        return shape_block
    
    def mkSquarePlane(self):
        """ Makes Rectangle Shapes """
        ''' DONE '''
        square_plane = cmds.polyPlane(name='squarePlane1', 
                        subdivisionsHeight=1, subdivisionsWidth=1,
                        width=self.shape_size, height=self.shape_size)
        return square_plane
    
    def mkRectanglePlane(self):
        """ Makes Rectangle Shapes """
        '''DONE'''
        rectangle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        return rectangle_plane
    
    def mkCloverPlane(self):
        """ Makes Clover Shapes """
        '''DONE'''
        clover_plane = cmds.polyDisc(subdivisions=1, sides=10)
        cmds.rotate(0, -18, 0, relative=True)
        cmds.select(f"{clover_plane[0]}.vtx[1]", add=True, replace=True)
        cmds.select(f"{clover_plane[0]}.vtx[3]", add=True)
        cmds.select(f"{clover_plane[0]}.vtx[5]", add=True)
        cmds.select(f"{clover_plane[0]}.vtx[7]", add=True)
        cmds.select(f"{clover_plane[0]}.vtx[9]", add=True)
        cmds.scale(.55, .55, .55, relative=True)
        cmds.select(clover_plane[0], replace=True)
        cmds.rename('cloverPlane1')
        cmds.scale(self.hole/self.size, self.hole/self.size, 
                   self.hole/self.size, relative=True)
        return clover_plane
    
    def mkStarPlane(self):
        """ Makes Star Shapes """
        '''DONE'''
        star_plane = cmds.polyDisc(subdivisions=0, sides=10)
        cmds.rotate(0, -18, 0, relative=True)
        cmds.select(f"{star_plane[0]}.vtx[1]", add=True, replace=True)
        cmds.select(f"{star_plane[0]}.vtx[3]", add=True)
        cmds.select(f"{star_plane[0]}.vtx[5]", add=True)
        cmds.select(f"{star_plane[0]}.vtx[7]", add=True)
        cmds.select(f"{star_plane[0]}.vtx[9]", add=True)
        cmds.scale(.55, .55, .55, relative=True)
        cmds.select(star_plane[0], replace=True)
        cmds.rename('starPlane1')
        scale = (self.hole/self.size)+(self.size/(100))
        cmds.scale(scale, scale, scale, relative=True)
        return star_plane
        
    def mkCirclePlane(self):
        """ Makes Circle Shapes """
        '''DONE'''
        circle_plane = cmds.polyPlane(name='circlePlane1', 
                        subdivisionsHeight=6, subdivisionsWidth=6,
                        height=self.shape_size, width=self.shape_size)
        cmds.polyCircularize(constructionHistory=True)
        return circle_plane
        
    def mkHeartPlane(self):
        """ Makes Heart Shapes """
        ''' DONE '''
        heart_plane = cmds.polyPlane(name='heartPlane1', 
                                   subdivisionsHeight=2, subdivisionsWidth=2)
        cmds.select(f'{heart_plane[0]}.vtx[7]', replace=True)
        cmds.scale(1, 1, .4, relative=True)
        cmds.scale(self.shape_area, 0, (self.hole/self.size)+(self.size/(100)))
        cmds.select(f'{heart_plane[0]}.vtx[0]', replace=True)
        cmds.select(f'{heart_plane[0]}.vtx[2]', add=True)
        cmds.scale(.6, 1, .4, relative=True)
        cmds.select(heart_plane[0], replace=True)
        cmds.scale(self.shape_size, self.shape_size, (self.shape_size) +
                   (self.size/(100)))
        return heart_plane
        
    def mkTriangleplane(self):
        """ Makes Triangle Shapes """
        '''DONE'''
        triangle_plane = cmds.polyDisc(subdivisions=0,
                        radius=self.hole/self.size)
        cmds.setAttr(f'{triangle_plane[1]}.heightBaseline', .25)
        cmds.rename('trianglePlane1')
        return triangle_plane
        
    def mkPentagonplane(self):
        """ Makes Pentagon Shapes """
        '''DONE'''
        pentagon_plane = cmds.polyDisc(sides=5, subdivisions=0, 
                        radius=self.hole/self.size)
        cmds.setAttr(f'{pentagon_plane[1]}.heightBaseline', .1)
        cmds.rename('pentagonPlane1')
        return pentagon_plane
        
    def mkTrapazoidPlane(self):
        """ Makes Trapazoid Shapes """
        ''' DONE '''
        trapazoid_plane = cmds.polyPlane(name='trapazoidPlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        cmds.scale(self.shape_area, 0, (self.shape_area)/2)
        cmds.select(f"{trapazoid_plane[0]}.e[3]", replace=True)
        cmds.scale(.8, 1, 1, relative=True)
        return trapazoid_plane
        
    def getXChanceLocation(self):
        """ Picks Random Location"""
        '''DONE'''
        stop = int((self.size*3)-1)
        # +1 since randrange only takes integer
        step = int((self.size/2)+1)
        random_x_space = random.randrange(0, stop, step)
        return random_x_space
    
    def getZChanceLocation(self, x_pos):
        """ Picks Random Location"""
        '''DONE'''
        stop = int((self.size*3)-1)
        # +1 since randrange only takes integer
        step = int((self.size/2)+1)
        if x_pos < self.size:
            start = int(self.size)
            random_z_space = random.randrange(start, stop, step)
            return random_z_space
        else:
            random_z_space = random.randrange(0, stop, step)
            return random_z_space
    
    def applyChanceLocationToGrid(self, pos):
        '''DONE'''
        chance = random.random()
        if chance <= .5:
            # neg grid
            pos = pos*(-1)
            return pos
        else:
            # positve grid
            return pos

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
        '''DONE'''
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
        cmds.select(f'{shape_block[0]}.scalePivot', replace=True)
        cmds.select(f'{shape_block[0]}.rotatePivot', add=True)
        cmds.move(0, 0, self.size/4)


    def editShapePivotRigSnap(self, shape_name):
        ''' Edits Object Pivot for Rig'''
        # TODO: implement feature
        # TODO: decide how pivot works
            # center pivot?
            # pivot on bottom -> snap into hole

    def editLidPivot(self):
        ''' Edits Lid Pivot'''
        '''DONE'''
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
        '''DONE'''
        self.mkCube()
        self.mkLid()
        self.editLidPivot()
        self.mkFloor()

    # TODO: move planes to align w/ box
    # TODO: turn planes into holes on box
    # TODO: rename holes

            
    def build(self):
        self.mkNonShapes()
        for idx in range(1, (self.hole*4)+1):
            # make random plane shape for hole
            # TODO: implement random
            shape_name = self.mkRectanglePlane()
            shape_block = self.convertsPlaneToBlock(shape_name)
            shape_height = self.getShapeHeight(shape_name)
            self.editShapePivotCenter(shape_block)
            self.moveBlock(shape_block, shape_height)
            self.movePlanesToOneSide(shape_name, idx)
            self.rotatePlanestoWholeBox(shape_name, idx)
            self.mergePlanesToBox()
            # TODO make planes into holes on toy function
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
    
