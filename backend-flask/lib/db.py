from psycopg_pool import ConnectionPool
import os
import re
import sys

class Db:
  def __init__(self):
    self.init_pool()

  def template(name):
    with open('create_activity.sql', 'r') as f:
      sql_query = f.read()

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

# Check for returning in all caps
  def query_commit(self, sql, parameters):
    print("SQL Statement - [commit with returning]-------")
    print(sql + "\n")

    pattern = r"\bRETURNING\b"
    is_returning_id = re.search(pattern, sql)

    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql, parameters)
      if is_returning_id:
        returning_id = cur.fetchone()[0]
      conn.commit()
      if is_returning_id:
        return returning_id
    except Exception as err:
      self.print_sql_err(err)


# commit data such as an insert
  # def query_commit(self, sql, *args):
  #   print("SQL Statement - [commit]-------")
  #   try:
  #     conn = self.pool.connection()
  #     cur = conn.cursor()
  #     cur.execute(sql)
  #     conn.commit()
  #   except Exception as err:
  #     print_sql_err(err)

# return json object
def query_object(self, sql):
  print("SQL Statement - [object] ----------")
  print(sql)
  wrapped_sql = self.query_wrap_object(sql)
  with self.pool.connection() as conn:
    with conn.cursor() as cur:
      cur.execute(wrapped_sql)
      # this will return a tuple
      # the first field being the data
      json = cur.fetchone()
      return json[0]

# return array of json objects
def query_array(self, sql):
  print("SQL Statement - [array] ----------")
  print(sql)

  wrapped_sql = self.query_wrap_array(sql)
  with self.pool.connection() as conn:
    with conn.cursor() as cur:
      cur.execute(wrapped_sql)
      # this will return a tuple
      # the first field being the data
      json = cur.fetchone()
      return json[0]

def query_wrap_object(self, template):
  sql = f"""
  (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
  {template}
  ) object_row);
  """
  return sql

def query_wrap_array(self, template):
  sql = f"""
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
  {template}
  ) array_row);
  """
  return sql

  def print_sql_err(self,err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print ("\npsycopg ERROR:", err, "on line number:", line_num)
    print ("psycopg traceback:", traceback, "-- type:", err_type)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

db = Db()