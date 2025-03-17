# OpenMarket Application Documentation

## Overview

OpenMarket is a dynamic and user-friendly web application that allows users to buy and sell items with ease. Users can create accounts, list items for sale, and purchase items listed by others. The application also includes a budget tracker, ensuring that users can monitor their spending and earnings directly on the platform. Designed and developed by Yuuto Akihiro in 2025, OpenMarket serves as a portfolio project and a practical exercise in building web applications using Flask and SQLite.

---

## Table of Contents

1. Features
2. Application Structure
3. Usage Guide
4. Technical Details
5. Development Insights

---

## 1. Features

### 1.1 Core Features

- **Home Page**: Serves as the landing page for users, providing an overview of the application.
- **Market Page**: Displays items available for purchase, with options for detailed views, purchasing, and filtering by categories.
- **Account Page**: Allows users to manage their listed items, add new items, and track purchased items.
- **Item Transactions**: Users can buy and sell items seamlessly. Purchased items are moved to the account page, and sold items are returned to the market.

### 1.2 User Account Management

- **Registration**: New users can register by providing a username, email, and password.
- **Login**: Existing users can log in to access their accounts.
- **Logout**: Securely logs users out, preventing unauthorized access to account data.

### 1.3 Budget Tracker

- Displays the current balance of the user prominently in the navigation bar.
- Tracks expenses and earnings from buying and selling items.

### 1.4 Interactive Modals

- **Purchase Modal**: Confirms purchases before deducting the cost from the user’s budget.
- **More Info Modal**: Displays additional details about items listed in the market.

---

## 2. Application Structure

### 2.1 Pages

1. **Home Page**

   - Default page for all users.
   - Contains navigation links to other sections of the site.

2. **Market Page**

   - Displays items listed for sale.
   - Users can view, buy, and get detailed information about items.

3. **Account Page**

   - Lists items owned by the user.
   - Provides options to sell owned items or add new items.

### 2.2 Key Functionalities

1. **Adding Items**

   - Users fill out a form with item details (e.g., name, description, price).
   - Items are added to the market and appear on the user’s account page.

2. **Buying Items**

   - Items listed in the market can be purchased.
   - Purchased items are transferred to the user’s account, and the budget is updated accordingly.

3. **Selling Items**

   - Users can list their items back on the market.
   - Upon selling, the item is removed from their account page and appears in the market.

---

## 3. Usage Guide

### 3.1 Getting Started

1. **Registration**

   - Click on the "Register" button on the navigation bar.
   - Provide a username, email, and password.
   - Submit the form to create an account.

2. **Login**

   - If you already have an account, click on the "Login" button.
   - Enter your username and password to access your account.

3. **Logout**

   - Click the "Logout" button to securely log out and return to the Home Page.

### 3.2 Managing Items

1. **Adding Items**

   - Navigate to the "Account Page" and click "Add Item."
   - Fill in the item details and confirm.
   - The item will appear in your account list.

2. **Buying Items**

   - Go to the "Market Page."
   - Click "Purchase" on the desired item and confirm.
   - The item will be added to your account.

3. **Selling Items**

   - On the "Account Page," click "Sell Item" next to an owned item.
   - The item will be listed back on the market.

### 3.3 Viewing Item Details

- Click "More Info" on any item in the market to see additional details provided by the seller.

---

## 4. Technical Details

### 4.1 Frameworks and Libraries

- **Flask**: Backend framework for routing, templates, and database integration.
- **SQLite**: Database used for storing user and item data.
- **Bootstrap**: CSS framework for responsive design and styling.

### 4.2 Database Structure

1. **Users Table**

   - Stores user details, including username, email, password, and balance.

2. **Items Table**

   - Contains item details, including name, description, price, and ownership status.

3. **Transactions Table (optional)**

   - Tracks item transactions for auditing purposes.

### 4.3 Cache Management

- Prevents users from accessing private pages after logout by disabling caching:
  ```python
  @app.after_request
  def add_header(response):
      response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
      response.headers["Pragma"] = "no-cache"
      response.headers["Expires"] = "0"
      return response
  ```

### 4.4 Security Features

- Passwords are securely hashed before storing in the database.
- Pages with sensitive data require user authentication.

---

## 5. Development Insights

### 5.1 Challenges and Solutions

1. **Preventing Unauthorized Access**

   - Implemented `@login_required` decorators to restrict access to private pages.

2. **Database Consistency**

   - Ensured items have unique identifiers and proper ownership tracking to avoid duplicates.

3. **Caching Issues**

   - Addressed by adding headers to disable caching of sensitive pages.

### 5.2 Lessons Learned

- Flask is highly flexible for building dynamic web applications.
- Proper database schema design is crucial for managing user and item data effectively.
- Security measures, such as hashing passwords and disabling caching, are essential in web development.

### 5.3 Future Enhancements

1. **Search and Filter**: Allow users to search for specific items and filter by categories.
2. **Notifications**: Notify users of new items added to the market.
3. **Enhanced Security**: Implement two-factor authentication for added account security.

---

## Conclusion

OpenMarket is a robust platform that demonstrates the core functionalities of a marketplace. With features for account management, item transactions, and budget tracking, it offers a comprehensive user experience. Built using Flask and SQLite, this project showcases the potential of Python-based web development while addressing real-world challenges like security and data consistency.

This application is a testament to Yuuto Akihiro’s dedication to learning and improving as a developer. It serves not only as a portfolio piece but also as a stepping stone toward more advanced projects.

