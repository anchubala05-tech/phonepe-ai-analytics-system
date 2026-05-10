from sqlalchemy import create_engine

password = "Anchitha%402005"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/phonepe_ml"
)