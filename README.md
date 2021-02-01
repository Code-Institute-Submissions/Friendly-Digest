<div align="center"> <img src="https://res.cloudinary.com/web-slinger/image/upload/v1608119278/Milestone%203/friendly-digest-favicon_n8ncda.png"> </div>

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

![Responsive showcase image of Friendly Digest website](https://res.cloudinary.com/web-slinger/image/upload/v1612106825/Milestone%203/showcase-img.png "Responsive showcase image of Friendly Digest website")

---

## :sparkles: **UX** <a name="ux"></a>

The user experience (UX) is what a user of a particular product experiences when using that product. A UX designer's job is thus to create a product that 
provides the best possible user experience. We're going to provide some insight into the UX process here, focusing on the important Who, What and How?

Friendly Digest, as previously stated, is a recipe website that's sole purpose is to not only provide people with tasty, clean, easy to follow recipes, 
but to teach and inspire, and to encourage people to share their own ideas. The hope is that anyone can pick up a simple recipe, cook it, and enjoy it
to the extent where they want to share their own. Do you have any tasty recipes that you would like to share? Click the link above, and register an account.

Carry on below and read some of Friendly Digest's user stories, and get a feel for what people originally wanted out of Friendly Digest.

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

The strategy of the Friendly Digest website is to provide good quality recipes to those who struggle to eat the correct foods due to having an illness such as 
an inflammatory bowel disease. It is hoped that people can learn from their experiences, and share what they have found. Our long term ambition is that Friendly
Digest builds an extensive library of recipes far beyond the current scope. Extra categories will be added in the future, along with specific filters for known 
allergens such as gluten and dairy. In the near future we will include a new section of the website dedicated to 'Favourite' recipes. A new function will be added
giving the user the ability to share their favourite recipes via social media platforms such as Facebook, Instagram, and WhatsApp. What's most important is that
people walk away with a feel-good vibe. A happy gut can lead to a happy mind. Our user's health and happiness is of the utmost importance.

---

### **SCOPE** <a name="scope"></a>

The scope of Friendly Digest is to provide a flawless user experience straight from the get-go. We want users to be highly engrossed in what they encounter. We
want users to be attracted to the layout, the colour scheme, the ease of navigation, and the simplicity of the registration / editing process. Ultimately we want
users to return time and time again, not only to absorb information they may not have encountered before, but to share information that may be highly beneficial for 
others.

---

### **STRUCTURE** <a name="structure"></a>

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

---

### **SKELETON** <a name="skeleton"></a>

#### *Sketches* <a name="sketches"></a>

Friendly Digest's website started on a piece of paper. Sketches were drawn out and a decent design was soon ready to leap into the digital world.
Below you shall find a link to a PDF document containing all of the original sketches used to help develop this project.
Please note - you may want to download this file to view it as intended.

* <a href="https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/sketches/ms3-sketches.pdf" target="_blank" rel="noopener">Friendly Digest Sketches PDF</a>

#### *Wireframes* <a name="wireframes"></a>

After drawing up the sketches it was time to get them onto the screen. To do this, a wireframe was created using Balsamiq Wireframes 4. 
Wireframes are used to display what the creator ultimately envisions the website to look like, roughly! It acts as one of the first stepping stones of the journey. 
Please find below a link to a PDF document containing all of the original Wireframes for Friendly Digest's project.
Please note - you may want to download this file to view it as intended.

* <a href="https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/wireframes/ms3-wireframes.pdf" target="_blank" rel="noopener">Friendly Digest Wireframes PDF</a>

#### *Mock Ups* <a name="mockups"></a>

Finally with the basics down on paper and screen, it was time to start shaping things up. After wireframes, it's time to take things a little more seriously. 
Enter Adobe XD. Adobe XD is a powerful piece of software designed to assist artists worldwide. More detailed designs are now progressed, and sketches etc.. 
are now a thing of the past! below, you will find a link to a PDF document containing Friendly Digest's Mock-Ups. You can clearly see how the project has evolved.
Please note - you may want to download this file to view it as intended.

* <a href="https://github.com/WebSlinger88/Friendly-Digest/blob/master/design/mockups/ms3-mockups.pdf" target="_blank" rel="noopener">Friendly Digest Mockups PDF</a>

---

### **SURFACE** <a name="surface"></a>

---

## :page_facing_up: **INFORMATION ARCHITECTURE** <a name="architecture"></a>

### **APPLICATION FRAMEWORK** <a name="app-framework"></a>

### **CSS FRAMEWORK** <a name="css-framework"></a>

### **DATABASE** <a name="database"></a>

---

## :page_facing_up: **EXISTING FEATURES** <a name="existing"></a>

### **NAVIGATION** <a name="navigation"></a>

### **SEARCH RECIPES** <a name="search"></a>

### **HOME PAGE** <a name="home"></a>

### **CATEGORIES** <a name="categories"></a>


#### *Meat* <a name="meat"></a>

#### *Fish* <a name="fish"></a>

#### *Veg* <a name="veg"></a>

#### *Dessert* <a name="dessert"></a>


### **VIEW RECIPES** <a name="recipe"></a>

### **LOG IN** <a name="log-in"></a>

### **REGISTER** <a name="register"></a>

### **MY RECIPES** <a name="my-recipes"></a>

### **ADD RECIPE** <a name="add-recipe"></a>

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