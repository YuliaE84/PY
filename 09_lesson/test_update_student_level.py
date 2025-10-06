from sqlalchemy import create_engine, text

db_connection_string = "postgresql+psycopg2://postgres:fatumss198484@localhost:5432/QA"
db = create_engine(db_connection_string)

conn = db.connect()

def test_update_student_level():
    try:
        insert_query = text("INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:uid, :lvl, :edform, :sid)")
        conn.execute(insert_query, {"uid": 2, "lvl": "Pre-Intermediate", "edform": "personal", "sid": 1})
        conn.commit()

        update_query = text("UPDATE student SET level=:new_lvl WHERE user_id=:uid")
        conn.execute(update_query, {"new_lvl": "Upper-Intermediate", "uid": 2})
        conn.commit()

        check_query = text("SELECT level FROM student WHERE user_id=:uid")
        result = conn.execute(check_query, {"uid": 2}).fetchone()
        assert result is not None and result[0] == "Upper-Intermediate"
    finally:
        cleanup_query = text("DELETE FROM student WHERE user_id=:uid")
        conn.execute(cleanup_query, {"uid": 2})
        conn.commit()
