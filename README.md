# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more ...

### 02 Creating apps

> - create django project
> - added some configurations to vs code
> - creating 6 apps
> - git repo

### 3 User App

#### 3.1 Introduction to the User Model (8-02)

> - Added User model (returning Users to admin)
> - Added Biografi field to Users
> - Git repo: 3.1 Introduction to the User Model (8-02)

### 3.2 First Model Fields (11-49)

> - Added avatar, gender and bio field to Users table
> - Distinguishing null=True, blank=True, and default=""
> - Git repo: 3.2 First Model Fields (11-49)

### 3.3 Finishing User Model (7-15)

> - Added more fields (GANDER_CHOICES, CURRENCY_CHOICES, and LANGUANGE_CHOICES) to Users table
> - Git repo: 3.2 First Model Fields (11-49)

### 3.4 Falling in Love with Admin Panel (9-12)

> - Customizing Users panel and filtering users fields
> - Git repo: 3.4 Falling in Love with Admin Panel (9-12)

### 3.5 UserAdmin + CustomAdmin (6-15)

> - Customizing User panel by modifying admin.py
> - Git repo: 3.5 UserAdmin + CustomAdmin (6-15)

### 3.6 RECAP OMG! (11-02)

> - 1. We create django projects with many folders
> - 2. Only one folder is the master, we named it config. The rest are the apps, that is the conversations, lists, reservations, reviews, romms, and users.
> - 3. The apps are just of a group of functionalities.
> - 4. So far, we touch only users app, especially the models.py and admin.py
> - 5. Remember, django uses your codes, NOT the oposite.
> - 6. Django talk to the database by using its ORM which translate your python codes into sql instruction for db.
> - 7. So, what ever you write in the model.py, then ORM will put it into your db table.
> - 8. Model: In the model we wrote the fields for the table. REMEMBER, in order to make our codes work, we MUST follow the django ways, NOT our ways, otherwise we will be in trables.
> - 9. To see how our model works, we must use (register) our model in the admin.py and see the result in admin panel.
> - 10. If we put the registered model ON TOP of the class CustomUserAdmin, then it will controll the model -> then we can modify fields in the db table as we like.
> - 11. FIELDSETS are the things with BLUE COLOR in admin panel.
> - 12. LIST_DISPLAY are things that we see in the admin panel, the way the admin panel look.
> - 13. FILTER is the othe way we can use to display things in admin panel.
> - 14. INHERITANCE: AbstractUser are codes that prepared by django. So, by using AbstractUser, it means that we use/take the ready-made-codes to perform as we like.
> - 15. To use our "users.User" model, we must tell the settings.py by puting this codes "AUTH_USER_MODEL="users.User" in it. In this case, we modify the look of the admin panel as we like by using django user.
> - 16. REGISTER: If you want django to see your app, you MUST REGISTER it in settings.py, otherwise, it will we just a folder for nothing in the project.
> - Git repo: 3.6 RECAP OMG! (11-02)


### 4 Room App

### 4.00 Start from ZERO

> - Delete all migration files
> - Delete the db
> - Re-configure User model
> - Make migrations, migrate, createsuperuser
> - Restart the server
> - Git repo : 4.00 Start from ZERO

### 4.0 TimeStampedModel (7-16)

> - Create an app named it 'core'
> - Register the core app
> - In core/model.py create an abstract class named it 'TimeStampedModel'
> - Note: all the fields in TimeStampedModel will be extended to almost all of the app due to the fields in this model are repeted fields
> - Add class Meta in this model
> - To use 'TimeStampedModel', import it to the respective models of the application
> - Git repo : 4.0 TimeStampedModel (7-16)
