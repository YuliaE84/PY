from sqlalchemy import create_engine, text

db_connection_string = "postgresql+psycopg2://postgres:fatumss198484@localhost:5432/QA"
db = create_engine(db_connection_string)

conn = db.connect()

def test_add_student():
    try:
        insert_query = text("INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:uid, :lvl, :edform, :sid)")
        conn.execute(insert_query, {"uid": 1, "lvl": "Pre-Intermediate", "edform": "group", "sid": 1})
        conn.commit()

        select_query = text("SELECT * FROM student WHERE user_id=:uid")
        result = conn.execute(select_query, {"uid": 1}).fetchone()
        assert result is not None and result[0] == 1
    finally:
        cleanup_query = text("DELETE FROM student WHERE user_id=:uid")
        conn.execute(cleanup_query, {"uid": 1})
        conn.commit()
