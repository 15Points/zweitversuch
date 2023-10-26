---
title: Data Model
parent: Technical Docs
nav_order: 3
---

Finn Höhne
{: .label }

# Data model
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


In comparison to the baseline I have added a table called User. It comprises all the necessary data to handle different users namely an id as primary key a username and a password.
I have also added the attribute user_id as a foreign key to both the table To-do and the table List.
