from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["04.0103","04.0200x005","04.0200x007","04.0202","04.0300x002","04.0300x003","04.0300x009","04.0300x010","04.0301","04.0303","04.0304","04.0305","04.0306","04.0307","04.0308","04.0309","04.0310","04.0400x025","04.0400x029","04.0401","04.0402","04.0403","04.0404","04.0405","04.0406","04.0407","04.0408","04.0409","04.0410","04.0411","04.0412","04.0413","04.0414","04.0415","04.0416","04.0417","04.0418","04.0419","04.0420","04.0421","04.0422","04.0423","04.0424","04.0425","04.0426","04.0500","04.0600x002","04.0715","04.0716","04.0717","04.0719","04.0720","04.0721","04.0733","04.1103","04.2x00x001","04.2x00x017","04.2x01","04.2x02","04.2x03","04.2x04","04.2x05","04.2x06","04.2x11","04.2x13","04.3x00x012","04.3x00x017","04.3x00x023","04.3x00x024","04.3x00x026","04.3x01","04.3x02","04.3x03","04.3x05","04.3x06","04.3x07","04.3x09","04.3x10","04.3x11","04.3x12","04.3x13","04.3x14","04.3x15","04.3x16","04.3x17","04.3x18","04.4100x007","04.4200x006","04.4200x007","04.4200x014","04.4900x033","04.4900x034","04.4900x035","04.4900x037","04.4900x042","04.4900x043","04.4900x044","04.4900x045","04.4912","04.5x02","04.5x03","04.5x04","04.5x05","04.5x06","04.5x09","04.5x10","04.6x00x014","04.6x00x018","04.6x00x020","04.6x01","04.6x03","04.6x06","04.6x07","04.6x08","04.6x09","04.6x10","04.6x11","04.7407","04.7408","04.7409","04.7410","04.7412","04.7413","04.7414","04.7417","04.7418","04.7500x002","04.7500x003","04.7900","04.8101","04.8106","04.8900","05.2100x002","05.2300x003","05.2300x006","05.2300x007","05.2400x003"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IG1入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IG1A_group(record):
      return 'IG12'

    if MDCI_DRG.IG15_group(record):
      return 'IG15'

    return 'IG1'
  else:
    return ''
