PROJECT REPORT

SMART RESUME ANALYZER

NATURAL LANGUAGE PROCESSING


RESUME ANALYSER USING PYTHON AND FLASK

A Web-Based Intelligent Resume Evaluation System



1.	Introduction

The recruitment process in modern organizations has evolved significantly with the integration of digital technologies. In today’s competitive job market, employers receive hundreds or even thousands of resumes for a single job opening. Reviewing each resume manually is both time-consuming and inefficient. To overcome this challenge, many organizations use automated systems known as Applicant Tracking Systems (ATS) to filter, rank, and shortlist resumes before they are reviewed by human recruiters.

Despite this advancement, a large number of job seekers are unaware of how resumes are evaluated. Many resumes are rejected not because candidates lack skills, but because their resumes are poorly structured, missing critical information, or not optimized for automated screening systems. As a result, there exists a clear need for a system that can assist individuals in evaluating and improving their resumes before submission.

The Resume Analyser project is designed to address this problem by creating an intelligent web-based system capable of analyzing resumes, extracting relevant information, evaluating structural completeness, identifying technical and soft skills, and assigning a quantitative score based on predefined evaluation metrics. The system provides constructive feedback to users, enabling them to enhance their resumes effectively.

This project integrates concepts from web development, text processing, pattern recognition, and basic natural language processing. It demonstrates how automation can be applied to resume screening and highlights the importance of structured data analysis in recruitment technologies.



2.	Background and Motivation

In traditional recruitment processes, resume screening is performed manually by HR professionals. However, due to the large volume of applications, organizations rely heavily on automated resume screening tools. These tools evaluate resumes based on keyword matching, structural completeness, and relevance to job descriptions.

Many job seekers lack access to such evaluation systems prior to submitting their resumes. As a result:

Important sections such as certifications or projects may be missing.

Contact information may not be clearly visible.

Skills may not be listed in a structured format.

The resume may not align with ATS parsing standards.


The motivation behind this project is to democratize access to resume evaluation tools by building a web-based application that allows users to upload their resumes and receive instant feedback.

The system aims to simulate basic ATS functionality while remaining lightweight and easy to use.



3.	Problem Statement

The primary problem addressed in this project is the lack of accessible tools for automated resume evaluation and feedback generation.

Specifically:

1.	Job seekers do not know whether their resume includes all essential sections.


2.	There is no immediate way to quantify resume quality.


3.	Missing skills or incomplete information reduce hiring chances.


4.	Users do not receive structured suggestions for improvement.



The challenge lies in designing a system that can:

Extract textual content from resume files.

Analyze text for important components.

Detect patterns such as emails and phone numbers.

Identify skills using keyword-based matching.

Generate a fair and explainable scoring mechanism.

Present results in a user-friendly interface.




5.	Objectives of the Project

The primary objective of the Resume Analyser system is to design and implement an automated resume evaluation platform using Python and Flask.

The specific objectives include:

Developing a web interface for resume upload.

Implementing PDF text extraction mechanisms.

Designing algorithms to detect resume sections.

Creating a scoring model based on multiple evaluation factors.

Generating improvement suggestions dynamically.

Visualizing results using an interactive frontend.

Ensuring system reliability and usability.




6.	Literature Review and Theoretical Foundation

Automated resume analysis systems are widely used in corporate recruitment platforms. These systems typically rely on:

Natural Language Processing (NLP)

Keyword extraction

Named Entity Recognition (NER)

Machine learning classification models

Semantic similarity algorithms


However, large-scale systems require complex infrastructure and datasets. For the scope of this project, a rule-based analytical model was implemented instead of a machine learning model.

The theoretical foundation of this project includes:

1.	Text Parsing: Converting PDF documents into machine-readable text.


2.	Regular Expressions: Pattern matching for emails and phone numbers.


3.	Keyword Matching: Identifying sections and skills using predefined lists.


4.	Heuristic Scoring: Assigning weights to resume components.


5.	Web Framework Architecture: Client-server communication via Flask.



This hybrid approach ensures computational efficiency while maintaining functional accuracy.



6.	System Architecture

The Resume Analyser follows a client-server architecture.

When a user uploads a resume through the web interface, the file is transmitted to the Flask backend server. The backend processes the file, extracts text, performs analysis, calculates a score, generates suggestions, and sends the results back to the frontend template for display.

The architecture consists of the following components:

1.	User Interface Layer (HTML/CSS)


2.	Application Layer (Flask)


3.	Processing Layer (Text Analysis Engine)


4.	Scoring Engine


5.	Result Rendering Module



The separation of concerns ensures modularity and maintainability.



6.	Detailed System Design

7.1 File Handling and Security

The system accepts only PDF files to ensure compatibility and prevent malicious uploads. The file is saved temporarily using secure filename handling provided by the Werkzeug library. This prevents directory traversal attacks and ensures safe file storage.

After processing, the file can be deleted to maintain storage efficiency.



7.2 PDF Text Extraction Process

The PDF extraction process is implemented using the PyPDF2 library.

The algorithm operates as follows:

1.	Open the PDF file in binary read mode.


2.	Initialize a PDF reader object.


3.	Iterate through each page.


4.	Extract textual content from each page.


5.	Concatenate extracted text into a single string variable.



Mathematically, if a PDF contains n pages:

Text_total = Σ ExtractText(Page_i) for I = 1 to n

This combined text is then normalized by converting it to lowercase to ensure case-insensitive analysis.



7.3 Contact Information Detection Using Regular Expressions

Regular expressions are used for pattern recognition.

Email detection pattern:

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+

Phone number detection pattern supports:

International formats

10-digit numbers

Numbers with separators


Regular expressions provide efficient O(n) time complexity for pattern matching, where n represents text length.



7.4 Section Detection Algorithm

Section detection is performed using keyword-based searching.

For example:

If “education” exists in text → Education section marked as present.

Let S be set of required sections:

S = {Education, Experience, Projects, Certifications, Skills}

For each section s ∈ S:

If keyword(s) ∈ Text → mark present
Else → mark missing

This rule-based detection ensures fast processing without requiring NLP parsing models.



7.5 Skills Detection Mechanism

Skills detection is performed using predefined lists of:

Technical skills

Soft skills


Each skill in the list is checked against the resume text.

If skill_i ∈ Text → add to detected skills list.

This approach ensures simplicity while covering commonly used skills.



7.6 Resume Scoring Model

The scoring model assigns weights to different components.

Let:

E = Email presence (1 or 0)
P = Phone presence (1 or 0)
Sec = Number of sections present
TS = Technical skills detected
SS = Soft skills detected

Score = Weighted sum of these parameters.

Final score is normalized to 10.

This ensures fairness and transparency in evaluation.



7.	User Interface Design

The frontend is designed using HTML and CSS with Jinja templating.

The result page includes:

Resume score visualization using progress bar

Highlighting of missing sections

List of detected skills

Improvement suggestions

Option to upload another resume


The UI emphasizes clarity, readability, and professional aesthetics.



8.	Testing and Validation

The system was tested using multiple resume samples:

Well-structured resumes

Incomplete resumes

Resumes without skills

Resumes missing contact information


Results showed that the system accurately detects missing components and assigns appropriate scores.



9.	Limitations

While effective, the system has limitations:

Skill detection limited to predefined list.

Does not perform deep semantic analysis.

Does not evaluate formatting or design layout.

Does not compare resume to job descriptions.




10.	Future Enhancements

Future improvements may include:

Integration of spaCy NLP library.

Named Entity Recognition for advanced parsing.

Machine learning scoring model.

Job-description matching system.

Grammar analysis integration.

Database storage for user reports.

Deployment on cloud platforms.




11.	Conclusion

The Resume Analyser project successfully demonstrates the development of a rule-based intelligent resume evaluation system using Python and Flask. It integrates text extraction, pattern recognition, structured evaluation, and web-based result visualization.

The system provides actionable insights, helping users improve their resumes before job applications. It showcases practical software engineering skills and demonstrates the application of computational techniques in recruitment technology.



                                                                          END OF REPORT
