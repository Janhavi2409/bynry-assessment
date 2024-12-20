# Gas Utility Service

This is a web application designed to streamline gas utility services by allowing users to submit service requests, track their status, and view detailed information about each request. The application provides an easy-to-use interface where users can submit their details and receive real-time updates about their service requests.

## Project Features
- **Submit Service Request**: Users can fill out a form to submit a service request for gas utility services.
- **View Service Request List**: A list of all service requests with their status, including a link to detailed request information.
- **Request Detail**: Users can see detailed information about each service request, including customer name, email, service type, description, and status.

## Requirements

To run this project, you'll need to have Python and Django installed on your machine. The following instructions will help you set up and run the project.

1. **Install Python**: Make sure you have Python 3.6 or above installed on your system.
2. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   ```
3. **Install Dependencies**: In the terminal, navigate to the project folder and run the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not present, you can manually install Django using:
   ```bash
   pip install django
   ```

4. **Run Migrations**: Before starting the server, run the migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**: Start the development server with the following command:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**: Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Application Flow

1. **Homepage**: The homepage displays a "Submit Request" button. Clicking this button smoothly scrolls to the "Submit Request" form.
2. **Submit Request**: Users can fill out and submit the service request form. Upon submission, the request is saved to the database, and the user is shown a confirmation message on the same page.
3. **Request List**: A list of all service requests is displayed, with links to view the detailed information about each request.
4. **Request Details**: Detailed information about a specific service request is displayed on a separate page.

## Templates and Views

- **`base.html`**: The base template includes common HTML structure such as the header, footer, and shared CSS.
- **`request_form.html`**: This template contains the form to submit a service request. It includes form validation and submission handling.
- **`request_list.html`**: Displays a list of all service requests with basic details like customer name, service type, and status.
- **`request_detail.html`**: Displays detailed information for a selected service request.

## Models

- **`ServiceRequest`**: The primary model that stores the details of each service request, such as customer name, email, service type, description, status, etc.

### Model fields:
- `customer_name`: CharField
- `email`: EmailField
- `service_type`: CharField
- `description`: TextField
- `status`: CharField
- `created_at`: DateTimeField
- `resolved_at`: DateTimeField (optional)

## Custom Styles

The application uses a simple CSS stylesheet located in `static/css/styles.css` for basic styling, including layout, button designs, and typography.

## Running Tests

You can run the tests to verify the application functionality using Django's built-in testing framework:
```bash
python manage.py test
```

## Conclusion

This project provides a simple and effective way to submit and track service requests for gas utility services. It uses Django to manage the backend, and the templates and static files provide a responsive and user-friendly frontend.


