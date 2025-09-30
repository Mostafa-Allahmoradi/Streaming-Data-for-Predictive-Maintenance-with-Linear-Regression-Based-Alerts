    # OPTIONAL Part 3: Create the Database Table
    # Creates a table in the database (if it doesn’t already exist).
    # This function gets called during initialization (inside init function) to ensure the database is ready.
    
import psycopg2
import pandas as pd

class DBManager:
    
    def __init__(self, columns):
        self.db_config = {
            "host": "ep-spring-surf-adwzqkg9-pooler.c-2.us-east-1.aws.neon.tech",
            "database": "neondb",
            "user": "neondb_owner",
            "password": "npg_2DdhmHi4GxFp",
            "port": "5432",
            "sslmode": "require",
        }
        self.table_name = "robot_readings"
        self.columns = columns
        self.connection = self._connect()

    def _connect(self):
        """Establish a connection to the PostgreSQL database."""
        return psycopg2.connect(**self.db_config)

    # OPTIONAL Part 3: Create the Database Table
    # Creates a table in the database (if it doesn’t already exist).
    def _drop_and_create_table(self):
        """Drop and recreate the robot_readings table from scratch."""
        with self.connection as conn:
            with conn.cursor() as cur:
                cur.execute(f"DROP TABLE IF EXISTS {self.table_name};")
                column_defs = ", ".join([f'"{col}" real' for col in self.columns if "Axis" in col])
                
                # timestamp TIMESTAMPTZ DEFAULT NOW(),

                cur.execute(f"""
                    CREATE TABLE {self.table_name} (
                        Id SERIAL PRIMARY KEY,
                        {column_defs},
                        Time varchar(50)
                    );
                """)
                conn.commit()
        print("🔁 robot_readings table dropped and recreated.")

    def insert_record(self, values):
        # Inserts each record into a Neon PostgreSQL database.
        with self.connection as conn:
            with conn.cursor() as cur:
                placeholders = ", ".join(["%s"] * len(values))
                cols = ", ".join([f'"{col}"' for col in self.columns])
                cur.execute(
                    f"INSERT INTO robot_readings ({cols}) VALUES ({placeholders});", values
                )
                conn.commit()

    def fetch_all(self):
        # print("🔍 Fetching all records from the database...")
        sql_query = f"SELECT * FROM {self.table_name};"

        # Fetches all records from the database.
        with self.connection as conn:
            df = pd.read_sql_query(sql_query, conn) 
            print(f"✅ Successfully loaded {len(df)} rows from {self.table_name} table.")
        return df