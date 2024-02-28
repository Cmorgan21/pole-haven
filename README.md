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