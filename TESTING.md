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