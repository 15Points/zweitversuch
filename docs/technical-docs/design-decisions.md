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

design decision: 15.10.23 user deletion on an extra page so that the user has to validate that he really wants to delete his account and can’t do it by accident

## 01: User deletion on an extra page 

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
 | **Advantages** | **Effortless implementation:** This option is definitely easier to implement than the other. **Simplicity:** It streamlines the process, making it easier for users to delete their accounts without additional steps and complexity to the website. **Faster Execution:** Users can delete their accounts quickly, which might be beneficial if they are certain about their decision. | **User Confirmation:** It adds an extra layer of security by requiring users to confirm their intent through password entry, reducing the likelihood of accidental deletions. **Reduced Unauthorized Deletions:** Provides better protection against unauthorized deletions as the user's password is required for confirmation. **User Education:** The additional page can include information about the consequences of account deletion, giving users a chance to reconsider their decision. |
 | **Decisive Factor** | ❌ While the just a button offers simplicity and efficiency in account deletion, it lacks the essential elements of user confirmation and education. Without these features, there is a higher risk of accidental deletions and users may not fully understand the implications of their actions. Consequently, this option doesn't align with my commitment to prioritize user safety and informed decision-making, which are essential for a positive user experience. | ✔️ **Enhanced User Experience:** The decisive factor in choosing the option of an extra page is the focus on providing an enhanced user experience. While the just a button offers simplicity and efficiency, the extra page prioritizes user engagement and safety. By requiring user confirmation and offering informative content, it fosters a more responsible and user-centric account deletion process. This approach ensures that users are fully aware of the consequences of their actions and helps them make informed decisions, ultimately leading to a more positive overall user experience. |

---
