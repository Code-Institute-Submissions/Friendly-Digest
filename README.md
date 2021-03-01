<div align="center">

<img src="https://res.cloudinary.com/web-slinger/image/upload/v1608119278/Milestone%203/friendly-digest-favicon_n8ncda.png">

# **FRIENDLY DIGEST** <a name="top"></a>

</div>

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

| **Name**          | **I want to...**                        | **So I can...**                                            |
|:------------------|:----------------------------------------|:-----------------------------------------------------------|
| Lindsay W         | View a selection of recipes             | Select some to cook                                        |
| Diane W           | View indivicual recipes                 | Identify cook times, ingredients, instructions, etc...     |
| Elliot R          | Easily register an account              | Have a personal account to view and upload my own recipes  |
| Abi C             | Easily login or logout                  | Access my personal account                                 |
| Jennifer C        | Add recipes                             | Share my amazing recipes with the world                    |
| Charlie W         | Edit recipes                            | Change my recipe if I've made a mistake or improved it     |
| Simon R           | Delete recipes                          | Remove any unwanted recipes from the site                  |
| Heather P         | Not have others edit/delete my recipes  | Keep my recipes personal and my own                        |
| Tom F             | Have my own recipes page                | Have all my uploaded recipes in one place                  |
| Becky D           | Search recipes                          | Find a specific recipe I'd like to cook                    |
| Phil W            | Have clear instructions                 | Follow the recipe easily without any issues                |
| Hilary M          | Navigate easily                         | Browse the website without any problems                    |

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
want users to be attracted to the layout, the colour scheme, the ease of navigation, and the simplicity of the registration/editing process. Ultimately we want
users to return time and time again, not only to absorb information they may not have encountered before but to share information that may be highly beneficial for 
others.

</div>

---

### **STRUCTURE** <a name="structure"></a>

<div align="justify">

The structure of Friendly Digest has been carefully thought-out to provide the best possible user experience. Everything from the layout to the navigation has been
structured for a friendly, easy to use, attractive approach. Please read below for a description of each page's structure.

* Each page has a Friendly Digest logo situated at the top center of the screen. Directly below this, you'll find a navigation bar which contains links to each
page within the Friendly Digest website. There are four main navigation links (Home, Recipes, Log In, Register), one of which (Recipes) being a hoverable dropdown 
menu with four additional links (Meat, Fish, Veg, Dessert). When a user logs in, the navigation bar expands, showing additional links (My Recipes, Add Recipe, Log Out),
and with the loss of two links (Register, Log In). There are twelve pages in total, each with their own unique features. Each page contains a footer located at the
bottom of the page. This footer includes developer information, copyright information, and links to the developer's social media. All pages feature a 'To Top Button' which
navigates the user to the top of the page. This button is located in the bottom right-hand side of the screen.

* The Home page consists of bright colourful images, easy to read text and intuitive buttons. The Home page serves to provide information about the Friendly Digest website.

* There are four category pages, each providing the user with specific recipes related to their respective category. Each page consists of a search bar, a main header, a text 
paragraph and a multitude of recipe cards containing an image, a title, a description, and a button.

* The Recipe page, or 'Cook' page, displays single recipes. The Recipe page has a main heading, a large image, and a description. Recipe Author, Level, Prep, Cook, Servings,
and Calories can be found under this by clicking on a collapsible accordion element. Below these elements are the Recipe Ingredients and Recipe Instructions, displayed in
a simple list format. At the bottom of the page, you'll find a 'Go Back' button.

* The Log In page follows the theme of a main header and a text paragraph centered on the screen. Below this you'll find a simple form consisting of three elements: a Username 
field, a Password field, and a Log In button. Underneath the log in form you'll find a register button for those who do not currently have an account.

* The Register page looks almost identical to the Log In page. Main header, text paragraph, three-element form, and the addition of a log in button.

* The My Recipes page is extremely similar to that of the category pages. Each page consists of a search bar, a main header, a text paragraph and a multitude of recipe cards 
containing an image, a title, a description, and three buttons (Cook, Edit, Delete). Above the main header you'll find a welcoming message which includes the user's username. 
There is an 'Add Recipe' button located at the bottom of the page.

* The Add Recipe page has a main header, text paragraph, and a form similar to the Log In & Register pages. The Add Recipe form is far more extensive and contains eleven
fields in total, two of which are select dropdown menus giving the user choices. The Add Recipe form fields include: Choose category, Recipe Name, Recipe Description, Prep Time,
Cook Time, Calories, Servings, Choose Difficulty, Recipe Ingredients, Recipe Instructions, and Image URL. The first select dropdown menu is 'Choose Category' which has the options
of Meat, Fish, Veg, and Dessert. The second select dropdown menu is 'Choose Difficulty' which has the options of Easy, Medium, and Hard. An Add Recipe button is located at the 
bottom of the form.

* When navigating to the Edit Recipe page, the user is presented with the same form found on the Add Recipe page. This form is automatically populated with the data related to
that specific recipe. Like the Add Recipe page, the Edit Recipe page has a main header, and text paragraph. At the bottom of the Edit Recipe form, there is an Edit Recipe button
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
Here are links to images of the original sketches used to help develop this project:

* [Home Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355747/Milestone%203/design/ms3-sketch-home_zzevjh.png)
* [Category Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355743/Milestone%203/design/ms3-sketch-category_v7hwsh.png)
* [Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355767/Milestone%203/design/ms3-sketch-recipe_mpyb5a.png)
* [Search Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355768/Milestone%203/design/ms3-sketch-search_nxxfkv.png)
* [Register Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355768/Milestone%203/design/ms3-sketch-register_epl0cl.png)
* [Log In Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355747/Milestone%203/design/ms3-sketch-login_d8ze4h.png)
* [My Recipes Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355767/Milestone%203/design/ms3-sketch-myRecipes_bsama0.png)
* [Add Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612355743/Milestone%203/design/ms3-sketch-addRecipe_nlllh9.png)

Here you shall find a link to a PDF document containing all of the original sketches used to help develop this project.
Please note - you may want to download this file to view it as intended. Large file size.

[Friendly Digest Sketches PDF](https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/sketches/ms3-sketches.pdf)

</div>

#### *Wireframes* <a name="wireframes"></a>

<div align="justify">

After drawing up the sketches it was time to get them onto the screen. To do this, a wireframe was created using Balsamiq Wireframes 4. 
Wireframes are used to display what the creator ultimately envisions the website to look like, roughly! It acts as one of the first stepping stones of the journey.
Here are links to images of the original sketches used to help develop this project:

* [Desktop Home Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-wireframe-home_fbsvnz.png)
    * [Mobile Home Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358972/Milestone%203/design/ms3-mobile-wireframe-home_n0tmar.png)
    * [Mobile Side Nav](https://res.cloudinary.com/web-slinger/image/upload/v1612358970/Milestone%203/design/ms3-mobile-wireframe-side-nav_gqwuec.png)

* [Desktop Category Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-wireframe-category_tjerhq.png)
    * [Mobile Category Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-mobile-wireframe-category_utv5py.png)

* [Desktop Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-wireframe-recipe_aarpec.png)
    * [Mobile Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358972/Milestone%203/design/ms3-mobile-wireframe-recipe_v3n7k7.png)

* [Desktop Search Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-wireframe-search_gxodi7.png)
    * [Mobile Search Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358970/Milestone%203/design/ms3-mobile-wireframe-search_n3z0kx.png)

* [Desktop Register Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-wireframe-register_riozi6.png)
    * [Mobile Register Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358970/Milestone%203/design/ms3-mobile-wireframe-register_b6o9vr.png)

* [Desktop Log In Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-wireframe-login_vpybrv.png)
    * [Mobile Log In Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358972/Milestone%203/design/ms3-mobile-wireframe-login_bysztd.png)

* [Desktop My Recipes Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-wireframe-myRecipes_im4ix8.png)
    * [Mobile My Recipes Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358972/Milestone%203/design/ms3-mobile-wireframe-myRecipes_zics4m.png)

* [Desktop Add Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358970/Milestone%203/design/ms3-wireframe-addRecipe_el4fs3.png)
    * [Mobile Add Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-mobile-wireframe-addRecipe_xzot7l.png)

* [Desktop Edit Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358970/Milestone%203/design/ms3-wireframe-editRecipe_zqfjxp.png)
    * [Mobile Edit Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612358971/Milestone%203/design/ms3-mobile-wireframe-editRecipe_gd5gmn.png)

Here you shall find a link to a PDF document containing all of the original wireframes used to help develop this project.
Please note - you may want to download this file to view it as intended. Large file size.

[Friendly Digest Wireframes PDF](https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/wireframes/ms3-wireframes.pdf)

</div>

#### *Mock Ups* <a name="mockups"></a>

<div align="justify">

Finally with the basics down on paper and screen, it was time to start shaping things up. After wireframes, it's time to take things a little more seriously. 
Enter Adobe XD. Adobe XD is a powerful piece of software designed to assist artists worldwide. More detailed designs are now progressed, and sketches etc.. 
are now a thing of the past! below, you will find links to the original Friendly Digest Mock-Ups. You can clearly see how the project has evolved.

* [Desktop Home Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360400/Milestone%203/design/ms3-mockup-home_myybod.png)
    * [Mobile Home Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mobile-mockup-home_nzjszl.png)
    * [Mobile Side Nav](https://res.cloudinary.com/web-slinger/image/upload/v1612360402/Milestone%203/design/ms3-mobile-mockup-sidenav_ca5uhn.png)

* [Desktop Category Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360400/Milestone%203/design/ms3-mockup-category_yree0t.png)
    * [Mobile Category Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mobile-mockup-category_czqjm4.png)

* [Desktop Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mockup-recipe_nzw4jn.png)
    * [Mobile Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360402/Milestone%203/design/ms3-mobile-mockup-recipe_lwajfa.png)

* [Desktop Search Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mockup-search_vfjx94.png)
    * [Mobile Search Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360402/Milestone%203/design/ms3-mobile-mockup-search_ld6npa.png)

* [Desktop Register Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mockup-register_wvead4.png)
    * [Mobile Register Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mobile-mockup-register_sknveq.png)

* [Desktop Log In Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360400/Milestone%203/design/ms3-mockup-login_ebyxir.png)
    * [Mobile Log In Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mobile-mockup-login_ai05jc.png)

* [Desktop My Recipes Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mockup-myRecipes_cck0vw.png)
    * [Mobile My Recipes Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mobile-mockup-myRecipes_mdzafx.png)

* [Desktop Add Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360400/Milestone%203/design/ms3-mockup-addRecipe_t1pcla.png)
    * [Mobile Add Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mobile-mockup-addRecipe_oxnxwo.png)

* [Desktop Edit Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360400/Milestone%203/design/ms3-mockup-editRecipe_outf9s.png)
    * [Mobile Edit Recipe Page](https://res.cloudinary.com/web-slinger/image/upload/v1612360401/Milestone%203/design/ms3-mobile-mockup-editRecipe_qbxdsa.png)

Here you shall find a link to a PDF document containing all of the original mockups used to help develop this project.
Please note - you may want to download this file to view it as intended. Large file size.

[Friendly Digest Mockups PDF](https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/mockups/ms3-mockups.pdf)

</div>

---

### **SURFACE** <a name="surface"></a>

<div align="justify">

The colour scheme chosen for this website offers healthy, earthy, green colours, as well as the addition of Eggshell.
There are five main colours for Friendly Digest. Three different shades of Green, Eggshell for backgrounds and Black for fonts.
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

<br></div>

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

[Font Awesome](https://fontawesome.com/) icon graphics were used in conjunction with Materialize, primarily to support form fields and submit buttons.

* Username: [fas fa-user-cog](https://fontawesome.com/icons/user-cog?style=solid)
* Add User: [fas fa-user-plus](https://fontawesome.com/icons/user-plus?style=solid)
* Password: [fas fa-user-lock](https://fontawesome.com/icons/user-lock?style=solid)
* Category: [fas fa-list-alt](https://fontawesome.com/icons/list-alt?style=solid)
* Recipe Name: [fas fa-pencil-alt](https://fontawesome.com/icons/pencil-alt?style=solid)
* Calories: [fas fa-weight](https://fontawesome.com/icons/weight?style=solid)
* Servings: [fas fa-users](https://fontawesome.com/icons/users?style=solid)
* Image: [fas fa-image](https://fontawesome.com/icons/image?style=solid)
* Prep & Cook Time: [fas fa-clock](https://fontawesome.com/icons/clock?style=solid)
* Description/Ingredients/Instructions: [fas fa-file-alt](https://fontawesome.com/icons/file-alt?style=solid)

</div>

---

## :page_facing_up: **INFORMATION ARCHITECTURE** <a name="architecture"></a>

### **APPLICATION FRAMEWORK** <a name="app-framework"></a>

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

<div align="justify">

Flask is a lightweight web application framework. It is designed to make getting started quick and easy, 
with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja 
and has become one of the most popular Python web application frameworks. Flask provides you with tools, 
libraries and technologies that allow you to build a web application. This web application can be some web pages, 
a blog, a wiki or go as big as a web-based calendar application or a commercial website. Flask was chosen because
of it's popularity, ease of use, and it was a prerequisite in the design of this project, according to the project brief.

</div>

### **CSS FRAMEWORK** <a name="css-framework"></a>

* [Materialize](https://materializecss.com/)

<div align="justify">

Created and designed by Google, Material Design is a framework that combines the classic principles of successful design 
along with innovation and technology. Google's goal is to develop a system of design that allows for a unified user experience 
across all their products on any platform. Materialize was chosen because of it's attractive design capabilities, its 
responsivness, and its ability to work with all modern browsers, including Internet Explorer 10+.

</div>

### **DATABASE** <a name="database"></a>

* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

<div align="justify">

MongoDB Atlas NoSQL database was used for this project. MongoDB is a document database with the scalability and flexibility 
that you want with the querying and indexing that you need. It claims to be the most innovative cloud database service on the market, 
with unmatched data distribution and mobility across AWS, Azure, and Google Cloud. MongoDB was chosen because MongoDB stores data in flexible, 
JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time.

</div>

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
* Username
* Password

To view a tree of Friendly Digest's database collections, click [here.](https://res.cloudinary.com/web-slinger/image/upload/v1612366559/Milestone%203/design/mongo-collections_z2ct58.png)

---

## :page_facing_up: **EXISTING FEATURES** <a name="existing"></a>

<div align="justify">

In computer programming, create, read, update, and delete (CRUD) are the four basic functions of persistent storage. Friendly Digest 
relies heavily on this concept, as the sole purpose of the website is to allow users to create recipes, view recipes, edit recipes,
and delete recipes. Within the information below, you'll find how CRUD has been used and why it has been used. Not to mention many 
more features.

</div>

### **NAVIGATION** <a name="navigation"></a>

<div align="justify">

* Each page features a top navigation bar which enables the user to navigate to most pages within the Friendly Digest website. 
The top navigation bar has different options depending on whether the user is logged in or logged out.

</div>

<br>

<div align="center">

If a user is logged in, the navigation links are as follows:

![Logged In Nav Bar](https://res.cloudinary.com/web-slinger/image/upload/v1612265623/Milestone%203/nav-in_urjtj5.png)

<br>

If a user is logged out, the navigation links are as follows:

![Logged Out Nav Bar](https://res.cloudinary.com/web-slinger/image/upload/v1612265623/Milestone%203/nav-out_a8chwk.png)

<br>

The Recipes tab features a dropdown menu which has additional options to choose from. These options are:

![Dropdown Menu](https://res.cloudinary.com/web-slinger/image/upload/v1612265971/Milestone%203/nav-drop_cz5qny.png)

</div>

<div align="justify">

* Friendly Digest has a highly responsive design meaning that the website displays perfectly on a mobile device.
When under 992px the top navigation bar transforms into a side navigation bar which is displayed when the user clicks
on the menu button. The menu button is displayed on the right hand side of the screen. It has a hamburger menu icon.

</div>

<br>

<div align="center">

Please see the side navigation bar below:

![Side Nav Bar](https://res.cloudinary.com/web-slinger/image/upload/v1612266447/Milestone%203/side-nav_r6ecr4.png)

</div>

<div align="justify">

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

* The search recipes page includes a return button for easy navigation.

* The search recipes page is fully responsive.

### **HOME PAGE** <a name="home"></a>

* The Home page is primarily used for the display of information to the user. The Home page gives explanation about Friendly Digest
as well as diatary advice. 

* It includes an animated image carousel.

* It includes some high-quality images with material boxed functionality.

* It features tooltipped images that produce additional information via modal messages.

* It features easy to access, user interactive information via tabbed info cards.

* Home page is fully responsive.

### **CATEGORIES** <a name="categories"></a>

* There are four categories within the Friendly Digest website. Each offers recipes containing different products. 

* A user can click the 'Cook' button to view the recipe in its entirety.

* A user can search for specific recipes or ingredients using the search bar located at the top of the screen.

* Category Pages are fully responsive.

#### *Meat* <a name="meat"></a>

* The Meat category will display recipes that only contain meat.

#### *Fish* <a name="fish"></a>

* The Fish category will display recipes that only contain fish.

#### *Veg* <a name="veg"></a>

* The Veg category will display recipes that only contain vegetables.

#### *Dessert* <a name="dessert"></a>

* The Dessert category will display recipes that only contain desserts.

### **VIEW RECIPES** <a name="recipe"></a>

* One of the main CRUD functionalities.

* The Recipes page is a page dedicated to a single specific recipe. This page will contain all of the information needed
for a user to ultimately cook a dish. At the top of the page you'll find a recipe name, an image, and a description.
Below that is a collapsible accordion element which is used to store information compactly. Each element acts as a 
dropdown box. Author, Level, Prep, Cook, Servings, and Calories are found here.

</div>

<div align="center">

Image of Collapsible Accordion:

![Collapsible Accordion](https://res.cloudinary.com/web-slinger/image/upload/v1612268924/Milestone%203/accordian_vvasyb.png)

</div>

<div align="justify">

* Below the collapsible accordion a user will find the Recipe Ingredients and the Recipe Instructions. These ingredients and
instructions are displayed in a list with bullet points. This was implemented to make the information clear and concise.

* As mentioned in the navigation section, there is a 'Go Back' button located at the bottom of the page.

* Recipes page is fully responsive.

### **LOG IN** <a name="log-in"></a>

* The Log In page features a login form consisting of two fields: username and password.

* Form validation (Javascript) is present here, fields will be underlined green if filled correctly, red if there is an error.

* Both fields have min length of 5 characters and max length of 15 characters.

* Required message will appear if a field is left blank, or there aren't enough characters in a field.

* Flash messages will appear if username and/or password is wrong or does not exist.

* Font Awesome icons are used.

* There is a certain level of animation for the form labels and submit button.

* Log In page is fully responsive.

### **REGISTER** <a name="register"></a>

* The Log In page features a login form consisting of two fields: username and password.

* Form validation (Javascript) is present here, fields will be underlined green if filled correctly, red if there is an error.

* Both fields have min length of 5 characters and max length of 15 characters.

* Required message will appear if a field is left blank, or there aren't enough characters in a field.

* Flash message will appear if username already exists.

* Font Awesome icons are used.

* There is a certain level of animation for the form labels and submit button.

* Register page is fully responsive.

### **MY RECIPES** <a name="my-recipes"></a>

* All CRUD (Create, Read, Update, Delete) functionalities are available here.

* My Recipes page is only visible to users logged into their own account.

* Users will be redirected to the Log In page if they try to navigate to the My Recipes page whilst not logged in.

* Special welcoming header that displays user's username.

* Only contains recipes that have been uploaded by the user in session.

* Extended recipe card containing 'Edit' and 'Delete' buttons.

* The only page where users can edit and delete their recipes.

* Search bar is present.

* Special modal message for delete button.

* My Recipes page is fully responsive.

### **ADD RECIPE** <a name="add-recipe"></a>

* One of the main CRUD functionalities.

* The Add Recipe page features a form consisting of eleven fields.
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

* There are two select dropdown fields. Please see images below.

* After form submission, the recipe will be visible in its category page, as well as the My Recipes page, and the Search Results page.

* Form validation (Javascript) is present here, fields will be underlined green if filled correctly, red if there is an error.

* All fields have a min and max length, excluding the select dropdown fields.

* Required message will appear if a field is left blank, or there aren't enough characters in a field.

* Font Awesome icons are used.

* There is a certain level of animation for the form labels and submit button.

* Add Recipe page is fully responsive.

</div>

<div align="center">

When a user clicks on the Category field they are presented with this selection:

![Choose Category](https://res.cloudinary.com/web-slinger/image/upload/v1612277140/Milestone%203/choose-category.png)

When a user clicks on the Difficulty field they are presented with this selection:

![Choose Difficulty](https://res.cloudinary.com/web-slinger/image/upload/v1612277140/Milestone%203/choose-difficulty.png)

</div>

<div align="justify">

### **EDIT RECIPE** <a name="edit-recipe"></a>

* One of the main CRUD functionalities.

* The Edit Recipe page features a form consisting of eleven fields.
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
    
* There are two select dropdown fields. Please see images above.

* All fields are automatically populated with data pulled from the MongoDB database when loaded.

* After form submission, the updated recipe will be visible in its category page, as well as the My Recipes page, and the Search Results page.

* After form submission, the My Recipes page will load.

* Form validation (Javascript) is present here, fields will be underlined green if filled correctly, red if there is an error.

* All fields have a min and max length, excluding the select dropdown fields.

* Required message will appear if a field is left blank, or there aren't enough characters in a field.

* Font Awesome icons are used.

* There is a certain level of animation for the form labels and submit button.

* Edit Recipe page is fully responsive.

### **DELETE RECIPE** <a name="delete-recipe"></a>

* One of the main CRUD functionalities.

* The Delete Recipe button can only be found in the My Recipes page. 

* Only users who are currently logged in may access the delete button. 

* Users can only delete recipes that they themselves have uploaded.

* The Delete Recipe button, unlike other buttons, does not redirect the user to another page. Instead, it initiates a function. 

* Clicking the delete button will prompt a warning message to appear (modal). 

* If user selects 'Yes' option, the recipe will be permanently removed from the MongoDB database and therefore completely removed from any Friendly Digest web page.

* Recipes cannot be retrieved after deletion.

* The delete function was implemented so that users are able to remove any unwanted recipes which may be inconsequential.

* Delete modal message is fully responsive.

### **LOG OUT** <a name="log-out"></a>

* The Log Out button is located within the main navigation bar. The Log Out button will only be visible to users who are currently logged in to their account.
The Log Out button initiates a function, similar to that of the delete function. Firstly, clicking the Log Out button will prompt a message to appear (modal). 
This is a warning message asking the user if they really wish to log out. If 'Yes' is selected, the user will be logged out of their current session and redirected 
to the Log In page. A message will appear informing the user that they have successfully logged out.

* The Log Out button can only be found in the main navigation bar/side navigation bar. 

* Only users who are currently logged in may access the log out button. 

* Clicking the log out button will prompt a warning message to appear (modal).

* If user selects 'Yes' option, the user session will be terminated and the user will be redirected to the Log In page. Flash message will appear.

### **OTHER FEATURES** <a name="other-feat"></a>

* If and when a user encounters an error, certain error messages will be displayed. The typical trigger for an error 404 message is when website content has been 
removed or moved to another URL. An Error 404 message will be displayed if a situation like this occurs. If there happens to be an internal server issue, an 
Error 500 message will be displayed. The 500 Internal Server Error is a very general HTTP status code that means something has gone wrong on the website's server 
but the server could not be more specific on what the exact problem is.

* Defensive programming has been put in place so users cannot access specific pages if they are not logged in. If for example, a user is on their My Recipes 
page and then logs out using the Log Out button, if they were to click their browser's back button, they wouldn't be able to access their My Recipes page. A message
will appear stating that you need to log in to see this page. The same applies for if you were to copy and paste a URL into the search box and/or go through your
search history. You will only be able to see your pages if you are logged in.

---

 ## :pencil2: **FEATURES LEFT TO IMPLEMENT** <a name="features-left"></a>

Friendly Digest is a big project, and although we are happy with everything that has been done to date, there are still multiple features that are yet to be
implemented. In the near future we hope to implement the following:

* Allergen filters.
* Extra Categories - Breakfast, Snacks, Light-Bites, Drinks.
* Food Genres - Chinese, Italian, Indian, Mexican, etc...
* Favourite Recipes - Users can flag their favourite recipes.
* Social Sharing - Users can share their favourite recipes via Facebook, Instagram, and WhatsApp.
* Reversing Deletion - Deleted recipes to be recovered in the event of human error.

</div>

---

## :cd: **TECHNOLOGIES USED** <a name="technologies"></a>

<div align="justify">

#### *Languages* <a name="languages"></a>

1. [HTML](https://html.spec.whatwg.org/multipage/)

    * The building blocks to everything that is code! Used to create the foundations of Friendly Digest's website.

2. [CSS](https://www.w3.org/Style/CSS/)

    * Who's got style? Used to style Friendly Digest's HTML code.

3. [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

    * Let's get dynamic! Used to bring life into Friendly Digest's code.

4. [Python](https://www.python.org/)

    * The brains behind it all. Used for backend development and database handling.


#### *Libraries* <a name="libraries"></a>

1. [Materialize](https://materializecss.com/)

    * Used for Materialize's grid system, Navigation, mobile responsiveness etc...

2. [Font Awesome](https://fontawesome.com/start)

    * Used to provide quality icons for Friendly Digest's forms, buttons, and footer.
    
3. [Google Fonts](https://fonts.google.com/)

    * Used to change the font throughout Friendly Digest's whole website.

4. [jQuery](https://jquery.com/)

    * Used to manipulate the DOM and bring life to Friendly Digest.

5. [Flask](https://flask.palletsprojects.com/en/1.1.x/)

    *  Flask is the micro web framework that runs the application.

6. [PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)

    * PyMongo was used to enable the Python application to access the Mongo database.

7. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

    * Used as the default templating language for flask and is used to display data from the Python application in the frontend HTML pages.


#### *Tools* <a name="tools"></a>

1. [GitHub](https://github.com/)

    * A code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

2. [GitPod](https://www.gitpod.io/docs/)

    * A cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser.

3. [Git](https://git-scm.com/)

    * A free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

4. [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

    * A global cloud database service for modern applications providing availability, scalability, and compliance with the most demanding data security and privacy standards.

5. [Cloudinary](https://cloudinary.com/)

    * A cloud-based image and video management service. It enables users to upload, store, manage, manipulate, and deliver images and video for websites and apps.

6. [Balsamiq Wireframes 4](https://balsamiq.com/)

    * Used to create Friendly Digest's Wireframes.

7. [Adobe XD](https://www.adobe.com/uk/products/xd.html)

    * Used to create Friendly Digest's logos and Mock Ups.

#### *Hosting* <a name="host"></a>

1. [Heroku](https://www.heroku.com/)

    * Used to host the deployed application.

</div>

---

## :test_tube: **TESTING** <a name="testing"></a>

<div align="justify">

Due to the extensive nature of the testing process, test analysis and reporting can be found by clicking on the following links. 
Here you shall find a separate markdown file as well as two files, one Excel spreadsheet and a downloadable PDF of the same spreadsheet.

* [TESTING.md](https://github.com/WebSlinger88/Friendly-Digest/blob/master/TESTING.md)
* [Friendly Digest Testing Docs](https://github.com/WebSlinger88/Friendly-Digest/tree/master/testing)

</div>

---

## :airplane: **DEPLOYMENT** <a name="deployment"></a>

<div align="justify">

[Heroku](https://www.heroku.com/) has been used to deploy the Friendly Digest website. Developers use Heroku to deploy, manage, and scale modern apps. 
The platform is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market. The Heroku experience provides services, 
tools, workflows, and polyglot support — all designed to enhance developer productivity.

### **DEPLOYMENT TO HEROKU** <a name="heroku"></a>

1. Create Heroku account.
2. Create a new app within Heroku. Set region to Europe.
3. Link new app to your Github repository via the 'Deploy' tab.
4. In the settings tab, navigate to 'Config Vars' and add five fields.
    * `IP: 0.0.0.0`
    * `PORT: 5000`
    * `MONGO_DBNAME: FDDB`
    * `MONGO_URI: mongodb+srv://WebSlinger:************`
    * `SECRET_KEY: ************`
5. Within Gitpod workspace terminal, create 'Procfile' by typing:
    * `$ echo web: python run.py > Procfile`
6. Push repository to Heroku by typing:
    * `$ git push heroku master`

After following these steps, Friendly Digest is now deployed to Heroku and can be seen [here.](https://friendly-digest.herokuapp.com/)

### **LOCAL DEPLOYMENT** <a name="local"></a>

In order to duplicate the database in MongoDB, create a free account on MongoDB and reproduce the 4 collections as described 
[here.](https://res.cloudinary.com/web-slinger/image/upload/v1612366559/Milestone%203/design/mongo-collections_z2ct58.png)

1. Navigate to the Github remote repository: [WebSlinger88: Friendly Digest.](https://github.com/WebSlinger88/Friendly-Digest)
2. Click button labelled "Code" with download icon visible (next to green Gitpod button).
3. Copy the clone HTTPS or SSH by clicking on the copy button.
4. Open your IDE, open a terminal window, and change to the directory where you want to clone this repository.
5. Type: `$ git init` in your IDE's terminal.
6. Type: `$ git clone https://github.com/WebSlinger88/Friendly-Digest.git` in your IDE's terminal.
7. You may need to install or upgrade pip by typing: `$ pip install -U pip` in your IDE's terminal.
8. Install all of the project's requirements by typing: `$ pip3 install -r requirements.txt` in your IDE's terminal.
9. Create a .env file within your IDE directory.
10. Add MongoDB Config Vars data to your .env file.
11. Add your .env file to your .gitignore file. If you do not have a .gitignore file, create one within your IDE directory.
12. In the last line of your run.py file, change from debug=False to debug=True.
13. You will then be able to run the app locally by typing: `$ python3 run.py` in your IDE's terminal.

</div>

---

## :clapper: **CREDITS** <a name="credits"></a>

<div align="justify">

Various websites were used for Friendly Digest's website to become what it is today. All content displayed is part of the public domain.

### **CONTENT** <a name="content"></a>

* Friendly Digest's logo was created and designed by [Lewis Wheeler](https://www.linkedin.com/in/lewis-wheeler-aa91791a0/) - Friendly Digest's Full Stack Web Developer, 
using [Adobe XD](https://www.adobe.com/uk/products/xd.html). Image for the logo was sourced from [Klipartz](https://www.klipartz.com/en).

* All textual content on the Friendly Digest website was written by [Lewis Wheeler](https://www.linkedin.com/in/lewis-wheeler-aa91791a0/) - Friendly Digest's Full Stack Web Developer.

### **MEDIA** <a name="media"></a>

* Imagery:
    * [Klipartz](https://www.klipartz.com/en).
    * [PxHere](https://pxhere.com/).

* Text:
    * [Google Fonts](https://fonts.google.com/).
    * [Font Awesome](https://fontawesome.com/icons?d=gallery&m=free).

### **ACKNOWLEDGEMENTS** <a name="thanks"></a>

Inspiration was used in various locations across the world wide web. Please see below some of the key sources used to help develop Quizzical.

* Code Instiute Video Tutorials.
* [Materialize](https://materializecss.com/) Documentation.
* [w3schools](https://www.w3schools.com/) Documentation.
* [jQuery](https://jquery.com/) Documentation.
* [MongoDB](https://docs.mongodb.com/) Documentation.
* [Heroku](https://devcenter.heroku.com/categories/reference) Documentation.

</div>

---
:star: *A special thank you to [Maranatha Ilesanmi](https://github.com/mbilesanmi) Code Institute Mentor and [Paul F_alumni](https://github.com/Spagettileg) for aid, assistance, and much-needed guidance.* :star:
---

---

***This document is for educational use.***

---
[:arrow_up: Return to top?](#top)