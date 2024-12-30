# microservices/aggregator-service/aggregator.py
import os
import requests
import psycopg2

PATIENT_SERVICE_URL = "http://patient-record-service/patients"
APPOINTMENT_SERVICE_URL = "http://appointment-scheduling-service/appointments"

def get_patient_data():
    resp = requests.get(PATIENT_SERVICE_URL)
    if resp.status_code == 200:
        # For demo, if your service returns a dict, adapt this accordingly
        return resp.json()
    return []

def get_appointment_data():
    resp = requests.get(APPOINTMENT_SERVICE_URL)
    if resp.status_code == 200:
        return resp.json()
    return []

def store_in_redshift(aggregated_data):
    conn = psycopg2.connect(
        dbname=os.getenv("REDSHIFT_DB"),
        user=os.getenv("REDSHIFT_USER"),
        password=os.getenv("REDSHIFT_PASSWORD"),
        host=os.getenv("REDSHIFT_HOST"),
        port=5439
    )
    cursor = conn.cursor()
    # For demonstration, create a simple insert
    insert_query = """
    INSERT INTO appointments_stats (doctor_id, appointments_count, run_date)
    VALUES (%s, %s, CURRENT_DATE)
    """
    for record in aggregated_data:
        cursor.execute(insert_query, (record['doctor_id'], record['count']))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    patients = get_patient_data()
    appointments = get_appointment_data()

    # Dummy logic: count by doctor_id
    aggregated = {}
    for appt in appointments:
        doc_id = appt['doctor_id']
        aggregated[doc_id] = aggregated.get(doc_id, 0) + 1

    aggregated_data = [
        {"doctor_id": doc_id, "count": count}
        for doc_id, count in aggregated.items()
    ]

    store_in_redshift(aggregated_data)
