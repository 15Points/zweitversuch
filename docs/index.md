---
title: Home
nav_order: 0
---

# To-Do App - Wiederholungsprüfung


## Finn Höhne

Matr.-Nr.
: 1917147

Semester
: 5.



## Eidesstattliche Erklärung

Ich erkläre an Eides statt:

> Diese Arbeit wurde selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entommenen Stellen sind als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen Inhalt und umfasst sowohl diese Dokumentation als auch den als Projektergebnis eingereichten Quellcode.



## Sources

All these sources I used in addition to the given tutorial to Full-Stack-Webdevelopment provided by Prof. Dr. Alexander Eck.

**Sources I used for the flask login and account handling:**
+ <https://flask-login.readthedocs.io/en/latest/> **(mandatory source)**
+ <https://www.youtube.com/watch?v=71EU8gnZqZQ>
+ <https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/>
  Those sources I used for the login and register function in app.py, forms.py, and db.py.

**Sources I used for Bootstrap:**
+ <https://www.youtube.com/watch?v=-qfEOE4vtxE> 
+ <https://getbootstrap.com/docs/5.3/components/buttons/> 
  I used these sources for every html-related element I added to the website, which ranged from elements like the logout button that I added to the base.html to entire HTML pages such as login.html or delete_account.html.

**Sources I used for the account deletion:**
+ <https://stackoverflow.com/questions/42450813/in-flask-how-do-i-prevent-a-route-from-being-accessed-unless-another-route-has> 
  While I didn't directly use code from this source, it provided the idea of not having a separate route for the confirmation page after deleting an account.

**Sources I used for the RESTful API:**
+ <https://flask-restful.readthedocs.io/en/latest/> **(mandatory source)**
+ <https://www.youtube.com/watch?v=GMppyAPbLYk> 
  I referred to these sources for the API that is just chunk of code in app.py.

**Other sources I used:**
+ <https://chat.openai.com>
  I used ChatGPT to improve some texts I had written for the documentation. Additionally, I used it to help me find errors in my code, which was sometimes very useful (though not always).


Last build: {{ site.time | date: '%d %b %Y, %R%:z' }}
{: .fs-2 }