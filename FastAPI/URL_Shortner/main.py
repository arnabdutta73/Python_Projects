import string
import random
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI()

# Database setup
conn = sqlite3.connect("urls.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS urls (short TEXT PRIMARY KEY, full TEXT)")
conn.commit()

# URL Model
class URL(BaseModel):
    full_url: str

# Function to generate short code
def generate_short_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

# Shorten URL
@app.post("/shorten/")
def shorten_url(url: URL):
    short_code = generate_short_code()
    print("short_code: ", short_code)
    # Ensure URL starts with http:// or https://
    if not url.full_url.startswith(("http://", "https://")):
        url.full_url = "https://" + url.full_url  # Default to https://

    cursor.execute("INSERT INTO urls (short, full) VALUES (?, ?)", (short_code, url.full_url))
    conn.commit()
    return {"short_url": f"http://127.0.0.1:8000/{short_code}"}

# Redirect to Original URL
@app.get("/{short_code}")
def redirect_url(short_code: str):
    cursor.execute("SELECT full FROM urls WHERE short = ?", (short_code,))
    result = cursor.fetchone()
    if result:
        return RedirectResponse(url=result[0])
    raise HTTPException(status_code=404, detail="Short URL not found")
