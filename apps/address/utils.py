from django.db import connection

def truncate_tables():
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM "address_districtdata"')
        cursor.execute('DELETE FROM "address_countydata"')
        cursor.execute('DELETE FROM "address_cpdata"')
