# ═══════════════════════════════════════════════════════════════════════
# DISEASE SUGGESTION DATABASE
# Maps wambugu71/crop_leaf_diseases_vit model labels → rich actionable info
# Covers the 13 supported classes for Corn, Potato, Rice, and Wheat
# ═══════════════════════════════════════════════════════════════════════

DISEASE_INFO = {

    # ──────────── CORN (MAIZE) ────────────
    "Corn___Common_Rust": {
        "disease": "Common Rust",
        "crop": "Corn",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Fungal disease caused by Puccinia sorghi. Appears as small, circular to elongated brown or orange pustules on both leaf surfaces.",
        "treatment": "Apply a triazole or strobilurin-based fungicide if the outbreak is severe. Early detection is key.",
        "fertilizer": "Maintain balanced NPK. Ensure adequate zinc as corn is highly sensitive to zinc deficiency.",
        "water": "Regular irrigation schedule. Focus on consistent soil moisture, especially during the silking stage.",
        "prevention": "Plant rust-resistant hybrids. Early planting reduces exposure to late-season spore showers."
    },
    "Corn___Gray_Leaf_Spot": {
        "disease": "Gray Leaf Spot",
        "crop": "Corn",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Fungal disease caused by Cercospora zeae-maydis. Produces distinct rectangular, pale brown to gray lesions that run parallel to leaf veins.",
        "treatment": "Apply azoxystrobin or pyraclostrobin fungicides at the tasseling stage (VT) if the lower leaves are heavily affected.",
        "fertilizer": "Ensure adequate nitrogen for plant vigor. Add potassium chloride to strengthen stalks and prevent lodging.",
        "water": "Avoid excessive overhead irrigation. Monitor soil moisture carefully.",
        "prevention": "Rotate crops away from corn (e.g., to soybeans) for 1-2 years. Till crop residue to reduce over-wintering spores."
    },
    "Corn___Northern_Leaf_Blight": {
        "disease": "Northern Leaf Blight",
        "crop": "Corn",
        "is_healthy": False,
        "severity": "Severe",
        "description": "Caused by Exserohilum turcicum. Identified by large, cigar-shaped (long elliptical) gray-green to tan lesions on the leaves.",
        "treatment": "Apply azoxystrobin + propiconazole fungicide at or just before tasseling to protect the upper canopy.",
        "fertilizer": "Ensure nitrogen is adequate but avoid over-application late in the season. Boost potassium for overall stress tolerance.",
        "water": "Reduce humidity in the field by optimizing plant spacing. Avoid late-evening overhead irrigation.",
        "prevention": "Use resistant hybrids carrying Ht resistance genes. Practice crop rotation and aggressively manage crop residue."
    },
    "Corn___Healthy": {
        "disease": "Healthy",
        "crop": "Corn",
        "is_healthy": True,
        "severity": "None",
        "description": "The corn leaf appears vibrant and healthy with no visible signs of disease.",
        "treatment": "No treatment needed. Continue good agricultural practices.",
        "fertilizer": "Side-dress with nitrogen (e.g., urea) at the knee-high stage (V6). Test soil annually.",
        "water": "Corn needs about 1 inch of water per week. The critical water-need period is during silking and grain fill.",
        "prevention": "Scout fields weekly. Rotate crops. Maintain proper plant population densities."
    },

    # ──────────── POTATO ────────────
    "Potato___Early_Blight": {
        "disease": "Early Blight",
        "crop": "Potato",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Caused by Alternaria solani. Produces dark brown spots with concentric, target-like rings, typically starting on older, lower leaves.",
        "treatment": "Apply protectant fungicides like chlorothalonil or mancozeb every 7-10 days. Azoxystrobin is also highly effective.",
        "fertilizer": "Nitrogen and potassium deficiency heavily increases susceptibility. Ensure strong potash application.",
        "water": "Avoid overhead irrigation, or water only early in the morning. Keep leaves as dry as possible.",
        "prevention": "Rotate crops with non-solanaceous plants for 3+ years. Remove infected plant debris at harvest."
    },
    "Potato___Late_Blight": {
        "disease": "Late Blight",
        "crop": "Potato",
        "is_healthy": False,
        "severity": "Severe",
        "description": "Caused by Phytophthora infestans. Very destructive disease causing dark, water-soaked spots that spread rapidly, often with a white mold halo on leaf undersides.",
        "treatment": "Act urgently. Apply mancozeb + metalaxyl immediately. If a significant percentage of the foliage is infected, destroy the plants to prevent spread.",
        "fertilizer": "Avoid excessive nitrogen which promotes soft, vulnerable leaf tissue. Maintain robust potassium levels.",
        "water": "STOP overhead watering immediately. Improve field drainage. Reduce canopy humidity.",
        "prevention": "Always use certified disease-free seed potatoes. Eliminate cull piles and volunteer potatoes."
    },
    "Potato___Healthy": {
        "disease": "Healthy",
        "crop": "Potato",
        "is_healthy": True,
        "severity": "None",
        "description": "The potato leaf appears perfectly healthy with no signs of fungal or bacterial infection.",
        "treatment": "No treatment required.",
        "fertilizer": "Apply NPK (e.g., 10-20-20) at planting, and side-dress with nitrogen during the hilling process.",
        "water": "Keep soil evenly moist. 1-2 inches per week is required, especially critical during early tuber formation and flowering.",
        "prevention": "Hill soil aggressively around stems to protect shallow tubers. Scout for Colorado potato beetles."
    },

    # ──────────── RICE ────────────
    "Rice___Brown_Spot": {
        "disease": "Brown Spot",
        "crop": "Rice",
        "is_healthy": False,
        "severity": "Moderate",
        "description": "Caused by Bipolaris oryzae. Identified by numerous circular to oval, dark brown lesions on the leaves, often with a yellow halo.",
        "treatment": "Apply a fungicide like edifenphos or mankind (mancozeb). Often a secondary disease caused by poor nutrition.",
        "fertilizer": "This disease specifically indicates severe nutritional deficiency. Apply balanced NPK immediately, focusing on Nitrogen and Silicon.",
        "water": "Maintain a consistent flood depth. Avoid prolonged drought stress, which severely exacerbates the disease.",
        "prevention": "Ensure seeds are treated before planting. Perform rigorous soil testing and fertilize appropriately."
    },
    "Rice___Leaf_Blast": {
        "disease": "Rice Blast",
        "crop": "Rice",
        "is_healthy": False,
        "severity": "Severe",
        "description": "Caused by Magnaporthe oryzae. The most devastating rice disease. Characterized by diamond or spindle-shaped lesions with gray centers and dark borders.",
        "treatment": "Apply systemic fungicides like tricyclazole or isoprothiolane immediately at first symptom detection.",
        "fertilizer": "AVOID applying large amounts of nitrogen fertilizer as it fuels the fungus. Supplement with silicon to toughen leaf epidermis.",
        "water": "Maintain deep, continuous flooding. Avoid draining fields which stresses plants and encourages blast.",
        "prevention": "Plant resistant or tolerant rice varieties. Avoid planting densely. Treat seeds with fungicides prior to sowing."
    },
    "Rice___Healthy": {
        "disease": "Healthy",
        "crop": "Rice",
        "is_healthy": True,
        "severity": "None",
        "description": "The rice leaves are green, structurally sound, and appear completely healthy.",
        "treatment": "No treatment required.",
        "fertilizer": "Apply nitrogen in splits (basal, active tillering, and panicle initiation).",
        "water": "Maintain a 2-3 inch continuous flood for weed control and optimal tillering.",
        "prevention": "Keep bunds clean to eliminate alternate host weeds."
    },

    # ──────────── WHEAT ────────────
    "Wheat___Brown_Rust": {
        "disease": "Leaf Rust (Brown Rust)",
        "crop": "Wheat",
        "is_healthy": False,
        "severity": "Severe",
        "description": "Caused by Puccinia triticina. Small, round to oval, orange-brown (rust-colored) pustules scattered across the upper surface of the leaves.",
        "treatment": "Apply azoxystrobin, tebuconazole, or propiconazole at the flag-leaf emergence stage (Feekes 8-9) to protect yield.",
        "fertilizer": "Maintain balanced soil fertility. High nitrogen alone without adequate potassium increases susceptibility.",
        "water": "Wheat is usually rainfed, but if irrigating, avoid excessive watering during cool, humid periods which favor spore germination.",
        "prevention": "The primary defense is planting robust, rust-resistant wheat varieties and removing volunteer wheat in the off-season."
    },
    "Wheat___Yellow_Rust": {
        "disease": "Stripe Rust (Yellow Rust)",
        "crop": "Wheat",
        "is_healthy": False,
        "severity": "Severe",
        "description": "Caused by Puccinia striiformis. Evident as bright yellow pustules arranged in distinct, longitudinal stripes following the leaf veins.",
        "treatment": "Apply systemic triazole or strobilurin fungicides early, as soon as stripes are observed. The flag leaf MUST be protected.",
        "fertilizer": "Standard NPK protocol. Avoid late, excessive nitrogen applications.",
        "water": "Irrigate only if absolutely necessary. Cool temperatures combined with leaf wetness drive this disease.",
        "prevention": "Plant resistant cultivars. Eradicate volunteer wheat and alternate weed hosts. Early sowing can sometimes help avoid peak infection periods."
    },
    "Wheat___Healthy": {
        "disease": "Healthy",
        "crop": "Wheat",
        "is_healthy": True,
        "severity": "None",
        "description": "The wheat leaves are dark green, upright, and display excellent health.",
        "treatment": "No treatment necessary.",
        "fertilizer": "Split nitrogen applications—apply a portion at sowing and the rest at the top-dressing stage (tillering).",
        "water": "Provide adequate moisture at the crown root initiation (CRI) and heading stages for maximum yield.",
        "prevention": "Practice good crop rotation, typically with legumes or oilseeds, to break disease cycles."
    }
}

def get_disease_info(label: str) -> dict:
    """Look up disease info by model label. Returns default if not found."""
    if label in DISEASE_INFO:
        return DISEASE_INFO[label]

    # Fallback for unknown labels (attempt parsing)
    crop_name = label.split("___")[0].replace("_", " ") if "___" in label else "Unknown"
    condition = label.split("___")[1].replace("_", " ") if "___" in label else label
    is_healthy = "healthy" in label.lower()

    return {
        "disease": condition.replace("_", " ").title() if not is_healthy else "Healthy",
        "crop": crop_name.title(),
        "is_healthy": is_healthy,
        "severity": "None" if is_healthy else "Unknown",
        "description": f"{'The plant appears healthy.' if is_healthy else f'Possible condition detected: {condition}'}",
        "treatment": "No treatment needed." if is_healthy else "Consult a local agricultural extension office for specific treatment advice.",
        "fertilizer": "Maintain balanced NPK nutrition. Conduct a soil test for specific recommendations.",
        "water": "Follow standard watering practices for this crop.",
        "prevention": "Practice regular crop rotation and field sanitation."
    }
