# Week 1 Data Collection Plan

Owner: A - Data & Ingestion

## Objective

Prepare a realistic corpus plan for Week 2 so ingestion can start without unclear ownership, missing metadata, or weak document diversity.

## Target Corpus

- Minimum documents: 25-30.
- Target size: about 300-500 pages.
- Subjects: at least 3 different courses or topics.
- Formats: PDF, DOCX, PPTX, and at least a few scanned/image-based documents.
- Include some dirty layouts: two-column PDFs, tables, formulas, low-quality scans, and unusual fonts.

## Metadata Schema v0

| Field | Description | Required |
| --- | --- | --- |
| doc_id | Stable document id, for example `doc_0001` | Yes |
| filename | Original file name | Yes |
| file_type | pdf, docx, pptx, image, scan_pdf | Yes |
| source | Who provided it or where it came from | Yes |
| subject | Course/topic | Yes |
| page_count | Estimated or exact page count | Yes |
| language | vi, en, mixed | Yes |
| permission | Whether the team can use it for this project | Yes |
| notes | Layout issues, scan quality, special handling | No |

## Collection Checklist

- List all documents currently available from team members.
- Check whether each document is allowed to be used.
- Place source files under `data/raw/` locally. Do not commit raw personal documents.
- Create metadata records under `data/metadata/` once the schema is confirmed.
- Flag documents that need OCR.

## Week 2 Gate

Week 2 can start when the team has corpus v0 plus metadata for each file.
