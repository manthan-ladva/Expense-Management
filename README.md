# 💰 Expense Management System

Welcome to the **Expense Management System**! This is a full-stack application built with Python that helps you track and analyze your expenses effortlessly. 🚀

## 📋 Overview

This project consists of:
- **Frontend**: A user-friendly Streamlit app for adding/updating expenses and viewing analytics 📊
- **Backend**: A robust FastAPI server for handling API requests ⚡
- **Utilities**: Reusable modules for database interactions, logging, and configurations 🔧

Perfect for personal finance management or as a learning project for Python web development! 💡

## ✨ Features

- 📅 **Date-based Expense Tracking**: Add and update expenses by date
- 📈 **Analytics Dashboard**: Visualize your spending patterns
- 🗄️ **Database Integration**: Supports MySQL and PostgreSQL
- 🔐 **Secure Credentials**: Environment-based configuration
- 📝 **Logging**: Comprehensive logging with request tracking
- 🧪 **Testable**: Includes test cases for reliability

## 🛠️ Tech Stack

- **Backend**: FastAPI, Pydantic
- **Frontend**: Streamlit
- **Database**: MySQL / PostgreSQL (via custom wrappers)
- **Utilities**: Python logging, dotenv for configs
- **Deployment**: Uvicorn for API, Streamlit for UI

## 🚀 Installation

### Prerequisites
- Python 3.8+
- MySQL or PostgreSQL database
- Git

### Steps

1. **Clone the repository** 📥
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```

2. **Install dependencies** 📦
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** 🔑
   Create a `.env` file in the root directory:
   ```env
   # Database configs (example for PostgreSQL)
   POSTGRES_EXPENSE_HOST=localhost
   POSTGRES_EXPENSE_PORT=5432
   POSTGRES_EXPENSE_DB=expense_db
   POSTGRES_EXPENSE_USER=your_user
   POSTGRES_EXPENSE_PASSWORD=your_password

   # API configs
   LOCAL_API_HOST=http://127.0.0.1:8000

   # Pool settings
   DB_POOL_MIN=2
   DB_POOL_MAX=10
   ```

4. **Set up the database** 🗃️
   - Create your database and tables as per your schema (check `backend/db_helper.py` for details)

## 🎯 Usage

### Run the Backend API
```bash
uvicorn backend.server:app --reload
```
The API will be available at `http://127.0.0.1:8000` 🌐

### Run the Frontend App
```bash
streamlit run frontend/app.py
```
Open your browser to the provided URL and start managing expenses! 🎉

### API Endpoints
- `GET /expenses/{date}`: Fetch expenses for a specific date
- `POST /expenses/{date}`: Add or update expenses for a date

## 📁 Project Structure

```
expense-management-system/
├── backend/
│   ├── __init__.py
│   ├── db_helper.py       # Database operations
│   └── server.py          # FastAPI app
├── frontend/
│   ├── __init__.py
│   └── app.py             # Streamlit app
├── pyreusables/
│   ├── configs/
│   │   └── credentials.py # Config management
│   ├── pydatabase/        # DB wrappers
│   └── utilities/
│       └── pylogger.py    # Logging utilities
├── logs/                  # Log files
├── .env                   # Environment variables
├── requirements.txt       # Dependencies
└── README.md              # This file!
```

## 🤝 Contributing

Contributions are welcome! 🎊 Please:
1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

If you have any questions or issues, feel free to open an issue on GitHub or reach out! 💬

---

Made with ❤️ and Python</content>
<parameter name="filePath">d:\Portfolio\Data-Analysis-Projects\Codebasics Bootcamp\Python\Expense_Management\README.md
