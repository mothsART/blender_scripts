import bpy
from mathutils import Vector


listOfVectors = [((0,0,0,1)),((1,0,0,1)),((2,0,0,1)),((2,3,0,1)),((0,2,0,1))]

# create a spline curve from a number of points
def MakePolyLine(objname, curvename, cList):
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')
    curvedata.dimensions = '2D'

    objectdata = bpy.data.objects.new(objname, curvedata)
    objectdata.location = (0,0,0) #object origin
    bpy.context.scene.objects.link(objectdata)

    polyline = curvedata.splines.new('POLY')
    polyline.points.add(len(cList)-1)

    for num in range(len(cList)):
        polyline.points[num].co = (cList[num])

    polyline.order_u = len(polyline.points)-1
    polyline.use_endpoint_u = True
    polyline.use_cyclic_u = True

MakePolyLine("NameOfMyCurveObject", "NameOfMyCurve", listOfVectors)
