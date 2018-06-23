import bpy, bmesh
bpy.ops.object.mode_set(mode='EDIT')

obj = bpy.context.object

# find max x,y,z

coords = obj.bound_box[:]
rotated = zip(*coords[::-1])

all_axis = []
push_axis = []
for (axis, _list) in zip('xyz', rotated):
    distance = max(_list)-min(_list)
    all_axis.append(distance)
    adjuster_distance = min(_list) + (distance/2)
    push_axis.append(adjuster_distance*-1)

long_side = max(all_axis)



from mathutils import Vector

# center the geometry to origin ( could be lazier)
bm = bmesh.from_edit_mesh(obj.data)

''' Yes this can all be done in a single loop '''

if True:
    for vertex in bm.verts:
        vertex.co.x += push_axis[0]
        vertex.co.y += push_axis[1]
        vertex.co.z += push_axis[2]

    bmesh.update_edit_mesh(obj.data)

# scale the beast.
if True:
    scale = Vector((long_side, 0, 0)).length / 2.0

    for vertex in bm.verts:
        vertex.co = vertex.co/scale

    bmesh.update_edit_mesh(obj.data)

# quantize
if True:
    for vertex in bm.verts:
        vertex.co.x = round(vertex.co.x, 1)
        vertex.co.y = round(vertex.co.y, 1)
        vertex.co.z = round(vertex.co.z, 1)

    bmesh.update_edit_mesh(obj.data)
