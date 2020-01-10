import numpy as np
import matplotlib.pyplot as plt

class polygon:
    def __init__(layer,uv,DF):
    ''' layer - GDSII layer for element (0-63)
        uv - polygon vertices; 2 x n matrix [u;v] (um)
        DF - dose factor for polygon''''
        self.layer = layer
        self.uv = uv
        self.DF = DF

class dot:
    def __init__(layer,uv,DF):
    ''' layer - GDSII layer for element (0-63)
            uv - dot position(s); 2 x n matrix [u;v] (um)
            DF - dose factor(s) for dot(s); if scalar, DF is applied to all
                dots specified by uv; if vector, must be of same length as uv'''
        self.layer = layer
        self.uv = uv
        self.DF = DF

class path:
    def __init__(layer,uv,w,DF):
    ''' layer - GDSII layer for element (0-63)
        uv - path vertices; 2 x n matrix [u;v] (um)
        w - width of path (um); value of zero yields single-pixel line; a
            negative value denotes an absolute width (not affected by
            magnification of any parent structure)
            DF - dose factor for path'''
        self.layer = layer
        self.uv = uv
        self.w = w
        self.DF = DF

class arc:
    def __init__(layer,uv_c,r,theta,angle,w,N,DF):
    ''' layer - GDSII layer for element (0-63)
        uv_c - arc centre; 1 x 2 vector [u_c v_c] (um)
        r - radius of arc; may be scalar for a circular arc, or a 1 x 2
            vector, [semi-major semi-minor] axes of an elliptical arc (um)
        theta - starting and ending angles of arc w.r.t. axis defined by
            angle argument; 1 x 2 vector [theta_1 theta_2] (degrees)
        angle - angle of rotation between positive u-axis and theta = 0
            axis (degrees)
        w - width of arc (um); if empty, arc is a filled elliptical disk
            segment; if zero, arc is a single-pixel line; if non-zero, arc
            has a width; a negative value denotes an absolute width (not
            affected by magnification of any parent structure)
        N - number of vertices
        DF - dose factor for arc'''
        self.layer = layer
        self.uv_c = uv_c
        self.r = r
        self.theta = theta
        self.angle = angle
        self.w = w
        self.N = N
        self.DF = DF

class circle:
    def __init__(layer,uv_c,r,w,N,DF):
    ''' layer - GDSII layer for element (0-63)
        uv_c - circle centre; 1 x 2 vector [u_c v_c] (um)
        r - radius of circle (um)
        w - width of circle (um); if empty, circle is filled (disk); if
            zero, circle is a single-pixel line; if greater than zero,
            circle has a width; a negative value denotes an absolute width
            (not affected by magnification of any parent structure)
        N - number of vertices
        DF - dose factor for circle'''
        self.layer = layer
        uv_self.c = uv_c
        self.r = r
        self.w = w
        self.N = N
        self.DF = DF

class ellipse:
    def __init__(layer,uv_c,r,w,angle,N,DF):
    ''' layer - GDSII layer for element (0-63)
        uv_c - ellipse centre; 1 x 2 vector [u_c v_c] (um)
        r - 1 x 2 vector, [semi-major semi-minor] axes of ellipse (um)
        w - width of ellipse (um); if empty, ellipse is filled (elliptical
            disk); if zero, ellipse is a single-pixel line; if greater than
            zero, ellipse has a width; a negative value denotes an absolute
            width (not affected by magnification of any parent structure)
        angle - angle between semi-major axis and u axis (degrees)
        N - number of vertices
        DF - dose factor for ellipse'''
        self.layer = layer
        self.uv_c = uv_c
        self.r = r
        self.w = w
        self.angle = angle
        self.N = N
        self.DF = DF

class text:
    def __init__(layer,uv_0,h,angle,uv_align,textlabel,DF):
    ''' layer - GDSII layer for element (0-63)
        uv_0 - text anchor point [u_0 v_0] (um)
        h - height of capital letters (um)
        angle - angle of rotation of text w.r.t. positive u-axis (degrees)
        uv_align - alignment w.r.t. anchor point; 1 x 2 vector
               [u_align v_align]; allowed values are 0 (left/top), 1 (centre),
               2 (right/bottom)
        textlabel - the text to be written (string); allowed characters are
               `1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+
               QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?� and [space]
        DF - dose factor for text '''
        self.layer = layer
        self.uv_0 = uv_0
        self.h = h
        self.angle = angle
        self.uv_align = uv_align
        self.textlabel = textlabel
        self.DF = DF

class fbmspath:
    def __init__(layer,uv,cvtr,w,DF):
    '''layer - GDSII layer for element (0-63)
       uv - path vertices; 2 x n matrix [u;v] (um)
       cvtr - curvature of path segments (um); if scalar and zero, the path
           comprises line segments (no curvature); if a 1 x n vector,
           cvtr(k) yields a circular arc with chord endpoints of uv(:,k-1)
           and uv(:,k) such that the radial distance between the arc and
           the chord centre is cvtr(k); a positive (negative) value of
           cvtr(k) corresponds to an arc to the left (right) of the chord;
           the value of cvtr(1) is ignored if cvtr is 1 x n
       w - width of path (um); if zero, path is a single-pixel line (no
           beam raster); if greater than zero, circle has a width (beam
           rastered during stage motion)
       DF - dose factor for path'''
        self.layer = layer
        self.uv = uv
        self.cvtr = cvtr
        self.w = w
        self.DF = DF

class fbmscircle:
    def __init__(layer,uv_c,r,w,DF):
    '''  layer - GDSII layer for element (0-63)
        uv_c - circle centre; 1 x 2 vector [u_c v_c] (um)
        r - radius of circle (um)
        w - width of circle (um); if zero, circle is a single-pixel line
            (no beam raster); if greater than zero, circle has a width
            (beam rastered during stage motion)
        DF - dose factor for circle'''
        self.layer = layer
        self.uv_c = uv_c
        self.r = r
        self.w = w
        self.DF = DF

class sref:
    def __init__(name,uv_0,mag=1,angle=0,reflect=0):
    ''' N.B.!  Transformations are applied in the following order: 1. scaling,
        mirroring; 2. rotation; 3. insertion.
            name - name of structure being referenced (string)
            uv_0 - structure origin; 1 x 2 vector [u_0 v_0] (um)
            mag - magnification factor [optional]; default is no magnification
                (mag = 1)
            angle - angle of rotation, counter-clockwise positive (degrees)
                [optional]; default is no rotation (angle = 0)
            reflect - Boolean flag for reflecting about u axis before other
                transformations [optional]; default is no reflection
                (reflect = 0)'''
        self.name = name
        self.uv_0 = uv_0
        self.mag = mag
        self.angle = angle
        self.reflect = reflect

class aref:
    def __init__(name,uv_0,n_colrow,a_colrow,mag=1,angle=0,reflect=0):
    ''' N.B.!  Raith interprets aref objects differently than the GDSII
    specification (e.g., as displayed using KLayout).  Given the number and
    spacing of rows and columns, a lattice of instance origins is
    generated, then rotation is applied to this lattice (if specified).  At
    each of these lattice points, a structure is placed, after first being
    scaled and/or rotated.
        name - name of structure being referenced (string)
        uv_0 - structure origin; 1 x 2 vector [u_0 v_0] (um)
        n_colrow - 1 x 2 vector indicating number of columns and rows,
            respectively
        a_colrow - 1 x 2 vector indicating lattice spacing in rows and
            columns, respectively (um)
        mag - magnification factor [optional]; default is no magnification
            (mag = 1)
        angle - angle of rotation, counter-clockwise positive (degrees)
            [optional]; default is no rotation (angle = 0)
        reflect - Boolean flag for reflecting about u axis before other
            transformations [optional]; default is no reflection
            (reflect = 0)'''
        self.name = name
        self.uv_0 = uv_0
        self.n_colrow = n_colrow
        self.a_colrow = a_colrow
        self.mag = mag
        self.angle = angle
        self.reflect = reflect
