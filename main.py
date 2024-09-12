from flask import Flask, render_template, request, redirect, url_for
from airtable import Airtable

app = Flask(__name__)


AIRTABLE_BASE_ID = 'your_base_id'
AIRTABLE_TABLE_NAME = ''
AIRTABLE_API_KEY = 'pat2QwwpmKHkee7GL.26cd860c6cbdef70f731fb8893ed731f0b9c13df61f8de83d551242f635e28bd'

airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)