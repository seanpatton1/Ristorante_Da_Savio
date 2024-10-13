# Ristorante Da Savio

![Website responsive image](images/responsive.png)

Welcome to Ristorante Da Savio – Your Culinary Journey Begins Here

At Ristorante Da Savio, we've created an online experience that’s as inviting as our in-house dining. Our newly designed website, powered by Django, offers a seamless and intuitive interface for all your reservation needs. Explore our seasonal menus, reserve your table with ease, and manage your bookings effortlessly through our user-friendly system.

Whether you're planning an intimate dinner or a large gathering, our responsive booking platform ensures a smooth experience across all devices. Dive into the vibrant world of Italian cuisine and let us handle the rest.

Your perfect dining experience is just a few clicks away!

Visit the deployed game [here](https://ristorante-da-savio-5fa53f108bbc.herokuapp.com/).

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Project Layout diagram](#project-goals)
    2. [Project Goals](#project-goals)
    3. [Implementation](#Implementation)
    3. [Color Scheme](#color-scheme)
2. [Features](#features)
    1. [Home Page](#home-page)
    2. [About Us](#about-Us)
    3. [Reservation](#reservation)
    4. [Menu](#menu)
    5. [Profile Page](#profile-page)
    6. [Signup](#signup)
    7. [Login](#login)
    8. [Admin Panel](#admin-panel)
    9. [Extra Features](#extra-features)
    10. [Technologies Used](#technologies-used)
    11. [Languages Used](#languages-used)
    12. [Libraries and Programs Used](#libraries-and-programs-used)
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

![ANSI Image](images/colours.png)


## Features

### Home Page

* The homepage features enticing food images accompanied by carefully selected quotes to set the tone and create an inviting atmosphere for visitors. 

![Home Page](images/welcome.png)

### About Us

* This section presents the restaurant's story through captivating images and includes a compelling call to action, inviting users to book their table.

![About Us](images/difficulty.png)

### Reservation

* On this screen, once logged in, users can book a table. A full calendar is available for desktop users, while mobile and tablet users are provided with convenient dropdown options for selecting their reservation date.

![Reservation](images/instructions.png)

### Menu

* This screen displays our menu, providing a detailed overview of all the options available to customers.

![Menu](images/start-game-image.png)

### Profile Page

* This screen presents the user with a list of all their reservations, along with options to edit or delete those reservations and update their profile if desired.

![Profile Page](images/correct-answer.png)

### Signup

* This page allows users to sign up, granting them access to the option of booking a table.

![Signup](images/incorrect-answer.png)

### Log-in

* This page allows the user to log in to their account

![Log-in](images/w-message.png)

### Admin Panel

* Admin privileges allow the restaurant owner to approve and edit bookings.

![Admin Panel](images/l-message.png)


## Technologies Used

### Languages Used

* HTML5(https://en.wikipedia.org/wiki/HTML5)

* CSS(https://en.wikipedia.org/wiki/CSS)

* Python(https://en.wikipedia.org/wiki/Python_(programming_language))

* JavaScript(https://en.wikipedia.org/wiki/JavaScript)

* PostgreSQL(https://en.wikipedia.org/wiki/PostgreSQL)


### Libraries and Programs Used


* [GitPod](https://gitpod.io/)
    - GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/)
    - GitHub was used to store the project after pushing.

* [Am I Responsive?](http://ami.responsivedesign.is/#)
    - Am I Responsive was used to for the beggining image at the beggining of this README

* [CI Python Linter](https://pep8ci.herokuapp.com/#)
    - CI Python Linter was used to validate the Python code.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    - Chrome DevTools was used during development process for code review and fix any visual errors throught the creation of the website.

* [W3C Markup Validator](https://validator.w3.org/)
    - W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/)
    - JSHint was used to validate the JavaScript code.

[Back to top ⇧](#table-of-contents)


## Testing

### Validator errors

### Python

- I have used [CI Python Linter](https://pep8ci.herokuapp.com/)

- I was given the following errors

![Linter Errors](images/linter.png)

- E302 expected 2 blank lines, found 1
    - To fix this I added another line, giving it the required 2 blank lines

- W293 blank line contacts whitespace
    - Removed white space through the code

- E501 line too long (91 > 79 characters)
    - As you can see from the above images there was quite a few over, I adjusted all code onto new lines where required.

- W292 no newline at end of file
    - Added new line at the end of the file

- E128 continuation line under-indented for visual indent
    - fixed indentation issue on linter and then adjusted on the run.py file

![Linter No Errors](images/linter-fixed.png)

### Manual Testing

* Game Testing

    Feature | Outcome | Example | Pass/Fail
    --- | --- | --- | ---
    Welcome message | When the game loads - Welcome message appears  and message asking user if they want to read instructions | ![Welcome Message](images/test-one.png) | Pass - Game screen loads as expected
    Optional instructions | Give user the option to see instructions by pressing either Y or N - pressing Y shows the user the instructions| ![instructions](images/test-two.png) | Pass - User sees instructions
    Optional instructions | Give user the option to see instructions by pressing either Y or N - pressing N takes the user to the difficulty selection screen | ![Difficulty Section](images/test-three.png) | Pass - User is taken to next screen, bypassing instructions.
    User selects letter, fills in guessed letters | User enters letter - guessed letter is added to guessed letters list | ![Guessed Letters One](images/test-four.png) ![Guessed Letters Two](images/test-five.png) | Pass - Letter added
    Confirmation message of correct letter | Message appears confirming the correct user guess | ![Correct Guess](images/test-six.png) | Pass - Message appears
    Confirmation message of incorrect letter | Message appears confirming the incorrect user guess | ![Incorrect Guess](images/test-seven.png) | Pass - Message appears
    Already guessed | user selects a letter already chosen - error message appears | ![Already Selected One](images/test-eight.png) ![Already Selected Two](images/test-nine.png) | Pass - Message appears
    User enters full word | User attempts to guess the word - relevant message appears if correct or incorrect | ![Guess Full Word One](images/test-ten.png) ![Guess Full Word Two](images/test-twelve.png) ![Guess Full Word Three](images/test-eleven.png) | Pass - Message appears
    Invalid entry | User enters incorrect character - correct error message appears | ![Invalid Character](images/test-thirteen.png) | Pass - Message appears
    Empty data entry | User clicks enter or space and enter - message appears telling user of invalid entry | ![Invalid Character Two](images/test-fourteen.png) | Pass - Message appears


[Back to top ⇧](#table-of-contents)

## Finished Product

### Game Page

* Landing Page

![Landing Page](images/landing-page.png)

* Instructions Page

![Instruction Page](images/intructions-page.png)

* Difficulty Page

![Difficulty Page](images/dif-selection-page.png)

* Game Start Page

![Game Start Page](images/game-start-page.png)

* Correct Guess

![Correct Guess](images/correct-guess.png)

* Incorrect Guess

![Incorrect Guess](images/incorrect-guess.png)

* Game Won

![Game Won](images/game-won.png)

* Game Lost

![Game Lost](images/game-lost.png)

* Play Again(No)

![Play Again(No)](images/play-again-no.png)



## Deployment


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

6. Some apps contain sensitive data within the Gitpod workspace, which isn't present in the GitHub repository due to being intentionally protected in the .gitignore file. Although I had no data to protect, the following steps would typically be followed.

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

* [Canva](https://www.canva.com/) - I used this to create the chart

* [CI Python Linter](https://pep8ci.herokuapp.com/#) - I used this to check for errors

* [ChatGPT](https://chatgpt.com/?oai-dm=1) - I used this to create the three groups of lists

### Content

- Throughout the development process of this game, I extensively utilized walkthrough videos as valuable resources. These videos, sourced from various creators, provided invaluable insights and guidance, enabling me to grasp essential concepts and tackle challenges effectively. Specifically, I frequently referred to tutorials hosted by [Kite](https://www.youtube.com/@KiteHQ) on their YouTube channel. Their detailed explanations and demonstrations significantly contributed to my understanding and proficiency in game development. I proceeded to enhance the program by incorporating additional features such as a difficulty selection option and displaying the guessed letters.

[Back to top ⇧](#table-of-contents)

## Acknowledgements

- Marcel, my mentor, provided invaluable guidance throughout the process, helping me maintain focus and steering me in the right direction.
- I'd also like to express my gratitude to my partner, who has shown remarkable patience as I've studied and worked on this project.

[Back to top ⇧](#table-of-contents)
