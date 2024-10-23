<h1 align="center">Medicine Array</h1>

Medicine Array is a Django-based web application that briefly details the available medicines in <strong>Bangladesh</strong>. This project is designed to visualize medicines data efficiently.

<div align="center">

  ![Screenshot (17)](https://github.com/user-attachments/assets/e3f882ea-8cc3-40e2-ab1d-6f9d84386434)

</div>

## Features

- **View Data**: View the imported data from the database.
- **Search for medicines**: It includes searching the medicine that is available in the market.
- **Responsive Design**: Works well on both desktop and mobile devices.
-
  <details>
  <summary>
      <strong>CSV to SQLite</strong>
  </summary>
  <br> 
    Data was imported straight into the SQLite database using a CSV file. The dataset below is used for medical data.
    <pre><code>https://www.kaggle.com/discussions/general/311821</code></pre>
  </br>
  </details>
  
<h2>Technologies Used</h2>

<ul>
  <li><strong>Backend</strong>: Django 4.x (Python)</li>
  <li><strong>Database</strong>: SQLite</li>
  <li><strong>Frontend</strong>: HTML, CSS, Bootstrap (for responsive design)</li>
  <li><strong>Version Control</strong>: Git</li>
</ul>
  

### Setup Instructions

1. Clone repository:
<pre><code>git clone https://github.com/AHMED-SAFA/Medicines-Array.git</code></pre>

2. Create and activate a virtual environment:
<pre><code>python -m venv .venv
source .venv/Scripts/activate</code></pre>

3. Install the required dependencies:
<pre><code>pip install -r requirements.txt
pip install django</code></pre>

4. Apply migrations to set up the SQLite database:
<pre><code>python manage.py migrate
python manage.py makemigrations</code></pre>

5. Create a superuser to access the Django admin panel:
<pre><code>python manage.py createsuperuser</code></pre>

6. Run the development server:
<pre><code>python manage.py runserver</code></pre>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
