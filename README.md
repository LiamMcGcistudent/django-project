[![Build Status](https://travis-ci.org/LiamMcGcistudent/django-project.svg?branch=master)](https://travis-ci.org/LiamMcGcistudent/django-project)


<h1>Confectionery Castle</h1>

<p>The goal of this project was to create an website using the Django framework containing several applications. I chose to create my own project, rather than follow the brief, and I decided to build a website that allows users to register and purchase baked goods from a bakery, leave reviews and make suggestions for things they would like to see added. A user can purchase any number of items from the store. There is also a statistics page where users can see which products are the most popular, which suggestions have the most upvotes and see how far along the suggestions are via their progress status.</p>

<h2>UX</h2>

<h3>User Stories</h3>

<ul>
    <li>As a user, I would like to be able to register an account and be able to view my profile.</li>
    <li>As a user, I would like to be able to view products and purchase any number of them.</li>
    <li>As a user, I would like to be able to leave a review and give my feedback on the products I purchased, my experience using the site etc.</li>
    <li>As a user, I would like to be able to leave a suggestion as to what I think would a be a great addition/improvement to the site/product selection.</li>
    <li>As a user, I would like to be able to comment on other people's reviews/suggestions to say whether I agree or disagree with them.</li>
    <li>As a user, I would like to be able to upvote suggestions that I think would be beneficial.</li>
</ul>

<h3>Wireframes</h3>

<p>I created my wireframes using Balsamiq and can be found here:</p>

<ul>
    <li><a href="/wireframes/Home_Page.png" target="_blank">Home</a></li>
    <li><a href="/wireframes/Products.png" target="_blank">Products</a></li>
    <li><a href="/wireframes/Reviews.png" target="_blank">Reviews</a></li>
    <li><a href="/wireframes/Suggestions.png" target="_blank">Suggestions</a></li>
    <li><a href="/wireframes/Statistics.png" target="_blank">Statistics</a></li>
    <li><a href="/wireframes/Checkout.png" target="_blank">Checkout</a></li>
    <li><a href="/wireframes/Cart.png" target="_blank">Cart</a></li>
    <li><a href="/wireframes/Profile.png" target="_blank">Profile</a></li>
</ul>

<h2>Existing Features</h2>

<ul>
    <li>Navbar with a logo that links to the home page, and navbar links to all other available pages (Products, Reviews, Suggestions, Stats, Login, Cart and Profile).</li>
    <li>User Registration - To create an account a user must enter an email address, username and password and their first and last names. This functionality was implemented using Django's authentication system. Once they have created an account the user is redirected to the login page.</li>
    <li>Login - A registered user can login using their username and password. Once a user has successfully logged in, they will be redirected to their profile page.</li>
    <li>Logout - A user can log out at any time by clicking on the Logout link on the right-hand side of the navbar. Once logged out the user will be redirected to the Login page.</li>
    <li>User Profile - A logged in user can visit their profile page by clicking on the relevant link in the navbar. The profile page displays their email address, sign-up date and last log in date.</li>
    <li>Products - If a user clicks on 'Products' in the navbar they will be taken to a page containing a list of all the available products. The card displays an image of the product, the name and a partial of the description for the product. Clicking on it links to a more detailed view of the product which gives a full description and the price, as well as the option for the user to add it to their cart.</li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>

