import boto3
import pygame
import os

# Initialize boto3 client for Polly
polly_client = boto3.Session(
    aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',                     
    aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
    region_name='YOUR_AWS_REGION'
).client('polly')

# Text to be converted to speech
text = "Sàng tiền minh nguyệt quang,Nghi thị địa thượng sương.Cử đầu vọng minh nguyệt,Đê đầu tư cố hương."

# Request speech synthesis
response = polly_client.synthesize_speech(VoiceId='Aditi',
                OutputFormat='mp3', 
                Text = text,
                LanguageCode='vi-VN')

# Save the audio file
filename = 'output.mp3'
with open(filename, 'wb') as file:
    file.write(response['AudioStream'].read())

# Initialize pygame
pygame.mixer.init()

# Load and play the audio file
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

# Wait until the audio is finished playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Unload the file before deletion
pygame.mixer.music.unload()

# Remove the file after playing
os.remove(filename)
