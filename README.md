# manage-recipe
a web app that allows users to create, update, delete and find recipes on a flask web app

## Table of Contents
1. [Introduction](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#an-introduction-to-the-project)
2. [Project Planning and Management](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#project-planning-and-management)
3. [Database Design](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#database-design)
4. [User Stories and Use Cases](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#user-stories-and-use-cases)
5. [Risk Assessment](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#risk-assessment)
6. [Testing](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#testing)
7. [The manage-recipe app](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#the-manage-recipe-app)
8. [CICD Pipeline](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#cicd-pipeline)
9. [Challenges and Known Issues](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#challenges-and-known-issues)
10. [Final Notes](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#final-notes)

## An Introduction to the Project

This is an individual project that is aimed to demonstrate learning of Python, Git, Databases and some other choice subjects. 
The app created for the project must have CRUD functionality and a relational database with two relating tables. 
To demonstrate an understanding of Project Management, a kanban board should be used to show that there was a sufficient amount of planning made.
The app must utilise Flask to create a functioning front-end website, a CI server for it to be built and a cloud-based virtual machine for the app to be deployed.
For integration into a Version Control system, Git has been chosen with a feature-branch model for development.

For this project, I have made sure that I am able to meet all requirments of the specification and to support this, I have produced the following documentation to display my work. The final product is a recipe library that allows the user to add, view, update, delete and search for recipes. In addition to this, the user can add notes to each recipe after they have cooked them to keep track of culinary skill progress.

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## Project Planning and Management

To give some direction for the project, I produced a trello board that helped me to organise my tasks and keep track of what was complete and what needed to be done. The following images show the process of using the trello board by movign tasks to different lists based on level of completion.

###### Start of the Project

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/kanban1.jpg" width="900" height="500"/>

###### During the Project

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/kanban2.jpg" width="900" height="500"/>

###### Last part of the project

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/kanban3.jpg" width="900" height="500"/>

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## Database Design

The initial vision for the database was to create a table of cuisines that can link to the recipes table and provide drop down options when creating a recipe. To add an extra function to the recipe library, I planned to create a table that stores notes for each recipe.

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/erd1.jpg" width="900" height="500"/>

After drawing my intial ERD diagram, I moved onto creating one with my chosen software, Star UML. This diagram is what I had intially planned for the database.

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/erd2.jpg" width="900" height="500"/>

Further developments were made and a final ERD diagram had been prodcuced. This diagram is true to the models created in the flask app.

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/erd3.jpg" width="900" height="500"/>

**Explaining the Database Relationships**

- The Cuisine table has a One to Many relationship with the Recipes. The Recipes table pulls data from the Cuisine table to populate the drop down option in a form that allows the user to create recipes. Everytime a cusine is created, an option is added to the drop down menu for the recipe creation form.
- The Recipe table has a one to many relationship with the Notes table as each recipe can have multiple notes. The user can add as many notes as they would like to the recipe and each recipe will have its own notes.
- As a whole, the user can create cuisines and recipes to add to the database, update added recipes, delete recipes and notes, view recipes and notes and search for recipes by their name.

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## User Stories and Use Cases

When creating a flask web app, users are important to consider as they will be using the app and they will want to it to function in the way that they desire. I have created users stories with use cases to demonstrate what users will want from the app and how they would ideally use it. I have created 4 user stories with thier own use cases.

###### A user that is currently on a diet
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/uesr-diet.jpg" width="900" height="500"/>

###### A user that has to prepare meals for their children
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/user-parent.jpg" width="900" height="500"/>

###### A user that is a chef wanting to be innovative with recipes
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/user-chef.jpg"  width="900" height="500"/>

###### A user that soley enjoys cooking at home
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/user-work.jpg"  width="900" height="500"/>

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## Risk Assessment

When creating a project, there will be risks involved and this means taht they need to be evaluated to see how greatly they would impact the proceedings of the project. I have created a risk asessment table that a produces a score for the severity of risks and what actions need to be taken to avoid them or resolve them if they should occur.

(Insert risk asessment here)

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## Testing

To ensure that an app is able to fit its purpose and CRUD functionality, testing should be conducted. In this project I utilised Git and Jenkins to ensure that my application functioned as it should. If I was to deploy the application for wider use, I would test the securtiy of the application, however, that is not currently needed.

**Unit Testing - Pytest**

The first stages of testing were conducted using pytest. The version control system I used was Git and this enabled me to test specific functions of the application to ensure that they did what they were intended to do. I used pytest to evaulate each feature of the flask app while trying my best to get the highest coverage percentage.
(Include images of the testing and coverage. Explain what the testing means)

**Jenkins Testing**


[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## The manage-recipe app

The app I have produced is a site that allows users to add recipes to a database and attach notes to each created recipe. The purpose of this app is to show my understanding of CRUD functionality. To comply with this, I have created functions that allows the user to create, view, update, delete and search for entries in the databse.

**The home page**
The home page allows the user to view the recipies that are in the database along with being able to update and delete each recipe. The navigation bar shows links to other pages on the site and there is a search bar that allows the user to go to a recipe's update menu after searching for it by name.
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/recipe-home-view.jpg" width="900" height="500"/>

**Adding a cuisine**
In order to add a cusine to the database, the user will have to visit the cusisine portal via the navigation bar. This page allows the user to add a new cuisine and view all the cuisines that are currently in the database. When a cuisine has been added, a flash message pops up to confirm that the addition was successful.
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/add-cuisine.jpg" width="900" height="500"/>

**Creating a recipe**
To create a recipe, the user will have to navigate to this page via the navigation bar. On this page, a user can add a recipe to the database and the cuisine drop down menu is linked to the cuisines table. When a recipe has been created, the web page will flash a confirmation message so the user knows that the addition has been successful.
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/create-recipe.jpg" width="900" height="500"/>

**Editing a Recipe**
To edit a recipe, a user would need to click on a recipe's "View" button to get to the right page. On this page, the user is able to change details of a recipe and change the information that is in the database after submitting. The update page has two tabs: one to change recipe details and one to add notes.
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/edit-recipe.jpg" width="900" height="500"/>

**Adding notes to a recipe**
To add notes to a recipe, a user would have to click on the notes tab next to the update tab. A user is able to add as many notes as they would like and they also have the option to delete notest that they no longer want. The notes will always sit at the bottom of the update page. This leaves room for the user to tailor a recipe while potentially leaving notes explaining why they have made changes.
<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/notes-recipe.jpg" width="900" height="500"/>

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## CICD Pipeline

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## Challenges and Known Issues

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)

## Final Notes

[Back to table of contents](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#table-of-contents)
