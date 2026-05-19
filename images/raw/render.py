"""Render specific lecture slide pages as JPEGs for the slide-ID quiz."""
import fitz, os, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDFS = {
    "wk4": r"C:\Users\produ\Downloads\20260406_Biol40a_Slides_Week4-W_mollhoff copy.pdf",
    "wk5": r"C:\Users\produ\Downloads\20260406_Biol40a_Slides_Week5-MW_mollhoff.pdf",
    "wk6": r"C:\Users\produ\Downloads\20260406_Biol40a_Slides_Week6-MW_mollhoff-3.pdf",
}

# (question_id, pdf_tag, page_number_1based)  — see slide bank for what each
# question references.  Page choices were made by scanning slide titles in
# images/raw/_titles.txt against the question prompts.
JOBS = [
    # Q1, Q2 already use external histologyguide URLs — no local images needed
    (3,  "wk4", 38),  # Supportive CT – Bone (dense bone micrograph)
    (4,  "wk4", 38),
    (5,  "wk4", 38),  # Spongy bone (same slide has both)
    (6,  "wk4", 38),
    (7,  "wk5",  8),  # Wk5 Q1a "Which types of connective tissue can you identify?"
    (8,  "wk5", 24),  # Wk5 Q3b "Which picture is showing skeletal muscle tissue?"
    (9,  "wk5", 19),  # Skeletal muscle slide
    (10, "wk5", 20),  # Cardiac muscle slide
    (11, "wk5", 21),  # Smooth muscle slide
    (12, "wk4", 84),  # Holocrine Secretion – Sebaceous Glands
    (13, "wk4", 84),
    (14, "wk5", 75),  # Wk5 Q3a "What are those brown speckles?"
    (15, "wk5", 71),  # Stratum Lucidum & Stratum Corneum
    (16, "wk5", 74),  # Stratum Basale
    (17, "wk5", 72),  # Stratum Granulosum
    (18, "wk5", 71),  # Stratum Lucidum & Stratum Corneum
    (19, "wk6", 21),  # Melanocytes
    (20, "wk6", 19),  # Merkel cells
    (21, "wk6", 18),  # Langerhans cells
    (22, "wk6", 54),  # Wound Healing — Clotting & Inflammation (Step 1)
    (23, "wk6", 54),  # Inflammation step shown on same slide
    (24, "wk6", 55),  # Proliferation of cells
    (25, "wk6", 56),  # Remodeling
    (26, "wk6", 61),  # Keloid
    (27, "wk6", 61),
    (28, "wk6", 61),
    (29, "wk6", 50),  # Vitamin D Synthesis
    (30, "wk6", 50),
    (31, "wk6", 50),
    (32, "wk5", 26),  # Key Characteristics of Nervous Tissue ("swirled & wavy")
    (33, "wk5",  7),  # Four Major Tissue Types overview
    (34, "wk5",  7),
    (35, "wk5",  7),
    (36, "wk5", 12),  # Wk5 Q2a "Spot the blood vessel(s)"
    (37, "wk5", 13),  # Wk5 Q2b "Spot the simple squamous epithelium"
    (38, "wk4", 34),  # CT Proper: Dense Connective Tissues
    (39, "wk4", 34),
    (40, "wk4", 33),  # CT Proper: Loose Connective Tissues (areolar)
    (41, "wk4", 33),  # Adipose is shown alongside areolar on the loose CT slide
    (42, "wk4",  9),  # Germ layers — Ectoderm
    (43, "wk4", 10),  # Germ layers — Mesoderm
    (44, "wk4", 11),  # Germ layers — Endoderm
    (45, "wk4", 40),  # Major Functions of CT (Storage)
    (46, "wk4", 40),
    (47, "wk4", 40),
    (48, "wk5", 65),  # Layers of the Skin (3D block diagram)
    (49, "wk5", 65),
    (50, "wk6", 31),  # Pigmentation in Scars
]

OUT_DIR = r"C:\Users\produ\midterm2-quiz\images"
SCALE = 2.0  # ~144 DPI render scale

docs = {tag: fitz.open(p) for tag, p in PDFS.items()}
mat = fitz.Matrix(SCALE, SCALE)

for qid, tag, page_no in JOBS:
    page = docs[tag][page_no - 1]
    pix = page.get_pixmap(matrix=mat, alpha=False)
    out = os.path.join(OUT_DIR, f"q{qid:02d}.jpg")
    with open(out, "wb") as f:
        f.write(pix.tobytes("jpeg", jpg_quality=82))
    sz = os.path.getsize(out) // 1024
    print(f"q{qid:02d} <- {tag} p{page_no:02d}  ({sz} KB)")

for d in docs.values():
    d.close()

print(f"\nrendered {len(JOBS)} images to {OUT_DIR}")
