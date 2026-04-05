"""
Agri Pulse – Leaf Disease Detection FastAPI Backend
Uses HuggingFace transformers + dima806/plant_disease_detection model
Runs locally — no external API calls needed at runtime
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from transformers import pipeline
import io
import logging

from disease_info import get_disease_info

# ─── Setup Logging ───
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ─── FastAPI App ───
app = FastAPI(
    title="Agri Pulse – Leaf Disease Detection API",
    description="Upload a leaf image to detect plant diseases using AI",
    version="1.0.0"
)

# ─── CORS (allow Vite dev server) ───
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://agripulse2.netlify.app"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Load AI Model (downloads once, cached locally) ───
logger.info("Loading plant disease detection model... (first time may take a minute to download)")
classifier = None

def get_classifier():
    global classifier
    if classifier is None:
        classifier = pipeline(
            "image-classification",
            model="wambugu71/crop_leaf_diseases_vit",
            top_k=3
        )
        logger.info("✅ Model loaded successfully!")
    return classifier


# ─── Health Check ───
@app.get("/api/health")
def health():
    return {"status": "ok", "model": "wambugu71/crop_leaf_diseases_vit"}


# ─── Main Prediction Endpoint ───
@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    """
    Accepts a leaf image, runs AI classification, and returns:
    - Top 3 disease predictions with confidence scores
    - Treatment, fertilizer, water, and prevention suggestions for each
    """
    # Validate file type
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload a valid image file (JPG, PNG).")

    try:
        # Read and open image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Run AI prediction
        clf = get_classifier()
        predictions = clf(image)

        # Enrich predictions with disease info + suggestions
        results = []
        for pred in predictions:
            label = pred["label"]
            score = round(pred["score"], 4)
            info = get_disease_info(label)

            results.append({
                "label": label,
                "confidence": score,
                "confidence_percent": round(score * 100, 1),
                **info
            })

        return {
            "success": True,
            "predictions": results,
            "top_prediction": results[0] if results else None,
            "image_name": file.filename
        }

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error analyzing image: {str(e)}")


# ─── Run with: uvicorn main:app --reload ───
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
