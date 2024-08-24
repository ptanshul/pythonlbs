import pyodbc

def print_available_odbc_drivers():
  """Prints a list of available ODBC drivers."""
  drivers = pyodbc.drivers()
  for driver in drivers:
    print(driver)

if __name__ == "__main__":
  print_available_odbc_drivers()