from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, HRFlowable
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from xml.sax.saxutils import escape
import os

OUT = "downloads/Anatomistvitalis_Research_Methodology_Study_Guide.pdf"
os.makedirs("downloads", exist_ok=True)
NAVY=colors.HexColor("#09213A"); TEAL=colors.HexColor("#087F75")
MINT=colors.HexColor("#DDF5EF"); GOLD=colors.HexColor("#E7A64B")
INK=colors.HexColor("#203344"); MUTED=colors.HexColor("#5D7180")
PALE=colors.HexColor("#F3F7FA"); LINE=colors.HexColor("#D6E1E8")
PAGE_W,PAGE_H=A4

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverBrand",fontName="Helvetica-Bold",fontSize=12,leading=16,textColor=colors.white,alignment=TA_CENTER,spaceAfter=8))
styles.add(ParagraphStyle(name="CoverTitle2",fontName="Helvetica-Bold",fontSize=31,leading=35,textColor=colors.white,alignment=TA_LEFT,spaceAfter=10))
styles.add(ParagraphStyle(name="CoverSub2",fontName="Helvetica",fontSize=12,leading=18,textColor=colors.HexColor("#D8F4EF"),alignment=TA_LEFT))
styles.add(ParagraphStyle(name="H1x",parent=styles["Heading1"],fontName="Helvetica-Bold",fontSize=17,leading=21,textColor=NAVY,spaceBefore=13,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name="H2x",parent=styles["Heading2"],fontName="Helvetica-Bold",fontSize=11.5,leading=15,textColor=TEAL,spaceBefore=8,spaceAfter=4,keepWithNext=True))
styles.add(ParagraphStyle(name="Bodyx",parent=styles["BodyText"],fontName="Helvetica",fontSize=8.8,leading=12.3,textColor=INK,spaceAfter=5))
styles.add(ParagraphStyle(name="Smallx",parent=styles["BodyText"],fontName="Helvetica",fontSize=7.4,leading=9.4,textColor=MUTED,spaceAfter=3))
styles.add(ParagraphStyle(name="Calloutx",parent=styles["BodyText"],fontName="Helvetica-Bold",fontSize=8.7,leading=12,leftIndent=7,rightIndent=7,borderColor=TEAL,borderWidth=.7,borderPadding=7,backColor=MINT,spaceBefore=4,spaceAfter=8))
styles.add(ParagraphStyle(name="TableHeadx",parent=styles["BodyText"],fontName="Helvetica-Bold",fontSize=7.5,leading=9,textColor=colors.white))
styles.add(ParagraphStyle(name="TOCx",parent=styles["BodyText"],fontName="Helvetica",fontSize=9.2,leading=14,textColor=INK,spaceAfter=2))
story=[]

def P(t,style="Bodyx"): story.append(Paragraph(t,styles[style]))
def H(t): P(t,"H1x")
def h2(t): P(t,"H2x")
def bullets(items):
    for item in items: P("•&nbsp;&nbsp;"+item)
def numbered(items):
    for i,item in enumerate(items,1): P(f"<b>{i}.</b>&nbsp;&nbsp;{item}")
def tbl(rows,widths=None):
    data=[]
    for ri,row in enumerate(rows):
        data.append([Paragraph(str(c),styles["TableHeadx"] if ri==0 else styles["Smallx"]) for c in row])
    t=Table(data,colWidths=widths,repeatRows=1,hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),NAVY),("GRID",(0,0),(-1,-1),.35,LINE),
        ("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),5),
        ("RIGHTPADDING",(0,0),(-1,-1),5),("TOPPADDING",(0,0),(-1,-1),5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,PALE])]))
    story.append(t); story.append(Spacer(1,6))
def callout(t): P(t,"Calloutx")
def page(): story.append(PageBreak())

def cover(c,doc):
    c.saveState()
    # Elegant editorial cover, with a custom vector research desk illustration.
    c.setFillColor(NAVY); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
    c.setFillColor(colors.HexColor("#103B50")); c.circle(PAGE_W+5*mm,PAGE_H-18*mm,78*mm,fill=1,stroke=0)
    c.setFillColor(colors.HexColor("#0B5D61")); c.circle(PAGE_W-8*mm,PAGE_H-38*mm,48*mm,fill=1,stroke=0)
    c.setFillColor(GOLD); c.roundRect(18*mm,PAGE_H-25*mm,12*mm,2*mm,1*mm,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold",10)
    c.drawString(18*mm,PAGE_H-20*mm,"ANATOMIST VITALIS")
    c.setFillColor(colors.HexColor("#B8D8E3")); c.setFont("Helvetica",7.5)
    c.drawString(18*mm,PAGE_H-29*mm,"ACADEMIC RESOURCE CENTER  |  HEALTH SCIENCE EDUCATION")
    # Decorative research pathway nodes
    node_y=PAGE_H-66*mm
    for i,(label,col) in enumerate([("ASK",TEAL),("DESIGN",GOLD),("COLLECT",colors.HexColor("#4D8FC4")),("ANALYSE",colors.HexColor("#9870C7")),("REPORT",TEAL)]):
        x=22*mm+i*34*mm
        c.setFillColor(col); c.circle(x,node_y,7*mm,fill=1,stroke=0)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold",6.4); c.drawCentredString(x,node_y-1*mm,label)
        if i<4:
            c.setStrokeColor(colors.HexColor("#9ABBC8")); c.setLineWidth(1.1)
            c.line(x+7*mm,node_y,x+27*mm,node_y)
    c.setFillColor(colors.HexColor("#77E0CF")); c.setFont("Helvetica-Bold",10)
    c.drawString(18*mm,PAGE_H-94*mm,"THE PRACTICAL, STEP-BY-STEP GUIDE")
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold",30)
    c.drawString(18*mm,PAGE_H-111*mm,"RESEARCH")
    c.drawString(18*mm,PAGE_H-126*mm,"METHODOLOGY")
    c.setFillColor(colors.HexColor("#D7E8EF")); c.setFont("Helvetica",12)
    c.drawString(18*mm,PAGE_H-139*mm,"For Health Science Students & Early-Career Researchers")
    # stylised study desk / laptop graphic
    desk_y=58*mm
    c.setFillColor(colors.HexColor("#B7773E")); c.roundRect(17*mm,desk_y,176*mm,5*mm,2*mm,fill=1,stroke=0)
    c.setFillColor(colors.HexColor("#203A50")); c.roundRect(62*mm,desk_y+5*mm,83*mm,48*mm,3*mm,fill=1,stroke=0)
    c.setFillColor(colors.HexColor("#EAF5F8")); c.roundRect(66*mm,desk_y+9*mm,75*mm,39*mm,2*mm,fill=1,stroke=0)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold",8); c.drawCentredString(103.5*mm,desk_y+39*mm,"RESEARCH WORKFLOW")
    labels=[("QUESTION",TEAL),("METHOD",GOLD),("DATA",colors.HexColor("#4387BD")),("FINDINGS",colors.HexColor("#8D65B7"))]
    for i,(lab,col) in enumerate(labels):
        x=70*mm+i*18*mm
        c.setFillColor(col); c.circle(x,desk_y+27*mm,4*mm,fill=1,stroke=0)
        c.setFillColor(NAVY); c.setFont("Helvetica",4.8); c.drawCentredString(x,desk_y+19*mm,lab)
        if i<3:
            c.setStrokeColor(TEAL); c.line(x+4*mm,desk_y+27*mm,x+14*mm,desk_y+27*mm)
    # books stack
    for i,(col,label) in enumerate([(TEAL,"RESEARCH DESIGN"),(colors.HexColor("#6653A6"),"DATA ANALYSIS"),(GOLD,"SCIENTIFIC WRITING")]):
        y=desk_y+3*mm+i*8*mm
        c.setFillColor(col); c.roundRect(19*mm,y,35*mm,6.5*mm,1*mm,fill=1,stroke=0)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold",5.5); c.drawString(21*mm,y+2*mm,label)
    # checklist notebook
    c.setFillColor(colors.HexColor("#F5F8FA")); c.roundRect(151*mm,desk_y+7*mm,35*mm,29*mm,2*mm,fill=1,stroke=0)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold",6); c.drawString(155*mm,desk_y+30*mm,"PROJECT PLAN")
    for i,lab in enumerate(["Question","Literature","Methods","Ethics","Analysis"]):
        yy=desk_y+24*mm-i*4*mm
        c.setStrokeColor(TEAL); c.rect(155*mm,yy-1*mm,2*mm,2*mm,fill=0,stroke=1)
        c.setFillColor(INK); c.setFont("Helvetica",5.4); c.drawString(159*mm,yy-.5*mm,lab)
    c.setFillColor(colors.HexColor("#C2D9E4")); c.setFont("Helvetica",8.5)
    c.drawString(18*mm,43*mm,"TOPIC SELECTION  •  PROPOSAL  •  METHODS  •  DATA  •  THESIS")
    c.setStrokeColor(TEAL); c.setLineWidth(1.3); c.line(18*mm,37*mm,192*mm,37*mm)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold",10)
    c.drawString(18*mm,27*mm,"Prepared by Ibine Oladipupo Rapheal")
    c.setFillColor(colors.HexColor("#C2D9E4")); c.setFont("Helvetica",7.5)
    c.drawString(18*mm,20*mm,"B.Sc. Anatomy  |  Anatomistvitalis Academic Resource Center")
    c.setFillColor(colors.HexColor("#77E0CF")); c.setFont("Helvetica-Oblique",8)
    c.drawRightString(192*mm,10*mm,"Good research builds better healthcare.")
    c.restoreState()

def footer(c,doc):
    if doc.page==1: return
    c.saveState()
    c.setStrokeColor(LINE); c.line(18*mm,15*mm,192*mm,15*mm)
    c.setFillColor(MUTED); c.setFont("Helvetica",7)
    c.drawString(18*mm,10*mm,"ANATOMIST VITALIS  •  RESEARCH METHODOLOGY STUDY GUIDE")
    c.drawRightString(192*mm,10*mm,str(doc.page))
    c.restoreState()

# Front matter
story.append(Spacer(1,10))
P("A practical workbook for undergraduate projects, postgraduate dissertations and doctoral research planning.","CoverSub2")
P("<b>Prepared by:</b> Ibine Oladipupo Rapheal<br/><b>Publisher:</b> Anatomistvitalis Academic Resource Center<br/><b>Edition:</b> Student learning edition, 2026","Bodyx")
callout("Important: this guide teaches general principles. Always follow your university handbook, supervisor's instructions, local law, ethics committee requirements, and the specific rules of your target journal or funder.")
page()
H("Welcome & how to use this guide")
P("Research can feel complicated because it combines a question, evidence, a defensible method, careful analysis and clear writing. The process becomes manageable when each decision follows logically from the one before it. This guide is written for health-science learners—including anatomy, physiology, nursing, medicine, public health, biomedical science, physiotherapy and related disciplines.")
bullets([
"Read the relevant chapter before making a research decision; keep a record of the decision and its justification.",
"Use the templates as starting points, not as a substitute for your department's prescribed format.",
"Discuss feasibility, ethics, methods and analysis with your supervisor before collecting data.",
"Never invent participants, measurements, results, ethics approvals, citations or statistical outputs.",
"Use the reporting guideline appropriate to your study design and check the current journal instructions."
])
H("Contents")
for item in [
"1. Research fundamentals and the research cycle","2. Choosing a topic and developing a research question",
"3. Literature searching, appraisal and the review chapter","4. Variables, hypotheses, objectives and conceptual frameworks",
"5. Quantitative, qualitative and mixed-methods designs","6. Population, sampling and sample-size planning",
"7. Instruments, data collection and laboratory methods","8. Research ethics, consent and integrity",
"9. Data management and statistical analysis","10. Writing the proposal and thesis/dissertation",
"11. Results, discussion, conclusion and recommendations","12. Referencing, plagiarism and responsible use of AI",
"13. Publication, presentation and oral defence","14. Worked examples, tables and templates",
"15. Final checklists and revision questions","References and further learning"
]: P("•&nbsp;&nbsp;"+item,"TOCx")
page()

H("1. Research fundamentals and the research cycle")
P("Research is a systematic and transparent process for answering a question using appropriate evidence. Good research is not simply collecting many observations; it is designing a process that can produce a trustworthy answer to a clearly defined question.")
h2("Core characteristics of good research")
bullets([
"<b>Clear:</b> the problem, aim and outcomes are stated precisely.",
"<b>Relevant:</b> the question addresses a meaningful knowledge gap or practical need.",
"<b>Methodologically sound:</b> the design, sample, measurements and analysis fit the question.",
"<b>Ethical:</b> participant welfare, privacy, justice and scientific integrity are protected.",
"<b>Transparent:</b> procedures, exclusions, limitations and analytic decisions are reported honestly.",
"<b>Reproducible where appropriate:</b> another qualified researcher could understand how the work was done."
])
h2("The research cycle")
tbl([["Stage","Key question","Output"],["Identify a problem","What is not known or not working?","Problem statement"],["Review evidence","What is already known, and what remains uncertain?","Critical literature review"],["Plan","What design and procedures can answer the question?","Protocol/proposal"],["Obtain approval","Are ethics, permissions and resources in place?","Approvals and documented permissions"],["Collect data","How will measurements be obtained consistently?","Quality-controlled dataset/materials"],["Analyse","What patterns or estimates answer the objectives?","Tables, figures, themes or model outputs"],["Interpret","What do the findings mean, and what are the limits?","Discussion and conclusions"],["Disseminate","How can others evaluate and use the work?","Thesis, report, presentation or paper"]],[32*mm,70*mm,72*mm])
callout("A useful rule: choose the research question first, then select the design and analysis. Do not choose a statistical test first and force a question to fit it.")
h2("Research, audit, service evaluation and quality improvement")
P("These activities can overlap but are not interchangeable. Research generally aims to generate or test knowledge beyond a single local service; audit compares practice with a defined standard; service evaluation describes how a service performs; quality improvement tests changes intended to improve a process. Classification and ethics requirements depend on the institution and jurisdiction—seek formal guidance rather than self-exempting a project.")

H("2. Choosing a topic and developing a research question")
P("A good topic is focused, feasible, ethically acceptable, relevant and supported by sufficient literature. A topic that sounds impressive but cannot be completed with available time, equipment, expertise or funds is a poor project choice.")
h2("A feasibility screen")
tbl([["Criterion","Questions to ask"],["Interest and relevance","Will the answer matter to a discipline, service, community or evidence gap?"],["Specificity","Can the topic be expressed as one answerable question?"],["Data access","Can you obtain the required records, participants, specimens or measurements legally and ethically?"],["Skills and facilities","Are equipment, supervision, methods and analytic skills available?"],["Time and cost","Can recruitment, experiments, analysis and writing fit the schedule and budget?"],["Ethics and safety","Can risks be minimised and approvals obtained before the work begins?"],["Novelty","Does the literature show a genuine gap rather than merely a topic that is new to you?"]],[33*mm,141*mm])
h2("Turn a broad interest into a researchable question")
P("<b>Broad area:</b> sleep and academic performance. <b>Focused question:</b> Among first-year health-science undergraduates at a specified institution, is self-reported sleep duration associated with end-of-semester examination scores during a defined academic session?")
P("This question identifies the population, exposure, outcome and setting. It does not prove causation. If the design is cross-sectional, report an association rather than claiming that sleep duration caused a change in examination performance.")
h2("Frameworks for structuring questions")
bullets([
"<b>PICO:</b> Population, Intervention, Comparator, Outcome—often useful for intervention questions.",
"<b>PEO:</b> Population, Exposure, Outcome—often useful for observational questions.",
"<b>SPIDER:</b> Sample, Phenomenon of Interest, Design, Evaluation, Research type—can help frame qualitative or mixed evidence questions."
])
h2("Writing a strong problem statement")
numbered([
"Introduce the broad context using reliable evidence.",
"Describe the specific problem and who or what is affected.",
"Summarise what existing studies have established.",
"Identify the precise gap, inconsistency or unresolved issue.",
"Explain why addressing that gap matters in the chosen setting.",
"End with the purpose of the proposed study."
])
callout("Avoid unsupported phrases such as “no study has ever been done.” Demonstrate the gap with a documented search and state the limits of that search.")

H("3. Literature searching, appraisal and the review chapter")
P("A literature review is a critical synthesis of relevant evidence, not a sequence of unrelated summaries. It shows what is known, how confidently it is known, where studies agree or differ, and why the proposed study is justified.")
h2("Build a search strategy")
numbered([
"Break the question into key concepts (for example, sleep duration, undergraduates, academic performance).",
"List synonyms, spelling variants and controlled vocabulary where available.",
"Combine synonyms with OR and different concepts with AND.",
"Search appropriate sources: PubMed/MEDLINE, Google Scholar, institutional library databases, Cochrane Library where relevant, and discipline-specific indexes.",
"Record database, search date, search terms, filters and the number of records retrieved.",
"Screen titles/abstracts, then full texts using stated inclusion and exclusion criteria.",
"Use reference lists and citation searching to identify additional relevant studies."
])
P("<b>Example search:</b> (student* OR undergraduate*) AND (sleep duration OR sleep quality) AND (academic performance OR examination score). Adapt the syntax to each database; do not assume every database uses identical operators.")
h2("Screen and appraise evidence")
bullets([
"Check whether the study design can answer the question it asks.",
"Assess sampling, measurement validity, missing data, confounding, bias and precision.",
"Distinguish statistical significance from clinical or practical importance.",
"Compare studies by population, setting, methods and outcomes—not just by conclusion.",
"Give appropriate weight to systematic reviews and high-quality primary studies, while checking currency and applicability."
])
h2("Literature matrix template")
tbl([["Author/year","Design and sample","Main outcome","Strengths/limitations","Relevance to your study"],["Surname et al. (year)","Design; setting; n=…","Outcome and estimate","Bias, precision, confounding","How it supports or differs from your question"],["","","","",""]],[27*mm,36*mm,35*mm,43*mm,33*mm])
P("In the review chapter, organise the synthesis by themes, concepts, methods or chronology when justified. Finish with a clear summary of the gap and show how your objectives address it. Avoid copying abstracts, excessive direct quotations and claims unsupported by the original sources.")

H("4. Variables, hypotheses, objectives and conceptual frameworks")
h2("Variables and operational definitions")
P("A variable is a characteristic that can vary between people, specimens, records, groups or time points. An operational definition explains exactly how a variable will be measured or classified in this study.")
tbl([["Term","Meaning","Example"],["Independent/exposure variable","Predictor, exposure or assigned intervention","Hours of sleep per night"],["Dependent/outcome variable","Outcome being measured","Examination score"],["Confounder","A factor associated with exposure and outcome that can distort an association","Prior academic performance or workload, depending on the question"],["Effect modifier","A factor across whose levels the association differs","A prespecified subgroup characteristic"],["Operational definition","Exact measurement rule and units","Average self-reported sleep hours over seven nights"]],[34*mm,68*mm,72*mm])
P("A confounder is not simply any variable that changes a model's p-value. Selection should be justified by subject knowledge and a causal framework where possible. Avoid adjusting automatically for mediators or colliders.")
h2("Aim, objectives and hypotheses")
P("The <b>aim</b> states the overall purpose. <b>Specific objectives</b> break it into measurable tasks, commonly using verbs such as estimate, compare, determine, describe, explore or assess. Each objective should have a corresponding method and result.")
P("<b>Example aim:</b> To assess the relationship between self-reported sleep duration and examination performance among a defined undergraduate population.")
bullets(["Estimate the distribution of reported sleep duration.","Describe examination scores in the study population.","Estimate the association between sleep duration and scores using a prespecified analysis.","Explore selected confounders justified in the protocol."])
P("A null hypothesis commonly states no difference or association under a specified model; an alternative hypothesis states the effect or association being investigated. Hypotheses should follow the question and design, not be added decoratively to every descriptive study.")
h2("Conceptual framework")
P("A conceptual framework maps the expected relationships among exposure, outcome, confounders, mediators and contextual factors. Explain why each arrow is proposed and distinguish established evidence from assumptions. A diagram is useful only when accompanied by a clear explanation.")

H("5. Quantitative, qualitative and mixed-methods designs")
tbl([["Design/approach","Typical purpose","Important caution"],["Cross-sectional","Estimate prevalence or describe relationships at a point/period","Temporality and causation are often uncertain."],["Case-control","Compare prior exposures in people with and without an outcome","Selection and recall bias; cannot directly estimate incidence from ordinary sampling."],["Cohort","Follow exposed/unexposed groups or use defined historical records","Loss to follow-up and confounding can affect estimates."],["Randomised controlled trial","Compare allocated interventions under a protocol","Requires ethical equipoise, allocation concealment and appropriate safeguards."],["Laboratory/experimental","Test effects under controlled conditions","Specify controls, replication, randomisation and experimental unit."],["Qualitative","Understand experiences, meanings, processes or context","Rigour requires transparent sampling, reflexivity and analytic description."],["Mixed methods","Integrate quantitative patterns with qualitative explanations","State why both strands are needed and how they will be integrated."],["Systematic review","Answer a focused question using explicit, reproducible methods","Requires a protocol, comprehensive search, screening and risk-of-bias appraisal."]],[34*mm,73*mm,67*mm])
h2("Validity, reliability and bias")
P("<b>Validity</b> asks whether the method measures or estimates what it is intended to. <b>Reliability</b> concerns consistency under comparable conditions. A measurement can be reliable but invalid. Pilot testing can reveal unclear items, timing problems and workflow issues, but a small pilot does not automatically establish validity.")
bullets([
"<b>Selection bias:</b> inclusion differs in a way related to exposure and outcome.",
"<b>Information bias:</b> exposure or outcome is measured inaccurately or differently across groups.",
"<b>Confounding:</b> another factor distorts the exposure–outcome relationship.",
"<b>Observer bias:</b> expectations influence assessment or interpretation.",
"<b>Attrition:</b> loss to follow-up differs or is related to outcomes.",
"<b>Mitigation:</b> use clear eligibility criteria, standard procedures, validated tools where suitable, blinded assessment when feasible, quality checks and prespecified analysis."
])
h2("Choosing a design")
P("Start with the main objective. For prevalence, a well-designed cross-sectional survey may be appropriate. For incidence and temporal sequence, a cohort design may fit. For rare outcomes, a case-control design may be efficient. For intervention effects, a trial may be suitable if ethical and feasible. For lived experience, interviews or focus groups may be more informative. A supervisor and methodologist should review the choice before recruitment or experimentation.")

H("6. Population, sampling and sample-size planning")
h2("Population and sampling terms")
bullets([
"<b>Target population:</b> the wider group to which the research question refers.",
"<b>Accessible population:</b> the part realistically reachable under the study conditions.",
"<b>Study sample:</b> the individuals, records, specimens or units actually included.",
"<b>Sampling frame:</b> the list or mechanism from which units can be selected.",
"<b>Eligibility criteria:</b> predefined inclusion and exclusion rules."
])
h2("Probability and non-probability sampling")
tbl([["Method","How it works","Typical consideration"],["Simple random","Every eligible unit has a known chance; selection is random","Needs a suitable sampling frame."],["Systematic","Select every kth unit after a random start","Check for periodic patterns in the list."],["Stratified","Sample within meaningful strata","Can improve representation; plan allocation."],["Cluster/multistage","Sample groups and possibly units within groups","Design effects and analysis weights may matter."],["Convenience","Recruit accessible units","Often more vulnerable to selection bias."],["Purposive","Select information-rich cases for a qualitative purpose","Justify the range and information needs."],["Snowball","Participants refer other eligible participants","Useful for hard-to-reach groups but network bias is possible."]],[33*mm,73*mm,68*mm])
h2("Sample-size planning")
P("Sample size depends on the primary outcome, design, expected prevalence or effect, desired precision, type-I error, power where relevant, allocation ratio, variability, clustering, anticipated non-response and feasible resources. Use a method or software appropriate to the design and document all assumptions. Do not select a number merely because a previous student used it.")
P("For a simple prevalence estimate under common assumptions, a familiar starting formula is <b>n = Z² p(1 − p) / d²</b>, where Z is the normal critical value for the confidence level, p is the anticipated prevalence and d is the desired absolute precision. This formula assumes a simple random sample and other conditions; it may need finite-population correction, design-effect adjustment and inflation for non-response. It is not suitable for every design.")
P("For an illustrative example only, if p = 0.50, Z = 1.96 and d = 0.05, the unadjusted estimate is about 384.16, commonly rounded up to 385. This is not a recommendation for your specific project; confirm assumptions with your supervisor/statistician.")
h2("Non-response adjustment")
P("If the required completed sample is n and the expected response proportion is r, an approximate recruitment target is n/r. For example, 385/0.90 ≈ 428 people if 90% response is realistically expected. This adjustment does not fix biased non-response.")
callout("For animal experiments, laboratory studies, trials, clustered samples and multivariable models, sample-size planning may require different calculations. Use design-specific guidance rather than applying a prevalence formula indiscriminately.")

H("7. Instruments, data collection and laboratory methods")
h2("Questionnaires and interview guides")
bullets([
"Map each item to an objective or variable; remove questions that do not serve a purpose.",
"Use plain, neutral wording and one idea per question. Avoid leading, double-barrelled and ambiguous questions.",
"Define response options, units, recall period, skip logic and missing-value codes.",
"Use validated instruments where suitable and follow licensing, scoring and adaptation requirements.",
"Pilot the full process with people similar to the intended participants; document changes.",
"Train data collectors, standardise instructions and protect confidentiality."
])
h2("Laboratory and anatomical/experimental studies")
P("A reproducible laboratory method specifies study material, inclusion criteria, sample preparation, reagents and concentrations, equipment and calibration, controls, exposure conditions, timing, temperature, measurement procedures, blinding where feasible, quality assurance, and the planned analysis. For animal studies, report the species, strain, sex, age/weight, housing, randomisation, welfare measures, humane endpoints, anaesthesia/analgesia and ethical approval as applicable. Follow relevant institutional and reporting standards.")
h2("Data collection plan")
tbl([["Element","What to specify"],["Who/what","Eligibility, recruitment or specimen source, sampling and responsible personnel."],["Where/when","Setting, dates, sequence, follow-up and timing of measurements."],["How","Instrument, SOP, calibration, interviewer/lab training and recording process."],["Quality control","Pilot, range checks, duplicate checks, controls, supervision and audit trail."],["Safety and privacy","Risk mitigation, secure storage, access restrictions and incident response."],["Data flow","Collection → coding → verification → secure storage → analysis → retention/disposal."]],[34*mm,140*mm])

H("8. Research ethics, consent and integrity")
P("Ethical review protects participants and helps ensure that risks, benefits, recruitment, consent, privacy and scientific methods are acceptable. Requirements differ by jurisdiction, institution, funding and study type; obtain formal guidance from the appropriate research ethics committee or institutional review body.")
h2("Core ethical principles")
bullets([
"<b>Respect for persons/autonomy:</b> provide understandable information and respect voluntary decisions.",
"<b>Beneficence and non-maleficence:</b> maximise justified benefits and minimise avoidable harm.",
"<b>Justice:</b> select participants fairly and avoid placing burdens on groups without justification.",
"<b>Privacy and confidentiality:</b> collect only necessary information and protect identifiable records.",
"<b>Scientific and social value:</b> poorly designed research can expose participants to burden without producing useful knowledge."
])
h2("Informed consent checklist")
numbered([
"Explain purpose, procedures, duration, foreseeable risks and potential benefits.",
"Explain alternatives, voluntary participation, withdrawal rules and any limits to withdrawal once data are anonymised or analysed.",
"Explain confidentiality, data access, storage, future use and contact routes for questions or complaints.",
"Allow time for questions and check understanding; use a language and format the person understands.",
"Document consent according to approved procedures; obtain assent and parental/guardian permission where required.",
"Do not recruit or begin procedures before required approvals and permissions are in place."
])
h2("Special cases")
P("Research involving children, people with impaired decision-making capacity, sensitive personal data, human tissue, identifiable records, biological hazards or animals may require additional safeguards and approvals. Consent alone does not replace ethics review. A retrospective-record study is not automatically exempt. Do not fabricate an approval number or claim approval that was not granted.")
h2("Research integrity")
bullets([
"<b>Fabrication:</b> making up data or results.",
"<b>Falsification:</b> manipulating methods, materials, images or data so the research record is misleading.",
"<b>Plagiarism:</b> presenting another person's words, ideas, images or work as one's own without proper acknowledgement.",
"Disclose conflicts of interest, funding, relevant assistance and deviations from the approved protocol.",
"Preserve original data and maintain a transparent audit trail; correct genuine errors promptly.",
"Do not selectively hide inconvenient findings or misrepresent exploratory analyses as prespecified."
])

H("9. Data management and statistical analysis")
h2("Before collection begins")
bullets([
"Create a data dictionary: variable name, meaning, type, units, allowable values and missing-value code.",
"Design a secure, access-controlled storage plan and separate identifiers from analytic data where possible.",
"Define validation checks, backups, version control, retention period and secure disposal.",
"Write a statistical analysis plan linked to the objectives before examining outcome patterns where feasible.",
"Document data cleaning rules, exclusions, transformations and deviations."
])
h2("Descriptive and inferential analysis")
tbl([["Question/data","Possible summary or method","Interpretation caution"],["Categorical variable","Count and percentage","Give the denominator and handle missing data transparently."],["Continuous, roughly symmetric","Mean and standard deviation","Describe distribution and outliers; these summaries may mislead if highly skewed."],["Skewed continuous/ordinal","Median and interquartile range","Do not infer normality from a small sample alone."],["Association between categorical variables","Chi-square or Fisher's exact test, as appropriate","Check expected counts and design assumptions."],["Two independent group means","Suitable t-test or alternative based on assumptions/design","Report effect estimate and confidence interval, not only p-value."],["Paired measurements","Paired method reflecting within-unit dependence","Do not treat paired observations as independent."],["Association between continuous variables","Correlation or regression chosen for the question","Correlation alone does not establish causation."],["Binary outcome with covariates","Appropriate logistic regression model","Assess model specification, confounding and precision."],["Time-to-event outcome","Survival methods when assumptions and data structure fit","Account for censoring and relevant assumptions."],["Qualitative interviews","Systematic coding and thematic/other justified analysis","Explain analytic process, reflexivity and evidence supporting themes."]],[42*mm,67*mm,65*mm])
P("Select methods based on the research question, measurement scale, design, dependence structure and assumptions. A p-value is not the probability that the null hypothesis is true. A statistically significant result may be clinically trivial; a non-significant result does not prove no effect. Report estimates, uncertainty, sample size, relevant assumptions and limitations.")
h2("Worked example: interpreting a hypothetical table")
tbl([["Sleep category","Mean score (out of 100)","SD","n"],["Less than 6 h","64.2","10.1","80"],["6–8 h","70.5","9.4","150"],["More than 8 h","68.0","10.8","55"]],[43*mm,48*mm,32*mm,25*mm])
P("<b>Example interpretation:</b> In this hypothetical dataset, the 6–8-hour group has the highest observed mean examination score. The table alone does not show whether differences are statistically compatible with chance, whether confounding explains the pattern, or whether sleep duration caused the scores. A suitable analysis, confidence intervals, data-quality checks and a cautious discussion would be required. These numbers are illustrative only, not real research findings.")
h2("Missing data and outliers")
P("Report how much data are missing for key variables and why, if known. Distinguish impossible values from genuine extreme observations. Do not delete outliers only because they weaken a preferred conclusion. Choose complete-case analysis, imputation or other approaches based on the missingness mechanism, assumptions, design and guidance from a statistician. Preserve a record of all changes.")
h2("Qualitative analysis in brief")
numbered([
"Familiarise yourself with transcripts or notes and document context.",
"Develop initial codes using a stated inductive, deductive or combined approach.",
"Compare codes across cases and group them into candidate categories/themes.",
"Review themes against the data, including contradictory or deviant cases.",
"Define and name themes; support claims with carefully selected, anonymised extracts where appropriate.",
"Explain researcher position/reflexivity, the analytic approach and how credibility was supported."
])

H("10. Writing the proposal and thesis/dissertation")
P("Your institution's handbook is authoritative for the required chapter structure, word count, referencing style, margins, front matter and appendices. The outline below is a flexible planning guide, not a universal rule.")
h2("Typical proposal structure")
numbered([
"Title page and required declarations/forms.",
"Abstract or project summary, if required.",
"Chapter 1 / Introduction: background, problem statement, justification/significance, aim, objectives, questions/hypotheses and scope.",
"Chapter 2 / Literature review: critical synthesis, theoretical/conceptual framework and identified gap.",
"Chapter 3 / Methodology: design, setting, population, eligibility, sample size, sampling, variables, instruments/procedures, data analysis, ethics and quality assurance.",
"Work plan/timeline and budget, where required.",
"References and appendices: tools, participant information/consent, approval documents and supplementary materials as appropriate."
])
h2("Typical completed dissertation structure")
tbl([["Section","What it should accomplish"],["Preliminary pages","Title page, declarations, abstract, acknowledgements, contents, lists of tables/figures and abbreviations as required."],["Chapter 1: Introduction","Explain the context, problem, rationale, aim/objectives and research questions."],["Chapter 2: Literature review","Critically synthesise prior work and establish the gap/framework."],["Chapter 3: Methodology","Give enough accurate detail to evaluate and, where appropriate, reproduce the methods."],["Chapter 4: Results","Present findings in a logical order without inventing or over-interpreting them."],["Chapter 5: Discussion","Interpret results against objectives and literature; address alternative explanations, strengths and limitations."],["Conclusion/recommendations","Answer the objectives, state implications proportionately and suggest justified next steps."],["References/appendices","Provide traceable sources and necessary supporting documents."]],[38*mm,136*mm])
h2("Suggested word-budget planning (illustrative only)")
tbl([["Section","Possible planning range"],["Abstract","200–350 words, subject to institutional/journal rules"],["Chapter 1","1,500–3,000 words"],["Chapter 2","3,000–7,000 words, depending on scope and programme"],["Chapter 3","1,500–3,500 words"],["Results","1,500–3,500 words"],["Discussion","2,000–4,000 words"],["Conclusion/recommendations","500–1,200 words"]],[55*mm,119*mm])
P("These ranges are planning aids, not prescribed requirements. Some departments use different chapter arrangements or total lengths; follow the current departmental handbook and supervisor's direction.")
h2("Writing a useful abstract")
P("A structured abstract often covers background/problem, objective, design/setting, participants or materials, methods, principal results and conclusion. For a proposal, describe planned methods and expected contribution without presenting hypothetical results as completed findings. For a completed study, report actual results with key estimates where appropriate.")
h2("Methods chapter: reproducibility test")
P("Could a competent researcher understand who or what was studied, how the sample was selected, what was measured, when and where procedures occurred, how quality was controlled, how ethics were handled and how the analysis was performed? If not, add the missing detail. Do not hide important methods in an appendix if the reader needs them to understand the study.")

H("11. Results, discussion, conclusion and recommendations")
h2("Results")
bullets([
"Organise results around objectives or research questions.",
"Describe the sample and relevant missingness before presenting outcome analyses.",
"Use tables and figures to complement—not duplicate—text.",
"Give denominators, units, effect estimates and uncertainty where appropriate.",
"Report prespecified and exploratory analyses transparently, identifying them as such.",
"Do not interpret every number in the Results section; reserve broader meaning for the Discussion."
])
h2("Discussion")
numbered([
"Summarise the principal findings in relation to the objectives.",
"Compare them with relevant prior studies, explaining similarities and differences.",
"Discuss plausible explanations without presenting speculation as fact.",
"Explain clinical, educational, laboratory or policy implications only as far as evidence permits.",
"State strengths and limitations, including bias, precision, generalisability and measurement constraints.",
"Identify implications for future research and avoid claims unsupported by the design."
])
h2("Conclusion and recommendations")
P("The conclusion should answer the research question directly and match the results. Recommendations should be specific, feasible and justified by the evidence. A small single-site observational study rarely justifies broad causal or national policy claims. Do not introduce new results in the conclusion.")
h2("Tables and figures")
bullets(["Give every table/figure a clear number and informative title.","Define abbreviations, units, denominators and statistical symbols in notes.","Avoid 3-D chart effects and misleading axes; choose a visual suited to the data.","Cite and obtain permission for reused material when required; label adaptations honestly.","Ensure tables and figures remain readable in print and on mobile screens."])

H("12. Referencing, plagiarism and responsible use of AI")
h2("Build a reliable reference trail")
bullets([
"Keep bibliographic details as soon as you save a source: authors, year, title, journal/book, volume, pages and DOI/URL as applicable.",
"Use a reference manager if available, but verify each citation and bibliography entry against the original source.",
"Choose the required style (for example, APA 7 or Vancouver) and apply it consistently.",
"Prefer original research, authoritative guidelines and current systematic reviews appropriate to the question.",
"Never cite a source you have not checked, invent a DOI, or rely on an AI-generated reference without verification."
])
h2("Paraphrasing correctly")
P("Read the source, close it, write the idea in your own structure and wording, then compare to ensure the meaning is accurate. Cite the source even when paraphrased. Direct quotations need quotation marks and a citation in styles that require them. Common terminology does not remove the need to credit distinctive ideas, data, images or methods.")
h2("AI tools and academic integrity")
P("Use AI, where permitted, for brainstorming, outlining, language feedback or learning statistical concepts—not as a substitute for source verification, ethical judgement or actual data analysis. Check institutional rules about disclosure. Do not upload identifiable participant information, confidential records or unpublished sensitive data to tools without authorisation. Researchers remain responsible for the accuracy of every claim, citation, analysis and conclusion.")
callout("A similarity score is not, by itself, a verdict on plagiarism. Review matched passages, attribution, quotations and institutional policy. The goal is honest scholarship, not merely a low percentage.")

H("13. Publication, presentation and oral defence")
h2("From thesis to manuscript")
P("Before choosing a journal, check scope, audience, article types, peer-review process, editorial board, indexing claims, fees and publication ethics. Be cautious of unsolicited promises of guaranteed acceptance or unrealistically rapid publication. Follow the target journal's author instructions and relevant reporting guideline.")
P("Common reporting resources include CONSORT for randomised trials, STROBE for observational studies, PRISMA for systematic reviews, STARD for diagnostic accuracy, CARE for case reports, COREQ/SRQR for qualitative studies and ARRIVE for animal research. Select the current guideline appropriate to the actual design; reporting checklists do not replace good methods.")
h2("Conference poster or oral presentation")
bullets(["State one clear research question and why it matters.","Use a simple structure: background/objective, methods, results, conclusion and limitations.","Show the most informative results, with readable labels and units.","Prepare a short verbal explanation and anticipate questions about design, sample size, bias and implications.","Disclose conflicts and acknowledge collaborators, funding and contributions accurately."])
h2("Defence preparation")
P("Prepare to explain why the question matters, how the literature supports the gap, why the design was appropriate, how sample size was determined, how bias and ethics were addressed, why the analysis fits the objectives, what the findings mean, and what the study cannot conclude. If you do not know an answer, state the limitation honestly and explain how you would investigate it.")

H("14. Worked examples, tables and templates")
h2("Template A: one-page concept note")
tbl([["Field","Complete this section"],["Working title","Specific population/setting + main exposure or phenomenon + outcome where useful."],["Background/problem","What is known, what is uncertain, and why does it matter?"],["Research question","One clear, answerable question."],["Aim and objectives","One overall aim and a small set of measurable objectives."],["Design and setting","Proposed design, site and time period."],["Population/sample","Eligibility, sampling method, sample-size rationale and access."],["Measures/procedures","Variables, tools, SOPs, quality controls."],["Analysis","Method mapped to each objective; software if relevant."],["Ethics/permissions","Risks, consent, confidentiality, approvals and permissions needed."],["Feasibility","Time, budget, equipment, expertise and anticipated barriers."],["Key references","A short list of verified sources underpinning the question and methods."]],[42*mm,132*mm])
h2("Template B: objective-to-analysis matrix")
tbl([["Objective","Variable/data","Source/instrument","Planned analysis","Output"],["Describe participant characteristics","Age, category, other defined measures","Questionnaire/record","Counts/percentages; appropriate continuous summaries","Table 1"],["Estimate primary outcome","Prespecified outcome measure","Validated tool/lab protocol","Estimate with confidence interval where appropriate","Primary result"],["Assess association/difference","Exposure/group and outcome","Defined protocol","Model/test chosen for design and assumptions","Effect estimate and uncertainty"]],[36*mm,36*mm,38*mm,43*mm,21*mm])
h2("Template C: simple data dictionary")
tbl([["Variable","Meaning","Type/unit","Allowed values","Missing code"],["id","Study identifier","Text/integer","Unique; no direct identifier","Not applicable"],["age_years","Age at enrolment","Numeric; years","Prespecified plausible range","NA or documented code"],["group","Exposure/category","Categorical","Defined labels and reference group","NA"],["outcome","Primary outcome","Defined scale/unit","Permitted range based on instrument","NA"]],[30*mm,42*mm,33*mm,42*mm,27*mm])
h2("Template D: sample results write-up")
P("“Of the [N] eligible participants approached, [n] were included in the analysis ([%]). The primary outcome was [estimate] ([95% confidence interval, if appropriate]). Compared with [reference group], [group] had [effect estimate] with [uncertainty measure]. These results should be interpreted in light of [key limitation].” Replace brackets only with verified results from your own analysis.")
h2("Template E: research budget headings")
bullets(["Personnel and training, where allowed.","Transport and field logistics.","Consumables, reagents, specimen handling and equipment access.","Printing, communication, data collection and secure storage.","Software or statistical support, including free institutional alternatives.","Ethics/administrative charges where applicable and officially confirmed.","Dissemination, contingency and justification for each cost."])
P("Do not invent quotations or hide costs. Separate one-off equipment from recurring costs, record the currency/date and follow funding or institutional rules.")

H("15. Final checklists and revision questions")
h2("Before proposal submission")
for x in [
"The research question, problem statement, aim and objectives align.",
"The literature review is critical, current enough for the field and accurately referenced.",
"The design fits the question; population, eligibility and sampling are explicit.",
"Sample size and its assumptions are justified by a suitable method.",
"Variables, instruments, procedures and quality assurance are described.",
"Analysis is mapped to each objective and planned before outcome-driven decisions.",
"Ethics, consent, privacy, safety and permissions are addressed honestly.",
"Timeline, budget and access to facilities/data are feasible.",
"All references, appendices and required institutional forms are checked."
]: P("☐&nbsp;&nbsp;"+x)
h2("Before final submission or defence")
for x in [
"Results match the verified dataset and no values have been fabricated or selectively concealed.",
"Every table and figure is numbered, readable, explained and cited where needed.",
"Discussion distinguishes findings from speculation and acknowledges limitations.",
"Conclusion answers the objectives without exceeding the evidence.",
"References and in-text citations agree and follow the required style.",
"Ethics approval details and consent statements are accurate.",
"Reporting guideline and university formatting requirements have been checked.",
"All co-authors/contributors, funding and conflicts are disclosed appropriately."
]: P("☐&nbsp;&nbsp;"+x)
h2("Revision questions with concise answers")
qa=[
("1. What distinguishes a research aim from an objective?","The aim is the overall purpose; objectives are specific, measurable steps used to achieve it."),
("2. Why should design follow the research question?","Different questions require different evidence; a mismatched design may not answer the question validly."),
("3. What is a confounder?","A factor related to exposure and outcome that can distort their observed association, under the causal structure of the study."),
("4. Does a small p-value prove clinical importance?","No. Magnitude, uncertainty, context and potential harms/benefits matter."),
("5. What does a confidence interval communicate?","A range of estimates compatible with the data under the method's assumptions, expressing uncertainty; it is not a guarantee that the true value lies in this particular interval."),
("6. Why pilot a questionnaire?","To identify comprehension, timing, response-option and workflow problems; piloting alone does not establish full validity."),
("7. Is convenience sampling always invalid?","Not always, but it limits representativeness and requires transparent justification and cautious interpretation."),
("8. Can consent replace ethics review?","No. Consent and independent ethics review serve related but distinct purposes where review is required."),
("9. What is the difference between fabrication and falsification?","Fabrication invents data/results; falsification manipulates research materials, processes or data so the record is misleading."),
("10. Why define missing data codes?","To distinguish absent responses from legitimate values and prevent accidental misclassification during analysis."),
("11. What should the discussion include?","Interpretation against objectives and prior evidence, plausible explanations, implications, strengths, limitations and future directions."),
("12. What is a reporting guideline for?","To improve completeness and transparency of reporting for a specific study design; it does not replace sound design or ethics."),
("13. Can a cross-sectional association establish causation?","Usually not on its own, because temporality and alternative explanations may remain uncertain."),
("14. What makes a reference trustworthy?","It is real, traceable, relevant, accurately represented and appropriate in quality and currency for the claim."),
("15. What is the most important rule when results are unexpected?","Report them honestly, check data and methods transparently, and do not change or conceal findings to fit expectations.")
]
for q,a in qa:
    P("<b>"+escape(q)+"</b>")
    P(escape(a))
h2("A final word")
P("Good research is a disciplined habit: ask a clear question, use methods that fit it, protect people and data, keep an honest record, analyse carefully and communicate within the limits of the evidence. No guide can replace a supervisor, statistician, ethics committee or university handbook, but a structured process makes discussions with them more productive.")

H("References and further learning")
P("The following authoritative resources are starting points for further reading. Consult the current version and the specific requirements relevant to your project. This guide is an independent educational resource and is not affiliated with or endorsed by the organisations listed.")
refs=[
"World Health Organization. (2020). <i>A practical guide for health researchers</i>. WHO Regional Office for the Eastern Mediterranean. https://www.who.int/publications/i/item/a-practical-guide-for-health-researchers",
"World Health Organization. (n.d.). <i>Recommended format for a research protocol</i>. Research Ethics Review Committee. https://www.who.int/groups/research-ethics-review-committee/recommended-format-for-a-research-protocol",
"World Health Organization. (n.d.). <i>Health Ethics &amp; Governance: Research</i>. https://www.who.int/teams/health-ethics-governance/governance/research",
"EQUATOR Network. (n.d.). <i>Reporting guidelines for health research</i>. https://www.equator-network.org/",
"Council for International Organizations of Medical Sciences. (2016). <i>International ethical guidelines for health-related research involving humans</i> (4th ed.). CIOMS. https://cioms.ch/publications/product/international-ethical-guidelines-for-health-related-research-involving-humans/",
"National Institutes of Health, Office of Research on Women's Health. (n.d.). <i>Research methods and study design resources</i>. Consult current NIH and institutional resources relevant to the topic.",
"International Committee of Medical Journal Editors. (n.d.). <i>Recommendations for the conduct, reporting, editing, and publication of scholarly work in medical journals</i>. https://www.icmje.org/recommendations/",
"American Psychological Association. (2020). <i>Publication manual of the American Psychological Association</i> (7th ed.). American Psychological Association."
]
for i,r in enumerate(refs,1): P(f"{i}. {r}")
P("<b>Recommended next step:</b> identify the reporting guideline for your design through EQUATOR Network, confirm the current university project handbook, and review the WHO research-protocol guidance before finalising a health-research proposal.")
P("<b>Educational disclaimer:</b> This guide is for learning and planning. It is not a substitute for professional statistical advice, legal guidance, ethics review, clinical judgement, or local institutional requirements.","Smallx")

doc=SimpleDocTemplate(OUT,pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=18*mm,bottomMargin=22*mm,title="Research Methodology Study Guide | Anatomist Vitalis",author="Ibine Oladipupo Rapheal",subject="Practical research methods for health-science students")
doc.build(story,onFirstPage=cover,onLaterPages=footer)
print(f"Created {OUT} ({os.path.getsize(OUT)} bytes)")
