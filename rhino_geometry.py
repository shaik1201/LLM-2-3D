import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

# Create a point at coordinates (0, 0, 0)
point = rg.Point3d(0, 0, 0)

# Create a line from (0, 0, 0) to (10, 0, 0)
line = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(10, 0, 0))

# Create a circle with center (5, 5, 0) and radius 3
circle_center = rg.Point3d(5, 5, 0)
circle_radius = 3

# Create a sphere with center (0, 0, 0) and radius 5
# sphere = rg.Sphere(rg.Point3d(0, 0, 0), 5)

# Add the point, line, circle, and sphere to the Rhino document
rs.AddPoint(point)
rs.AddLine(line.From, line.To)  # Add the line using its start and end points
rs.AddCircle(circle_center, circle_radius)  # Add the circle with center and radius
# rs.AddSphere(sphere)
