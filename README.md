# Pole Haven

Pole Haven is a Pole retail store and blog website. Where polers and ariel altheletes alike can keep up to date on the latest news within the pole community and purchase the newest and comfortable pole gear!

Live Site: [Pole Haven](https://pole-haven-539c8a40c44d.herokuapp.com/)

![Website](/images/live-website.png)

## Contents

- [Design](#design)
  - [The Strategy Plane](#the-strategy-plane)
  - [The Scope Plane](#the-scope-plane)
  - [The Structure Plane](#the-structure-plane)
  - [The Skeleton Plane](#the-skeleton-plane)
  - [The Surface Plane](#the-surface-plane)
- [Agile Methodology](#agile-methodology)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Languages](#languages)
- [Frameworks and Libraries](#frameworks-and-libraries)
- [Tools and Technologies](#tools-and-technologies)
- [Testing and Validation](#testing-and-validation)
- [Bugs and Fixes](#bugs-and-fixes)
- [Deployment](#deployment)
- [Cloning this repository](#cloning)
- [Forking a branch](#forking)
- [Credits](#credits)

## Design

### The Strategy Plane

#### Target Audience:
The target audience for Pole Haven is Pole Dancers, Ariel athletes, and individuals looking to get into pole. The strategy revolves around providing a comprehensive platform that caters to both the experienced pole community and newcomers. 

#### Objectives:
- Provide a centralized hub for the pole community to stay updated on the latest news, trends, and events.
- Offer a seamless shopping experience for high-quality and comfortable pole gear such as pole grips, clothes and accessories.
- Create a supportive and engaging environment for sharing experiences, tips, and knowledge.
- Encourage inclusivity by catering to all skill levels, from beginners to advanced practitioners.

#### Scalability:
The website has been designed with scalability. Allowing pagination and as many posts as possible retaining the same website format throughout the blog and the store. 

For future growth this website has been designed for scalability with minimal changes neede to the website

#### Community:
Allowing users to interact and share their throughts, tips and insights within the blog section with their comments. This allows users to engage in a communtity and use the platform to develop their knowledge

The scope of Pole Haven is outlined based on user stories, ensuring a comprehensive and user-centric experience:

#### Standard User

1. **Navigation:**
   - Users can seamlessly navigate the entire website, ensuring a user-friendly experience across different sections.

2. **Blog Viewing:**
   - Users can view individual blog posts with clear and engaging content.
   - Users have the ability to read articles and view comments for an interactive experience.
   - Users have the ability to engage with the blog and comment their thoughts and opinions with the community

3. **Clear Call to Action:**
   - The website provides clear and concise calls to action, guiding users on how to execute various actions such as making a purchase, subscribing to the newsletter, or participating in community discussions.

   - The website also provides the user with alerts to inform the user if something needs to be done, they have done something or an error has occured.

   - Users will be informed with detail why an error may occure

4. **Store Section:**
   - Users can explore the store section, showcasing a variety of pole gear including pole grips, clothing, and accessories.
   - Each item in the store is presented individually, with detailed information, pricing, and visuals.
   - Users can add items to an order and view their order summary with quantity, price and total price for all items. Users also have the ability to remove an item from the order within the item page
   - Users can view related and suggested items based on the product they have viewed below the item

5. **Filtering Items:**
   - Users have the ability to filter out the category of item for seemeless accesiblity and navigation

6. **User Account Creation:**
   - Users can create accounts to gain additional accessibility features.
   - Account creation provides the ability to comment on blog posts, add items to the basket for future purchase, and track order history.
   - Users will have a more personalised experince with the website with their usernane.


#### Registered User:

7. **Commenting on Blog Posts:**
   - Registered users can leave comments on individual blog posts, promoting community engagement and discussion.

8. **Adding and Removing from Basket:**
   - Registered users have the functionality to add items to their basket for convenient and streamlined shopping.
   - Funcitonality to remove items from the basket for items the user does not want

### Admin User:

9. **Content Management:**
    - Admin users have the ability to manage and update blog content, ensuring the latest and relevant information is available to the community.

10. **Product Management:**
    - Admin users can manage product listings, including adding new items, updating prices, and removing outdated products.

11. **Approve Content:**
    - Admin users can approve comments and content. This is to ensure all content is safe and secure and no harmful content is displayed for users.

This comprehensive scope ensures that Pole Haven caters to the needs of different user segments, providing a seamless and engaging experience for both standard and registered users, while offering premium features for those seeking an enhanced experience. Admin functionalities enable efficient content and product management for a well-maintained platform.

### Structure Plane

The Structure Plane outlines the high-level architecture and organization of Pole Haven, defining the major components and their relationships:

#### Data Model Tables 

The following tables are the data models of the the Store Page. All Models were neccesary for a user to view an item. Add it to an order and delete it from their order

##### Store Models
![Item Model](images/item-model.png)
```
class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=ITEM_CATEGORY, max_length=3)
    item_description = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
```

![Order-item Model](images/order-item-model.png)

```
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

```

![Order Model](images/order-model.png)

```
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

```


The following tables are the data models of the the Blog Page. All Models were neccesary for a user to view a blog page, who it was created by and comment on a specific blog post

##### Blog Models

![Post Model](images/post-model.png)

```
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

```


![Comment Model](images/comment-model.png)

```
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    approved = models.BooleanField(default=False)
```



#### Frontend Architecture:

- **Django Templates and JavaScript:**
  - Frontend components are developed using Django templates and enhanced with JavaScript for dynamic and interactive elements.

- **Responsive Design:**
  - Utilizing responsive design principles to ensure a consistent and user-friendly experience across various devices and screen sizes.

#### Backend Architecture:

- **Django Framework:**
  - Backend server implemented using the Django web framework, handling HTTP requests and integrating seamlessly with the frontend.

- **PostgreSQL Database:**
  - PostgreSQL is used as the relational database to store user accounts, blog content, and product information. 

- **RESTful APIs:**
  - Django REST framework is employed to create RESTful APIs, facilitating data exchange between the frontend and backend.

- **Cloudinary Images:**
- Cloudinary was used for image storing as Cloudinary was a more efficient method for websites that may not have been used or accessed for a period of time

#### User Authentication:

- **Django Authentication System:**
  - User authentication is managed using the built-in Django authentication system for secure and efficient user management.

#### E-commerce Platform:

- **Django Models for Product Listings:**
  - Products in the store are modeled using Django models, and data is retrieved from the PostgreSQL database.

- **Shopping Cart Functionality:**
  - Users can add items to their shopping cart, and the state is managed to ensure a seamless shopping experience.

#### Community Engagement:

- **Django Models for Comments and Discussions:**
  - Blog comments and community discussions are stored in PostgreSQL using Django models.

- **Forum Integration:**
  - Forum discussions are facilitated through Django-powered components.

#### Admin Tools:

- **Django Admin Panel:**
  - Admin users have access to the Django Admin Panel for content and product management.

#### Deployment:

- **Heroku Cloud Platform:**
  - The application is deployed on the Heroku cloud platform, providing scalability and accessibility.

This high-level structure ensures a modular, scalable, and maintainable architecture for Pole Haven. Components and features are organized to provide a seamless and engaging experience for users, while backend systems handle data storage, authentication, and content management efficiently.

### The Skeleton Plane

The Skeleton Plane focuses on the wireframes and basic structure of the user interface. Below are wireframes for key pages:

#### Home Page

![Home Page Wireframe](images/home-page.png)

- The home page displays a clear welcome message for the landing page. Clear call to action for shoppers and cards of the latest items on display

- Blog section to display some of the latest blogs for uses to quickly access if they are looking for blog content

#### About Page

![About Page Wireframe](images/about.png)

- Detailed information about Pole Haven. What our purpose is and how we started

#### Contact Page

![Contact Page Wireframe](images/contact.png)

- Contact Page for users to contact the website. Through an email form

- Subject to filter issue quicker


#### Blog Page

![Blog Page Wireframe](images/blog-page.png)

- Collection of blog posts to view with date created, blog title for reference anad a anchor tag to direct user to more detailed induvidual blog post

- Pagination so users can view more ad older blog posts and easily access them without comprimsing on UX

#### Blog Detail Page
![Blog Detail Page Wireframe](images/blog-detail-page.png)


- Individual blog posts with clear headings, publication date, author, description and a section for user comments

- Allow users to view blog page in a full screen format. This allows them to see the blog in much better detail

#### Store Page

![Store Page Wireframe](images/store-page.png)

- Products listed with images, title and price or discount price if applicable

- Filter options for users to easily navigate and find specific items.

- If a category does not exist this will be displayed to the user

#### Store Detail Page

![Store Detail Page Wireframe](images/store-detail-page.png)

- Products listed with images, descriptions, and prices.

- This also allows authenticated users to add to basket, remove from basket and add a specific quantity. Non authenticated users will be redirected to the login page

- Related products section is also accesed at the bottom of the page with items within the same category

#### Order Summary Page

![Order Summary Wireframe](images/order-summary.png)

- Items ordered are displayed. Quantity and Price / Discount Price and Total of all items

- Adds item in a column fashion so users can easily see what they have ordered

#### Login, Logout Pages

![Login Wireframe](images/pole-haven-sign-in.png)

- Allows users to login to their account

- Redirects users to make an account or recover account if user can't / don't have an account

![Signout Wireframe](images/pole-haven-signout.png)

- Gives the users a prompt to ensure they want to sign out


![Signup Wireframe](images/signup-page.png)
- Username, Password, Confirm Password fields

- Clear Password requirements so user understands what their password has to consist of

- Directory to to Sign in

- Allows users to be redirected to login page if they already have an account


#### Responsive Design

Responsive design has been carfully developed for desktop, tablet, mobile phone repsonsiveness. So users can get the best experience with any device they use to visit the website. 

For best spacing and optimization a hamburger menu will has been used for mobile device users

Hamburger
![Hamburger Menu](images/mobile-hamburger.png)

Blog Page
![Mobile view of blog page](images/mobile-blog.png)

Store
![Mobile view of store](images/mobile-store-display.png)

Viewed Product
![Mobile view of viewed product](images/mobile-product-detail.png)

Footer
![Mobile view of footer](images/mobile-footer.png)

### The Surface Plane

In the Surface Plane, we focus on the visual and sensory elements of the Pole Haven website, ensuring an aesthetically pleasing and engaging user experience.

#### Color Palette

The color palette is chosen to reflect the energetic and vibrant nature of pole dancing and aerial activities. Bright and contrasting colors are utilized to draw attention to key elements, while softer tones enhance readability and overall user comfort.

![Colour Pallete](images/colour-pallet.png)

#### Typography

Clear and readable fonts are selected to enhance the legibility of content across the website. The typography is carefully chosen to convey a modern and dynamic vibe.

Basic and consistont font allows the user to easily and clearly navigate throughout the website without struggling to read content

![Colour Pallete](images/colour-contrast.png)


#### Imagery

High-quality images and visuals are incorporated to showcase pole gear, community events, and the dynamic world of pole dancing. The imagery is curated to resonate with the target audience and evoke a sense of excitement.

- **Carousel Images:** Engaging visuals of the latest blog posts and featured pole gear. This allows a visually appealing method to display what the website has to offer without comprimising on UX 
![Carousel](images/carousel.png)

- **Image Cards:** Eye-catching visuals that complement the blog content.
![Store Page](images/pole-store.png)


#### UI Elements

Consistent and intuitive UI elements are implemented throughout the website to provide a seamless and user-friendly navigation experience. Buttons, forms, and other interactive elements are designed to be easily recognizable and responsive with nice padding and spacing so the website isn't clustered.

- **Buttons:** 
- Bold and Clear button with a hover effect when the user hovers over it. This is a simple, but effective feature for a user to access other pages and content

- Clear call to action

![Button](images/button.png)
- Hover effect

![Button with Hover Effect](images/button-hover.png)


- **Navigation:**
The Navigation was created with simple but effective styling to ensure Users could easily access and visibly see the content. The spacing has been affective by allowing the naviagtion to be readable

The Logo and Website name was another feature of the navigation to effective UX design for the user to see a rememberable logo and the company name

#### Branding

The Pole Haven logo and branding elements are strategically placed to reinforce the identity of the platform. The logo reflects the dynamic and inclusive nature of the pole community.

- **Logo:** Clear and scalable logo placed in the header for brand visibility.

![Logo](./images/pole-haven-logo.png)


In the Surface Plane, our goal is to create a visually appealing and cohesive design that aligns with the brand identity and resonates with the target audience. The combination of color, typography, imagery, UI elements, and branding ensures a memorable and immersive user experience on Pole Haven.

### Agile Methodology

#### User Stories

- User stories are used as a fundamental tool to define and communicate project requirements from an end user's perspective.
- Each user story describes a specific piece of functionality or a feature, outlining what the user wants to achieve.




#### Story Points
- Story points are assigned to user stories to estimate and measure the complexity of implementation.
- This agile estimation technique helps the development team gauge the effort required for each user story.

To view User Stories and Story Points click here [User Stories Project](https://github.com/users/Cmorgan21/projects/3)

#### Sprints Timetable
- The project follows a sprint-based development approach with defined timeframes for each sprint.
- Sprints are organized periods, usually 1-2 weeks, during which a set of user stories are planned, developed, tested, and delivered.

These agile methodologies ensure a flexible and iterative development process, allowing for continuous improvement and adaptability to changing requirements.

| Sprint | Goals                                               | Tasks                                                                      |
|--------|-----------------------------------------------------|----------------------------------------------------------------------------|
| 1      | Initial Setup and Project Structure                | - Project initialization: Django setup, database configuration, and project structure.<br>- Define data models for blog and store.<br>- Implement basic templates for landing page, blog, and store. |
| 2      | Navigation, Footer and Static Pages                        | - Implement a user-friendly navigation system.<br>- Develop static pages: About, Contact, "What We Do".<br>- Style and design static pages for a consistent look and feel. |
| 3      | Blog Functionality                                 | - Develop blog functionality with view and comment features.<br>- Create individual blog post pages with comments.<br>- Implement pagination system for blog posts. |
| 4      | Store Functionality                                | - Implement store functionality to showcase pole gear products.<br>- Create detailed views for individual store items.<br>- Add filtering options for store items by category. |
| 5      | User Authentication and Accounts                   | - Implement user authentication for account creation and login.<br>- Develop user account functionality with additional features.<br>- Enhance user profiles and account settings. |
| 6      | Admin Panel and Content Management                 | - Create an admin panel for content and product management.<br>- Implement content approval and moderation functionalities.<br>- Ensure secure and efficient content management. |
| 7      | Responsive Design and Cross-Browser Compatibility  | - Implement responsive design for a seamless experience on various devices.<br>- Ensure cross-browser compatibility for widespread accessibility.<br>- Conduct testing on different devices and browsers. |
| 8      | Deployment and Final Testing                       | - Prepare for deployment on the Heroku cloud platform.<br>- Perform final testing and validation of the entire application.<br>- Ensure proper documentation for future maintenance. |

### Existing Features

#### Navigation
- The website features a user-friendly navigation system allowing users to seamlessly explore different sections.
- A clear and concise menu structure facilitates easy access to key pages such as Home, Blog, Store, and User Account.
- Brand Logo for a more visually appealing naviation and will help users remeber the website

![Navigation](images/navigation.png)


#### Footer
- The footer provides additional navigation options and essential links for users to access information such as About, Contact, and Policies.

- Quick access to pages from footer with quick links

- Summary of Pole Haven
- Contact text with Developers Links

![footer](images/footer.png)


#### Landing Page
- The landing page welcomes users with a dynamic carousel showcasing the latest blog posts and highlighted pole gear.
- A visually appealing layout encourages users to explore the website further.

**Welcome Section** 
![Welcome Image](images/home-welcome-section.png)

- Clear and Concise Message for users when they enter the website

- Call to action for users looking to shop with direct link to store

**Home Store** 
![Home Store Image](images/home-store-section.png)

- Store section for users to see displayed items as they enter the website. This allows users that are looking for items to see a limited about straight away.

**Home Blog** 
![Home Blog Image](images/home-blog-section.png)

- Blog section to as users naviagte through the home page they can see another quality feature the website has. 

- Detail about what the pole blog page has to offer

- Call to action link directing users to blog page

**Home What we do** 
![What we do Image](images/what-we-do-section.png)

- What we do section for users that are interested a bit more in what Pole Haven do and what they offer. 

- The least important content at the bottom as Most User desire will be to shop or check tips and tricks first


#### About Page
- The About page provides detailed information about Pole Haven, its mission, and the team behind the platform.

- Links directing to the important and main features of the website

![About Page](images/about-page.png)


#### Blog Page
- Users can access a dedicated Blog page that presents a collection of engaging and informative articles.

- Each blog post is displayed with clear headings, publication dates, and an interactive section for user comments.

![Blog Page](images/pole-blog.png)

#### Blog Post Page
- Individual blog post pages allow users to delve into specific topics, providing a comprehensive reading experience.

- A call-to-action button encourages users to explore related blog posts for continuous engagement.


**Blog Post** 
![Blog Post](images/blog-detail.png)

**Blog Comment** 

- Ability to comment on the blog posts and engage with the community and share thoughts

- Users willbe directed to log in if the user has not logged in yet. If the user has logged it they be be presented with a box to input their content

![Blog Comment](images/comments.png)

![Blog Logged in Comment](images/loggedin-comment.png)


#### Store Page
- The Store section showcases a variety of pole gear, including pole grips, clothing, and accessories.
- Each item is presented individually, featuring detailed information, pricing, and visuals to aid users in making informed decisions.

![Store Page](images/pole-store.png)

- Users will be able to filter the category of what they want to view for easier accesibility. If there are no items within the category the user will be informed

![Filter Feature](images/filter-feature.png)

![No items filter](images/no-category-item.png)


#### Store Item Page
- Users can view detailed information about specific store items, including product descriptions and pricing.

- The streamlined layout enhances the shopping experience, allowing users to easily add items to their basket.

**Item Detail Page** 
![Item detail page](images/product-detail-view.png)

**Related Items section** 

- Users can View related items within the category and it will direct them straight to the items page for quick access

- Users will be informed if there are no related products within the catergory.

![Related Products](images/related-products.png)

![No Related Products](images/no-related-products.png)

#### Contact Page
- The Contact page provides a means for users to connect with Pole Haven, fostering communication and engagement.

- Users can submit inquiries or feedback through a user-friendly contact form.

![Contact Page](images/contact-form.png)

- Once user has submited contact form they will be displayed with a contact success form

![Contact Success](images/email-success.png)

#### LogIn, Logout, and Signup Page
- User account functionalities are seamlessly integrated, allowing users to create accounts, log in, and log out.

- Account creation provides users with additional accessibility features, including the ability to comment on blog posts and track order history.

![Signup Page](images/signup.png)

![Signin Page](images/pole-haven-sign-in.png)
![Signout Page](images/pole-haven-signout.png)


These existing features form the foundation of Pole Haven, providing a well-rounded and user-centric experience. Each feature is designed to enhance user engagement, streamline navigation, and offer a seamless platform for both content consumption and shopping.

### Order Summary 
![Signup Page](images/pole-haven-order-summary.png)

## Future Features

### Checkout
- Implementation of a streamlined and user-friendly checkout process for seamless and secure transactions.
- Integration of payment gateways and confirmation mechanisms for successful purchases.

### Liking Posts
- Introduction of a feature that allows users to express their appreciation for blog posts by liking or upvoting them.
- Enhanced engagement through positive feedback and acknowledgment of valuable content.

### Wishlist
- Implementation of a wishlist functionality, enabling users to curate a personalized list of desired products.
- Users can easily add and manage items in their wishlist for future consideration and purchase.

### Profile Pictures
- Integration of profile picture functionality for users to personalize their accounts.
- Users can upload and manage their profile pictures, enhancing the community and social aspects of the platform.

These future features are planned enhancements that will further enrich the user experience on Pole Haven. Each feature aims to provide additional functionality, interactivity, and personalization for users engaging with the platform.

## Languages

- HTML
- CSS 
- Javascript
- Python

## Tools and Technologies

[Heruko](https://www.heroku.com/) - Host website

[Visual Studios](https://code.visualstudio.com/) create website

[Code Anywhere](https://codeanywhere.com/)

[Balsamiq](https://balsamiq.cloud/) - create wireframe of website

[Unsplashed](https://unsplash.com/) - use copyright free images

[Draw.io](http://draw.io)

[Contrast Checker](https://webaim.org/resources/contrastchecker/) - check contrast of colours on wesbite 

[Boostrap](https://getbootstrap.com/)

[ChatGPT](https://chat.openai.com/)

[StackOverflow](https://stackoverflow.com/)

[Cloudinary](https://cloudinary.com) - Image API platform 

[ElephantSQL](https://www.elephantsql.com) - Used to store the PostgreSQL database.

[Canva](https://www.canva.com) - Used to create the website logo image.

[Jshint](https://jshint.com/) - Used to validate the JavaScript code.

[W3C - CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate the CSS code.

[CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate the Python code.

[Nu HTML Checker](https://validator.w3.org/nu/) - Used to validate the HTML code.

## Testing and Validation

The testing approach involves a combination of unit tests, integration tests, and manual testing to ensure the reliability and functionality of the Pole Haven website. 

To view testing click the link below

[Testing Documentation](testing.md)

## Bugs and Fixes
| Bug                                                                                                  | Fix                                                                                                                |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Adding incorrect quantity to the checkout section. It would either add +1 or nothing at all.       | Implemented proper handling of quantity input in the checkout section to accurately reflect user input.          |
| Overriding Bootstrap with custom CSS sheets. Sometimes styles would work, and sometimes they wouldn't. | Resolved CSS conflicts by reordering the stylesheet links and ensuring custom styles did not override Bootstrap styles consistently. |
| Delete functionality within the checkout area for orders not working.                               | Fixed the delete functionality in the checkout area by implementing the removal of items within the item page and updating the order summary accordingly. |

## Cloning this repository

To clone this repository for local development, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
   ```
   git clone https://github.com/your-username/pole-haven.git
   ```
4. cd into project directory

5. 
    ```
    Run python3 manage.py runserver
    ```

## Credits

- [ChatGPT](https://chat.openai.com/auth/login) for helping me understand more indepth about data models and how to create a relationship between models

- [How to override Boostrap 5 with CSS styling](https://stackoverflow.com/questions/46715789/cant-override-bootstrap-class?rq=3) guidance on resolving overriding bootsrap styling with CSS files

- [Procfile Heruko error issue](https://stackoverflow.com/questions/19846342/unable-to-parse-procfile) - for troubleshooting Procfile with case sensitivity for heruko

- [URLS APP Name](https://stackoverflow.com/questions/61254816/what-is-the-purpose-of-app-name-in-urls-py-in-django) - Djanog urls error when django template can't be found solutiokn

## Acknowledgements

- Code Institute for providing the foundation knowledge of creating a full stack application using HTML, CSS, Javascript and Python

- Chatgpt for helping me understand data, resolving bugs and giving feedback on code. 

- Django Documentation

- Bootstrap documentation and installation for use in website

- Stackoverflow for support with overriding Bootstrap and different methods and ways to handle functions within Django