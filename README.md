# Django_Project_1

## Project Requirements

### Main Objective
The main objective behind this project is to build a back-end Django application using what you learn during this week. Moreover, to evaluate Django learning outcomes by applying main concepts using technologies related such as MVT pattern, PostgreSQL, ORM, etc.

### Project Idea

shawer project: It is a consulting service that enables the consultant to create an account and view his profile for users, and the user can view the consultant’s customer comments and also enables him to write a comment and delete it whenever he wants. 


### Essential Requirements

- Create at least two applications.  # DONE, create ShawerApp and User
- Apply MVT pattern through views, templates, and models.  # DONE
- Write Global and Local Routers (URL Mapping). # DONE
- Apply Bootstrap on your templates. # DONE 
- Create at least two models. # DONE, create counselor and comment
- Use string representation on your models. # DONE
- Write at least four different model fields. # DONE, in counselor(first_name,last_name,start_date,expertise_field,...) and comment (name,email,body,comment_date,...)
- Use a one-many relationship between the models.  # DONE, we use relation between counselor profile and comment. each counselor profile has many comment but the comment have one profile.  
- Create an Admin Account. # DONE, user: admin, password: 123456
- Register your models on the Admin page. # DONE
- Customize the Admin page using list_display and list_filter. # DONE
- Serve static and media files on your apps. # DONE
- Connect your project with the PostgreSQL database. # DONE
- Use Django ORM to migrate your models on PostgreSQL. # DONE
- Create a form with form validation.
- Apply CRUD operations on the database. (**Note**: You have to use **all** the following function .all(), .get(), .delete(), and .save()) # DONE

### Optional Requirements
- Use new features to customize your Admin page.
