# BloggerPost - Django Blog Website

Welcome to **BloggerPost**, a beautifully designed and functional blog website built using Django. This project allows users to read, create, and manage blog posts in a seamless and engaging way.

## Features

- 🌍 **Home Page:** Displays all blog posts with a clean and modern UI.
- ✍ **Create, Edit & Delete Posts:** Admins can manage blog content effortlessly.
- 🔍 **Search Functionality:** Users can search for specific blog posts.
- 📄 **About Page:** Information about the website and creator.
- 📩 **Contact Page:** Allows users to send messages via Email or LinkedIn.
- 🎨 **Responsive Design:** Built with HTML, CSS, and JavaScript for a visually appealing experience.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default) / PostgreSQL (optional)
- **Deployment:** To be determined (Heroku, AWS, or other platforms)

## Installation & Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/AmoghShukla/Django_Blog_Website_Project.git
   cd Django_Blog_Website_Project
   ```

2. **Create a Virtual Environment & Activate it**
   ```sh
   python -m venv env
   source env/bin/activate  # For macOS/Linux
   env\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a Superuser** (for accessing the admin panel)
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   Open your browser and go to `http://127.0.0.1:8000/`

## Contact Page Functionality

- Users can send messages via **Gmail** directly by clicking the "Send via Email" button.
- The LinkedIn button redirects users to the profile for direct contact.

## Contributing

Contributions are welcome! If you'd like to contribute:
- Fork the repo
- Create a new branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -m "Added new feature"`)
- Push the branch (`git push origin feature-branch`)
- Create a Pull Request

## License

This project is open-source and available under the MIT License.

---
### 🔗 Connect with Me:
- **GitHub:** [AmoghShukla](https://github.com/AmoghShukla)
- **LinkedIn:** [Amogh Shukla](https://www.linkedin.com/in/amoghshukla548)
