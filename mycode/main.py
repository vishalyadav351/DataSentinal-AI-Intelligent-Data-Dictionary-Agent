from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
import csv
import io

from mycode.database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DataSentinel: Intelligent Data Dictionary Agent",
    description="Backend API for Dynamic CSV Ingestion and Schema Exploration"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "DataSentinel Backend is Live!",
        "documentation": "/docs"
    }

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Sirf CSV files allow hain!")
        
    try:
        content = await file.read()
        decoded_content = content.decode("utf-8")
        reader = csv.reader(io.StringIO(decoded_content))
        
        header = next(reader, None)
        
        for row in reader:
            if len(row) >= 2:
                db.execute(
                    text("INSERT IGNORE INTO users (name, email) VALUES (:name, :email)"),
                    {"name": row[0], "email": row[1]}
                )
        db.commit()
        return {"message": f"Success: {file.filename} ka data 'users' table mein upload ho gaya!"}
    except Exception as e:
        db.rollback()
        return {"error": f"Upload fail: {str(e)}"}

@app.get("/tables")
def get_tables(db: Session = Depends(get_db)):
    """Database ki saari tables ki list dikhata hai"""
    result = db.execute(text("SHOW TABLES"))
    return [row[0] for row in result]

@app.get("/schema/{table_name}")
def get_schema(table_name: str, db: Session = Depends(get_db)):
    """Kisi bhi table ka structure (columns & types) batata hai"""
    try:
        result = db.execute(text(f"DESCRIBE {table_name}"))
        columns = [{"name": row[0], "type": row[1]} for row in result]
        return {"tableName": table_name, "columns": columns}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' nahi mili!")

@app.post("/chat")
def chat_with_db(user_query: dict):
    table = user_query.get('tableName', 'Database')
    return {"reply": f"Main {table} ke metadata aur schema ke baare mein aapki help kar sakta hoon!"}