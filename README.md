# django_crud

https://github.com/HaneenHaashlamoun/django_crud/pull/1

# Feature Tasks and Requirements
- [x] Create snacks_crud_project Django project
- [x] Create snacks app
- [x] Create Snack model
    - title field
    - purchaser field
    - description field
    - Register model with admin
- [x] Create SnackListView that extends appropriate generic view
    - associated url path is an empty string
- [x] Create SnackDetailView that extends appropriate generic view
    - associated url path is `<int:pk>`/
- [x] Create SnackCreateView that extends appropriate generic view
    - associated url path is create/
- [x] Create SnackUpdateView that extends appropriate generic view
    - associated url path is `<int:pk>`/update/
- [x] Create SnackDeleteView that extends appropriate generic view
    - associated url path is `<int:pk>`/delete/
- [x] Add urls to support all views, with appropriate names
- [x] Add templates to support all views
- [x] Add navigation links in appropriate locations to access all pages
- [x] Make all necessary changes to project level files for project to run
    - In other words, make it work