#writing the OOP classes to handle the following scenerios
#A user can create and view 2-D coordinates
#A user can find out the distance between 2 coordinates
#A user can find the distance of a coordinate from the origin
#A user can check if the point lies on the given line
#A user can find the distance between the 2-D point and the given line
#H.W QUESTION we have to check the the two lines are intersected or not
class point:
    def __init__(self,x,y):  #parametrized concept
        self.x_cod = x
        self.y_cod = y

    def __str__(self):      #this is use for print
        return '({},{})'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):   #self(x1,y1) and other(x2,y2)
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return (self.x_cod**2 + self.y_cod**2)**0.5
    

#for question no 4 we have to create a different class called line
class Line:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return '{}x + {}y +{}c=0'.format(self.a,self.b,self.c)
    
    def point_on_line(line,point):
        if line.a*point.x_cod + line.b*point.y_cod + line.c ==0:
            return 'lies on the line'
        else:
            return 'does not lies on the line '
        
    def distance_of_line_from_the_point(line,point):
        if (line.a*point.x_cod + line.b*point.y_cod + line.c)<0:
          return (-1 * (line.a*point.x_cod + line.b*point.y_cod + line.c))/(line.a**2 + line.b**2)**0.5
        else:
            return (line.a*point.x_cod + line.b*point.y_cod + line.c)/(line.a**2 + line.b**2)**0.5
        
    def intersectin_of_two_lines(self,other):
        D=self.a*other.b - other.a*self.b
        if D!=0:
            return 'lines are intersecting'
        else:
            return 'lines are not intersecting'
        
l1=Line(1,4,89)
l2=Line(4,16,32)
print(l1.intersectin_of_two_lines(l2))