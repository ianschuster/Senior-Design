1.  [Project Description (updated to include 400-character abstract and should reflect final version of the project)](https://github.com/ianschuster/Senior-Design/blob/main/project-description.md)

2.  [User Interface Specification (optional inclusion of UI design)](#ui-specification)

3.  [Test Plan and Results (describe execution and results of all tests)](https://github.com/ianschuster/Senior-Design/blob/main/Homeworks/seniordesign%20test%20plan.pdf)

4.  [User Manual (includes links and screenshots of online user manual; include FAQ in report)](https://github.com/ianschuster/Senior-Design/blob/main/UserGuide.md)

5.  [Spring Final PPT Presentation,](https://docs.google.com/presentation/d/1YG5sl0y60M1_kWhWt-65IkbAQFn56dPzIMEzrSycII4/edit#slide=id.p)

6.  [Final Expo Poster](https://drive.google.com/file/d/1vePU4g8YiPHxov0ruWXQrGYFvn7KgfSE/view)

7.  Assessments

[Initial Self-Assessments](#self-assessment-essays)

Final Self-Assessments (spring semester, do not include confidentialTeam-Assessments)

8.  Summary of Hours and Justification (one per individual team member)

# Auto Laser

### **Team Members**
Name | Major | Email
---- | ----- | -----
Braydon Garrett | Computer Science | garretjb@mail.uc.edu
Ian Schuster | Computer Science |  schustic@mail.uc.edu

**Team Advisor:** Fred Annexstein

### **Getting Started**

The Auto Laser User Guide can be found [here](https://github.com/ianschuster/Senior-Design/blob/main/UserGuide.md).

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
[Powerpoint Presentation](Homeworks/TeamAutoLaser.pptx)

# Self Assessment Essays
## Ian
My senior design project is going to primarily revolve around an artificial intelligence performing image recognition. This image recognition is going to provide x/y coordinate data to an Arduino controlled laser pointer with some sort of motor that can move its direction. It is my hope that this project will expand on my Python programming skills as that is the language I plan to primarily use in this project. I also am hoping to gain valuable experience with AI and the training side of things. Lastly, getting hands-on experience with making a physical product that I control via a computer will be a great new learning experience. Overall academically this project is going to expand my knowledge and experience with these concepts and help me really master them.

The way I look at it there are two main halves to this project; The AI side of things and the physical hardware side of things. The artificial intelligence side of things is going to incorporate two different classes I’ve taken, the obvious of which due to the name is CS 4033 AI Principles and Applications. The other class will be CS 2021 Python Programming, Python is my language of choice to program in since taking the course and lucky for me it is also highly supported in the AI community. None of my classes have directly taught me how to do the second part of this, the physical laser control part, however the programming logic will utilize skills learned throughout all of my programming focused curriculum. I am anticipating the AI side of the project to be the majority of work so having multiple classes in that field will be a great help, but undoubtedly I will still have to learn much of this on my own.

Both of the companies I have co-op’ed with have involved primarily front end web-app development using Javascript/HTML/CSS. The first of these was with Siemens PLM where I first learned these technologies. I don’t anticipate the technologies learned at Siemens to play a strong role in this project however I did have multiple high level presentations there and I think this could definitely help when it comes to presenting this project. My second (and current) company is an IoT solutions company called Losant. Losant is a small (~40 employees, ~8 software engineers) startup which has really helped me learn how to play a big role in a code base, expand my code review skills, and my coding prowess in general. Being an IoT company I also have gained some skills around IoT devices which I should be able to use on the physical side of this project. Both companies also used Git, and Losant uses Github which is our repo host of choice for this project.

I am extremely excited for this project as its the first big “choose your own project” assignment I’ve had in a long time. This particular project especially excites me for the AI element. As mentioned before I have taken an AI class however we really didn’t go into modern AI technology/usage which is what I really had hoped I’d get out of that class. I think this project has the potential to scratch that itch and give me the experience and knowledge I want to have in this field. Outside of the learning aspect I think the concept behind this is a really cool, practical idea that will demo very well. Having the physical side in my mind will give me something I can excitedly show anyone “hey watch this, I made that!” which motivates me to do this project and do it well.

The high-level preliminary approach to this will be to first design an AI that can identify balloons using pictures, followed by mapping the balloon centers to x/y coordinates. Once I have this the plan is to build the laser pointer motor/holder, and develop a program which maps these x/y coordinates to commands for the laser pointer holder. Finally will be combining the two/using a webcam to feed images into the AI that feeds commands to the motor/laser pointer. My expected result will be having a system where you can point the webcam at a room with balloons, run the system and have the laser pointer pop the correct balloons based on either color or pattern or symbols. I will know this was a success if I learn how to make a working AI, and if I am able to demo this and get that “wow” reaction out of people.
## James
From an academic perspective, my senior design project is the combination of many different technical concepts that I perceive to be of high value in the field of computer science. It makes usage of things like data science, IOT, Rest APIs, and even some computer engineering for the hardware components will be built. It also applies a real-world usage of Artificial Intelligence. I believe that it will greatly impact my own academic development, as it will require me to explore ideas, frameworks, and processes that I do not have much experience in. I also believe it will look great on a resume. All in all, I am excited to apply what I currently know, and to discover what I do not know when it comes time to start building this project.

After four and a half years in college, I have taken many classes that have prepared me for this senior design project. One such class is Python Programming (CS 2021). This class provided me with a good basis on which to stand when developing things using the Python coding language, which is what we plan to use for part of the senior design project. Another class is AI Principles and Applications (CS 4033). This class gave me a decent idea on what it takes to create a functional Artificial Intelligence. The final two classes in my curriculum that I believe hold value for this project are Data Structures (CS 2028C) and Discrete Structures (CS 2071), as they both generally taught me good coding practices.

In total, I have taken on four complete semesters of co-ops at two different companies. The first company was Siemens PLM where I worked as a Software Engineer and Quality Assurance Engineer in the Spring and Fall semesters of 2019. While at Siemens, I acquired a lot of good practice in working with a team of people. Since I was brand-new to the code base, I was constantly asking questions and I very quickly realized how valuable a second opinion on a problem can be. My project partner, (Ian Schuster) and I also worked on the same team at Siemens, so I believe we will work well together for this project. The second company I co-oped at was CADTalk, where I also worked as a Software Engineer and QA Engineer. While I was working at CADTalk, they had me create a Rest API for their products’ release notes. From this project, I gained a lot of experience working with back-end code. I also developed code which made use of Azure API calls to capture data. Then I developed various methods of filtering and processing that data to be uploaded as a "releasenotes.json" file in a database which would be used to present the release note information in a way that would be convenient for a customer to see. I also had to develop the automatic build pipeline for this project, as well as for various other projects. I believe that my experience with building the Rest API is extremely applicable to this project as this project heavily requires the transferring and processing of data for the Artificial Intelligence. I also think we may want a Rest API so that we can have a convenient interface with the machine that is controlling the laser.

My motivation for this project was brought to life organically through my own passion to solve an existing problem. For some back-story: I was on co-op during the COVID quarantine, and I was working from home. I also adopted a cat who required a little more attention than I had the capacity to give her at the time, so I started thinking of a solution. My idea was to create an autonomous laser-pointer toy that could play with my cat while giving me time to focus on my work. I crafted the general basis of this senior design project from that very same idea. However, my project partner and I decided to make the project idea a little more interesting.

My partner and I re-designed the plans I created for the autonomous cat laser to instead be a practical laser-targeting system that can pop balloons. The expected result will be that the Artificial Intelligence will be trained to recognize the general shape and color of a balloon, and the shape of a target that we draw on the balloon. Then, depending on if the balloon fits a specified criterion, the AI will send a command to an Arduino to point the laser at a specific coordinate and pop the balloon. My own contributions will be tracked via how many lines of code I write, and what physical contributions I make by crafting the hardware that will be used in our project. We will know that we are done when we have created a functional, autonomous laser targeting system which can identify balloons of a specified criterion and command the machine to shine the laser at that balloon. We will know that we have done a good job if the system can effectively identify which balloons fit the criterion that we give it, and if the system can pop only those balloons and no others. I am very excited for this project as it seems like a very fun opportunity to gain some experience in concepts that I am interested in!

# UI Specification

Our UI has 3 states it can be in and was built using PySimpleGUI

## Startup State

![image](https://user-images.githubusercontent.com/66269649/164272592-405c3ef1-be4f-49b8-8025-63b5b59409a6.png)

This state serves as our "Main Menu", you can reach the other two states via this one which is displayed on startup.

## Calibration State

![image](https://user-images.githubusercontent.com/66269649/164273175-15cd4f55-5f8a-46ad-82cf-65ef1f8bfa13.png)

This state serves as a way to modify the data.pkl file which contains the color bounds information for all the different balloon colors. Users can use the dropdown to switch between balloon colors whose values are initialized using the file and can save new values for these bounds.

## Running State

![image](https://user-images.githubusercontent.com/66269649/164273390-9d9faf85-5686-4c6d-9d84-5f3a6d46d12d.png)

This state is where the actual balloon tracking and Arduino commands are ran. Users can use the radio buttons to switch which balloon they are targeting.

# Professional Biographies
## Ian
## **Contact Information**
- Name: Ian Schuster
- Email: schustic@mail.uc.edu

## **Coop Work Experience**

### **Losant IoT**
Front End Intern Jun 2020-Present
* Working on an Iot Solutions webapp adding new features and fixing defects
* Extensive experience with React
* Minor feature work on NodeJS back-end
* Experience doing testing and QA with React Testing Library
* Performing code review
* Writing documentation on new features

### **Siemens PLM Software**
Student Co-Op Jan-May 2019 and Aug-Dec 2019
* Worked on framework focused agile team for a PLM web app
* Fixed a myriad of defects ranging from styling issues and client code issues to back-end server issues
* Presented high level demonstrations of client processes for upper management and documentation teams
* Used Angular, JQuery, GraphQL, and Docker

## **Project Sought**
- Something with an end result people will actually be able to use/have their hands on
- Can be physical or fully digital, something with IoT based devices would be desirable
- Preferably written with Python (not required)
- Working with AI would be a positive
- Prefer not to have a research based project
## James
## Contact Information
Email: garretjb@mail.uc.edu
Phone: 513-543-9825

## Co-op Work Experience

### Siemens PLM - Spring and Fall Semesters 2019
**Quality Assurance and Defect Engineer**
-  Worked in a position fixing code defects contained in two software products: Active Workspace and Team Center respectively. 
-  Found and fixed approximately 30 significant defects in areas related to: Security (Cross Site Scripting), Server-Side Regression, Unintended Command Behavior and User Interface Commands. 
-  Became proficient and gained experience with programming languages and frameworks such as: Java, JavaScript, C/C++, HTML, CSS/SASS, Node, Angular and JSON. 

**Software Engineer - Dead Command Reference Cleaner**
-  Created a utility that was used to traverse thousands of files and millions of lines of code to remove deprecated commands from the Team Center application. 

**Software Engineer – Chrome Developer Tools Extension**
-  Created a universal Chrome Extension that could be used to collect the property variables of a webpage into one window and then automatically update those variables when the page refreshed. This utility was created so that web pages of the Team Center product could be debugged more efficiently.

### CADTalk - Spring and Summer Semesters 2021
**Software Engineer - ReleaseNotes API**
- Created an Azure Function App as well as an App Service called ExtractReleaseNotes and CADTalkReleaseAPI respectively.
- Leveraged Azure DevOps API calls to automate the extraction of release note data from each build of a product iteration.
- Became proficient with Durable Functions (an extension of Azure Functions).
- Gained a lot of experience coding in C# and creating Rest API's.
- Created both integration tests and unit tests, as well as custom build pipelines for the apps mentioned above.

**Quality Assurance and Defect Engineer**
- Worked across more than 20 different codebases for various products to find and fix bugs of almost any type you could think of.
- Gained experience coding in Visual Basic.
- Created more than 50 unit tests spread over a few different codebases.

## Project Sought
- Combine a robotic arm with a laser-pointer, a camera, and the power of AI in order to create an interactive laser-pointer to keep a cat entertained and occupied throughout the day. 
- Anything that has to do with AI, data science, or Rest API's

# Appendix
Original idea and 3D printer plans for the laser control assembly can be found [here](https://www.instructables.com/CheetahBeam-a-DIY-Automatic-Cat-Laser-Toy/).
