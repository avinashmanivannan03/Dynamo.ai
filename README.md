# Dynamo AI: Inclusive Multi-Lingual AI-Based Chatbot for Enterprises

## Overview

Dynamo AI is an inclusive, multi-lingual AI-powered chatbot designed specifically for enterprises to enhance organizational efficiency. Built with advanced technologies, this platform uses **Retrieval-Augmented Generation (RAG)** on top of **LLAMA 3.1** to provide accurate, context-aware responses to user queries.

This solution is designed to boost productivity, improve decision-making, and ensure data security, all while offering an engaging and personalized user experience.

## Features

- **Multi-lingual Support**: The chatbot supports multiple languages for both input and output (text and audio), ensuring accessibility and inclusiveness across diverse user groups.
- **Role-Based Access Control (RBAC)**: The system implements **Role-Based Access to Content**, allowing fine-grained control over document access. Only authorized users can access sensitive information.
- **Two-Factor Authentication (2FA)**: Integrated 2FA via **Gmail SMTP** to enhance login security, supporting multiple users simultaneously.
- **Offensive Language Detection**: Utilizes **Contextual Transformers** to detect and prevent the use of offensive language, maintaining a respectful environment.
- **User-Friendly Interface**: The app offers an intuitive user interface, simplifying document upload, query interactions, and ensuring seamless access for multiple users.
- **Open-Source Technology**: Built entirely with open-source software, Dynamo AI is easy to deploy, cost-effective, and easily customizable for enterprise needs.

## Technologies Used

- **LLAMA 3.1** (for RAG-powered chatbot)
- **Streamlit** (for front-end development)
- **Gmail SMTP** (for two-factor authentication)
- **Pydantic** (for data validation)
- **TensorFlow** (for machine learning models)
- **Google Text-to-Speech (gTTS)** (for audio responses)
- **Deep Translator** (for multi-lingual support)
- **Langchain** (for language model integrations)

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository/dynamo-ai.git
    cd dynamo-ai
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

## Usage

- After the app is up and running, visit the local server URL displayed in the terminal (usually `http://localhost:8501`).
- Log in using your credentials, and complete the two-factor authentication (2FA) process.
- You will be able to upload documents, interact with the chatbot, and access content based on your user role.

## Contributing

We welcome contributions to improve the functionality and performance of the application. If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## Team Members

1. **Aditya V**
2. **Ananth Shyam S**
3. **Avinash M**
4. **CH SriCheran**
5. **Sajan A**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
