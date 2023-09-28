# SwapHub 🌐

## Description 📝

**SwapHub** is a Minimal Viable Product (MVP) that serves as a data aggregator for liquidity pools from decentralized exchanges such as Uniswap and PancakeSwap. Built using `Python`, the application fetches the top 10 liquidity pools and stores them in a `PostgreSQL` database for further analysis. Please note that this is a work in progress and will be updated with more features in the future.

## Features 🌟

- 📊 Fetches liquidity pool data from Uniswap and PancakeSwap using `GraphQL`.
- 🗃 Stores pool data in a `PostgreSQL` database.
- 🐍 Written in `Python`.

## Prerequisites 🛠

- Docker 🐳
- Docker Compose 🔄
- Python 3.x 🐍

## Local Setup 🚀

### Step 1: Clone the Repository 📂

```
git clone https://github.com/your-username/SwapHub.git
```

### Step 2: Set up Docker 🐳

If you haven't installed Docker yet, download and install it from [here](https://www.docker.com/products/docker-desktop).

### Step 3: Create a Docker Compose File 📜

Create a `docker-compose.yml` file in the root directory of the project with the following content:

```
version: '3'
services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: yourpassword
      POSTGRES_DB: swap_hub_db
    ports:
      - "5432:5432"
```

### Step 4: Start the Docker Container 🔄

Open your terminal and navigate to the root directory where your `docker-compose.yml` file is located. Run the following command to start the Docker container:

```
docker-compose up -d
```

### Step 5: Install Python Dependencies 🐍

Before running the application, make sure to install the required Python packages. You can install them using `pip` as follows:

```
pip install -r requirements.txt
```

### Step 6: Initialize the Database 🗄️

Once Docker is up and running, you will need to initialize your PostgreSQL database. Use the following commands to create the required tables:

```
python database.py
```

### Step 7: Run the Application 🚀

Now that everything is set up, you can run the application using the following command:

```
python main.py
```

This will fetch data from Uniswap and PancakeSwap, and store it in your local PostgreSQL database.
