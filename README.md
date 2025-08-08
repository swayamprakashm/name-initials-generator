
# **Name Initials Generator**

A simple Flask web app that takes a user's full name and generates their initials.  
Example:  
  Macharla Swayam Prakash → M.S.P.

---

## Features
- Enter full name via a web form
- Extract and display initials (e.g., John Smith → J.S.)
- Responsive, modern UI with gradient background
- Dark Mode Toggle with persistent preference
- Simple and lightweight (only Flask and HTML/CSS/JS)

---

## Project Structure
```

name-initials-generator/
├── app.py                 # Flask application
├── templates/
│   └── index.html         # HTML frontend
├── static/
│   └── style.css          # CSS styling (Light/Dark Mode)
└── README.md              # Project documentation

---
---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/name-initials-generator.git
cd name-initials-generator
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

* Windows: `venv\Scripts\activate`
* Mac/Linux: `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the app

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## Usage

1. Type your full name in the input box.
2. Click "Get Initials".
3. View your initials instantly.
4. Toggle Dark Mode for a different theme.

---

## Screenshots

### Light Mode

![Light Mode Screenshot](screenshots/light-mode.png)

### Dark Mode

![Dark Mode Screenshot](screenshots/dark-mode.png)

---

## Future Improvements

* Allow custom separators (e.g., J-S or J|S)
* Download initials as .txt file
* Add speech-to-text name entry
* Deploy online via Render, Replit, or Vercel

```




