<div align="center">

<img src="https://res.cloudinary.com/web-slinger/image/upload/v1608119278/Milestone%203/friendly-digest-favicon_n8ncda.png">

</div>

# **FRIENDLY DIGEST** <a name="top"></a>

<div align="justify">

Friendly Digest is a website designed to provide food recipes, primarily for people with chronic inflammatory bowel diseases such as Crohn's Disease & Colitis.
Users are able to follow the four basic CRUD functions, Create, Read, Update, and Delete. This means that you can register an account, create and upload your
own recipes, view other user's recipes, edit your own recipes, and delete your own recipes.

Friendly Digest is intended to provide great value to those who seek special diatary advice. Whether you suffer yourself, have a friend or family member who 
suffers, or whether you want to clean up your own diet, we hope Friendly Digest can guide you to a cleaner, happier, pain-free lifestyle.

The idea for Friendly Digest originates very close to home. An extremely close family member unfortunately suffers from Crohn's disease, therefore we have spent
many years struggling to find decent recipes which are suitable for those who have a variety of different requirements. Although it has been a long journey, we 
are now able to live a healthier, somewhat pain-free lifestyle due to what we put in our bodies. We hope that we can share some of this knowledge with you.

Feel free to browse through Friendly Digest's extensive library of recipes, we hope that you manage to find something yummy to satisfy your needs! Create an 
account and upload your own yummy dishes to share with others, but remember, keep it clean!

</div>

---

## :books: **TABLE OF CONTENTS**

1. [Live Demo](#live-demo)  

2. [UX](#ux)
    * [User Stories](#stories)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
        * [Sketches](#sketches)
        * [Wireframes](#wireframes)
        * [Mockups](#mockups)
    * [Surface](#surface)

3. [Information Architecture](#architecture)
    * [Application Framework](#app-framework)
    * [CSS Framework](#css-framework)
    * [Database](#database)

4. [Existing Features](#existing)
    * [Navigation](#navigation)
    * [Search Recipes](#search)
    * [Home](#home)
    * [Categories](#categories)
        * [Meat](#meat)
        * [Fish](#fish)
        * [Veg](#veg)
        * [Dessert](#dessert)
    * [View Recipe](#recipe)
    * [Log In](#log-in)
    * [Register](#register)
    * [My Recipes](#my-recipes)
    * [Add Recipe](#add-recipe)
    * [Edit Recipe](#edit-recipe)
    * [Delete Recipe](#delete-recipe)
    * [Log Out](#log-out)

5. [Features left to Implement](#features-left)

6. [Technologies](#technologies)

7. [Testing](#testing)

8. [Deployment](#deployment)
    * [Deployment to Heroku](#heroku)
    * [Local Deployment](#local)

9. [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#thanks)

---

## :computer: **LIVE DEMO** <a name="live-demo"></a>

Please feel free to delve into a demo of Friendly Digest's website.

You can live demo Friendly Digest's website here: [Friendly Digest](https://friendly-digest.herokuapp.com/).

<div align="center">

![Responsive showcase image of Friendly Digest website](https://res.cloudinary.com/web-slinger/image/upload/v1612106825/Milestone%203/showcase-img.png "Responsive showcase image of Friendly Digest website")

</div>

---

## :sparkles: **UX** <a name="ux"></a>

<div align="justify">

The user experience (UX) is what a user of a particular product experiences when using that product. A UX designer's job is thus to create a product that 
provides the best possible user experience. We're going to provide some insight into the UX process here, focusing on the important Who, What and How?

Friendly Digest, as previously stated, is a recipe website that's sole purpose is to not only provide people with tasty, clean, easy to follow recipes, 
but to teach and inspire, and to encourage people to share their own ideas. The hope is that anyone can pick up a simple recipe, cook it, and enjoy it
to the extent where they want to share their own. Do you have any tasty recipes that you would like to share? Click the link above, and register an account.

Carry on below and read some of Friendly Digest's user stories, and get a feel for what people originally wanted out of Friendly Digest.

</div>

---

### **USER STORIES** <a name="stories"></a>

>   Healthy foods tend to be green. Green would be a great colour for this website. - Lindsay W

>   Need an attractive logo which really captures the eye. One that has purpose. - Diane W

>   Need a good font, one that's not too hard to read. Must look good. - Bob R

>   Must be easy to navigate. I'm not good on computers so ease of navigation is key. - Hilary M

>   I have lots of recipes to share with people. I'd love to be able to upload my own recipes. - Jennifer C

>   Definitely need to be able to edit and delete recipes. If I make a mistake I need to fix it. - Charlie W

>   I hope people can't edit or delete my recipes. - Heather P

>   Can I create my own account and have a page dedicated to MY recipes? - Tom F

>   I'd like to be able to search all recipes that contain certain ingredients. I have allergies. - Becky D

---

### **STRATEGY** <a name="strategy"></a>

<div align="justify">

The strategy of the Friendly Digest website is to provide good quality recipes to those who struggle to eat the correct foods due to having an illness such as 
an inflammatory bowel disease. It is hoped that people can learn from their experiences, and share what they have found. Our long term ambition is that Friendly
Digest builds an extensive library of recipes far beyond the current scope. Extra categories will be added in the future, along with specific filters for known 
allergens such as gluten and dairy. In the near future we will include a new section of the website dedicated to 'Favourite' recipes. A new function will be added
giving the user the ability to share their favourite recipes via social media platforms such as Facebook, Instagram, and WhatsApp. What's most important is that
people walk away with a feel-good vibe. A happy gut can lead to a happy mind. Our user's health and happiness is of the utmost importance.

</div>

---

### **SCOPE** <a name="scope"></a>

<div align="justify">

The scope of Friendly Digest is to provide a flawless user experience straight from the get-go. We want users to be highly engrossed in what they encounter. We
want users to be attracted to the layout, the colour scheme, the ease of navigation, and the simplicity of the registration / editing process. Ultimately we want
users to return time and time again, not only to absorb information they may not have encountered before, but to share information that may be highly beneficial for 
others.

</div>

---

### **STRUCTURE** <a name="structure"></a>

<div align="justify">

The structure of Friendly Digest has been carefully thought-out to provide the best possible user experience. Everything from the layout to the navigation has been
structured for a friendly, easy to use, attractive approach. Please read below for a description of each page's structure.

* Each page has a Friendly Digest logo situated at the top center of the screen. Directly below this you'll find a navigation bar which contains links to each
page within the Friendly Digest website. There are four main navigation links (Home, Recipes, Log In, Register), one of which (Recipes) being a hoverable dropdown 
menu with four additional links (Meat, Fish, Veg, Dessert). When a user logs in, the navigation bar expands, showing additional links (My Recipes, Add Recipe, Log Out),
and with the loss of two links (Register, Log In). There are twelve pages in total, each with their own unique features. Each page contains a footer located at the
bottom of the page. This footer includes developer information, copyright information, and links to the developer's social media. All pages feature a 'To Top Button' which
navigates the user to the top of the page. This button is located in the bottom right side of the screen.

* The Home page consists of bright colourful images, easy to read text, and intuitive buttons. The Home page serves to provide information about the Friendly Digest website.

* There are four category pages, each providing the user with specific recipes related to their respective category. Each page consists of a search bar, a main header, a text 
paragraph and a multitude of recipe cards containing an image, a title, a description, and a button.

* The Recipe page, or 'Cook' page, displays single recipes. The Recipe page has a main heading, a large image, and a description. Recipe Author, Level, Prep, Cook, Servings,
and Calories can be found under this by clicking on a collapsible accordion element. Below these elements are the Recipe Ingredients and Recipe Instructions, displayed in
a simple list format. At the bottom of the page you'll find a 'Go Back' button.

* The Log In page follows the theme of a main header and a text paragraph centered on the screen. Below this you'll find a simple form consisting of three elements: a Username 
field, a Password field, and a Log In button. Underneath the log in form you'll find a register button for those who do not currently have an account.

* The Register page looks almost identical to the Log In page. Main header, text paragraph, three element form, and the addition of a log in button.

* The My Recipes page is extremely similar to that of the category pages. Each page consists of a search bar, a main header, a text paragraph and a multitude of recipe cards 
containing an image, a title, a description, and three buttons (Cook, Edit, Delete). Above the main header you'll find a weloming message which includes the user's username. 
There is an 'Add Recipe' button located at the bottom of the page.

* The Add Recipe page has a main header, text paragraph, and a form similar to the Log In & Register pages. The Add Recipe form is far more extensive and contains eleven
fields in total, two of which are select dropdown menus giving the user choices. The Add Recipe form fields include: Choose category, Recipe Name, Recipe Description, Prep Time,
Cook Time, Calories, Servings, Choose Difficulty, Recipe Ingredients, Recipe Instructions, and Image URL. The first select dropdown menu is Choose Category which has the options
of Meat, Fish, Veg, and Dessert. The second select dropdown menu is Choose Difficulty which has the options of Easy, Medium, and Hard. An Add Recipe button is located at the 
bottom of the form.

* When navigating to the Edit Recipe page, the user is presented with the same form found on the Add Recipe page. This form is automatically populated with the data related to
that specific recipe. like the Add Reipe page, the Edit Recipe page has a main header, and text paragraph. At the bottom of the Edit Recipe form there is an Edit Recipe button
and a Return button.

* The Search Recipes page is a page which is generated after entering text into the Search Bar. The Search Bar can be found at the top of multiple pages, below the navigation bar.
The Search Bar is present in each of the category pages, the My Recipes page, and the Search Recipes page. The Search Recipes page is laid out similar to the category pages and the 
My Recipes page. It consists of a search bar, a main header, and a multitude of recipe cards containing an image, a title, a description, and a button.

</div>

---

### **SKELETON** <a name="skeleton"></a>

#### *Sketches* <a name="sketches"></a>

<div align="justify">

Friendly Digest's website started on a piece of paper. Sketches were drawn out and a decent design was soon ready to leap into the digital world.
Below you shall find a link to a PDF document containing all of the original sketches used to help develop this project.
Please note - you may want to download this file to view it as intended.

</div>

* <a href="https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/sketches/ms3-sketches.pdf" target="_blank" rel="noopener">Friendly Digest Sketches PDF</a>

#### *Wireframes* <a name="wireframes"></a>

<div align="justify">

After drawing up the sketches it was time to get them onto the screen. To do this, a wireframe was created using Balsamiq Wireframes 4. 
Wireframes are used to display what the creator ultimately envisions the website to look like, roughly! It acts as one of the first stepping stones of the journey. 
Please find below a link to a PDF document containing all of the original Wireframes for Friendly Digest's project.
Please note - you may want to download this file to view it as intended.

</div>

* <a href="https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/wireframes/ms3-wireframes.pdf" target="_blank" rel="noopener">Friendly Digest Wireframes PDF</a>

#### *Mock Ups* <a name="mockups"></a>

<div align="justify">

Finally with the basics down on paper and screen, it was time to start shaping things up. After wireframes, it's time to take things a little more seriously. 
Enter Adobe XD. Adobe XD is a powerful piece of software designed to assist artists worldwide. More detailed designs are now progressed, and sketches etc.. 
are now a thing of the past! below, you will find a link to a PDF document containing Friendly Digest's Mock-Ups. You can clearly see how the project has evolved.
Please note - you may want to download this file to view it as intended.

</div>

* <a href="https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/mockups/ms3-mockups.pdf" target="_blank" rel="noopener">Friendly Digest Mockups PDF</a>

---

### **SURFACE** <a name="surface"></a>

<div align="justify">

The colour scheme chosen for this website offers healthy, earthy, green colours, as well as the addition of Eggshell.
There are five main colours for this website. Three different shades of Green, Eggshell for backgrounds and Black for fonts.
This was chosen because of the colours' positive vibe and feel-good effect.

</div>

<div align="center">

Chosen colours for Friendly Digest Website:

![Website Colour Scheme](https://res.cloudinary.com/web-slinger/image/upload/v1612213815/Milestone%203/ms3-colors_b0lmh1.png "Website Colour Scheme")

| **Colour Name**   | **Colour RGB Code**    
| -------------     |:-------------:| 
| Black             |#0F0901
| Custom Green #1   |#92D68C
| Custom Green #2   |#A0DB9B
| Custom Green #2   |#AEE6A9
| Eggshell          |#FAFAF2

<br></div>

<div align="justify">
There are two more colours which are less frequent, they are the colours which appear when a user has entered data into a form field or has missed a field completely.
When a user enters data into any field within the Friendly Digest website, the fields will be underlined green, else they'll be underlined red.
This is true for the Log In, Register, Add, and Edit forms.
</div>

<div align="center">

Chosen colours for Form Validation:

![Website Colour Scheme](https://res.cloudinary.com/web-slinger/image/upload/v1612214511/Milestone%203/ms3-form-colors_rzixpw.png "Website Colour Scheme")

| **Colour Name**   | **Colour RGB Code**    
| -------------     |:-------------:| 
| Green             |#4CAF50
| Red               |#F44336

<br></div>

<div align="justify">

The image used for Friendly Digest's logo was chosen because it relates to the theme of the website. By this, I refer to the chef hat image. 
Images for Friendly Digest were sourced from [PxHere](https://pxhere.com/) and [Klipartz](https://www.klipartz.com/en).<br>

Two fonts are used throughout Friendly Digest's website: [Google Fonts' - Calligraffitti](https://fonts.google.com/specimen/Calligraffitti?query=Calligraffitti) and [Google Fonts' - Cinzel](https://fonts.google.com/specimen/Cinzel?query=Cinzel).
If at any point a browser cannot support these fonts, the browser will fall back on Serif and Cursive.

</div>

---

## :page_facing_up: **INFORMATION ARCHITECTURE** <a name="architecture"></a>

### **APPLICATION FRAMEWORK** <a name="app-framework"></a>

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

Flask is a lightweight web application framework. It is designed to make getting started quick and easy, 
with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja 
and has become one of the most popular Python web application frameworks. Flask provides you with tools, 
libraries and technologies that allow you to build a web application. This web application can be some web pages, 
a blog, a wiki or go as big as a web-based calendar application or a commercial website. Flask was chosen because
of it's popularity, ease of use, and it was a prerequisite in the design of this project, according to the project brief.

### **CSS FRAMEWORK** <a name="css-framework"></a>

* [Materialize](https://materializecss.com/)

Created and designed by Google, Material Design is a framework that combines the classic principles of successful design 
along with innovation and technology. Google's goal is to develop a system of design that allows for a unified user experience 
across all their products on any platform. Materialize was chosen because of it's attractive design capabilities, its 
responsivness, and its ability to work with all modern browsers, including Internet Explorer 10+.

### **DATABASE** <a name="database"></a>

* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

MongoDB Atlas NoSQL database was used for this project. MongoDB is a document database with the scalability and flexibility 
that you want with the querying and indexing that you need. It claims to be the most innovative cloud database service on the market, 
with unmatched data distribution and mobility across AWS, Azure, and Google Cloud. MongoDB was chosen because MongoDB stores data in flexible, 
JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time.

The database consists of the following collections:

* Categories
* Difficulties
* Recipes
* Users

The collections within the database consist of the following document inserts:

* Category_name
* Recipe_name
* Recipe_description
* Recipe_prep_mins
* Recipe_cook_mins
* Recipe_calories
* Recipe_servings
* Recipe_level
* Recipe_ingredients
* Recipe_instructions
* Recipe_image
* Author_name

---

## :page_facing_up: **EXISTING FEATURES** <a name="existing"></a>

### **NAVIGATION** <a name="navigation"></a>

* Each page features a top navigation bar which enables the user to navigate to most pages within the Friendly Digest website. 
The top navigation bar has different options depending on whether the user is logged in or logged out. 

<div align="center">

If a user is logged in, the navigation links are as follows:

![Logged In Nav Bar](https://res.cloudinary.com/web-slinger/image/upload/v1612265623/Milestone%203/nav-in_urjtj5.png)

If a user is logged out, the navigation links are as follows:

![Logged Out Nav Bar](https://res.cloudinary.com/web-slinger/image/upload/v1612265623/Milestone%203/nav-out_a8chwk.png)

The Recipes tab features a dropdown menu which has additional options to choose from. These options are:

![Dropdown Menu](https://res.cloudinary.com/web-slinger/image/upload/v1612265971/Milestone%203/nav-drop_cz5qny.png)

</div>

* Friendly Digest has a highly responsive design meaning that the website displays perfectly on a mobile device.
When under 992px the top navigation bar transforms into a side navigation bar which is displayed when the user clicks
on the menu button. The menu button is displayed on the right hand side of the screen. It has a hamburger menu icon.

<div align="center">

Please see the side navigation bar below:

![Side Nav Bar](https://res.cloudinary.com/web-slinger/image/upload/v1612266447/Milestone%203/side-nav_r6ecr4.png)

</div>

* Located at the bottom right hand side of the screen there is a 'To Top Button' which when clicked, automatically
takes the user back to the top of the screen. When at the top of the screen, this button disappears. It only
reappears when the user scrolls down.

* Throughout the website there are multiple buttons which divert the user to different pages. The Log In page has a Register
button at the bottom of the page, and likewise, the Register page has a Log In button at the bottom of the page. the Recipe 
page has a Go Back button and the My Recipes page has buttons which allow you to view recipes and even edit recipes. The 
Edit Recipes page also features a Return button.

* The search bar which is present in various pages features a search button which takes the user to a Search Recipes page. The
Search Recipes page also features a Return button.

* The footer has two links which take the user to two seperate external websites. These links are to the developers social profiles
within GitHub and LinkedIn.

### **SEARCH RECIPES** <a name="search"></a>

* The Search Recipes feature is a very handy tool which is sure to be of great benefit to users. A user can type anything they wish 
into the search bar and the Search Recipes page will be generated. Depending on what the user types, depends on what is displayed on
this page. If the searched words correlate with anything in a recipe, that recipe will be displayed. If there are no search results,
a message will appear informing the user that the search was unsuccessful. The search bar is present within each of the category pages,
as well as the My Recipes page.

### **HOME PAGE** <a name="home"></a>

* The Home page is primarily used for the display of information to the user. The Home page gives explanation about Friendly Digest
as well as diatary advice. It also includes some high-quality images and success stories from the general public.

### **CATEGORIES** <a name="categories"></a>

There are four categories within the Friendly Digest website. Each offers recipes containing different products. A user can click the
'Cook' button to view the recipe in its entirety. As mentioned above, a user can also search for specific recipes or ingredients using
the search bar located at the top of the screen.

#### *Meat* <a name="meat"></a>

* The Meat category will display recipes that only contain meat.

#### *Fish* <a name="fish"></a>

* The Fish category will display recipes that only contain fish.

#### *Veg* <a name="veg"></a>

* The MVeg category will display recipes that only contain vegetables.

#### *Dessert* <a name="dessert"></a>

* The Dessert category will display recipes that only contain desserts.

### **VIEW RECIPES** <a name="recipe"></a>

* The Recipes page is a page dedicated to a single specific recipe. This page will contain all of the information needed
for a user to ultimately cook a dish. At the top of the page you'll find a recipe name, an image, and a description.
Below that is a collapsible accordion element which was used to store information compactly. Each element acts as a 
dropdown box. Author, Level, Prep, Cook, Servings, and Calories are found here.

<div align="center">

Image of Collapsible Accordian:

![Collapsible Accordian](https://res.cloudinary.com/web-slinger/image/upload/v1612268924/Milestone%203/accordian_vvasyb.png)

</div>

* Below the collapsible accordian a user will find the Recipe Ingredients and the Recipe Instructions. These ingredients and
instructions are displayed in a list with bullet points. This was implemented to make the information clear and concise.

* As mentioned in the navigation section, there is a 'Go Back' button located at the bottom of the page.

### **LOG IN** <a name="log-in"></a>

* The Log In page is fairly basic in terms of appearance. The user is presented with a header, a text paragraph and a log in form.
The log in form consists of two fields, Username, and Password. Below this there is a Log In button. The form contains Font Awesome
icons which offer the user a better experience. A Register button is located at the bottom of the page in case the user doesn't
have an account. When a user types in their username and password, the data is sent to MongoDB. The data is checked and if that username
exists and it matches up with the correct password, then the user is granted access. If the username and/or password cannot be found, or
they don't match on MongoDB, then a message will appear stating this fact. The user will not be granted access.

### **REGISTER** <a name="register"></a>

* Similar to the Log In page, the Register page is fairly basic in terms of appearance. The user is again presented with a header, a text
paragraph, and a register form. The register form consists of two fields, Username, and Password. Below this there is a Register button. 
The form contains Font Awesome icons which offer the user a better experience. A Log In button is located at the bottom of the page 
in case the user already has an account. When a user types in their desired username and password and clicks the register button, the 
data is sent to MongoDB and is checked to see if that username already exists. If the username already exists, a message will appear
informing the user that the username already exists. If the username doesn't exist, then a new user account is created within the database
and the user is redirected to the My Recipes page.

### **MY RECIPES** <a name="my-recipes"></a>

* The My Recipes page is only visible to users logged into their own account. A member of the general public will not be able to see
a user's My Recipes page. If a user does try to access another user's My Recipes page, the Log In page will be loaded and a message will 
appear stating that you need to log in to see this page.

* This page holds all recipes which have been uploaded by the user currently logged in. There is a search bar at the top of the screen
as well as a welcoming message which includes the user's username. There is a My Recipes heading and a text paragraph to follow. A user
is able to view recipes by clicking on the 'Cook' button, this will direct the user to the Recipe page. A user is also able to edit recipes
and delete recipes from this page. Please note that a user can only edit and delete recipes that have been uploaded themselves. The 'Edit'
and 'Delete' buttons are located next to the 'Cook' button. Clicking the edit button will direct the user to the Edit Recipe page. Clicking 
the delete button will action a pop up message (modal), which asks the user if they are sure they want to delete the recipe. If 'Yes' is 
clicked, the recipe will be gone forever. If there are no recipes to display, then a message will be shown stating that there are none to
show. There is an 'Add Recipe' button at the bottom of the page which will direct the user to the Add Recipe page. 

### **ADD RECIPE** <a name="add-recipe"></a>

* The add recipe page is where the user will complete a form in order to upload a recipe to the Friendly Digest website. Once uploaded, the
recipe will be visible in its category page, as well as the My Recipes page, and the Search Results page.

* A main heading and text paragraph is present keeping the theme of the website. Below this the user will find a form. This form is similar
to the form found within the Log in and Register pages. The form consists of eleven fields, two of which are select dropdowns. Each field
features a Font Awesome icon. The eleven fields are:

    * Choose Category
    * Recipe Name
    * Recipe Description
    * Prep Time (Mins)
    * Cook Time (Mins)
    * Calories
    * Servings
    * Choose Difficulty
    * Recipe Ingredients
    * Recipe Instructions
    * Paste Image URL

* The two select dropdowns are an excellent feature which enables the user to choose from a series of options. The select dropdowns are
for the fields Choose Category, and Choose Difficulty. 

<div align="center">

When a user clicks on the Category field they are presented with this selection:

![Choose Category](https://res.cloudinary.com/web-slinger/image/upload/v1612277140/Milestone%203/choose-category.png)

When a user clicks on the Difficulty field they are presented with this selection:

![Choose Difficulty](https://res.cloudinary.com/web-slinger/image/upload/v1612277140/Milestone%203/choose-difficulty.png)

</div>

### **EDIT RECIPE** <a name="edit-recipe"></a>

### **DELETE RECIPE** <a name="delete-recipe"></a>

### **LOG OUT** <a name="log-out"></a>

### **OTHER FEATURES** <a name="other-feat"></a>

---

 ## :pencil2: **FEATURES LEFT TO IMPLEMENT** <a name="features-left"></a>

 ---

## :cd: **TECHNOLOGIES USED** <a name="technologies"></a>

---

## :test_tube: **TESTING** <a name="testing"></a>

---

## :airplane: **DEPLOYMENT** <a name="deployment"></a>

### **DEPLOYMENT TO HEROKU** <a name="heroku"></a>

### **LOCAL DEPLOYMENT** <a name="local"></a>

---

## :clapper: **CREDITS** <a name="credits"></a>

### **CONTENT** <a name="content"></a>

### **MEDIA** <a name="media"></a>

### **ACKNOWLEDGEMENTS** <a name="thanks"></a>

---
:star: *A special thank you to [Maranatha Ilesanmi](https://github.com/mbilesanmi) Code Institute Mentor and [Paul F_alumni](https://github.com/Spagettileg) for aid, assistance, and much-needed guidance.* :star:
---

---

***This document is for educational use.***

---
[:arrow_up: Return to top?](#top)