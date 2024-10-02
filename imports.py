import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import storage
import csv

# Initialize Firestore
cred = credentials.Certificate(r"C:\Users\user\Downloads\harmonycollective-d613d-17ff5af82b24.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Initialize Cloud Storage client
storage_client = storage.Client()

# Reference to your bucket
bucket_name = 'universalsongs'  # Replace with your actual bucket name
bucket = storage_client.bucket(bucket_name)

# Download the CSV file from Cloud Storage
blob = bucket.blob('artits/artists.csv')  # Path to your CSV file in the bucket
csv_file_path = r'C:\Users\user\OneDrive - Strathmore University\Desktop\hc\artists.csv'  # Local path for Windows

# Download the blob to a local file
blob.download_to_filename(csv_file_path)

# Read the artists CSV with specified encoding
with open(csv_file_path, 'r', encoding='utf-8', errors='ignore') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if necessary
    for row in reader:
        artist = row[0]  # Adjust index if necessary

        # Add artist to Firestore
        db.collection('artists').add({
            'name': artist
        })

print("Artists imported successfully!")


