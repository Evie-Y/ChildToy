import maya.cmds as cmds

class ChildToy():
    def __init__(self):
        self.size = 5
        self.hole = 4
        pass

    def mkCube(self):
        """ Makes Cube """
        # creates cube based on selected size
        ShapeSortingCube = cmds.polyCube(depth=self.size, height=self.size, width=self.size)
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
        cmds.setAttr("polyCube1.subdivisionsWidth", 2)
        cmds.setAttr("polyCube1.subdivisionsWidth", 2)
        cmds.setAttr("polyCube1.subdivisionsWidth", 2)
        pass

    def mkLid(self):
        """ Makes Lid of Cube """
        # create lid
        pass

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
    main()