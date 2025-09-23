    # OPTIONAL Part 3: Create the Database Table
    # Creates a table in the database (if it doesn’t already exist).
    # This function gets called during initialization (inside init function) to ensure the database is ready.
    
import psycopg2

class DBManager:
    
    def __init__(self, db_config, columns):
        self.db_config = db_config
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
                cur.execute("DROP TABLE IF EXISTS robot_readings;")
                column_defs = ", ".join([f'"{col}" real' for col in self.columns if "Axis" in col])
                
                # timestamp TIMESTAMPTZ DEFAULT NOW(),

                cur.execute(f"""
                    CREATE TABLE robot_readings (
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
        print("🔍 Fetching all records from the database...")
        # Fetches all records from the database.
        with self.connection as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM robot_readings;")
                return cur.fetchall()