<div align="center">

<img src="https://res.cloudinary.com/web-slinger/image/upload/v1608119278/Milestone%203/friendly-digest-favicon_n8ncda.png">

# **FRIENDLY DIGEST TESTING** <a name="top"></a>

</div>

<div align="justify">

Within this markdown file, you shall find extensive test analysis and reporting for the Friendly Digest website.
This has been added in a separate file for its readability and user-friendly approach. You can return
to Friendly Digest's main readme file here: [README.md](https://github.com/WebSlinger88/Friendly-Digest/blob/master/README.md).

You can also find an Excel spreadsheet (saved as PDF) containing extensive test analysis and reporting. This spreadsheet is intended to provide a more visual report.
You can find a link to the Excel (PDF) report here: [Friendly Digest Testing PDF]().

</div>

---

## :books: **TABLE OF CONTENTS**

1. [Testing](#testing)
    * [Navigation](#nav-test)
    * [Search Recipes](#search-test)
    * [Home](#home-test)
    * [Categories](#categories-test)
        * [Meat](#meat-test)
        * [Fish](#fish-test)
        * [Veg](#veg-test)
        * [Dessert](#dessert-test)
    * [View Recipe](#recipe-test)
    * [Log In](#log-in-test)
    * [Register](#register-test)
    * [My Recipes](#my-recipes-test)
    * [Add Recipe](#add-recipe-test)
    * [Edit Recipe](#edit-recipe-test)
    * [Delete Recipe](#delete-recipe-test)
    * [Log Out](#log-out-test)
    * [Error Page](#error-test)

2. [Display Testing](#display-test)

3. [Code Validation](#validation)

4. [Other](#other)
    * [Image Size Reduction](#size)
    * [Spelling & Grammar](#spell)
    * [Bugs](#bugs)

---

## :test_tube: **TESTING** <a name="testing"></a>

### **Navigation** <a name="nav-test"></a>

* Navigation bar present within all web pages.
* Navigation bar contains four tabs when not in session, five tabs when in session, across all web pages.
* Recipes tab acts as a dropdown menu. Menu appears when mouse is hovered. True for all web pages.
* Hover.css animation works when mouse is hovered over tabs.
* Color change of dropdown menu tabs when hovered works as expected.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* Log In & Register page buttons at bottom load correct pages. Submit buttons work perfectly.
* Add Recipe button at bottom of My Recipes page loads correct page.
* Search bar submit button loads searchRecipes.html page as expected. Back button returns to previous page as expected.
* All 'Cook' buttons for recipes load the correct recipe page.
* Recipe page back button returns to previous page as expected.
* All 'Edit' buttons work recipes load the correct edit recipe page. 
* Edit page's return button returns to previous page as expected.
* Footer's social links load correct pages as expected.
* Log Out button loads correct page.
* Delete button loads correct page.
* Side Navigation icon appears when under 992px.
* When clicked, side nav appears to right hand side of screen.
* All links within mobile side nav work as expected. Dropdown menu for Recipes also works perfectly.
* All navigation bars and their content are responsive.

***No Issues were found whilst testing the Navigation functionality.***

### **Search Recipes** <a name="search-test"></a>

* Am able to type into search box.
* Submit buttons works without issue.
* Return button returns to previous page as expected.
* When typing known ingredient into box, correct recipes appear.
* When typing random word into box, No Search Results Found message appears, as expected.
* When typing category name into search box, all recipes in category appear, as expected.
* Search box only appears on Category pages, and My Recipes page, as expected.
* Search bar and Search Recipes page are all responsive.

***No Issues were found whilst testing the Search Recipes functionality.***

### **Home** <a name="home-test"></a>

* All text and images are responsive.
* Materialize grid works as expected.
* Carousel scrolls through images as expected with correct interval.
* Carousel gets smaller when under 992px for smaller devices. Works well.
* Materialboxed effect works as expected when clicking images in desktop view.
* Materialboxed effect does not work for Tuna image when in mobile view. [See Bugs](#bugs).
* Info card tabs work perfectly.
* Success Stories' Tooltips appear when images are hovered. As expected.
* Success Stories' Tooltips do not appear in mobile view. As expected.
* Modal messages appear when Success Stories' images are clicked. Both desktop & mobile.

### **Categories** <a name="categories-test"></a>

* All categories are displayed on one HTML file.
* Which category is displayed is determined by which tab is selected by the user.
* The correct heading appears when each category tab is clicked.
* The correct text paragraph appears when each category tab is clicked.
* The correct recipes appear when each category tab is clicked.
* All cards and content are responsive.

#### **Meat** <a name="meat-test"></a>

* Only meat recipes are displayed.
* If there are no meat recipes in database, message is displayed.

#### **Fish** <a name="fish-test"></a>

* Only fish recipes are displayed.
* If there are no fish recipes in database, message is displayed.

#### **Veg** <a name="veg-test"></a>

* Only veg recipes are displayed.
* If there are no veg recipes in database, message is displayed.

#### **Dessert** <a name="dessert-test"></a>

* Only dessert recipes are displayed.
* If there are no dessert recipes in database, message is displayed.

***No Issues were found whilst testing the Categories functionalities.***

### **View Recipe** <a name="recipe-test"></a>

* Correct recipe was loaded when 'Cook' button was clicked.
* All text and images are responsive.
* Collapsible accordian is responsive.
* Collapsible accordian works as expected when clicked.
* Ingredients and Instructions are split into lists. 
* All data from MongoDB is displayed as expected.

***No Issues were found whilst testing the Recipe functionality.***

### **Log In** <a name="log-in-test"></a>

* Log In page is fully responsive.
* Able to type in both username and password fields.
* Characters are hidden within password field.
* Required message appears when submit button is clicked and fields aren't populated.
* Flash message appears if username is incorrect and/or doesn't exist.
* Flash message appears if password is incorrect and/or doesn't exist.
* Flash message is displayed when user logs out and Log In page is loaded.
* Form validation colors display as expected. Red for empty/incorrect entry. Green for correct entry.
* When username and password is entered correctly and submit button is clicked, session begins as expected.

***No Issues were found whilst testing the Log In functionality.***

### **Register** <a name="register-test"></a>

* Register page is fully responsive.
* Able to type in both username and password fields.
* Characters are hidden within password field.
* Required message appears when submit button is clicked and fields aren't populated.
* Required message appears if user doesn't enter enough characters into either field.
* Form validation colors display as expected. Red for empty/incorrect entry. Green for correct entry.
* When username and password is entered correctly and submit button is clicked, session begins as expected.

***No Issues were found whilst testing the Register functionality.***

### **My Recipes** <a name="my-recipes-test"></a>

* My Recipes page is full responsive.
* Page is only accessible when user session is active.
* If user tries yto access another user's page, Log In page will be loaded with flash message.
* Only recipes uploaded by session user are displayed. As expected.
* If no recipes are present, message is displayed stating there are no recipes to display.
* Page header displays session user's username. As expected.
* 'Cook' button loads correct recipe.
* 'Edit' Button loads correct recipe to edit.
* 'Delete' button loads modal message as expected. Clicking 'No' stays on page. Clicking 'Yes' removes recipe from page.
* Search bar will search all recipes in database - this is expected.

***No Issues were found whilst testing the My Recipes functionality.***

### **Add Recipe** <a name="add-recipe-test"></a>

* Add Recipe page is fully responsive.
* Able to type in all text fields.
* Two select dropdown fields (Category & Difficulty) work as expected.
* Images within select dropdown fields display correctly and in the order intended.
* Min and Max length for all fields works as expected.
* Required message appears when submit button is clicked and fields aren't populated.
* Required message appears if user doesn't enter enough characters into either field.
* Form validation colors display as expected. Red for empty/incorrect entry. Green for correct entry.
* Add Recipe button loads correct page and uploads correct data to MongoDB.
* Only issue to mention is Materialize textarea and input tags have different label animations. Unable to equalize.

### **Edit Recipe** <a name="edit-recipe-test"></a>

* Edit Recipe page is fully responsive.
* All fields were automatically populated with correct recipes data.
* Able to type in all text fields.
* Two select dropdown fields (Category & Difficulty) work as expected.
* Images within select dropdown fields display correctly and in the order intended.
* Min and Max length for all fields works as expected.
* Required message appears when submit button is clicked and fields aren't populated.
* Required message appears if user doesn't enter enough characters into either field.
* Form validation colors display as expected. Red for empty/incorrect entry. Green for correct entry.
* Edit Recipe button loads correct page and uploads correct data to MongoDB. Also displays correct Flash message.
* Only issue to mention is Materialize textarea and input tags have different label animations. Unable to equalize.

### **Delete Recipe** <a name="delete-recipe-test"></a>

* When Delete button is clicked, warning modal message appears.
* Clicking 'No' will keep recipe.
* Clicking 'Yes' will remove recipe from all recipe pages and MongoDB entirely.
* Deleting recipe cannot be reversed.
* Delete modal message is fully responsive.

***No Issues were found whilst testing the Delete functionality.***

### **Log Out** <a name="log-out-test"></a>

* When Log Out button is clicked, warning modal message appears for desktop view.
* Modal does not appear for mobile view. This is expected because of issues with Material side nav.
* Clicking 'No' will keep the user in active session.
* Clicking 'Yes' will remove user from active session and load Log In page. Flash message appears as expected.
* Modal message is fully responsive until it diseapprs under 992px.

### **Error Page** <a name="error-test"></a>

* Any user error will force the 404.html page to load.
* If typing a dumby URL into the URL field (http://friendly-digest.herokuapp.com/this/is/a/test), the 404.html page loads.

* Any unexpected server error will force the 500.html page to load.


---

## :tv: **DISPLAY TESTING** <a name="display-test"></a>

---

## :heavy_check_mark: **CODE VALIDATION** <a name="validation"></a>

---

## :memo: **OTHER** <a name="other"></a>

### **IMAGE SIZE REDUCTION** <a name="size"></a>

### **SPELLING & GRAMMAR** <a name="spell"></a>

### **BUGS** <a name="bugs"></a>

---

***This document is for educational use***

---

[:arrow_up: Return to top?](#top)
