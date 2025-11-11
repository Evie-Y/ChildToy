# ChildToy
<<<<<<<
# Creating a procedural child shape sorting toy in Maya

Creates a primitive cube shape based on the input dimensions given.
Creates a lid on the desired side of the box.
Creates unique hole shapes based on the desired input number.
    Specific Shapes and holes per side can be inputted.
Creates toy blocks to match holes.
    Scatters across map based on inputs (extra)
All shapes rigged.
    Custom colors for lid, cube, and blocks respectively.

# Inputs
=======
## Creating a procedural child shape sorting toy in Maya

### Goals
- Creates a primitive cube shape based on the input dimensions given.
- Creates a lid on the desired side of the cube.
- Creates unique hole shapes based on the desired input number.
*Specific shapes and holes per side can be inputted.*
- Creates toy blocks to match holes.
*Scatters across map based on inputs.*
- All shapes rigged.
*Custom colors for lid, cube, and blocks respectively.*

### Inputs
- Cube Size
- Lid Location
- Holes per side
- Shape specifications
- Color
- Block Location

## TODO:
- Create Primitives
  - ~Cube~ 
  - ~Lid~
  - ~Floor~
  - Blocks
    - ~Rectangle~
    - Star
    - Circle
    - Heart
    - Triangle
    - Trapazoid
    - Semi-Oval *(extra)*
    - Pentagon *(extra)*
    - Clover *(extra)*
    - Diamond *(extra)*
  - Holes
    - Rectangle
    - Star
    - Circle
    - Heart
    - Triangle
    - Trapazoid
    - Semi-Oval *(extra)*
    - Pentagon *(extra)*
    - Clover *(extra)*
    - Diamond *(extra)*

- Rigging
  - Cube
    - Has a control
    - Unique color
  - Lid
  - Has a control
    - Pivot edited so control works
    - Arrow control
    - Unique color
  - Blocks
    - Has a control
    - Pivot edited
      - when vertex aligned with hole, slots in

- Features
    - Make Holes
    - ~Make Lid on cube~
      - Lid can be placed on any side of cube (except bottom)
    - allows user to edit cube size
    - code accommodates (different holes per side) inputs
    - holes appear as different shapes
      - allows user to specify certain shapes 
    - ~1:1 ratio of block shapes to hole shapes~
    - object are generated w/ colors
      - gives user option to color blocks/cube/floor/lid/rig controls
    - ~move blocks across floor~
      - allows user to specify where blocks can be laid
    - randomize option **(extra)**
>>>>>>> 49991559bcd067fc08fc1cd326093fd5653941d4
