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