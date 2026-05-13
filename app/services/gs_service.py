import gspread as gs

def gs_connector(creds, sheet_id, sheet_name):
    client = gs.service_account(creds)
    sheet = client.open_by_key(sheet_id)
    return sheet.worksheet(sheet_name)