import cv2
import numpy as np
from PIL import Image
import io
import os
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from typing import Optional, List

class ImageProcessor:
    def __init__(self):
        # Cargar modelo preentrenado VGG16
        self.model = VGG16(weights='imagenet', include_top=False, pooling='avg')
        
    def extract_features(self, img_path: str) -> Optional[np.ndarray]:
        """Extrae características de una imagen usando VGG16"""
        try:
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            features = self.model.predict(img_array, verbose=0)
            return features.flatten()
        except Exception as e:
            print(f"Error extrayendo características de {img_path}: {e}")
            return None

    def extract_features_from_bytes(self, file_content: bytes) -> Optional[np.ndarray]:
        """Extrae características de una imagen desde bytes"""
        try:
            img = Image.open(io.BytesIO(file_content))
            img = img.convert('RGB')
            img = img.resize((224, 224))
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            features = self.model.predict(img_array, verbose=0)
            return features.flatten()
        except Exception as e:
            print(f"Error extrayendo características de imagen: {e}")
            return None

    def calculate_similarity(self, features1: np.ndarray, features2: np.ndarray) -> float:
        """Calcula la similitud coseno entre dos vectores de características"""
        try:
            similarity = cosine_similarity(
                features1.reshape(1, -1),
                features2.reshape(1, -1)
            )[0][0]
            return float(similarity)
        except Exception as e:
            print(f"Error calculando similitud: {e}")
            return 0.0

    def find_image_by_barcode(self, barra: str, images_dir: str = "images") -> Optional[str]:
        """Busca una imagen por código de barra"""
        extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']
        for ext in extensions:
            img_path = os.path.join(images_dir, f"{barra}{ext}")
            if os.path.exists(img_path):
                return img_path
        return None

    def preprocess_image_opencv(self, img_path: str) -> Optional[np.ndarray]:
        """Preprocesa imagen usando OpenCV para análisis adicional"""
        try:
            img = cv2.imread(img_path)
            if img is None:
                return None
            
            # Convertir a RGB
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Redimensionar
            img_resized = cv2.resize(img_rgb, (224, 224))
            
            return img_resized
        except Exception as e:
            print(f"Error preprocesando imagen con OpenCV: {e}")
            return None

    def extract_color_histogram(self, img_path: str) -> Optional[np.ndarray]:
        """Extrae histograma de colores como característica adicional"""
        try:
            img = cv2.imread(img_path)
            if img is None:
                return None
            
            # Convertir a HSV para mejor representación de colores
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            # Calcular histograma
            hist = cv2.calcHist([hsv], [0, 1, 2], None, [50, 60, 60], [0, 180, 0, 256, 0, 256])
            
            # Normalizar
            hist = cv2.normalize(hist, hist).flatten()
            
            return hist
        except Exception as e:
            print(f"Error extrayendo histograma: {e}")
            return None

# Instancia global del procesador de imágenes
image_processor = ImageProcessor()