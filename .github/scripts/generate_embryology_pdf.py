from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from xml.sax.saxutils import escape
import os

OUT = "downloads/Anatomistvitalis_Embryology_Study_Guide.pdf"
os.makedirs("downloads", exist_ok=True)
navy = colors.HexColor("#0A2034")
teal = colors.HexColor("#0B8178")
pale = colors.HexColor("#EAF5F4")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=31, textColor=navy, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontSize=12, leading=18, textColor=teal, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontSize=17, leading=21, textColor=navy, spaceBefore=12, spaceAfter=7, keepWithNext=True))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontSize=12, leading=15, textColor=teal, spaceBefore=8, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontSize=9.2, leading=13.2, spaceAfter=6))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontSize=8, leading=10, textColor=colors.HexColor("#465766"), spaceAfter=4))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontSize=9, leading=13, leftIndent=8, rightIndent=8, borderColor=teal, borderWidth=0.8, borderPadding=7, backColor=pale, spaceBefore=5, spaceAfter=9))
story=[]

def P(t, style="Bodyx"):
    story.append(Paragraph(t, styles[style]))
def H(t): P(t,"H1x")
def h2(t): P(t,"H2x")
def bullets(items):
    for item in items: P("• "+item)
def table(rows, widths=None):
    data=[[Paragraph(str(c), styles["Smallx"]) for c in row] for row in rows]
    t=Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),navy),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),0.35,colors.HexColor("#CBD6DD")),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#F5F8FA")])]))
    story.append(t); story.append(Spacer(1,7))

story += [Spacer(1,38), Paragraph("ANATOMISTVITALIS", styles["CoverSub"]), Spacer(1,15), Paragraph("EMBRYOLOGY<br/>STUDY GUIDE", styles["CoverTitle"]), Paragraph("From gametogenesis to organogenesis and fetal development", styles["CoverSub"]), Spacer(1,20)]
P("A structured introductory resource for anatomy, medicine, nursing, midwifery, physiotherapy and other health-science students.", "Bodyx")
story += [Spacer(1,16)]
P("<b>Prepared by:</b> Ibine Oladipupo Rapheal<br/><b>Platform:</b> Anatomistvitalis Academic Resource Center<br/><b>Language:</b> English (British spelling)", "Bodyx")
story += [Spacer(1,18)]
P("Learning purpose: build a clear developmental timeline, connect embryological events to adult anatomy, and revise key concepts using active recall. This guide supports—not replaces—your prescribed curriculum and standard embryology texts.", "Callout")
story.append(PageBreak())

H("How to use this guide")
bullets(["Read the timeline first, then study each process in sequence.", "For every structure, ask: what tissue does it arise from, when does it develop, and what can happen if development is disrupted?", "Draw the sequence from memory and explain it aloud.", "Use the revision questions at the end, then verify difficult topics in a recommended textbook."])
H("1. Scope and developmental timeline")
P("Human embryology studies development from formation of gametes and fertilisation through the embryonic and fetal periods. The pre-embryonic period covers approximately the first two weeks; the embryonic period spans weeks 3–8, when the basic body plan and major organ primordia form; the fetal period begins in week 9 and continues to birth, with growth and functional maturation.")
table([["Time","Major events"],["Before fertilisation","Spermatogenesis and oogenesis produce haploid gametes."],["Day 0","Fertilisation usually occurs in the ampulla of the uterine tube; a zygote forms."],["Days 1–3","Cleavage divisions produce blastomeres; the morula forms."],["Days 4–5","Blastocyst forms, with embryoblast and trophoblast."],["Days 6–12","Implantation progresses; bilaminar embryonic disc and extra-embryonic tissues develop."],["Week 3","Gastrulation, trilaminar disc, notochord and early neurulation."],["Weeks 4–8","Folding and organogenesis; body form becomes recognisable."],["Week 9–birth","Fetal growth, tissue differentiation and functional maturation."]],[30*mm,130*mm])
H("2. Gametogenesis")
h2("Spermatogenesis")
P("Spermatogenesis occurs in seminiferous tubules. Diploid spermatogonia divide mitotically; primary spermatocytes undergo meiosis I to form haploid secondary spermatocytes; meiosis II produces spermatids, which differentiate by spermiogenesis into spermatozoa. Sertoli cells support developing germ cells, while Leydig cells in the interstitial tissue produce testosterone under LH stimulation.")
h2("Oogenesis")
P("Oogonia proliferate during fetal life. Primary oocytes begin meiosis I and arrest in prophase I until puberty. Usually one resumes maturation in a cycle; the secondary oocyte is ovulated and arrests in metaphase II. Completion of meiosis II normally follows fertilisation. Unequal cytokinesis preserves most cytoplasm in the functional oocyte.")
P("Clinical connection: meiotic nondisjunction can produce aneuploid gametes, contributing to conditions such as trisomy 21. Risk depends on several factors; it should not be reduced to a single deterministic rule.", "Callout")
H("3. Fertilisation and week one")
P("Fertilisation typically occurs in the ampulla of the uterine tube. Capacitation prepares sperm for fertilisation; the acrosome reaction assists penetration of the zona pellucida. Fusion of sperm and oocyte membranes triggers oocyte activation and cortical granule release, helping prevent polyspermy. The oocyte completes meiosis II; male and female pronuclei form and their genetic material combines as development proceeds.")
P("Cleavage consists of mitotic divisions without a major increase in overall conceptus size. Compaction helps establish cell populations. The morula develops into a blastocyst with an outer trophoblast, an inner cell mass (embryoblast) and a blastocyst cavity. The zona pellucida is shed before implantation.")
H("4. Implantation and week two")
P("Implantation begins around day 6–7 after fertilisation. Trophoblast differentiates into cytotrophoblast and syncytiotrophoblast; the latter invades endometrial tissue and contributes to the fetal component of the placenta. The embryoblast forms a bilaminar disc of epiblast and hypoblast. The amniotic cavity and yolk sac develop, while extra-embryonic mesoderm and the chorionic cavity form.")
P("The term 'week of twos' is a useful memory cue for paired structures such as epiblast/hypoblast and cytotrophoblast/syncytiotrophoblast, but not every event fits a strict two-part pattern.")
H("5. Gastrulation and the three germ layers")
P("During week 3, the primitive streak appears in the epiblast. Epiblast cells migrate inward to replace hypoblast and form definitive endoderm; others form intra-embryonic mesoderm. Epiblast remaining at the surface becomes ectoderm. Gastrulation establishes the trilaminar disc and body axes. The notochord helps organise axial development and induces the overlying ectoderm to form the neural plate.")
table([["Germ layer","Major derivatives (examples)"],["Ectoderm","Epidermis and its appendages; central and peripheral nervous systems; lens and selected sensory epithelia."],["Mesoderm","Muscle, bone, cartilage, connective tissues, cardiovascular system, kidneys and much of the reproductive system."],["Endoderm","Epithelial lining of much of the digestive and respiratory tracts; parenchymal epithelium of liver and pancreas; selected endocrine and urinary tract epithelia."]],[34*mm,126*mm])
P("Important: germ-layer derivatives are a framework, not an exhaustive one-to-one list. Many organs contain tissues derived from more than one embryonic source.", "Callout")
H("6. Neurulation, somites and body folding")
P("Neurulation begins when the neural plate forms, bends into neural folds and closes as the neural tube. The cranial neuropore closes approximately day 25 and the caudal neuropore around day 27; timing varies slightly between references. The neural tube gives rise to the brain and spinal cord. Neural crest cells migrate widely and contribute to structures including peripheral ganglia, Schwann cells, melanocytes and much of the craniofacial connective tissue.")
P("Paraxial mesoderm segments into somites. Somite derivatives include sclerotome (vertebrae and ribs), myotome (skeletal muscle) and dermatome (dermis in defined regions). Lateral folding and cephalocaudal folding transform the flat disc into a more cylindrical embryo, incorporate part of the yolk sac into the gut tube, and help position the heart and body wall.")
H("7. Organogenesis: high-yield overview")
table([["System/structure","Key developmental point"],["Cardiovascular","The heart begins forming early and starts beating at about day 22; partitioning and remodelling continue."],["Respiratory","The respiratory diverticulum buds from foregut endoderm; branching and maturation continue well into fetal life and after birth."],["Digestive","Gut tube forms through folding; foregut, midgut and hindgut have distinct arterial territories and derivatives."],["Urinary","Intermediate mesoderm contributes to the urinary system; the definitive kidney is the metanephros."],["Reproductive","Gonadal and duct development depends on chromosomal, genetic, hormonal and tissue-level signals."],["Musculoskeletal","Somites and lateral plate mesoderm contribute to axial and appendicular structures; limb buds appear in week 4."],["Face and palate","Facial prominences grow and fuse; abnormal fusion can cause cleft lip and/or palate."]],[34*mm,126*mm])
H("8. Placenta, membranes and fetal circulation")
P("The placenta is a fetomaternal exchange organ. The fetal component develops principally from chorion frondosum; the maternal component is associated with decidua basalis. Chorionic villi contain fetal vessels and are bathed by maternal blood in the intervillous space under normal placental architecture. Maternal and fetal blood usually remain in separate circulations while gases, nutrients, wastes and selected antibodies cross the placental interface.")
P("The umbilical cord typically contains two umbilical arteries carrying blood from fetus to placenta and one umbilical vein carrying oxygenated blood toward the fetus. Fetal circulation includes the ductus venosus, foramen ovale and ductus arteriosus, which help direct blood around the liver and lungs before birth. After birth, changes in pressure and oxygenation promote functional closure; anatomical remodelling follows over time.")
H("9. Congenital anomalies and teratology")
P("A congenital anomaly is a structural or functional condition present at birth, although it may be detected later. Causes may be genetic, environmental, multifactorial or unknown. Teratogens can include certain medicines, infections, alcohol, radiation and maternal metabolic conditions; effects depend on dose, timing, exposure duration and susceptibility. The embryonic period is especially sensitive for major structural malformations, while the fetal period remains important for growth and functional development.")
bullets(["Primary prevention includes preconception care, folic acid according to local guidance, vaccination planning, control of maternal disease and avoiding known teratogens.", "Neural tube defects are associated with failure of neural tube closure and can be reduced in risk by adequate periconceptional folate.", "A congenital anomaly should not automatically be attributed to parental behaviour; many have complex or unknown causes."])
H("10. Exam-focused distinctions")
table([["Term","Distinction"],["Embryoblast","Inner cell mass; forms the embryo proper and some associated tissues."],["Trophoblast","Outer blastocyst cell population; contributes to chorion and fetal placental tissues."],["Epiblast","Source of all three definitive germ layers during gastrulation."],["Hypoblast","Contributes to extra-embryonic endodermal lining; not the source of the embryo's definitive endoderm."],["Neural tube","Forms CNS."],["Neural crest","Migratory cells with numerous peripheral nervous system and other derivatives."],["Umbilical arteries","Carry blood from fetus to placenta."],["Umbilical vein","Carries blood from placenta toward fetus."]],[35*mm,125*mm])
H("11. Revision questions")
qs=[
("1. Where does fertilisation most commonly occur?","Ampulla of the uterine tube."),
("2. What are the two principal cell populations of the blastocyst?","Trophoblast and embryoblast (inner cell mass)."),
("3. Which embryonic layer gives rise to all three definitive germ layers?","Epiblast."),
("4. What process establishes ectoderm, mesoderm and endoderm?","Gastrulation."),
("5. What is the main derivative of the neural tube?","The central nervous system: brain and spinal cord."),
("6. Name two derivatives of neural crest cells.","Examples include peripheral ganglia, Schwann cells and melanocytes."),
("7. What do sclerotome cells contribute to?","Vertebrae and ribs, among other axial skeletal components."),
("8. What is the definitive kidney called?","Metanephros."),
("9. Which umbilical vessel carries oxygenated blood toward the fetus?","The umbilical vein."),
("10. What is the embryonic period?","Approximately weeks 3–8 after fertilisation, when major organ primordia develop."),
("11. Why can the timing of teratogen exposure matter?","Different tissues have different sensitive windows during development."),
("12. What does the notochord do in early development?","It helps establish the body axis and signals the overlying ectoderm during neural development."),
("13. What structures are separated by the trophoblast layers?","Cytotrophoblast is the inner cellular layer; syncytiotrophoblast is the outer invasive multinucleated layer."),
("14. What are the three major fetal-circulation shunts?","Ductus venosus, foramen ovale and ductus arteriosus."),
("15. What is the main purpose of folding?","To shape the embryo and incorporate part of the yolk sac into the gut while repositioning body structures.")
]
for q,a in qs:
    story.append(KeepTogether([Paragraph("<b>"+q+"</b>",styles["Bodyx"]),Paragraph("<font color='#0B8178'><b>Answer:</b></font> "+a,styles["Bodyx"])]))
H("Glossary")
table([["Term","Meaning"],["Blastocyst","Early conceptus with trophoblast, embryoblast and a cavity."],["Gastrulation","Process establishing the three definitive germ layers."],["Organogenesis","Formation and early development of organ systems."],["Neurulation","Formation of the neural tube."],["Teratogen","Exposure that can disturb prenatal development."],["Somite","Segmented paraxial mesodermal structure."],["Chorion","Outer fetal membrane contributing to placenta."],["Amnion","Membrane enclosing the amniotic cavity."]],[34*mm,126*mm])
H("Recommended standard references")
bullets(["Moore, Persaud and Torchia. The Developing Human: Clinically Oriented Embryology. Elsevier.", "Sadler. Langman's Medical Embryology. Wolters Kluwer.", "Schoenwolf and colleagues. Larsen's Human Embryology. Elsevier."])
P("Use the latest edition available through your library and follow the terminology preferred by your course. This guide is an original study aid; verify detailed dates, diagrams and clinical recommendations against standard texts and your lecturer's teaching.", "Callout")
P("© Anatomistvitalis Academic Resource Center · Ibine Oladipupo Rapheal · Educational use. Not a substitute for formal instruction or clinical guidance.", "Smallx")

def footer(canvas, doc):
    canvas.saveState()
    w,h=A4
    canvas.setStrokeColor(colors.HexColor("#D7E1E6")); canvas.line(18*mm,15*mm,w-18*mm,15*mm)
    canvas.setFont("Helvetica",7.5); canvas.setFillColor(colors.HexColor("#526472"))
    canvas.drawString(18*mm,10*mm,"ANATOMISTVITALIS • EMBRYOLOGY STUDY GUIDE")
    canvas.drawRightString(w-18*mm,10*mm,f"Page {doc.page}")
    canvas.restoreState()

doc=SimpleDocTemplate(OUT,pagesize=A4,rightMargin=20*mm,leftMargin=20*mm,topMargin=18*mm,bottomMargin=22*mm,title="Anatomistvitalis Embryology Study Guide",author="Ibine Oladipupo Rapheal")
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(f"Created {OUT}")
