# Blogging Application  

A Django-powered blogging application to create, manage, and share blog posts. The project has moved beyond initialization, with several features now functional and the foundation for a robust blogging platform well underway.  

**Note:** The name of the project is yet to be finalized, so it will temporarily be referred to as **"Blogging Application"**.  

---

## **Purpose**  

The purpose of this project is to create a platform where users can:  

- Write and share blogs.  
- Organize posts by categories and tags.  
- Track and display posts by popularity or personal preference.  

This project also serves as a hands-on learning experience in developing scalable and maintainable Django applications.  

---

## **Features (Planned and Implemented)**  

### **Implemented**  

1. **Create and Manage Blog Posts**:  
   - Users can create and save blog posts.  
   - Dynamic handling of tags (multiple) and categories (single), including:  
     - Automatic creation of new tags if they don’t exist.  
     - Adding new categories directly during post creation.  

2. **Categorization and Filtering**:  
   - Blog posts organized by categories and tags.  

3. **Core Templates and UI**:  
   - `main.html`: Base template for all pages.  
   - `navbar.html`: Reusable navigation bar.  
   - `home.html`: Initial structure for displaying blog posts.  
   - `create_post.html`: A form for blog post creation.  
   - `add_category.html`: Interface for adding new categories dynamically.  

4. **Views and Forms**:  
   - Views: `home`, `createPost`, `addCategory`.  
   - Forms: `PostForm`, `CategoryForm`.  

### **Planned**  

- Saving drafts and publishing posts.  
- Enhanced categorization and filtering options (e.g., search).  
- Responsive and user-friendly design for all devices.  
- Privacy options for blog posts (private vs. public).  
- User authentication for personalized blog management.  

---

## **Current Status**  

- **Core Functionality Added**: Users can now create posts, add new tags and categories, and view blog posts on the homepage.  
- **Project Setup**: The Django project `bloggingApp` is active and functional.  
- **Virtual Environment**: `.venv` is configured for local development.  

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

   ```bash  
   pip install django  
   ```  

4. **Start the Django Development Server**:  

   ```bash  
   python manage.py runserver  
   ```  

---

## **Future Development**  

- Enhance UI with CSS and introduce styling consistency.  
- Expand the blog filtering and categorization features.  
- Implement user authentication for personalized blog management.  
- Add features for saving drafts and scheduling posts.  

---

## **Contributing**  

Contributions are welcome! If you'd like to collaborate, feel free to fork the repository and submit a pull request.  

---

## **License**  

This project is licensed under the MIT License. See the LICENSE file for details.  

---

### **Note**  

This README will continue to be updated as the project evolves, reflecting new features and instructions.  
