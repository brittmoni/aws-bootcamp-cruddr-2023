import json
import psycopg2
import os

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    print("User Attributes")
    print(user)

    user_display_name = user['name']
    user_handle = user['preferred_username']
    user_email = user['email']
    user_cognito_user_id = user['sub']

    try:
        print("Entered try")
        conn = psycopg2.connect(os.getenv('CONNECTION_URL'))
        cur = conn.cursor()

        sql = f"""
            INSERT INTO public.users (display_name, handle, email, cognito_user_id) 
            VALUES(%s, %s, %s, %s)
        """

        print("SQL Statement")
        print(sql)

        conn = psycopg2.connect(os.getenv('CONNECTION_URL'))
        cur = conn.cursor()
        parameters = [
            user_display_name, user_handle, user_email, user_cognito_user_id
        ]
        cur.execute(sql, *parameters)
        conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event