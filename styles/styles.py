draggableButtonStyle = """
DraggableButton{
    margin: 0px 10px; 
    border-radius: 10%; 
    font-family: roboto mono;
    font-weight: bold;
    border: 1px Solid white;
    background-color: rgb(35, 35, 35);
}
::hover{
    border: 1px solid rgb(35, 35, 255);
}
"""

nonDraggableButtonStyle = """
QPushButton{
    margin: 0px 10px; 
    border-radius: 10%; 
    border: 1px Solid white;
    font-family: roboto mono;
    font-weight: bold;
    background-color: rgb(35, 35, 35); 
}
QPushButton::hover{
    margin: 0px 10px;
    border: 1px solid rgb(35, 120, 215); 
    border-radius: 10%; 
    background-color: rgb(35, 35, 35); 
}
QPushButton::pressed{
    margin: 0px 10px; 
    border-radius: 10%; 
    background-color: rgb(35, 120, 215); 
} 
"""

convolutionDialogStyle = """
QDialog{
    background-color: rgb(19, 20, 22);
    border-radius: 10%; 
}
"""

layerObjectStyle = """
border: 1px solid white; 
padding: 15px 60px; 
border-radius: 10%;
font-family: roboto;
font-weight: bold;
"""

layerObjectSelectedStyle = """
border: 1px solid rgb(35, 120, 215); 
padding: 15px 60px; 
border-radius: 10%;
font-family: roboto;
font-weight: bold;
"""

runButtonStyle = """
QPushButton{
    margin: 0px 10px; 
    border-radius: 10%; 
    background-color: transparent;
}
QPushButton::hover{
    margin: 0px 10px; 
    border-radius: 10%; 
    border:1px solid rgb(0, 120, 250);
}
QPushButton::pressed{
    margin: 0px 10px; 
    border-radius: 10%; 
    background-color: rgb(60, 0, 255);
}
"""

draggableButtonStyleInsideDialog = """
height: 35px;
border: 1px solid white;
border-radius: 10%;
font-family: roboto;
font-weight: bold;
"""

propertyWindowStyle = """
QFrame{
    background-color: rgb(35, 35, 35); 
    border-radius: 10%;
}
"""

propertyFrameStyle = """

"""

dropDownWidgetStyle = """
background-color: rgb(35, 35, 35);
border-radius: 10%; 
"""

dropDownCloseButtonStyle = """
QPushButton{
    border: 1px solid rgb(35, 125, 210);
}

QPushButton::pressed{
    border: 1px solid rgb(35, 125, 210);
    background-color: rgb(85, 125, 210);
}
"""

propertyWindowCloseButtonStyle = """
QPushButton::pressed{
    background-color: rgb(35, 125, 210)
}
"""

parameterFrameStyle = """
background-color: rgb(35, 35, 35);
border-radius: 10%;
"""

parameterLabelStyle = """
"""

tabStyle = """
QPushButton{
    color: #fff;
    border: 1px solid white;
    background-color: rgb(35, 35, 35);
    border-radius: %d%%;
}
QPushButton::hover{
    border: 1px solid rgb(150, 150, 150);
}
QPushButton::pressed{
    color: #ddd;
    border: 1px solid rgb(255, 255, 255);
}
"""


selectedTabStyle = """
QPushButton{
    color: #fff;
    border: 1px solid white;
    background-color: rgb(100, 100, 100);
    border-radius: %d%%;
}

QPushButton::pressed{
    color: #ddd;
    border: 1px solid rgb(255, 255, 255);
}
"""

folderDropWidgetStyle = """
border: 1px dashed #3DB874; 
border-radius: 20px; 
background-color: rgb(40, 40, 40);
"""

datasetTypeButtonsStyle = """
QPushButton{
   font-family: Roboto mono; 
    font-size: 18px; 
    border: 2px solid rgb(35, 120, 210); 
    border-radius: 15px;
    color: white;
}

QPushButton::hover{
    background-color: rgba(35, 120, 210, 128);
}

QPushButton::pressed{
    background-color: rgba(35, 120, 210, 200);
}
"""

sidebarStyle = """
background-color: rgb(50, 50, 50);
border-right: 1px solid rgb(92, 92, 92); 
border-bottom: 1px solid rgb(92, 92, 92); 
border-top: 1px solid rgb(92, 92, 92); 
border-top-right-radius: 15px; 
border-bottom-right-radius: 15px;
"""

sidebarButtonStyle = """
QPushButton{
    border: none;
    border-radius none;
    background-color: transparent;
}
QPushButton::hover {
    border-radius: 25%;
    background-color: rgb(92, 92, 92);
}
QPushButton::pressed{
    border: none;
    border-radius none;
    background-color: rgb(60, 60, 60);
}
"""

animatedButtonStyle = """
AnimatedButton{
    background-color: transparent;
    border: none;
    border-radius: none;
    text-align: left;
    padding-left: 23px;
    
}
::hover{
    background-color: rgb(92, 92, 92);
}
::pressed{
    border: none;
    border-radius none;
    background-color: rgb(60, 60, 60);
    
}
"""

animatedButtonStyle1 = """
border: 1px solid white; 
border-radius: 5px; 
text-align: left; 
padding: 12px;
"""

sidebarLabelStyle = """
border: none; 
border-radius: none; 
font-family: roboto mono; 
font-size: 18px; 
font-weight: bold; 
color: rgb(220, 220, 220);
"""

selectedAnimatedButtonStyle = """
AnimatedButton{
    background-color: rgb(150, 150, 150);
    border: none;
    border-radius: none;
    text-align: left;
    padding-left: 23px;
    
}
"""

datasetParameterHeadStyle = """
background-color: rgb(50, 50, 50); 
border-top-right-radius: 10px; 
border-top-left-radius: 10px; 
border: 1px solid rgb(90, 90, 90);
"""

bodyOpenButtonStyle = """
QPushButton{
    border: none;
    background-color: rgb(92, 92, 92);
    border-radius: none;
    padding: none; margin: none;
}
QPushButton::hover{
    background-color: rgb(60, 60, 60);
}
QPushButton::pressed{
    background-color: rgb(92, 92, 92);
}
"""

bodyOpenStyle = """
background-color: rgb(40, 40, 40);
border: 1px solid rgb(92, 92, 92);
border-radius: 10px;
"""