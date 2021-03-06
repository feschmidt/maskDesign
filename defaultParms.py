#!/usr/bin/python
'''
This module contains the default variables for maskDesign
'''
um = 1e3
mm = 1e6

print 'loading default parameters'

def dLists():
    '''
    populate the borderTagList and offcenters and return them
    '''

    #border sizes
    borderTagList = [(),
            (7000*um, 2000*um), #1-3: Zurich / UQ design sizes 
            (7000*um, 4300*um),
            (7000*um, 6600*um),
            (9.7*mm,4.7*mm), #4-5: Oxford Magnon design sizes: these are actually 5*10 and 5*5, but with an inside border
            (4.7*mm,4.7*mm),
            (4.5*mm, 2.8*mm),   #Edward Laird group sizes 
            (10*mm, 10*mm),
            (9.7*mm,3.033*mm)] #with bordergap=300um its a 10mm x 3.333 mm chip
    
    #Qudev / UQ parameters
    #offCenters = {'A' : 2470*um, 'B' : (2470*um, 1170*um, 2300*um), 
    #    'C' : (925*um, 2775*um, 875*um, 2625*um)} '''

    offCenters = {'A' : 2470*um, 
            'B' : (2470*um, 1170*um, 2300*um), 
            'C' : (925*um, 2775*um, 875*um, 2625*um), 
            'D' : (3990*um, 1330*um), 
            'E' : 3990*um, 
            'F' : 1740*um}  #CNTGatemonChip QEDox

    # entry 3 and 4: third number is distance form left center to left upper launcher
    #last entry, last 4 numbers: vertical distances, then horizontal distances
 
    return borderTagList, offCenters


def dPars():
    '''
    populate and return a dictionary with default design values
    '''

    defDict = {'centerConductor'    : 10*um,    #beware, this is 2a or W in the literature
            'CPWGap'                : 19*um,    #Beware, this is 2b or W+2S in the literature
            'minimumRadius'         : 100*um,   #Minimum radius for bends (rbend)
            'borderGap'             : 600*um,   #Gap between chips
            'posResEdge'            : 20*um,    #border edge thickness for posRes chips
            'alignDistance'         : 300*um,   #Distance between border and alignment markers
            'LAlignSize'            : 500*um,   #Horizontal size of L-shaped alignment mark
            'LAlignThick'           : 100*um,   #Thickness of L-shaped alignment mark
            'launcherWidth'         : 150*um,   #Launcher
            'launcherWideLen'       : 250*um,
            'launcherTaperLen'      : 250*um,
            'gapCouplerSize'        : 5*um,     #GapCoupler
            'fingerCenterLen'       : 100*um,   #FingerCoupler
            'fingerTaperLen'        : 100*um,
            'fingerLen'             : 70*um,    
            'fingerThick'           : 3*um,
            'fingerGapWidth'        : 3*um,
            'fingerGapHeight'       : 3*um,
            'ABbridgeLenX'          : 40*um,   #airbridge Options (start with AB)
            'ABbridgeLenY'          : 10*um,
            'ABfooterLen'           : 30*um,
            'ABreflowGap'           : 3*um,
            'ABirGap'               : 40*um,
            'ABlayers'              : (2,1,25),
            'ABdistance'            : 200*um,
            'ABstart'               : 100*um,   #start and end distance for airbridges
            'ABend'                 : 100*um,
            'transmonWidth'         : 300*um,
            'transmonHeight'        : 150*um,
            'cornerTransmonWidht'   : 300*um,
            'cornerTransmonHeight'  : 150*um,
            'labelFont'             : 'romand', 
            'gateGapLen'            : 25*um,    #gap length at the end of the  gateLine
            'fluxGap'               : 2*um,     #Gap for current flow at the fluxline      
            'fluxLen'               : 40*um,    #Length of the fluxLine end      
            'fluxWidth'             : 30*um,    #Final width of the flux line      
            'lambdahalf65'          : 2*4670*um,
            'waferSize'             : 2*25.4*mm,
            'labelFontSize'         : 360*um,   # take ~.9*labelSpace
            'labelSpace'            : 400*um,   #space for labels on mostly black chips
            'MMPXEdge'              : (3.5*mm, 5.2*mm),     # side MMPX dimensions
            'MMPXTopWidth'          : 4.5*mm,
            'MMPXConnectLen'        : 1000*um,
            'MMPXOverlapWidth'      : .5*mm,     #half a mm overlap with PCB on each side
            'PCBcenter'             : .382*mm,  #This is 2a or W in the literature
            'PCBgap'                : .5*mm,   #This is 2b or W+2S in the literature
            'PCBChipMargin'         : .5*mm,    #total maring: half of this is added to each side
            'PCBScrewHole'          : 2.7*mm,
            'PCBrbend'              : 1*mm,     #minimum bend radius
            #'viaDiameter'           : .004*mm,       #Matthias           
            #'interviaDistance'      : .008*mm,       #Matthias
            #'viaHorizDistance'      : .0195*mm,      #Matthias
            #'randomViaDistance'     : .2*mm}     #Matthias  distance between randomly placed vias
            'viaDiameter'           : .5*mm,                 
            'interviaDistance'      : 1*mm,
            'viaHorizDistance'      : .5*mm,
            'randomViaDistance'     : 2*mm,    #distance between randomly placed vias
            'TransBoxAlignDis1'     : 520*um,  #One of the characterisitc distances used in placing alignment marks
            'TransBoxAlignDis2'     : 420*um}  #One of the characterisitc distances used in placing alignment marks

    return defDict

