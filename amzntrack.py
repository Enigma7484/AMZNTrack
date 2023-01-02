import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/Logitech-Lightspeed-Suspension-LIGHTSYNC-Technology/dp/B084TFWTH5/?_encoding=UTF8&pd_rd_w=yFhf4&content-id=amzn1.sym.b09e9731-f0de-43db-b62a-8954bcec282c&pf_rd_p=b09e9731-f0de-43db-b62a-8954bcec282c&pf_rd_r=YR9FKYDPMKN10GN41YX3&pd_rd_wg=ujhst&pd_rd_r=a3c5ddc3-1653-4347-b960-d5b427694e63&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1'

headers = {
    "User-Agent": 'https://www.amazon.ca/Logitech-Lightspeed-Suspension-LIGHTSYNC-Technology/dp/B084TFWTH5/?_encoding=UTF8&pd_rd_w=yFhf4&content-id=amzn1.sym.b09e9731-f0de-43db-b62a-8954bcec282c&pf_rd_p=b09e9731-f0de-43db-b62a-8954bcec282c&pf_rd_r=YR9FKYDPMKN10GN41YX3&pd_rd_wg=ujhst&pd_rd_r=a3c5ddc3-1653-4347-b960-d5b427694e63&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.get_text)