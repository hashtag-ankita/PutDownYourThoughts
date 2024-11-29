# Blogging Application

A Django-powered blogging application to create, manage, and share blog posts. This project is currently in the early stages of development, with the groundwork being laid for building a robust blogging platform.

**Note:** The name of the project is yet to be finalized, so it will temporarily be referred to as **"Blogging Application"**.

## **Purpose**

The purpose of this project is to create a platform where users can:

- Write and share blogs.
- Organize posts by categories and tags.
- Track and display posts by popularity or personal preference.

This project will also serve as a hands-on learning experience in developing scalable and maintainable Django applications.

---

## **Features (Planned)**

1. **Create and Manage Blog Posts**:

   - Support for saving drafts and publishing posts.
   - Dynamic handling of categories (single) and tags (multiple).

2. **Categorization and Filtering**:
   - Posts organized by categories and tags.
   - Search and filter options for users.

3. **User Experience Enhancements**:
   - Responsive design for desktop and mobile.
   - Streamlined blog navigation.

4. **Privacy Options**:
   - Ability to keep posts private or make them public.

---

## **Current Status**

- **Project Setup**: The Django project `bloggingApp` has been initialized.
- **Virtual Environment**: A Python virtual environment `.venv` has been created and activated.

---

## **Getting Started**

### **Prerequisites**

Ensure you have the following installed:

- Python (>= 3.8)
- Django (latest stable version)
- pip (Python package manager)

---

### **Setup**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/hashtag-ankita/bloggingApp.git
   cd bloggingApp
   ```

2. **Set Up the Virtual Environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   *(Currently, no dependencies apart from Django are required, but this will change as the project grows.)*

   ```bash
   pip install django
   ```

4. **Start the Django Development Server**:

   ```bash
   python manage.py runserver
   ```

---

## **Future Development**

- Add models for BlogPost, Category, and Tags.

- Create views and templates for blog creation, listing, and detail views.
- Implement authentication for user-specific blog management.
- Enhance the UI using HTML and CSS.

---

## **Contributing**

Contributions are welcome! If you'd like to collaborate, feel free to fork the repository and submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

---

### **Note**

As this project progresses, this README will be updated to reflect the current state and new instructions.
