---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

Finn Höhne
{: .label }

# Design decisions
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## 01: Usage of Flask-Login for user account handling

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 09-Oct-2023

### Problem statement

Which Flask extension should I use to facilitate the implementation of user account handling?

### Decision

I have chosen to use Flask-Login because it appeared to be suitable for most of the features I require. While implementing login via RESTful may be somewhat complex, the familiarity I already have with Flask-Login influenced my decision. I believe it will facilitate user account management in this todo web application effectively.

### Regarded options

| **Criterion** | **Flask-HTTPAuth** | **Flask-Login** | **Flask-Praetorian** | **Flask-User** |
| :------------ | :----------------- | :-------------- | :------------------- | :------------- |
| **Know-how** | ❌ No experience with HTTPAuth | ✔️ Some experience with Flask-Login because of the first trial in this course |	❌ No experience with Praetorian |	❌ No experience with Flask-User |
| **Pro and Con** | **Advantages:** Simple and lightweight for implementing HTTP authentication. Suitable for basic use cases where token-based or session-based authentication is not required. **Disadvantages:** Limited in features and may not provide full user management capabilities. Not designed for managing user sessions or handling complex user authentication requirements. | Specifically designed for managing user sessions and authentication. Highly customizable and flexible for tailoring authentication processes to specific needs. Offers security features like password hashing and session management. Disadvantages: May have a learning curve for effective utilization of its features and customization options. | **Advantages:** Tailored for token-based authentication in RESTful applications. Provides features for token generation, validation, and access control. Suitable for securing API endpoints and resources in a RESTful application. **Disadvantages:** less suitable for applications that require traditional user session management and user registration. | **Advantages:** Offers user registration, password reset, email confirmation, and other user management features. Suitable for applications that require a full suite of user account functionality. **Disadvantages:** Adds complexity and features that may not be needed in applications with basic user authentication requirements. May require more effort to customize for specific use cases. |
| **Decisive Factor** | ❌ Flask-HTTPAuth is primarily designed for basic HTTP authentication and may not provide the built-in tools and features required for handling user login and logout operations. | ✔️ Flask-Login aligns with the specific requirements of my web application, including user registration, login, and access control. It offers customization and flexibility, security, and ease of integration. Furthermore, the documentation was most understandable to me, possibly because I already had some prior knowledge about it. | ❌ While Flask-Praetorian excels at token-based authentication for securing RESTful APIs, it may not be as well-suited for managing  traditional user authentication with a web interface. Implementing features like user registration and login forms for web applications may require more custom development work and could be less intuitive compared to using Flask-Login, e.g. | ❌ Flask-User just seemed very complex to me and I didn't look further into it. |

---

## 02: User deletion on an extra page 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 15-Oct-2023

### Problem statement

Should the user deletion be handled on an extra html page or just with a push of a button on a page that already exists?

### Decision

I've added an extra page with a separate route to enhance user awareness regarding their actions before proceeding. The additional page allows for more comprehensive warnings and includes a feature that prompts the user to enter their password as a confirmation of their intent.

(While it is probably possible to achieve the same functionality without adding an extra page, I opted for this approach over a simple button that deletes the account upon clicking.)

### Regarded options

 | **Criterion** | **Just a button** | **An extra page** |
 | :------------ | :---------------- | :---------------- |
 | **Advantages** | ✔️ **Effortless implementation:** This option is definitely easier to implement than the other. **Simplicity:** It streamlines the process, making it easier for users to delete their accounts without additional steps and complexity to the website. **Faster Execution:** Users can delete their accounts quickly, which might be beneficial if they are certain about their decision. | ✔️ **User Confirmation:** It adds an extra layer of security by requiring users to confirm their intent through password entry, reducing the likelihood of accidental deletions. **Reduced Unauthorized Deletions:** Provides better protection against unauthorized deletions as the user's password is required for confirmation. **User Education:** The additional page can include information about the consequences of account deletion, giving users a chance to reconsider their decision. |
 | **Decisive Factor** | ❌ While the just a button offers simplicity and efficiency in account deletion, it lacks the essential elements of user confirmation and education. Without these features, there is a higher risk of accidental deletions and users may not fully understand the implications of their actions. Consequently, this option doesn't align with my commitment to prioritize user safety and informed decision-making, which are essential for a positive user experience. | ✔️ **Enhanced User Experience:** The decisive factor in choosing the option of an extra page is the focus on providing an enhanced user experience. While the just a button offers simplicity and efficiency, the extra page prioritizes user engagement and safety. By requiring user confirmation and offering informative content, it fosters a more responsible and user-centric account deletion process. This approach ensures that users are fully aware of the consequences of their actions and helps them make informed decisions, ultimately leading to a more positive overall user experience. |

---