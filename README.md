# FA-Boxjelly
## Project overview
The overall gaol of our part of the project is integrating a thermal camrea to a robot named farmbot, so that the users could collect thermal data of plants remotely. Users should access the camera on farmbot web-app and can take thermal pictures if they wish. Once there is an emergency (for example threatening temperature) the system could send alarms to user.

**More information** : https://confluence.cis.unimelb.edu.au:8443/display/COMP900822023SM1FABoxJelly/Farmbot+Project+Home

## Goals of the Whole Project
* Integration of an e-nose sensor within the web-app controlling the robot
* **Integration of an thermal camera within the web-app controlling the robot (our part)**
* Integration of AI solvers that automatically control the robot.

**Client** : Nir Lipovetzky

**Supervisor** : Lin Li

## Team Members
| Name              | Role                         | E-mail                                        |
|-------------------|------------------------------|-----------------------------------------------|
| Dikai ZHU         | Scrum Master                 | dikai.zhu@student.unimelb.edu.au              |
| Chengtian Jiang   | Software Developer           | chengtian.jiang@student.unimelb.edu.au        |
| Yuxi He           | Product Owner                | yuxi.he2@student.unimelb.edu.au               |
| Tingzheng Ren     | Test Leader                  | tingzheng.ren@student.unimelb.edu.au          |
| Zhiyu Chen        | Software Developer           | zhiyu.chen3@student.unimelb.edu.au            |

## Repository structure and navigation
**├── docs/**                     # Documentation files (you can create subfolders here to organize your requirements) <br />
**├── src/**                      # src code <br />
**├── tests/**                      # User/system tests <br />
**├── prototypes/low fidelity/**   # low fidelity files (screens, mockups and so on) <br />
**├── prototypes/high fidelity/**  # high fidelity files (screens, source files and so on) <br />
**├── ui/**                        # All the images created for the prototypes (icons, fonts, backgrounds... should be here. This is different from the prototypes' folders.  These are the graphical elements that goes into the prototypes) <br />
**├── data samples/**              # Documents you need to generate with all the data (inputs) necessary to simulate/demonstrate your prototype (whatever can be provided as an input in your prototype) <br />
**└── README.md**                  #(this file must be updated at all times. please, make sure you explain your github structure here and generate changelogs for each sprint before you tag it)

**Branch details:**
* main: The place to release the final version.
* vanilla_farmbot_app: Default deployment code, project starting point
* thermal_control: Our code branch, including the code for thermal camera and the integration with farmbot app.
* web_app_front: The code for farmbot app, including the code for the web app and the integration with farmbot.
* farmbot_os: The code for farmbot os, including the code for the farmbot os and the integration with farmbot.
* rpi-v18.1(and other branch: rpi3-v18.1 and rpi4-v18.1): The code for raspberry pi, including the code for the raspberry pi and the integration with farmbot.

**Baseline tag convention:**
COMP90082_2023_SM1\_\<TwoDigits\>\_\<team\>\_BL\_\<sprint\>
<br />- BL means BASELINE. A baseline is a reference point in the software development life cycle marked by the completion and formal approval of a set of predefined work products
<br />- Example of TAG in this subject: COMP90082_2023_SM1_CM_Wombat_BL_SPRINT1


**Current Status:**
<br />- Finished the first sprint(2023-03-26)
<br />- Finished the second sprint, include code and physical camera. (2023-04-30)
<br />- Finished the Third sprint, include code and physical camera. (2023-05-25)
<br />***- Finished the Fourth sprint. (2023-06-25)***

## Sprint Change Log
**Sprint 1(Finished: 2023-03-26):**
<br />- Finish the project plan and the project overview. (2023-03-26)
<br />- Project review and Sprint 1 release. (2023-03-26)
<br />****All files are not changed in this sprint.***

**Sprint 2(Finished: 2023-04-30):**
<br />**Code:**
<br />- Web app page: Add a new page for thermal camera. (2023-04-25)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/tree/3b7c5c4d4c465f7100e7d8c42c1ebdd8241d1fb0/src/front_end/frontend/camera
<br />- Thermal camera: Add a new thermal camera control python script. (2023-04-25)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/tree/e32b4bd674f53096204b8d2fdd65d27c1874a65c/src/thermal_comtrol_scripts
<br />****All changed codes in src folder***
<br />**Document:**
<br />- Code review: Add code review document. (2023-04-25)
<br />- Confluence ducument: Add confluence document. (2023-04-25)
<br />****All changed documents in docs folder***

**Sprint 3(Finished: 2023-05-25):**
<br />**Code:**
<br />- Web app page: Add Thermal Camera images in our panel. (2023-05-25)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/tree/789d38f3e2c01152238359ec3b8ca6f29ff4973d/src/front_end
<br />- Resberry pie: Add python code for our own resberry pie server (2023-05-25)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/tree/789d38f3e2c01152238359ec3b8ca6f29ff4973d/src/Rasp%20server
<br />- rpi3: Add python code for rpi3 (2023-05-25)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/tree/789d38f3e2c01152238359ec3b8ca6f29ff4973d/src/rpi3
<br />- Farmbot OS: Add python code for farmbot os (2023-05-25)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/tree/789d38f3e2c01152238359ec3b8ca6f29ff4973d/src/Farmbot_os
<br />****All changed codes in src folder***
<br />**Document:**
<br />- Confluence ducument: Add confluence document. (2023-05-25)
<br />****All changed documents in docs folder***

**Sprint 4(Finished: 2023-06-8):**
<br />- Finish group reflection. (2023-06-8)
<br />- Project review and Sprint 4 release. (2023-06-8)
<br />- Demo video. (2023-06-8)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/blob/319b42b49b31d267c63bfeea2d09034c20444b42/docs/demo.mp4
<br />- Release Note. (2023-06-8)
<br />https://github.com/COMP90082-2023-SM1/FA-Boxjelly/blob/319b42b49b31d267c63bfeea2d09034c20444b42/RELEASE%20NOTE.pdf
<br />****All files are not changed in this sprint.***