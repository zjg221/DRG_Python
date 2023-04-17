from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["34.7400x001","34.7400x005","34.7400x007","34.7400x008","34.7400x009","34.7400x010","34.7401","34.7402","34.7403","34.7900x001","34.7900x002","34.7900x003","34.7900x004","34.8101","34.8102","39.9801","40.2900x019","77.1001","77.1002","77.1003","77.1101","77.1102","77.1103","77.1104","77.2100x001","77.2100x002","77.2101","77.2102","77.2103","77.2104","77.3001","77.3101","77.3102","77.3103","77.3104","78.0000x003","78.0100x002","78.0101","78.0102","78.0103","78.0104","78.1101","78.1102","78.1103","78.1104","78.2001","78.2002","78.2003","78.3000","78.4101","78.4102","78.4103","78.4104","78.4105","78.4106","78.5100x003","78.5100x004","78.5100x005","78.5100x006","78.5100x007","78.5100x009","78.5100x010","78.5100x011","78.5100x012","78.5100x013","78.5100x014","78.5100x015","78.5100x016","78.5100x017","78.5100x018","78.5101","78.5102","78.5103","78.5104","78.7101","78.7102","78.7103","78.7104","78.9900x001","79.1901","79.3900x034","79.3900x036","79.3900x049","79.3900x053","79.3900x054","79.3903","79.3905","79.4900","79.5900","79.6000","79.7000","79.9000","79.9900","80.1900","80.5900x001","80.5900x003","80.9900x001","80.9900x002","80.9900x003","80.9900x004","80.9900x005","80.9900x006","80.9901","80.9902","80.9903","81.5900","81.9101","81.9201","81.9202","81.9900","82.0300","82.3100","82.9300x001","83.0300","83.0301","83.0900x003","83.0901","83.0902","83.0903","83.0904","83.1900x001","83.1900x003","83.1900x008","83.1900x009","83.1900x010","83.1900x012","83.1900x013","83.1900x017","83.1900x018","83.1900x019","83.1900x020","83.1900x023","83.1900x024","83.1900x025","83.1900x026","83.1900x027","83.1900x028","83.1900x030","83.1900x031","83.1901","83.1902","83.1903","83.1904","83.2900x001","83.2900x002","83.2900x003","83.3100","83.3100x001","83.3100x008","83.3101","83.3900x001","83.3900x016","83.3900x017","83.3901","83.3902","83.3903","83.3904","83.4500x001","83.4500x003","83.4500x004","83.4500x005","83.4500x006","83.4500x007","83.4500x008","83.4501","83.4502","83.4900","83.5x00","83.8400","83.8401","83.8800x001","83.8800x010","83.8800x012","83.8800x014","83.8800x015","83.8800x016","83.8800x017","83.8800x018","83.8801","83.8802","83.8803","83.9400","83.9600","83.9800x001","83.9900x003","83.9901","84.2900","84.3x00","84.4400","84.4800","84.5300","84.5400x001","84.5500x003","84.5500x004","84.5500x005","84.5501","84.5600x001","84.5601","84.5700x001","84.9200","84.9300","84.9400","84.9900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IJ1入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IJ15_group(record):
      return 'IJ15'

    if MDCI_DRG.IJ1A_group(record):
      return 'IJ12'

    return 'IJ1'
  else:
    return ''

