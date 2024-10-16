# Ristorante Da Savio

![Website responsive image](static/images/responsive-1.png)

Welcome to Ristorante Da Savio – Your Culinary Journey Begins Here

At Ristorante Da Savio, we've created an online experience that’s as inviting as our in-house dining. Our newly designed website, powered by Django, offers a seamless and intuitive interface for all your reservation needs. Explore our seasonal menus, reserve your table with ease, and manage your bookings effortlessly through our user-friendly system.

Whether you're planning an intimate dinner or a large gathering, our responsive booking platform ensures a smooth experience across all devices. Dive into the vibrant world of Italian cuisine and let us handle the rest.

Your perfect dining experience is just a few clicks away!

Visit the deployed game [here](https://ristorante-da-savio-5fa53f108bbc.herokuapp.com/).

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Project Goals](#project-goals)
    2. [Implementation](#Implementation)
    3. [Color Scheme](#color-scheme)
    4. [Database Model](#database-model)
    5. [Wireframes](#wireframes)
2. [Features](#features)
    1. [Home Page](#home-page)
    2. [About Us](#about-Us)
    3. [Reservation](#reservation)
    4. [Menu](#menu)
    5. [Profile Page](#profile-page)
    6. [Signup](#signup)
    7. [Login](#login)
    8. [Admin Panel](#admin-panel)
    9. [Technologies Used](#technologies-used)
    10. [Languages Used](#languages-used)
    11. [Libraries and Programs Used](#libraries-and-programs-used)
4. [Testing](#testing)
    1. [Validator errors](#validator-errors)
    2. [Manual Testing](#manual-testing)
5. [Finished Product](#finished-product)
    1. [Home Page](#home-page)
    2. [About Us](#about-Us)
    3. [Reservation](#reservation)
    4. [Menu](#menu)
    5. [Profile Page](#profile-page)
    6. [Signup](#signup)
    7. [Login](#login)
    8. [Admin Panel](#admin-panel)
6. [Deployment](#deployment)
    1. [GitHub Pages](#github-pages)
7. [Credits](#credits)
    1. [Content](#content)
8. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Project Goals

- I want customers to be able to easily navigate the website and make reservations effortlessly
    - Was this achieved?
        - Yes
    - How was this achieved?
        - The website features a clear and intuitive layout with easy-to-use navigation. The booking system allows users to seamlessly select a date, time, and party size, and submit their reservation details in just a few clicks. The FullCalendar integration enhances user interaction by allowing them to easily select a date from the calendar.

- I want customers to manage their reservations (view, edit, and cancel) directly on the website.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - Once logged in, users can view their reservation history, edit their upcoming reservations, and cancel bookings if needed. This feature ensures flexibility and control for customers managing their dining plans.

- I want the website to be responsive and accessible across all devices, including mobile and tablets.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - The website is built using Bootstrap for responsive design, ensuring optimal display on various screen sizes. A drop-down date selection was added for mobile and tablet screens, with visual elements (such as food pictures) filling in space on larger devices. The design automatically adjusts to the user's device for a smooth experience.

- I want the user registration process to be simple, with an option to include contact information during sign-up.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - The registration form was extended to request additional contact information like phone numbers. The process remains simple and user-friendly, allowing customers to sign up quickly while providing the restaurant with important details for communication.

- I want the website to have a professional and visually appealing design that reflects the restaurant's ambiance.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - The website's design uses clean aesthetics, a well-organized layout, and vibrant food images to represent the atmosphere of Ristorante Da Savio. Additionally, elements like a refined header, styled navigation bar with borders, and a centered footer for social media icons create a polished and professional look.

### Implementation

At the outset of this project, I began by designing the core functionality of the website, including key features such as reservations, user registration, and responsiveness. This initial design, outlined in my project plan, served as the foundation upon which the website was built.

To start, I familiarized myself with Django's structure, using official documentation and online resources to guide me through setting up models, views, and templates. I first implemented a basic layout with static pages, such as the homepage and about page, before incorporating more complex functionality, like the booking system.

Once the core of the website was in place, I focused on extending its functionality to include user authentication, profile management, and reservation editing. I also ensured that the website was responsive by utilizing Bootstrap, refining the design to cater to mobile, tablet, and desktop users.

Throughout the development process, I adhered to the initial project blueprint, making incremental adjustments to meet the specific needs of the restaurant, such as adding features like a calendar for booking and the option for users to manage their reservations.

The final result is a professional, user-friendly, and responsive website that reflects both the vision and technical requirements laid out at the start of the project.


### Color Scheme

- The color palette for the website has been carefully selected to reflect the atmosphere and design of the restaurant itself. Each color complements the others, creating a cohesive and visually pleasing experience that enhances the overall aesthetic. These tones work harmoniously across the site, from the headers and navigation to the footer and interactive elements.

- To provide balance and contrast, forms that appear to users—such as reservation or contact forms—are designed in white. This contrast not only draws the user's attention to important interactive elements but also maintains a clean and modern look, ensuring ease of use while maintaining the sophisticated feel of the restaurant's branding. The combination of these thoughtful color choices creates an inviting and elegant online experience, mirroring the ambiance of the restaurant.

![Colour Image](static/images/colour%20scheme.png)

### Typography

I chose Arial and Whisper as the fonts for the captions and the restaurant name. For the menu, I kept the default font as it complements the overall design. Sans-Serif was the backup

### Database Model

- The database model was designed using DrawSQL, and a relational database is being managed with PostgreSQL.

![Database Image](static/images/postgreSQL.png)

1. User Table:
 - id: A unique identifier for each user (Primary Key).
 - Username: The username for each user, stored as a char field (string).
 - email: The email address for each user, stored as a char field (string).

2. Customer Table:
 - id: A unique identifier for each user (Primary Key).
 - A one-to-one relationship with the User table, indicating that each customer has exactly one associated user account.
 - phone_number: A char field that stores the customer’s phone number.
 - address (optional): A text field that stores the customer’s address, which can be left blank.

3. Booking Table:
 - id: A unique identifier for each user (Primary Key).
 - customer (fk): A foreign key that links to the Customer table, establishing a many-to-one relationship
 - date: A date field representing the booking date.
 - time: A time field representing the time of the booking.
 - guests: An int field storing the number of guests for the booking.
 - special_request: A text field where customers can leave special requests (this field can be optional).
 - created_on: A time field representing when the booking was created.
 - status: A char field storing the status of the booking (e.g., pending, confirmed, or canceled).


### Wireframes

- Wireframes done on Balsamiq

* Home Page

![HomePage](static/images/Home-Balsamiq.png)

* About

![About](static/images/About-us-balsamiq.png)

* Reservation

![Reservation](static/images/Reservation-balsamiq.png)

* Menu

![Menu](static/images/Menu-balsamiq.png)

* Booking

![Booking](static/images/Book-balsamiq.png)

* Login

![Login](static/images/Login-balsamiq.png)

* Profile

![Profile](static/images/Profile-balsamiq.png)


## Features

### Home Page

* The homepage features enticing food images accompanied by carefully selected quotes to set the tone and create an inviting atmosphere for visitors. 

### About Us

* This section presents the restaurant's story through captivating images and includes a compelling call to action, inviting users to book their table.

### Reservation

* On this screen, once logged in, users can book a table. A full calendar is available for desktop users, while mobile and tablet users are provided with convenient dropdown options for selecting their reservation date.

### Menu

* This screen displays our menu, providing a detailed overview of all the options available to customers.

### Profile Page

* This screen presents the user with a list of all their reservations, along with options to edit or delete those reservations and update their profile if desired.


### Signup

* This page allows users to sign up, granting them access to the option of booking a table.


### Log-in

* This page allows the user to log in to their account


### Admin Panel

* Admin privileges allow the restaurant owner to approve and edit bookings.

![Admin Panel](static/images/admin.png)


## Technologies Used

### Languages Used

* HTML5(https://en.wikipedia.org/wiki/HTML5)

* CSS(https://en.wikipedia.org/wiki/CSS)

* Python(https://en.wikipedia.org/wiki/Python_(programming_language))

* JavaScript(https://en.wikipedia.org/wiki/JavaScript)

* PostgreSQL(https://en.wikipedia.org/wiki/PostgreSQL)

* Balsamiq(https://en.wikipedia.org/wiki/Balsamiq)

### Frameworks Used

* [Django](https://www.djangoproject.com/)
    - Django is a high-level Python web framework used for building the backend of the website.

### Libraries and Programs Used


* [GitPod](https://gitpod.io/)
    - GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/)
    - GitHub was used to store the project after pushing.

* [Am I Responsive?](http://ami.responsivedesign.is/#)
    - Am I Responsive was used to for the beginning image at the beginning of this README

* [CI Python Linter](https://pep8ci.herokuapp.com/#)
    - CI Python Linter was used to validate the Python code.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    - Chrome DevTools was used during development process for code review and fix any visual errors throughtout the creation of the website.

* [W3C Markup Validator](https://validator.w3.org/)
    - W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/)
    - JSHint was used to validate the JavaScript code.

[Back to top ⇧](#table-of-contents)


## Testing

### Validator errors

- All testing complete through validators and code passes.

### Python

- I was given the following errors throughout my code which have been adjusted

- E302 expected 2 blank lines, found 1

- W293 blank line contacts whitespace

- E501 line too long (91 > 79 characters)

- W292 no newline at end of file

### Manual Testing

* Page & Functionality Testing

    Feature | Outcome | Pass/Fail
    --- | --- | ---
    Page Carousel | Pictures change - they do not change size or alter the page in any other way. | Pass
    Login  | Prevents login without details - logs in with correct credentials | Pass
    invalid email format | tested and was unable to submit an invalid email address in the field | Pass
    Weak or Mismatched Passwords | Passwords have to be the same and message appears if common/weak password | Pass
    "Remember Me" functionality | selected "Remember Me" on multiple log in's. | Pass
    Updating Account Details | The user is able to change details and save amended information | Pass
    Reservations In Database | THis is checked in admin and reservations are present | Pass
    Logged In | Shows the user their profile page with booking information | Pass
    Logged Out | User cannot view profile page and is unable to book a reservation until logged in | Pass
    Responsiveness Bookings | Admin users are able to change status of booking which is reflected on the website to the user | Pass
    Users | All users can only see the profile page and booking - no admin privileges shown | Pass
    Time | User must select time within 15 minute intervals when booking | Pass
    User Bookings | The user can see all future bookings and can edit this booking | Pass
    Links | Links accross the page work as expected | Pass
    

[Back to top ⇧](#table-of-contents)

## Finished Product

* Landing Page

![Landing Page](static/images/home_page.png)

* About Page

![About Page](static/images/about.png)

* Sign-in

![Sign-in](static/images/sign-in.png)

* Reservation Page

![Reservation Page](static/images/reservation-page.png)

* Make A Reservation

![Make A Reservation](static/images/make-reservation.png)

* Menu

![Menu](static/images/menu.png)

* Profile

![Profile](static/images/profile.png)

* 404

![404](static/images/404.png)


## Deployment

## [Heroku](#heroku)

Deploying this project to Heroku involved several steps:

1. If I installed any packages in Gitpod, I would need to add them to a requirements list.

    - To accomplish this, I'd type pip3 freeze > requirements.txt and press enter. This action updates the requirements.txt file.
    - Then, I would commit and push this to GitHub.
    - Heroku utilizes this list to install the dependencies into the application prior to running the project.
    - However, I didn't require any packages.
    - I navigated to my Heroku dashboard and selected 'create a new app'.

2. I selected a name for my app; each app must have a unique name. Since 'hangman' was already taken, I opted for 'hangman-terminal-game'.

3. I chose my region and clicked 'create app'.

4. Next, I accessed the 'settings' tab located at the top of the page.

6. Some apps contain sensitive data within the Gitpod workspace, which isn't present in the GitHub repository due to being intentionally protected in the .gitignore file. Although I had to input my DATABASE_URL and SECRET_KEY.

    - To do this, I would click 'reveal config vars'.
    - Fill in the key, for example: CREDS.
    - Then, I would copy and paste the contents of the 'CREDS' file into the value field and click 'add'.

7. I included the required buildpacks by selecting the buildpack button.

    - I selected 'python' and pressed 'save changes'.
    - Then, I repeated the process, selecting 'nodejs' this time.
    - I ensured it was done in that order, with 'python' at the top and 'nodejs' below.

8. I scrolled back up to the tab at the top and clicked 'deploy'.

9. I selected 'GitHub' as the deployment method and clicked 'connect to GitHub'.

10. After selecting this, I searched for my GitHub repository name and connected to the correct repository.

11. Then, I scrolled down, where there were two options:

    - The first option is to enable automatic deployment, meaning Heroku will rebuild the app every time I push a change to GitHub.
    - The second option is to manually deploy, which I chose for this project at the beginning and after used automatic deploys.

12. Once all the code is received from GitHub, there is a 'view' button that links to the running app. I clicked this to ensure everything was running as expected.

Go back to [Table of contents](#table-of-contents)

## Credits 

* [drawsql](https://drawsql.app/diagrams) - I used this to create the chart

* All Validators Mentioned - I used all of these tools to check for errors

* [ChatGPT](https://chatgpt.com/?oai-dm=1) - I used this to create the about me text.

* [Pexels](https://www.pexels.com/search/restaurant/) - I used this for images on the website

* [JS Calendar](https://www.jsdelivr.com/package/npm/fullcalendar) - I used this package for the calendar


### Content

- Throughout the development of this project, I used the previous walkthrough as a guide while building it. I also relied on StackOverflow for solutions, and received invaluable support from my mentor and tutors, who provided excellent guidance in troubleshooting. My partner, who is Italian and knowledgeable about Italian cuisine, assisted with the content. Additionally, I watched several Bootstrap tutorials and referenced course materials for help with JavaScript.

[Back to top ⇧](#table-of-contents)

### Future Implementations

- Due to time constraints, there are several features that I have not implemented but plan to include in future releases. These features include the ability to book a table, a "Contact Us" form or live chat, a rating system (such as integration with Trustpilot), and an area where users can provide and save their allergy information.

## Acknowledgements

- Marcel, my mentor, helped me when I was on a tight schedule due to unforseen circumstances. he squeezed in time and helped me alot with the project
- I'd also like to express my gratitude to my partner, who created the menu for me, as she is Italian
- I would also like to thank my family and friends who helped me test the website when required

[Back to top ⇧](#table-of-contents)
