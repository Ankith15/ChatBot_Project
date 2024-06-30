import re
from pdfminer.high_level import extract_text

from pypdf import PdfReader
data=PdfReader('Job Profile Details.pdf')
text=''
for page in data.pages:
  text+=page.extract_text()
print(text)
ctc_regex = re.compile(r'(?i)(CTC|Cost to Company|Salary|Total Compensation|Total Remuneration|Pay Package|Compensation Package|Salary Package|Total Rewards|Total Earnings|Gross Salary|Total Pay|Complete Salary Package|Yearly Salary|Overall Compensation|Overall Salary|Aggregate Salary|Annual Compensation|Employee Cost|Comprehensive Salary|Overall Cost to Company|Total Salary)(.*?)(?=\n|$)')
location_regex = re.compile(r'(?i)(Job Location|Office|Work Location)(.*?)(?=\n|$)')
role_regex = re.compile(r'(?i)(Role:|Position:|Title:)(.*?)(?=\n|$)')
job_description_regex = re.compile(r'(?i)(Job Description:|Description:|Job Details:|Job Responsibility:|Qualifications\n)(.*?)(?=\n|$)')

ctc = ctc_regex.findall(text)
location = location_regex.findall(text)
role = role_regex.findall(text)
description = job_description_regex.findall(text)

ctc_details = [match[1].strip() for match in ctc]
location_details = [match[1].strip() for match in location]
role_details = [match[1].strip() for match in role]
description_details = [match[1].strip() for match in description]

print("CTC Details:", ctc_details)
print("Location Details:", location_details)
print("Role Details:", role_details)
print("Job Description Details:", description_details)