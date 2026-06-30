from src.loader import DataLoader
from src.writer import DataWriter
from src.database import DatabaseConnector


def main():
    # Load data
    loader = DataLoader()
    data = loader.load_data("data/sample.csv")

    # Write data
    writer = DataWriter()
    writer.write_data(data, "outputs/sample_output.csv")
    writer.write_data(data.to_dict(orient="records"), "outputs/sample_output.json")
    writer.write_data("Sample text file", "outputs/sample_output.txt")
    writer.write_data(data, "outputs/sample_output.pkl")

    # Database
    db = DatabaseConnector()
    db.connect()

    print("Database Connected:", db.is_connected)

    db.close()

    print("Project executed successfully!")


if __name__ == "__main__":
    main()