import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings


CREDENTIAL = F'{settings.BASE_DIR}/services/google/credentials/credentials.json'

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIAL, scope)


class Sheet:
  file = None
  sheet = None
  name = None

  def __init__(self, name):
    self.name = name
    self.file = gspread.authorize(credentials)
    self.sheet = self.file.open(self.name).sheet1

  def get_all(self, head=1):
    return self.sheet.get_all_records(head=head)

  def batch_get(self, index: int):
    try:
      return self.sheet.batch_get([f'A{index}:D'])[0]
    except:
      return []

  def add_row(self, row: list):
    self.sheet.append_row(row)

  def update_all(self, array, cels='A1'):
    self.sheet.update(cels, array)

  @property
  def row_count(self):
    return len(self.get_all())
