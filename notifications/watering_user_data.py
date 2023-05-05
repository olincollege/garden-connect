"""
Display for completion of survey results
"""
#!/usr/bin/env python
import cgi

from plant_interest_survey import PlantInterest # pylint: disable=E0401

form = cgi.FieldStorage()

plants_interest = form.getvalue("plants_interest")
garden_location = form.getvalue("garden_location")
watering_time = form.getvalue("watering_time")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Python Survey Results</title>")
print("</head>")
print("<body>")
print("<h1>Python Survey Results</h1>")
print("<p>Thank you for taking our survey!</p>")

survey = PlantInterest()

survey.plants_interest = plants_interest
survey.garden_location = True if garden_location == "outside" else False
survey.watering_time = int(watering_time)
