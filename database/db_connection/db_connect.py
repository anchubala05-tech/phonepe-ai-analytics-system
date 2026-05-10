from sqlalchemy import create_engine

# Replace password with your MySQL password
password = "Anchitha@2005"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/phonepe_ml"
)

print("Database Connected Successfully!")