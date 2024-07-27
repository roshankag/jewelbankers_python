import json
from fastapi import HTTPException
import google.generativeai as genai
import os
import json 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'c:\Users\deepa\Downloads\orbital-stream-426213-r2-6040f858ab8b.json'
prompt= """
  Given the need, generate a JSON response based on the following conditions:

  1. If the need is "pledge", return JSON with:
     - need
     - customer_name
     - weight
     - article (auto-filled based on item_description)
     - item_description
     - amount
  
     The article should be filled as follows:
     - If item_description contains 'gold', set article to 'gold'.
     - If item_description contains 'silver', set article to 'silver'.
     - Otherwise, set article to 'ornament'.

  2. If the need is "redeem", return JSON with:
     - billnumber
       - bill_serial
       - bill_number

  3. If the need is "search", return JSON with:
     - customer_name
     - bill_number

  4. If the need is "print", return JSON with:
     - print_details (details to be specified based on the context of the print operation)
  if there is no proper text supply all value as null and bill serial is the alphabet present before the bill number 
  Return the JSON in the following format:
  {
    "need": str,
    "customer_name": str (optional),
    "weight": float (optional),
    "article": str (optional),
    "amount": int (optional),
    "item_description": str (optional),
    "billnumber": {
      "bill_serial": str (optional),
      "bill_number": str (optional)
    },
    "print_details": str (optional)
  }
"""


def speech(inp):
    api_key='AIzaSyCivb2rBfdp-xP-nU7xCszkpOo5JdJM-24'
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-001",generation_config={"response_mime_type": "application/json"})
    response=model.generate_content(prompt+inp)
    try:
        response_json = json.loads(response.text)
        return response_json
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")




