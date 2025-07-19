# 🕵️ Chat Insider

**Chat Insider** is a Python-powered tool designed to analyze WhatsApp chat exports from individuals or groups.  
It transforms raw text chats into insightful visual statistics like timelines, message counts, user activity, and more.

---

## 📊 Key Features

- 📅 **Monthly Timeline Analysis**
- ⏰ **Daily and Weekly Chat Trends**
- 📈 **Bar Charts for Most Active Days**
- 👤 **Top Contributors in Group Chats**
- 🧹 **Removes system messages & cleans data**
- 🧠 **Stopword filtering (supports Hinglish)**
- 📤 **Export structured data for analysis**

---

## 📂 Folder Structure

```
Chat-Insider/
├── app.py                  # Main logic runner
├── helper.py               # Functions for plotting/stats
├── preprocessor.py         # Data cleaning
├── stop_hinglish.txt       # Hinglish stopwords
├── Chat_Insider_Logo.png   # Logo/Screenshot
└── README.md               # Project description
```

---





## 📸 Screenshots

### 🖼️ Screenshot 1  
![Screenshot 1](https://github.com/piyush5093/ChatInsider/raw/master/Screenshot%202025-04-26%20090519.png)

### 🖼️ Screenshot 2  
![Screenshot 2](https://github.com/YourUsername/YourRepoName/raw/main/Screenshot%202025-04-26%20090537.png)

### 🖼️ Screenshot 3  
![Screenshot 3](https://github.com/YourUsername/YourRepoName/raw/main/Screenshot%202025-04-26%20090652.png)

### 🖼️ Screenshot 4  
![Screenshot 4](https://github.com/YourUsername/YourRepoName/raw/main/Screenshot%202025-04-26%20090714.png)

### 🖼️ Screenshot 5  
![Screenshot 5](https://github.com/YourUsername/YourRepoName/raw/main/Screenshot%202025-04-26%20090739.png)



---

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas matplotlib seaborn

# Run the application
python app.py
```

---

## 🧠 How it Works

1. Export your WhatsApp chat in `.txt` format.
2. Load it using this tool.
3. The app will:
   - Clean system messages
   - Extract users & messages
   - Generate timelines and charts

---

## 📦 Dependencies

- Python 3.13+
- pandas
- matplotlib
- seaborn

---

## 📌 Future Ideas

- 📊 Pie charts for media vs text vs links
- 📱 Mobile-friendly dashboard
- 🧠 NLP-based message summarization

---

## 👨‍💻 Developed by

**Piyush Sharad Patil**  
Final Year IT Student @ PES Modern College of Engineering, Pune  
Aiming to deliver the best chat insight platform 💬📈
