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

Für diese Webanwendung verwende ich Python und Flask. Vieles an Code war bereits vorgegeben. Meine Aufgabe ist es, die bereits vorhandene Applikation, um User-handling und eine API zu erweitern. 

Deshalb werde ich während der Bearbeitung vermutlich:

+ Mehrere Ansätze versuchen, um das User-handling erfolgreich zu implementieren

+ Den bereits vorhandenen Code teilweise verändern


### Decision

I've added an extra page with a separate route to enhance user awareness regarding their actions before proceeding. The additional page allows for more comprehensive warnings and includes a feature that prompts the user to enter their password as a confirmation of their intent.

(While it is probably possible to achieve the same functionality without adding an extra page, I opted for this approach over a simple button that deletes the account upon clicking.)

### Regarded options

| **Criterion** | **Just a button** | **An extra page** |
| :------------ | :---------------- | :---------------- |
| **advantages** | 
+ **effortless implementation:** this option is definitely easier to implement than the other  
+ **Simplicity:** It streamlines the process, making it easier for users to delete their accounts without additional steps and complexity to the website.
+ **Faster Execution:** Users can delete their accounts quickly, which might be beneficial if they are certain about their decision. |     
+ **User Confirmation:** It adds an extra layer of security by requiring users to confirm their intent through password entry, reducing the likelihood of accidental deletions.
+ **Reduced Unauthorized Deletions:** Provides better protection against unauthorized deletions as the user's password is required for confirmation.
+ **User Education:** The additional page can include information about the consequences of account deletion, giving users a chance to reconsider their decision. |
| **disadvantages** |     

| **decisive factor** |

---
