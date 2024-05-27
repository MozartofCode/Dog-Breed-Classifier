# Load model directly
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import requests
import torch
import matplotlib.pyplot as plt
import io



# Getting the Pre-trained model from Hugging Face
processor = AutoImageProcessor.from_pretrained("dima806/133_dog_breeds_image_detection")
model = AutoModelForImageClassification.from_pretrained("dima806/133_dog_breeds_image_detection")

def load_image(path):
#     response = requests.get(url)
#     img = Image.open(io.BytesIO(response.content)).convert("RGB")
    
    image = Image.open(path)
    
    return image


def get_breed(path):

        
    image = load_image(path)
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        
        # Get the predicted class
        predicted_class_idx = torch.argmax(outputs.logits, dim=-1).item()

                
        # Get the predicted class
        predicted_class_idx = torch.argmax(outputs.logits, dim=-1).item()

        # Define class labels as per the Kaggle notebook
        class_names = ['Affenpinscher', 'Afghan_hound', 'Airedale_terrier', 'Akita', 'Alaskan_malamute', 'American_eskimo_dog', 
                    'American_foxhound', 'American_staffordshire_terrier', 'American_water_spaniel', 'Anatolian_shepherd_dog', 
                    'Australian_cattle_dog', 'Australian_shepherd', 'Australian_terrier', 'Basenji', 'Basset_hound', 'Beagle', 
                    'Bearded_collie', 'Beauceron', 'Bedlington_terrier', 'Belgian_malinois', 'Belgian_sheepdog', 'Belgian_tervuren', 
                    'Bernese_mountain_dog', 'Bichon_frise', 'Black_and_tan_coonhound', 'Black_russian_terrier', 'Bloodhound', 
                    'Bluetick_coonhound', 'Border_collie', 'Border_terrier', 'Borzoi', 'Boston_terrier', 'Bouvier_des_flandres', 
                    'Boxer', 'Boykin_spaniel', 'Briard', 'Brittany', 'Brussels_griffon', 'Bull_terrier', 'Bulldog', 'Bullmastiff', 
                    'Cairn_terrier', 'Canaan_dog', 'Cane_corso', 'Cardigan_welsh_corgi', 'Cavalier_king_charles_spaniel', 
                    'Chesapeake_bay_retriever', 'Chihuahua', 'Chinese_crested', 'Chinese_shar-pei', 'Chow_chow', 'Clumber_spaniel', 
                    'Cocker_spaniel', 'Collie', 'Curly-coated_retriever', 'Dachshund', 'Dalmatian', 'Dandie_dinmont_terrier', 
                    'Doberman_pinscher', 'Dogue_de_bordeaux', 'English_cocker_spaniel', 'English_setter', 'English_springer_spaniel', 
                    'English_toy_spaniel', 'Entlebucher_mountain_dog', 'Field_spaniel', 'Finnish_spitz', 'Flat-coated_retriever', 
                    'French_bulldog', 'German_pinscher', 'German_shepherd_dog', 'German_shorthaired_pointer', 
                    'German_wirehaired_pointer', 'Giant_schnauzer', 'Glen_of_imaal_terrier', 'Golden_retriever', 'Gordon_setter', 
                    'Great_dane', 'Great_pyrenees', 'Greater_swiss_mountain_dog', 'Greyhound', 'Havanese', 'Ibizan_hound', 
                    'Icelandic_sheepdog', 'Irish_red_and_white_setter', 'Irish_setter', 'Irish_terrier', 'Irish_water_spaniel', 
                    'Irish_wolfhound', 'Italian_greyhound', 'Japanese_chin', 'Keeshond', 'Kerry_blue_terrier', 'Komondor', 'Kuvasz', 
                    'Labrador_retriever', 'Lakeland_terrier', 'Leonberger', 'Lhasa_apso', 'Lowchen', 'Maltese', 'Manchester_terrier', 
                    'Mastiff', 'Miniature_schnauzer', 'Neapolitan_mastiff', 'Newfoundland', 'Norfolk_terrier', 'Norwegian_buhund', 
                    'Norwegian_elkhound', 'Norwegian_lundehund', 'Norwich_terrier', 'Nova_scotia_duck_tolling_retriever', 
                    'Old_english_sheepdog', 'Otterhound', 'Papillon', 'Parson_russell_terrier', 'Pekingese', 'Pembroke_welsh_corgi', 
                    'Petit_basset_griffon_vendeen', 'Pharaoh_hound', 'Plott', 'Pointer', 'Polish_lowland_sheepdog', 'Pomeranian', 
                    'Poodle', 'Portuguese_water_dog', 'Saint_bernard', 'Silky_terrier', 'Smooth_fox_terrier', 
                    'Soft_coated_wheaten_terrier', 'Spinone_italiano', 'Staffordshire_bull_terrier', 'Standard_schnauzer', 
                    'Sussex_spaniel', 'Tibetan_mastiff', 'Tibetan_terrier', 'Toy_fox_terrier', 'Vizsla', 'Weimaraner', 
                    'Welsh_springer_spaniel', 'West_highland_white_terrier', 'Whippet', 'Wirehaired_pointing_griffon', 'Yorkshire_terrier']

        # Get the class label
        predicted_class_label = class_names[predicted_class_idx]
        print(f"Predicted breed: {predicted_class_label}")

        return predicted_class_label