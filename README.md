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
    <li>Reviews - If a user clicks on 'Reviews' in the navbar they will be taken to a page containing all reviews that they and other users have posted. Clicking on 'Read More' takes the user to a the full review and if they are the author of the review they will be able to edit it. Users can also leave comments.</li>
    <li>Suggestions - If a user clicks on 'Suggestions' in the navbar they will be taken to a page containing all suggestions that they and other users have posted. Clicking on 'View suggestion' takes the user to a the full suggestion where they can upvote the suggestion and leave comments.</li>
    <li>Statistics - Clicking on 'Statistics' in the navbar brings the user to a page with three graphs showing the most popular products based on views, the number of suggestions with a certain status (To do, In progress or Completed) and the most upvoted suggestions.</li>
    <li>Cart - Brings the user to the cart page where they can see what items they have decided to purchase and where they can amend the quantity should they decide they want more or less of said item.</li>
    <li>Checkout - Here the user should fill in a form detailing their full-name, address, phone number, credit card number (Stripe recommends a test number of 4242 4242 4242 4242, do not enter any real credit card information), an expiry month and year, a CVV number (three random digits) and country of residence. The user's shopping cart is also visible at the top of the page. Upon completion the user should click on the Submit Payment button where they will be re directed back to the Products page.</li>
</ul>

<h2>Technologies Used</h2>

<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript/jQuery</li>
    <li>Font Awesome</li>
    <li>Django</li>
    <li>Python</li>
    <li>Stripe</li>
    <li>Whitenoise</li>
    <li>Postgres/Sqlite3</li>
    <li>Bootstrap</li>
</ul>

<h2>Deployment</h2>

<p>This project was created using AWS Cloud 9 and is stored in a repository on github which can be found <a href="https://github.com/LiamMcGcistudent/django-project">here</a>.</p>
<p>The project was hosted on Heroku. The running application is available <a href="https://confectionery-castle.herokuapp.com/">here</a>.</p>

<p>To deploy my project to Heroku I did the following:</p>

<ul>
    <li>Created a requirements.txt file to hold a list of the dependencies needed to run the project.</li>
    <li>Created an env.py file, and added it to .gitignore, to store any environment variables that I didn't want pushed to GitHub.</li>
    <li>Created a new GitHub repository.</li>
    <li>Created a Heroku app with a unique name.</li>
    <li>Connected my GitHub repository to my Heroku app and enabled automatic deploys.</li>
    <li>Under the Deploy tab I scrolled down to add-ons and connected to the Postgres database.</li>
    <li>Under the settings tab, I clicked on Reveal Config Vars and stored the relevant environment variables as cofig variables.</li>
    <li>Ensured all existing migrations were pushed to the new Postgres database by running: python3 manage.py makemigrations python manage.py migrate.</li>
    <li>Created a Procfile at the top level of my project to tell Heroku what kind of app was being deployed.</li>
    <li>Added the Heroku app to ALLOWED_HOSTS in settings.py file.</li>
</ul>

<h2>Testing</h2>

<p>Views, models and forms were validated using the PEP8 checker, there were a couple of warnings regarding line length, but the code would not function if those lines were split up.</p>
<p>All templates were validated using a HTML validator. The only warnings were when the validator failed to recognise the Django template tags.</p>
<p>CSS was validated using the Jigsaw Validator.</p>
<p>The site was tested for responsiveness using the DevTools, various devices of different sizes including smart phones, tablets, larger monitors etc, as well as on different browsers, including Firefox, Opera, IE and Chrome.</p>
<p>To test the registration functionality I created several accounts. I ensured that password validation worked correctly by typing mismatched passwords and attempting to sign up. I also tried to create two different users with the same username and/ or email address to see if this was allowed, it wasn't.</p>
<p>To test the login functionality I used the wrong username/ password combination to see if I could access an account. I also logged in using the correct credentials to make sure I was redirected to the user profile page.</p>
<p>I confirmed that clicking on the checkout button would take me to a payment from asking for the correct details. I filled out the form several times making sure that the relevant error messages were displayed and that the form could not be submitted with blank fields. I also checked that upon successful submission of the form I was redirected back to the 'Products' page.</p>

<h2>Credits</h2>

<h4>Content</h4>
<ul>
    <li>All images used in the project were obtained from <a href="https://pexels.com">Pexels</a> or from a google search with specifications that the pictures were free to use in the public domain.</li>
    <li>The paginator came from the Django documentation and Corey Schafer's YouTube Django tutorials.</li>
    <li>The idea and code for the animated social links in the footer came from MiroslavSvec</li>
    <li>The code used for stripe payments was supplemented by code from Haley from Tutor Support.</li>
</ul>

<h3>Special Thanks</h3>
<p>Thanks to my course mates on Slack who helped solve errors during development and for reviewing my almost finished project and providing constructive feedback.
Thank you to my mentor Moosa Hassan for his help and support throughout development of the project.
And an extraspecial thank you to all the tutors at Code Institute on tutor support for helping me with technical issues and for being so patient with me, even when the issue was very simple.</p>