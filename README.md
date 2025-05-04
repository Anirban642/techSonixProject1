# Anirban's Portfolio

This is my personal portfolio built using Flask, showcasing my skills, projects, and contact information. It includes a modern, responsive design with smooth hover effects, interactive project cards, and a contact form that saves messages to a SQLite database.

## Features

- **Home**: A welcoming section with a brief introduction about me.
- **About**: A section with details about my background and journey in web development.
- **Projects**: A list of my projects with links to live demos and descriptions.
- **Contact**: A form to send me a message, which is stored in a SQLite database.

## Tech Stack

- **Flask**: Python web framework for building the backend.
- **SQLite**: Lightweight database used to store messages from the contact form.
- **HTML/CSS**: Frontend for structuring and styling the pages.
- **JavaScript**: Added for smooth interactions and form validation.

## Setup

To run this project locally, follow the steps below:

### Prerequisites

- Python 3.x installed on your machine.
- pip (Python package installer).

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/portfolio.git
    cd portfolio
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/` to view the portfolio.

### SQLite Database

The application automatically creates an SQLite database (`database.db`) when you submit the contact form. You can use any SQLite browser to view or edit the messages.

## Customization

- You can customize the content in the `about.html` and `projects.html` pages by editing the respective files.
- Change the contact form action or add new fields as needed.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, feel free to reach out via the contact form or [email me](mailto:your-email@example.com).
