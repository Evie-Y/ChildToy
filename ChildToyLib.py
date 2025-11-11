from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

import maya.cmds as cmds
import random

def get_maya_main_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)

class ToyGenWin(QtWidgets.QDialog):
    '''Child Toy Window Class'''

    def __init__(self):
        # runs the init code of the parent QDialog class
        super().__init__(parent=get_maya_main_win())
        self.toyGen = ChildToy()
        self.setWindowTitle("Child Toy Generator")
        self.resize(250, 500)
        self._mk_main_layout()
        self._connect_signals()

    def _connect_signals(self):
        self.cancel_btn.clicked.connect(self.cancel)
        self.build_btn.clicked.connect(self.build)
        
    def cancel(self):
        self.close()

    @QtCore.Slot()
    def build(self):
        self._update_toyGen_properties()
        self.toyGen.build()

    def _update_toyGen_properties(self):
        self.toyGen.__init__()  # reset properties to default
        self.toyGen.hole = self.hole_spnbx.value()
        print(self.toyGen.holes)
        self.toyGen.size = self.size_spnbx.value()
        print(self.toyGen.box)

    def _mk_main_layout(self):
        # Create vertical box layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self._add_form_layout()
        self._enable_simple_shapes()
        self._enable_complex_shapes()
        self._mk_btn_layout()
        # Set Dialog window to use main layout
        self.setLayout(self.main_layout)

    def _add_form_layout(self):
        self.form_layout = QtWidgets.QFormLayout()
        self._add_size()
        self._add_holes()
        self._add_color_box()
        self._add_color_blocks()
        self.main_layout.addLayout(self.form_layout)

    def _add_size(self):
        self.size_spnbx = QtWidgets.QSpinBox()
        self.size_spnbx.setValue(5)
        self.size_spnbx.setMaximum(50)
        self.size_spnbx.setMinimum(1)
        self.form_layout.addRow('Size: ', self.size_spnbx)

    def _add_holes(self):
        self.hole_spnbx = QtWidgets.QSpinBox()
        self.hole_spnbx.setValue(4)
        self.hole_spnbx.setMaximum(4)
        self.hole_spnbx.setMinimum(1)
        self.form_layout.addRow('Holes: ', self.hole_spnbx)
    
    def _add_color_box(self):
        self.color_cldlg = QtWidgets.QColorDialog()
        self.form_layout.addRow('Box Color: ', self.color_cldlg)

    def _add_color_blocks(self):
        self.color_blocks_cldlg = QtWidgets.QColorDialog()
        self.form_layout.addRow('Blocks Color: ', self.color_blocks_cldlg)

    def _enable_simple_shapes(self):
        self.sshp_layout = QtWidgets.QHBoxLayout()
        self.enable_rect_cb = QtWidgets.QCheckBox('Rectangle')
        self.enable_sqr_cb = QtWidgets.QCheckBox('Square')
        self.enable_crcl_cb = QtWidgets.QCheckBox('Circle')
        self.enable_tri_cb = QtWidgets.QCheckBox('Triangle')
        self.sshp_layout.addWidget(self.enable_rect_cb)
        self.sshp_layout.addWidget(self.enable_sqr_cb)
        self.sshp_layout.addWidget(self.enable_crcl_cb)
        self.sshp_layout.addWidget(self.enable_tri_cb)
        self.main_layout.addLayout(self.sshp_layout)

    def _enable_complex_shapes(self):
        self.cshp_layout = QtWidgets.QHBoxLayout()
        self.enable_clvr_cb = QtWidgets.QCheckBox('Clover')
        self.enable_str_cb = QtWidgets.QCheckBox('Star')
        self.enable_hrt_cb = QtWidgets.QCheckBox('Heart')
        self.enable_ptgn_cb = QtWidgets.QCheckBox('Pentagon')
        self.enable_trpd_cb = QtWidgets.QCheckBox('Trapazoid')
        self.cshp_layout.addWidget(self.enable_clvr_cb)
        self.cshp_layout.addWidget(self.enable_str_cb)
        self.cshp_layout.addWidget(self.enable_hrt_cb)
        self.cshp_layout.addWidget(self.enable_ptgn_cb)
        self.cshp_layout.addWidget(self.enable_trpd_cb)
        self.main_layout.addLayout(self.cshp_layout)

    def _mk_btn_layout(self):
        self.btn_layout = QtWidgets.QHBoxLayout()
        # Create 'build' button
        self.build_btn = QtWidgets.QPushButton('Build')
        self.random_btn = QtWidgets.QPushButton('Randomize')
        self.cancel_btn = QtWidgets.QPushButton('Cancel')
        # Add the build button to first row
        self.btn_layout.addWidget(self.build_btn)
        self.btn_layout.addWidget(self.random_btn)
        self.btn_layout.addWidget(self.cancel_btn)
        self.main_layout.addLayout(self.btn_layout)

class ChildToy():
    def __init__(self):
        self.box_color = [0, 0, 100]
        self.block_color = [0, 0, 255]
        self.size = 6
        self.hole = 3
        self.shape_size = (self.size/self.hole)
        if self.shape_size >= self.size:
            self.shape_size = (self.size/self.hole)-(self.size*.25)
        self.shape_area = self.shape_size*1.1
        # TODO:
        # make UI (5 buttons)
        # figure out color (diff funct for box, lid, blocks, no floor)
        # make list of shapes to randomize
        # get rid of rig, make blcoks dif colors

        # self.size
        # self.hole
        # pick hole/block shape
        # pick block color(s)
        # pick block/lid/plane color

    def assignBoxColor(self):
        ''' Give Box and Lid Colors '''
        all_objects = cmds.ls(dag=True, long=False, type='transform')
        box = []
        for obj in all_objects:
            if 'ShapeSortingCube' in obj.lower():
                box.append(obj)
        for obj in box:
            cmds.connectAttr(force=True)
            shader = cmds.createNode('standardSurface', asShader=True, name=
                            'box_material')
        pass
    

    def assignBlocksColors(self):
        ''' Give Blocks Colors'''

    def mkFloor(self):
        """ Makes Floor"""
        # edit name & subdivisions
        floor = cmds.polyPlane(name='Floor',
                            subdivisionsHeight=1, subdivisionsWidth=1)
        # scale x,y,z
        cmds.scale(self.size * 6, 0, self.size * 6)
        return floor

    def mkCube(self):
        """ Makes Cube """
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
        if self.hole <= 2:
            x_pos = 0
        else:
            x_pos = self.getholeXpos(idx)
        return x_pos        
    
    def getHoleNumY(self, idx):
        if self.hole == 1:
            y_pos = self.size/2
        if self.hole == 2:
            y_pos = self.getHoleYPosForTwo(idx)
        else:
            y_pos = self.getHoleYPos(idx)
        return y_pos
    
    def getHoleYPosForTwo(self, idx):
        odd = self.isOdd(idx)
        if odd == True:
            y_pos = self.size/4
        else:
            y_pos = (self.size/2)+(self.size/4)
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
    
    def moveBlock(self, shape_block, shape_height):
        """ Move Block Around Grid """
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
        square_plane = cmds.polyPlane(name='squarePlane1', 
                        subdivisionsHeight=1, subdivisionsWidth=1,
                        width=self.shape_size, height=self.shape_size)
        return square_plane
    
    def mkRectanglePlane(self):
        """ Makes Rectangle Shapes """
        rectangle_plane = cmds.polyPlane(name='rectanglePlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        cmds.scale(self.shape_area, 0, (self.shape_area)/3)
        return rectangle_plane
    
    def mkCloverPlane(self):
        """ Makes Clover Shapes """
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
        circle_plane = cmds.polyPlane(name='circlePlane1', 
                        subdivisionsHeight=6, subdivisionsWidth=6,
                        height=self.shape_size, width=self.shape_size)
        cmds.polyCircularize(constructionHistory=True)
        return circle_plane
        
    def mkHeartPlane(self):
        """ Makes Heart Shapes """
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
        triangle_plane = cmds.polyDisc(subdivisions=0,
                        radius=self.hole/self.size)
        cmds.setAttr(f'{triangle_plane[1]}.heightBaseline', .25)
        cmds.rename('trianglePlane1')
        return triangle_plane
        
    def mkPentagonplane(self):
        """ Makes Pentagon Shapes """
        pentagon_plane = cmds.polyDisc(sides=5, subdivisions=0, 
                        radius=self.hole/self.size)
        cmds.setAttr(f'{pentagon_plane[1]}.heightBaseline', .1)
        cmds.rename('pentagonPlane1')
        return pentagon_plane
        
    def mkTrapazoidPlane(self):
        """ Makes Trapazoid Shapes """
        trapazoid_plane = cmds.polyPlane(name='trapazoidPlane1', 
                                   subdivisionsHeight=1, subdivisionsWidth=1)
        cmds.scale(self.shape_area, 0, (self.shape_area)/2)
        cmds.select(f"{trapazoid_plane[0]}.e[3]", replace=True)
        cmds.scale(.8, 1, 1, relative=True)
        return trapazoid_plane
        
    def getXChanceLocation(self):
        """ Picks Random Location"""
        stop = int((self.size*3)-1)
        # +1 since randrange only takes integer
        step = int((self.size/2)+1)
        random_x_space = random.randrange(0, stop, step)
        return random_x_space
    
    def getZChanceLocation(self, x_pos):
        """ Picks Random Location"""
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
        shape_height = cmds.getAttr(f"{shape[0]}.scaleZ")
        return shape_height
    
    def isOdd(self, num):
        if num % 2 == 0:
            return False
        else:
            return True

    def editShapePivotCenter(self, shape_block):
        ''' Edits Object Pivot for Translation'''
        cmds.select(f'{shape_block[0]}.scalePivot', replace=True)
        cmds.select(f'{shape_block[0]}.rotatePivot', add=True)
        cmds.move(0, 0, self.size/4, relative=False)

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
            
    def mkNonShapes(self):
        ''' Make Everything But Shapes'''
        self.mkCube()
        self.mkLid()
        self.editLidPivot()
        self.mkFloor()
  
    def build(self):
        self.mkNonShapes()
        for idx in range(1, (self.hole*4)+1):
            # TODO: implement random
            shape_name = self.mkRectanglePlane()
            shape_block = self.convertsPlaneToBlock(shape_name)
            shape_height = self.getShapeHeight(shape_name)
            self.editShapePivotCenter(shape_block)
            self.moveBlock(shape_block, shape_height)
            self.movePlanesToOneSide(shape_name, idx)
            self.rotatePlanestoWholeBox(shape_name, idx)
            self.mergePlanesToBox()
        self.mkGroup()
        print(self.hole)
        print(self.size)

if __name__ == "__main__":
    toy1 = ChildToy()
    toy1.build()
    
