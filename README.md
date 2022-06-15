# manage-recipe
a web app that allows users to create, update, delete and find recipes on a flask web app

## Table of Contents
1. [Introduction](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#an-introduction-to-the-project)
2. [Project Planning and Management](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#project-planning-and-management)
3. [Database Design](https://github.com/ebie-mondaisy/manage-recipe/edit/dev/README.md#database-design)
4. [User Stories and Use Cases]()
5. [Risk Assessment]()
6. [Testing]()
7. [CICD Pipeline]()
8. [Challenges and Known Issues]()
9. [Final Notes]()

## An Introduction to the Project

This is an individual project that is aimed to demonstrate learning of Python, Git, Databases and some other choice subjects. 
The app created for the project must have CRUD functionality and a relational database with two relating tables. 
To demonstrate an understanding of Project Management, a kanban board should be used to show that there was a sufficient amount of planning made.
The app must utilise Flask to create a functioning front-end website, a CI server for it to be built and a cloud-based virtual machine for the app to be deployed.
For integration into a Version Control system, GitHub has been chosen with a feature-branch model for development.

For this project, I have made sure that I am able to meet all requirments of the specification and to support this, I have produced the following documentation to display my work. The final product is a recipe library that allows the user to add, view, update, delete and search for recipes. In addition to this, the user can add notes to each recipe after they have cooked them to keep track of culinary skill progress.

## Project Planning and Management

To give some direction for the project, I produced a trello board that helped me to organise my tasks and keep track of what was complete and what needed to be done. The following images show the process of using the trello board by movign tasks to different lists based on level of completion.

###### Start of the Project

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/kanban1.jpg" width="900" height="500"/>

###### During the Project

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/kanban2.jpg" width="900" height="500"/>

###### Last part of the project

<img src="https://github.com/ebie-mondaisy/manage-recipe/blob/dev/image-source/kanban3.jpg" width="900" height="500"/>

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

## User Stories and Use Cases

When creating a flask web app, users are important to consider as they will be using the app and they will want to it to function in the way that they desire. I have created users stories with use cases to demonstrate what users will want from the app and how they would ideally use it. I have created 4 user stories with thier own use cases.
