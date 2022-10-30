<p align="center">

# A3 Report - Group 23
#### Samuel Daniel Leinum & Patrick Dahlgreen Petersen

</p>

## 3A Analyse use case
The tool should give the user the possibility to fast and easy investigate the quality of daylight in an earlier stage of modelling.

Use case is "Lighting analysis" and BIM Used as a forecast for performance of daylight. This tool relates to the design phase as illustrated and descirbed in 'Mapping BIM Uses' (p. 2).


## 3B Propose (a design) for a tool / workflow
![BPMN_Daylight](https://user-images.githubusercontent.com/112398725/197546660-99b6733f-4d84-4e98-8072-c1d6eeb8046c.svg)

The tools need an IFC-file and a requirement of the level of daylight to run and evaluate the performance. When this is done, the tool will gather information about the properties of the zone/room/building. These information includes areas of zones, walls, ceiling and floors along with assignmed materials and their respective properties for light reflectace. Furhtermore data about the glazing (LT-value), area, placement and orienration of the window is inheritated. From this state, the code will run a simulation to evaluate the daylight and present it for the client and if it complies with the acceptable requirement. 

## 3C Information exchange
Please see the file 'Exchange Information Group23.xlsx' for the specification of what information the tool requires to run.
IFC Entities and related property type:
- IfcSpace: NetFloorArea.
- IfcWindow: Translucency, Area, Orientation.
- IfcWall: Area, Reflection colour.
- IfcFloor: Area, Reflection colour.
- IfcCeiling: Area, Reflection colour.


## 3D Value what is the potential improvement to offer by this tool
This tool delivers a performance result of the daylight with only the IFC-file as an input. It can help the designers estimating the indoor environment according to daylight and saves both time and economi in the early design phase.
If the client sets goals and requirements for the indoor environment this tool can help improving the daylight which leads to a better effectivity of its users and a better all around health conditions.

## 3E Delivery
With the input from the client our tool can provide information about the level of daylight. The results can either actively be improved by the responsable parties and the client by changing properties of the windows, sizes or orientation, or the client can decide to go further with the already anayzed design proposal. If it is decided to change the design the model must go through the tool once again to evaluate the performance of daylight.
