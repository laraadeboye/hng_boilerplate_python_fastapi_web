
# DEVOPS WORKFLOW FOR A PYTHON-FASTAPI BOILERPLATE
### Steps
First run the application locally. it is important to run the application locally first before setting up a CI/CD pipeline. Running the application locally allows you to:

- **Verify Environment Configuration**: Ensure that all environment variables and configurations are correctly set up.
- **Identify Dependencies**: Confirm that all dependencies are installed and compatible.
- **Catch Initial Errors**: Detect and resolve any errors or issues in the application setup.
- **Understand Application Behavior**: Gain a clear understanding of how the application starts, runs, and functions.

## Running the Boiler plate locally
#### Step 1 - Set up the environment

1. Clone the Repository and change directory to the cloned repository.
```sh
git clone https://github.com/laraadeboye/boilerplate_python_fastapi.git

cd boilerplate_python_fastapi
```
2. Set up the database.
We will be using postgresql.
- Start the postgresql database and access the psql cli as user `postgres`:
```sh
sudo service postgresql start
sudo -u postgres psql 
```
- Create a database with password and grant privileges. Replace `mydb`, ` myuser`, `mypassword` with the database name, username and password respectively:
```sh
CREATE DATABASE mydb;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
\q
```
3. Create and Activate a Virtual Environment
```sh
python3 -m venv .venv
source .venv/bin/activate
```
4. Install Dependencies:
```sh
pip install -r requirements.txt
```
5. Set up the environment variables
```sh
cp .env.sample .env
# Edit the .env file with your specific environment variables including the database details.
```
#### Step 2 - Run the application

1. Apply the Database Migrations:
```sh
alembic upgrade head
```

2. Start the FastAPI Server:
```sh
python main.py
```

3. Verify the application
Navigate to the following on your browser:
```sh
http://localhost:7001
http://localhost:7001/docs
http://localhost:7001/redoc
```

*Troubleshooting*: 
If you get errors relating to dependencies, use pip to install the necessary dependencies.

Also errors due to conflicting databases. Comment out the mongo database(no sql) in the main.py. This is because you are running with postgresql.


1. List the database and users in the postgresql machine

```sh
sudo -u postgres psql
psql
```

```sh
\l
\du
\q
```

2. Revoke privileges, drop user from database named `mydb`, user named `myuser`.
```sh
sudo -u postgres psql
psql
```
```sh
REVOKE ALL PRIVILEGES ON DATABASE mydb FROM myuser;
DROP USER myuser;
-- If you want to also drop the database, uncomment the next line
-- DROP DATABASE mydb;
\q
```