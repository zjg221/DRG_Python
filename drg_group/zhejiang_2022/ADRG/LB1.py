from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCL_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.1x00x006","39.1x00x008","39.1x07","39.2200x011","39.2401","39.2600x004","39.2605","39.5500","39.5900x010","55.0108","55.0303","55.3903","55.4x00","55.4x01","55.4x02","55.4x03","55.4x04","55.4x05","55.5100","55.5101","55.5102","55.5103","55.5104","55.5105","55.5106","55.5200","55.5201","55.5300x001","55.5400","55.5401","55.7x00","55.7x01","55.8101","55.8102","55.8600x006","55.8601","55.8602","55.8603","55.8604","55.8605","55.8606","55.8701","55.8702","55.8703","55.8704","55.8900x002","55.8900x003","55.8900x004","55.8901","55.8902","55.8903","55.9100x004","55.9100x005","55.9701","55.9702","55.9800","55.9900x001","55.9901","55.9903","56.4200","56.4201","56.7102","56.7104","56.7105","56.8100","56.8201","56.8900x001","56.8900x006","56.8901","56.8902","56.8903","56.8904","56.8905","56.8906","56.8907","56.8908","56.8909","57.6x00","57.6x01","57.6x02","57.6x03","57.6x04","57.6x05","57.6x06","57.7100","57.7101","57.7102","57.7103","57.7900x001","57.7901","57.8500x002","57.8501","57.8502","57.8600","57.8700x005","57.8700x006","57.8700x007","57.8700x008","57.8700x009","57.8701","57.8702","57.8703","57.8704","57.8705","57.8706","57.8707","57.9103","70.5300x001","70.5300x002"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LB1入组条件，匹配规则：某一手术匹配')
    
    if MDCL_DRG.LB11_group(record):
      return 'LB11'

    if MDCL_DRG.LB13_group(record):
      return 'LB13'

    if MDCL_DRG.LB15_group(record):
      return 'LB15'

    return 'LB1'
  else:
    return ''

