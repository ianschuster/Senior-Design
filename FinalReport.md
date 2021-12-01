
# Auto Laser

### **Team Members**
Name | Major | Email
---- | ----- | -----
Braydon Garrett | Computer Science | garretjb@mail.uc.edu
Ian Schuster | Computer Science |  schustic@mail.uc.edu

**Team Advisor:** Fred Annexstein
### **Project Abstract**

The Auto Laser project will revolve around controlling a laser pointer which moves based on an AI which detects and tracks objects such as balloons. The laser pointer will be powerful enough to pop said balloons, and should be able to take different inputs such as color or shape to determine whether to target the balloon(s) or not.

# User Stories and Design Diagrams

### User Stories

As an end user, I want to be able to select a symbol from a list of symbols so that the artificial intelligence may target the symbol with the laser.

As an end user, I want the artificial intelligence to detect only ***balloons*** that have symbols on them so that random objects do not get burnt.

As an end user, I want to be able to stop the laser at any point (like a kill switch) in the event of an emergency.


### Design Diagrams
![Level 0](/Design_Diagrams/DesignD0.png)

![Level 1](/Design_Diagrams/DesignD1.png)

![Level 2](/Design_Diagrams/DesignD2.png)

# Project Tasks and Timeline
## Task List
### James

1.  Research tensorflow and other similar AI libraries to find one that fits our use case
    
2.  Research and 3D print laser pointer controller.
    
3.  Obtain powerful laser pointer
    
4.  Obtain lots of balloons
    
5.  Design a high level plan of how AI, camera, and laser pointer setup will interact and adapt as balloons are popped
    
6.  Develop AI tool to acquire balloon targets and output their x/y position
    

  

### Ian

1.  Test AI tool extensively to ensure only balloons will be recognized, I.E. make sure people’s heads don’t get marked as targets.
    
2.  Develop a script to take x/y position and map to a command for controlling the laser pointer.
    
3.  Investigate using arduino to control laser pointer setup
    
4.  Obtain Raspberry PI or Arduino
    
5.  Test controlling laser pointer with hard coded commands to ensure script maps values properly
    
6.  Connect AI and laser pointer setup together and test basic functionality

8.  Discover the limits of everything, can it handle moving targets? A room full of balloons?
## Timeline
|Task| Start |End|
|--|--|--|
|**1.** Research tensorflow and other similar AI libraries to find one that fits our use case| 10/10/2021 | 10/17/2021|
|**2.** Design a high level plan of how AI, camera, and laser pointer setup will interact and adapt as balloons are popped|11/07/2021|11/14/2021|
|**3.** Research and 3D print laser pointer controller|11/07/2021|11/14/2021|
|**4.** Obtain powerful laser pointer|11/07/2021|11/14/2021|
|**5.** Obtain lots of balloons|11/07/2021|11/14/2021|
|**6.** Develop AI tool to acquire balloon targets and output their x/y position|11/21/2021|12/11/2021|
|**7.** Test AI tool extensively to ensure only balloons will be recognized, I.E. make sure people’s heads don’t get marked as targets| 1/10/2022 | 1/16/2021|
|**8.** Investigate using arduino to control laser pointer setup|1/16/2022|1/23/2022|
|**9.** Obtain Raspberry PI or Arduino|1/23/2021|1/30/2022|
|**10.** Develop a script to take x/y position and map to a command for controlling the laser pointer|1/30/2022|2/06/2022|
|**11.** Test controlling laser pointer with hard coded commands to ensure script maps values properly|2/06/2022|2/13/2022|
|**12.** Connect AI and laser pointer setup together and test basic functionality|2/13/2022|2/20/2022|
|**13.** Discover the limits of everything, can it handle moving targets? A room full of balloons?|2/20/2022|2/27/2022|


## Effort Matrix

|     Task       |				James			 |			  Ian			   |
|----------------|-------------------------------|-----------------------------|
|**Task 1**|50%|50%|
|**Task 2**|0%|100%|
|**Task 3**|100%|0%|
|**Task 4**|100%|0%|
|**Task 5**|100%|0%|
|**Task 6**|50%|50%|
|**Task 7**|0%|100%|
|**Task 8**|0%|100%|
|**Task 9**|100%|0%|
|**Task 10**|0%|100%|
|**Task 11**|50%|50%|
|**Task 12**|50%|50%|
|**Task 13**|50%|50%|
# Powerpoint Slideshow
[Powerpoint Presentation](homeworks/Team Auto Laser.pptx)
