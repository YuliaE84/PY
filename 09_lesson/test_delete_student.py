from sqlalchemy import create_engine, text

db_connection_string = "postgresql+psycopg2://postgres:fatumss198484@localhost:5432/QA"
db = create_engine(db_connection_string)

conn = db.connect()

def test_delete_student():
    try:
        insert_query = text("INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:uid, :lvl, :edform, :sid)")
        conn.execute(insert_query, {"uid": 3, "lvl": "Beginner", "edform": "group", "sid": 1})
        conn.commit()

        delete_query = text("DELETE FROM student WHERE user_id=:uid")
        conn.execute(delete_query, {"uid": 3})
        conn.commit()

        check_query = text("SELECT COUNT(*) FROM student WHERE user_id=:uid")
        result = conn.execute(check_query, {"uid": 3}).fetchone()
        assert result is not None and result[0] == 0
    except Exception as e:
        raise AssertionError(f"Test failed with error: {e}")
    