# Testing

## Code Validating

<details>
  <summary>HTML Validator</summary>

  All HTML Pages were ran through HTML Validator to ensure all content was clean and optimised.

  Throughout the test the only warning with all pages was to ensure correct headings were being used. This was due to each html document not displaying the base.html with the other html documents from Django. However correct headings were used

### Home Page
![W3C HTML Validator - Home Page](./static/images/testing-images/html-home.png)

### About Page
![W3C HTML Validator - About Page](./static/images/testing-images/html-about.png)

### Contact Page
![W3C HTML Validator - Contact Page](./static/images/testing-images/html-contact.png)

### Blog Page
![W3C HTML Validator - Blog Page](./static/images/testing-images/html-blog.png)

### Store Detail Page
![W3C HTML Validator - Store Page](./static/images/testing-images/html-about.png)

### Order Summary Page
![W3C HTML Validator - Order Summary Page](link-to-validation-report)

</details>

<details>
  <summary>CSS Validator</summary>

  All styling pages were ran through a CSS Validator to ensure all code was optimised and no errors or bugs could take place.

  All Pages passed the CSS Validator with no erros

### about.css
![W3C CSS Validator - about CSS](./static/images/testing-images/css-about.png)

### blog-styles.css
![W3C CSS Validator - blog styles CSS](./static/images/testing-images/css-blog-styles.png)

### contact.css
![W3C CSS Validator - contact CSS](./static/images/testing-images/css-contact.png)

### forms.css
![W3C CSS Validator - forms CSS](./static/images/testing-images/css-forms.png)

### online-store.css
![W3C CSS Validator - online store CSS](./static/images/testing-images/css-online-store.png)

### styles.css
![W3C CSS Validator - styles CSS](./static/images/testing-images/css-styles.png)

</details>

<details>
<summary>JSHINT</summary>

Overall both javascript files were tested and came back clear. Both files had no errors displayed

Messages.js
![JSHINT - messages.js](./static/images/testing-images/messages-javascript.png)

comments.js 
![JSHINT - comments.js](./static/images/testing-images/comments-javascript.png)
</details>

<details>
<summary>PYLINT</summary>

| App   | File             | Result           |
|-------|------------------|------------------|
| Pole_Store | settings.py       |   4 * Lines too long   |
|  | urls.py       | 4 * Lines too long        |
| about | urls.py       | Pass       |
| | views.py | Pass       |
| blog | views.py | 4 * Lines too long      |
| | urls.py | 2 * Lines too long      |
| | models.py | Pass     |
| | forms.py | Pass     |
| store | urls.py | Pass     |
| | forms.py | Pass     |
| | views.py | Pass     |

Overall the only error encountered throughout the pylint was 'Lines too long'. This could not be changed due to indentation affecting the code or comments of explination for the code.

Overall the rest of the code was clear and had no other errors

</details>

## Lighthouse Score

All Pages were tested with a lighhouse score Desktop and Mobile. This is to ensure the most effecient loading time, SEO, and Accessibiltiy. Here are the scores below

### Home Page
#### Desktop

![Lighthouse Score - Home Page Desktop](./static/images/testing-images/home-desktop.png)

#### Mobile 
![Lighthouse Score - Home Page Mobile](./static/images/testing-images/home-mobile.png)

### About Page

#### Desktop
![Lighthouse Score - Blog Page Desktop](./static/images/testing-images/about-desktop.png)

#### Mobile
![Lighthouse Score - About Page Mobile](./static/images/testing-images/about-mobile.png)

### Contact Page

#### Desktop
![Lighthouse Score - Contact Page Desktop](./static/images/testing-images/contact-desktop.png)

#### Mobile
![Lighthouse Score - Contact Page Mobile](./static/images/testing-images/contact-mobile.png)

### Store Page

#### Desktop
![Lighthouse Score - Store Page Desktop](./static/images/testing-images/store-desktop.png)

#### Mobile
![Lighthouse Score - Store Page Mobile](./static/images/testing-images/store-mobile.png)

### Product Page

#### Desktop
![Lighthouse Score - Product Page Desktop](./static/images/testing-images/product-desktop.png)

#### Mobile
![Lighthouse Score - Product Page Mobile](./static/images/testing-images/product-mobile.png)

### Blog Page

#### Desktop
![Lighthouse Score - Blog Page Desktop](./static/images/testing-images/blog-desktop.png)

#### Mobile
![Lighthouse Score - Blog Page Mobile](./static/images/testing-images/blog-mobile.png)

### Blog Detail Page

#### Desktop
![Lighthouse Score - Blog Page Desktop](./static/images/testing-images/blog-detail-desktop.png)

#### Mobile
![Lighthouse Score - Blog Page Mobile](./static/images/testing-images/blog-detail-mobile.png)

### Order Summary

#### Desktop
![Lighthouse Score - Order Page Desktop](./static/images/testing-images/order-desktop.png)

#### Mobile
![Lighthouse Score - Order Page Mobile](./static/images/testing-images/order-mobile.png)


Overall the lighthouse scores were high and to the best of the abaility to ensure best peformance and accesibility for users. Then only error that I had encountered but couldnt rectify was cloudinary images being displayed an insecure http requests.

After research I could not find a suitable or correct method to remove this error to improve the best practice score.