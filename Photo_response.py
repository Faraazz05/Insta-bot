# Function to generate a fake photo response JSON
def generate_photo_response():
    return {
        'status': 'success',
        'photo_id': 'fake_photo_id_123'
    }

# Generate fake photo response
fake_photo_response = generate_photo_response()

# Print the fake photo response JSON
print(fake_photo_response)
